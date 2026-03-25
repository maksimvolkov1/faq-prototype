from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.faq_generate import DE_STOPWORDS, _clean_keywords, _ensure_cols, _format_answer_structured
from src.ollama_client import OllamaClientError, chat_json


EMPTY_SECTION = {
    "short_solution": "",
    "steps": [],
    "notes": [],
    "support": [],
}


def _build_topic_and_representatives(df: pd.DataFrame, cfg: dict) -> Tuple[Dict[int, str], Dict[int, List[int]], Dict[int, List[str]]]:
    tf_cfg = cfg.get("tfidf", {})
    faq_cfg = cfg.get("faq", {})

    vectorizer = TfidfVectorizer(
        ngram_range=tuple(tf_cfg.get("ngram_range", [1, 2])),
        max_features=int(tf_cfg.get("max_features", 2000)),
        min_df=int(tf_cfg.get("min_df", 1)),
        max_df=float(tf_cfg.get("max_df", 1.0)),
        sublinear_tf=bool(tf_cfg.get("sublinear_tf", False)),
        stop_words=list(DE_STOPWORDS) if bool(tf_cfg.get("use_stopwords", True)) else None,
    )
    X = vectorizer.fit_transform(df["clean_text"].fillna("").astype(str).tolist())
    feature_names = np.array(vectorizer.get_feature_names_out())

    top_keywords = int(faq_cfg.get("top_keywords", 5))
    top_tickets = int(faq_cfg.get("top_tickets", 3))

    topic_labels: Dict[int, str] = {}
    rep_indices: Dict[int, List[int]] = {}
    keywords_by_cluster: Dict[int, List[str]] = {}

    for cid in sorted(df["cluster_id"].astype(int).unique()):
        mask = (df["cluster_id"].values.astype(int) == cid)
        idx = np.where(mask)[0]
        if len(idx) == 0:
            continue

        centroid = X[idx].mean(axis=0)
        centroid_vec = np.asarray(centroid)
        centroid_arr = centroid_vec.ravel()

        kw_idx = np.argsort(centroid_arr)[::-1][:top_keywords]
        raw_keywords = feature_names[kw_idx].tolist()
        keywords = _clean_keywords(raw_keywords, limit=top_keywords)
        keywords_by_cluster[cid] = keywords

        base = " / ".join(keywords[:3]) if keywords else f"Cluster {cid}"
        cat_prefix = ""
        if "category" in df.columns:
            try:
                cat_prefix = df.iloc[idx]["category"].value_counts().idxmax()
            except Exception:
                cat_prefix = ""
        topic_labels[cid] = f"{cat_prefix}: {base}" if cat_prefix else base

        sims = cosine_similarity(X[idx], centroid_vec).ravel()
        rep_order = idx[np.argsort(sims)[::-1]]
        rep_indices[cid] = [int(x) for x in rep_order[: max(1, min(top_tickets, len(rep_order)))]]

    return topic_labels, rep_indices, keywords_by_cluster


def _cluster_context(df: pd.DataFrame, rep_idx: List[int]) -> str:
    blocks: List[str] = []
    for pos, row_idx in enumerate(rep_idx, start=1):
        row = df.iloc[int(row_idx)]
        blocks.append(
            "\n".join([
                f"Ticket {pos}:",
                f"- ticket_id: {row.get('ticket_id', '')}",
                f"- subject: {row.get('subject', '')}",
                f"- request_text: {row.get('request_text', '')}",
                f"- answer_text: {row.get('answer_text', '')}",
            ])
        )
    return "\n\n".join(blocks)


def _build_prompt(*, topic_label: str, keywords: List[str], context: str) -> str:
    kw_text = ", ".join(keywords) if keywords else ""
    return f'''Du bist ein Assistent für IT-Wissensmanagement.

Erzeuge aus dem folgenden Support-Kontext genau einen FAQ-Eintrag.

Regeln:
- Antworte nur als gültiges JSON.
- Keine Erklärungen vor oder nach dem JSON.
- Nutze nur Informationen aus dem Kontext.
- Erfinde keine zusätzlichen Ursachen, Schritte oder Support-Aktionen.
- Fasse doppelte Informationen zusammen.
- Formuliere die Frage klar für Endnutzer.
- Schreibe die Antwort neutral, verständlich und kurz im Stil einer Knowledge Base.
- Halte dich exakt an die JSON-Struktur.
- "steps", "notes" und "support" müssen Arrays sein.
- Wenn Informationen fehlen, verwende für das Feld einen leeren String oder ein leeres Array.

Gewünschtes JSON-Format:
{{
  "question": "string",
  "answer": {{
    "short_solution": "string",
    "steps": ["string"],
    "notes": ["string"],
    "support": ["string"]
  }}
}}

Cluster-Thema: {topic_label}
Keywords: {kw_text}

Support-Kontext:
{context}
'''


def _normalize_llm_answer(answer: Any) -> Dict[str, Any]:
    result = dict(EMPTY_SECTION)
    if not isinstance(answer, dict):
        return result

    short_solution = answer.get("short_solution", "")
    result["short_solution"] = short_solution.strip() if isinstance(short_solution, str) else ""

    for key in ["steps", "notes", "support"]:
        value = answer.get(key, [])
        if isinstance(value, str):
            value = [value]
        if isinstance(value, list):
            result[key] = [str(x).strip() for x in value if str(x).strip()]

    return result


def _markdown_from_llm_answer(answer: Dict[str, Any]) -> str:
    parts: List[str] = []

    short_solution = answer.get("short_solution", "")
    if short_solution:
        parts.append(f"**Kurzlösung:** {short_solution}\n")

    steps = answer.get("steps", [])
    if steps:
        parts.append("**Schritte:**")
        for i, step in enumerate(steps, start=1):
            parts.append(f"{i}. {step}")
        parts.append("")

    notes = answer.get("notes", [])
    if notes:
        parts.append("**Hinweise:**")
        for note in notes:
            parts.append(f"- {note}")
        parts.append("")

    support = answer.get("support", [])
    if support:
        parts.append("**Support:**")
        for item in support:
            parts.append(f"- {item}")
        parts.append("")

    return "\n".join(parts).strip()


def generate_llm_faq_from_clustered_csv(clustered_csv_path: str, out_dir: str, cfg: dict, name_suffix: str = "gemma3") -> Dict[str, str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(clustered_csv_path, dtype=str, keep_default_na=False)
    _ensure_cols(df, ["ticket_id", "cluster_id", "subject", "request_text", "answer_text", "clean_text"])
    df["cluster_id"] = df["cluster_id"].astype(int)

    llm_cfg = cfg.get("llm_faq", {})
    topic_labels, rep_indices, keywords_by_cluster = _build_topic_and_representatives(df, cfg)

    base_url = str(llm_cfg.get("base_url", "http://localhost:11434"))
    model = str(llm_cfg.get("model", "gemma3:4b"))
    timeout_sec = int(llm_cfg.get("request_timeout_sec", 120))
    temperature = float(llm_cfg.get("temperature", 0.2))
    use_fallback = bool(llm_cfg.get("fallback_to_extract", True))

    entries: List[Dict[str, Any]] = []

    for cid in sorted(df["cluster_id"].unique()):
        rep_idx = rep_indices.get(int(cid), [])
        if not rep_idx:
            continue

        context = _cluster_context(df, rep_idx)
        prompt = _build_prompt(
            topic_label=topic_labels.get(int(cid), f"Cluster {cid}"),
            keywords=keywords_by_cluster.get(int(cid), []),
            context=context,
        )

        raw_response: Dict[str, Any] | None = None
        error_message = ""
        try:
            raw_response = chat_json(
                base_url=base_url,
                model=model,
                prompt=prompt,
                timeout_sec=timeout_sec,
                temperature=temperature,
            )
            question = str(raw_response.get("question", "")).strip()
            answer_struct = _normalize_llm_answer(raw_response.get("answer", {}))
            answer_md = _markdown_from_llm_answer(answer_struct)
            if not question or not answer_md:
                raise OllamaClientError("Modellantwort enthält keine verwertbare Frage oder Antwort.")
        except Exception as exc:
            error_message = str(exc)
            rep_subject = df.iloc[int(rep_idx[0])]["subject"]
            question = rep_subject.strip() if rep_subject.strip().endswith("?") else rep_subject.strip() + "?"
            if use_fallback:
                bullets: List[str] = []
                seen = set()
                max_bullets = int(cfg.get("faq", {}).get("max_answer_bullets", 8))
                for j in rep_idx:
                    ans = df.iloc[int(j)]["answer_text"]
                    for line in str(ans).splitlines():
                        sent = line.strip(" -•\t")
                        key = sent.lower()
                        if not sent or key in seen:
                            continue
                        seen.add(key)
                        bullets.append(sent)
                        if len(bullets) >= max_bullets:
                            break
                    if len(bullets) >= max_bullets:
                        break
                answer_md = _format_answer_structured(bullets, max_steps=max_bullets)
                answer_struct = dict(EMPTY_SECTION)
            else:
                raise

        entries.append({
            "faq_id": f"FAQ-{int(cid):03d}",
            "cluster_id": int(cid),
            "topic_label": topic_labels.get(int(cid), f"Cluster {cid}"),
            "keywords": keywords_by_cluster.get(int(cid), []),
            "question": question,
            "answer_structured": answer_struct,
            "answer_markdown": answer_md,
            "supporting_ticket_ids": df.iloc[rep_idx]["ticket_id"].tolist(),
            "llm_model": model,
            "llm_error": error_message,
            "raw_llm_response": raw_response,
        })

    suffix = f"_{name_suffix}" if name_suffix else ""
    faq_json_path = out / f"faq{suffix}.json"
    faq_md_path = out / f"faq{suffix}.md"
    faq_csv_path = out / f"faq_entries{suffix}.csv"

    faq_json_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [f"# FAQ ({model}, automatisch generiert)\n\n"]
    for e in entries:
        md_lines.append(f"## {e['question']}\n\n")
        md_lines.append(f"**Topic/Label:** {e['topic_label']}\n\n")
        md_lines.append(f"**Antwort:**\n{e['answer_markdown']}\n\n")
        md_lines.append(f"**Belege (Tickets):** {', '.join(e['supporting_ticket_ids'])}\n\n")
        if e.get("llm_error"):
            md_lines.append(f"**LLM-Hinweis:** Fallback genutzt ({e['llm_error']})\n\n")
        md_lines.append("---\n\n")
    faq_md_path.write_text("".join(md_lines), encoding="utf-8")

    pd.DataFrame([
        {
            "faq_id": e["faq_id"],
            "cluster_id": e["cluster_id"],
            "topic_label": e["topic_label"],
            "question": e["question"],
            "supporting_ticket_ids": ";".join(e["supporting_ticket_ids"]),
            "llm_model": e["llm_model"],
            "llm_error": e.get("llm_error", ""),
        }
        for e in entries
    ]).to_csv(faq_csv_path, index=False, encoding="utf-8")

    return {
        "out_faq_json": str(faq_json_path),
        "out_faq_md": str(faq_md_path),
        "out_faq_csv": str(faq_csv_path),
    }

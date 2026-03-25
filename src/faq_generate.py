from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List, Any

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.text_postprocess import neutralize_sentence


# Stopword-Liste 
DE_STOPWORDS = {
    "und","oder","aber","wenn","dann","dass","der","die","das","ein","eine","einer","einem","einen",
    "ist","sind","war","waren","sein","im","in","am","an","auf","aus","bei","für","von","mit","ohne",
    "zu","zum","zur","des","den","dem","ich","du","er","sie","es","wir","ihr","mein","dein","sein",
    "kann","können","bitte","danke","hallo","hi","nicht","mehr","nur","auch","noch","heute","seit",
    "wird","wurde","werden","fehlt","geht","gehen","kommt","komme"
}

SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
LEADING_FILLER_RE = re.compile(r"^(bitte|gern|tipp|hinweis)\s*[:\-]?\s*", re.IGNORECASE)


def _ensure_cols(df: pd.DataFrame, cols: List[str]) -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}. Found: {list(df.columns)}")


def _make_question(subject: str) -> str:
    s = (subject or "").strip()
    if not s:
        return "Wie kann ich das Problem lösen?"
    return s if s.endswith("?") else s + "?"


ABBR = {
    "z.B.": "z_B_",
    "ggf.": "ggf_",
    "ca.": "ca_",
    "bzw.": "bzw_",
}
ABBR_REV = {v: k for k, v in ABBR.items()}


INFO_RE = re.compile(r"\b(sende|schicke|bestätige|nenne|benutzername|rechnername|personalnummer|projektname|rolle|freigabe|ticket|seriennummer)\b", re.IGNORECASE)
HINT_RE = re.compile(r"\b(innerhalb|spätestens|danach|sobald|warte|minuten|stunden|hinweis|tipp|ggf\.|falls)\b", re.IGNORECASE)



CAUSE_RE = re.compile(
    r"^(das ist|das deutet|das passiert|das kann|das liegt|das hängt|häufig|oft|wahrscheinlich|typischerweise|meist|in vielen fällen)\b",
    re.IGNORECASE,
)


SUPPORT_RE = re.compile(r"\b(it-support)\b|^der it-support\b", re.IGNORECASE)

def _canon(s: str) -> str:
    """Normalisiert Text zum Deduplizieren (casefold + remove punctuation)."""
    s = (s or "").strip().lower()
    s = re.sub(r"[^0-9a-zäöüß]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s



STEP_RE = re.compile(
    r"^(prüfe|öffne|starte|stoppe|beende|entferne|füge|installiere|aktualisiere|melde|setze|lösche|wähle|trenne|verbinde|deaktiviere|aktiviere|ändere|stelle|nutze|klicke|gib|führe|sende|schicke)\b",
    re.IGNORECASE,
)

GENERIC_STEP_RE = re.compile(r"\b(neu starten|neustart|erneut versuchen|nochmal versuchen|versuche es erneut)\b", re.IGNORECASE)


BAD_KW = {
    "sich","habe","haben","kann","können","bitte","gern","tipp","hinweis","komme","kommt","gehen","geht",
    "ich","du","er","sie","wir","ihr","mehr","nur","auch","noch","heute","seit"
}

def _sentence_case(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return s
    # Nicht anfassen, wenn es wie Code/Pfad aussieht
    if s.startswith(("http", "\\", "C:\\", "D:\\", "E:\\")) or s.lower().startswith(("ipconfig", "ping ", "nslookup", "tracert")):
        return s
    if s[0].islower():
        s = s[0].upper() + s[1:]
    return s

def _clean_keywords(kws: List[str], limit: int) -> List[str]:
    out: List[str] = []
    for kw in kws:
        kw = (kw or "").strip()
        if not kw:
            continue
        tokens = [t for t in re.split(r"\s+", kw) if t]
        if any(t.lower() in DE_STOPWORDS or t.lower() in BAD_KW for t in tokens):
            continue
        if all(len(t) < 3 for t in tokens):
            continue
        out.append(kw)
        if len(out) >= limit:
            break
    return out

def _format_answer_structured(bullets: List[str], max_steps: int = 8) -> str:
    """Formatiert extrahierte Sätze in eine KB-ähnliche Struktur.

    Ziel: 'Schritte' sollen echte Handlungen sein. Erklärungen -> 'Ursache/Erklärung',
    Support-Aktionen -> 'Support', Wartezeiten/Alternativen -> 'Hinweise'.
    """
    if not bullets:
        return "- Bitte prüfe die Einstellungen und versuche es erneut."

    # 1) Vorverarbeitung
    seen = set()
    cleaned_bullets: List[str] = []
    for b in bullets:
        b = (b or "").strip()
        if not b:
            continue
        b = _sentence_case(b)
        #b = neutralize_sentence(b)
        key = _canon(b)
        if not key or key in seen:
            continue
        seen.add(key)
        cleaned_bullets.append(b)

    # 2) Klassifikation
    infos: List[str] = []
    steps: List[str] = []
    causes: List[str] = []
    hints: List[str] = []
    support: List[str] = []

    for b in cleaned_bullets:
        if INFO_RE.search(b):
            infos.append(b)
        elif SUPPORT_RE.search(b):
            support.append(b)
        elif CAUSE_RE.search(b):
            causes.append(b)
        elif STEP_RE.search(b):
            steps.append(b)
        elif HINT_RE.search(b):
            hints.append(b)
        else:
            
            steps.append(b)

    # 3) 
    if len(steps) > 1:
        generic = [s for s in steps if GENERIC_STEP_RE.search(s)]
        if generic:
            steps = [s for s in steps if not GENERIC_STEP_RE.search(s)]
            hints = generic + hints

    # 4) Kurzlösung
    def _step_score(s: str) -> int:
        score = 0
        if STEP_RE.search(s):
            score += 3
        if GENERIC_STEP_RE.search(s):
            score -= 3
        if re.search(r"\b(dienst|druckwarteschlange|vpn|proxy|dns|sso|mfa|2fa|ad|outlook|teams|treiber|netzwerk|wlan|lan|aktivierung|lizenz|drucker|scanner)\b", s, re.IGNORECASE):
            score += 1
        return score

    short_solution = max(steps, key=_step_score) if steps else ""

    # 5) Begrenzen
    steps = steps[:max_steps]
    causes = causes[:3]
    infos = infos[:5]
    hints = hints[:4]
    support = support[:3]

    # 6) Markdown 
    md: List[str] = []

    if short_solution:
        md.append(f"**Kurzlösung:** {short_solution}\n")

    if causes:
        md.append("**Ursache/Erklärung:**")
        for c in causes:
            md.append(f"- {c}")
        md.append("")

    if steps:
        md.append("**Schritte:**")
        for i, step in enumerate(steps, 1):
            md.append(f"{i}. {step}")
        md.append("")

    if infos:
        md.append("**Benötigte Angaben:**")
        for it in infos:
            md.append(f"- {it}")
        md.append("")

    if hints:
        md.append("**Hinweise:**")
        for h in hints:
            md.append(f"- {h}")
        md.append("")

    if support:
        md.append("**Support:**")
        for s in support:
            md.append(f"- {s}")
        md.append("")

    return "\n".join(md).strip()

def _split_sentences(text: str) -> List[str]:
    t = (text or "").strip()
    if not t:
        return []

    # 1) Abkürzungen normalisieren
    t = re.sub(r"\bz\.\s*b\.", "z.B.", t, flags=re.IGNORECASE)
    t = re.sub(r"\bu\.\s*a\.", "u.a.", t, flags=re.IGNORECASE)

    # 2) Maskieren 
    for k, v in ABBR.items():
        t = t.replace(k, v)

    t = t.replace("\r", "\n")
    parts = []
    for block in t.split("\n"):
        block = block.strip()
        if not block:
            continue
        parts.extend(SENT_SPLIT_RE.split(block))

    cleaned = []
    buffer = ""
    par_balance = 0  

    for p in parts:
        p = p.strip(" -•\t").strip()
        if not p or p == ".":
            continue

        # Abkürzungen
        for v, k in ABBR_REV.items():
            p = p.replace(v, k)

        p = LEADING_FILLER_RE.sub("", p).strip()
        if len(p) < 4:
            continue

        # 3) Klammer-Fragmente
        par_balance += p.count("(") - p.count(")")
        if buffer:
            buffer = f"{buffer} {p}".strip()
        else:
            buffer = p

        if par_balance <= 0:
            cleaned.append(buffer)
            buffer = ""
            par_balance = 0

    if buffer:
        cleaned.append(buffer)

    return cleaned


def generate_faq_from_clustered_csv(clustered_csv_path: str, out_dir: str, cfg: dict, name_suffix: str = "") -> Dict[str, str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(clustered_csv_path, dtype=str, keep_default_na=False)
    _ensure_cols(df, ["ticket_id", "cluster_id", "subject", "request_text", "answer_text", "clean_text"])

    # cluster_id als int für Sortierung
    df["cluster_id"] = df["cluster_id"].astype(int)

    faq_cfg = cfg.get("faq", {})
    top_tickets = int(faq_cfg.get("top_tickets", 2))
    top_keywords = int(faq_cfg.get("top_keywords", 5))
    max_bullets = int(faq_cfg.get("max_answer_bullets", 8))

    tf_cfg = cfg.get("tfidf", {})
    ng = tuple(tf_cfg.get("ngram_range", [1, 2]))
    max_features = int(tf_cfg.get("max_features", 2000))

    vectorizer = TfidfVectorizer(
        ngram_range=ng,
        max_features=max_features,
        min_df=int(tf_cfg.get("min_df", 1)),
        max_df=float(tf_cfg.get("max_df", 1.0)),
        sublinear_tf=bool(tf_cfg.get("sublinear_tf", False)),
        stop_words=list(DE_STOPWORDS) if bool(tf_cfg.get("use_stopwords", True)) else None,
    )
    X = vectorizer.fit_transform(df["clean_text"].fillna("").astype(str).tolist())
    feature_names = np.array(vectorizer.get_feature_names_out())

    faq_entries: List[Dict[str, Any]] = []

    for cid in sorted(df["cluster_id"].unique()):
        mask = (df["cluster_id"].values == cid)
        idx = np.where(mask)[0]
        if len(idx) == 0:
            continue

        # "Zentroid" als Mittelwert
        centroid = X[idx].mean(axis=0)          # np.matrix
        centroid_vec = np.asarray(centroid)     # -> ndarray (1, n_features)
        centroid_arr = centroid_vec.ravel()


        kw_idx = np.argsort(centroid_arr)[::-1][:top_keywords]
        raw_keywords = feature_names[kw_idx].tolist()
        keywords = _clean_keywords(raw_keywords, limit=top_keywords)
        base = " / ".join(keywords[:3]) if keywords else f"Cluster {cid}"
        cat_prefix = ""
        if "category" in df.columns:
            try:
                cat_prefix = df.iloc[idx]["category"].value_counts().idxmax()
            except Exception:
                cat_prefix = ""
        topic_label = f"{cat_prefix}: {base}" if cat_prefix else base

        # höchste Similarity zum Zentroid
        sims = cosine_similarity(X[idx], centroid_vec).ravel()


        rep_order = idx[np.argsort(sims)[::-1]]
        rep_idx = rep_order[: max(1, min(top_tickets, len(rep_order)))]

    
        rep_subject = df.iloc[int(rep_idx[0])]["subject"]
        question = _make_question(rep_subject)

        bullets: List[str] = []
        seen = set()
        for j in rep_idx:
            ans = df.iloc[int(j)]["answer_text"]
            for sent in _split_sentences(ans):
                key = sent.lower()
                if key in seen:
                    continue
                seen.add(key)
                bullets.append(sent)
                if len(bullets) >= max_bullets:
                    break
            if len(bullets) >= max_bullets:
                break

        # Fallback: wenn answer_text leer -> request_text (erster Satz)
        if not bullets:
            req = df.iloc[int(rep_idx[0])]["request_text"]
            sents = _split_sentences(req)
            if sents:
                bullets = sents[: min(2, max_bullets)]
            else:
                bullets = ["Bitte prüfe die Einstellungen und versuche es erneut."]

        answer_md = _format_answer_structured(bullets, max_steps=max_bullets)

        supporting_ids = df.iloc[rep_idx]["ticket_id"].tolist()

        faq_entries.append({
            "faq_id": f"FAQ-{cid:03d}",
            "cluster_id": int(cid),
            "topic_label": topic_label,
            "keywords": keywords,
            "question": question,
            "answer_markdown": answer_md,
            "supporting_ticket_ids": supporting_ids,
        })

    # Export
    suffix = f"_{name_suffix}" if name_suffix else ""
    faq_json_path = out / f"faq{suffix}.json"
    faq_md_path = out / f"faq{suffix}.md"
    faq_csv_path = out / f"faq_entries{suffix}.csv"

    faq_json_path.write_text(json.dumps(faq_entries, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown
    md_lines = ["# FAQ (automatisch generiert)\n\n"]
    for e in faq_entries:
        md_lines.append(f"## {e['question']}\n\n")
        md_lines.append(f"**Topic/Label:** {e['topic_label']}\n\n")
        md_lines.append(f"**Antwort:**\n{e['answer_markdown']}\n\n")
        md_lines.append(f"**Belege (Tickets):** {', '.join(e['supporting_ticket_ids'])}\n\n")
        md_lines.append("---\n\n")

    faq_md_path.write_text("".join(md_lines), encoding="utf-8")

    # CSV
    pd.DataFrame([{
        "faq_id": e["faq_id"],
        "cluster_id": e["cluster_id"],
        "topic_label": e["topic_label"],
        "question": e["question"],
        "supporting_ticket_ids": ";".join(e["supporting_ticket_ids"]),
    } for e in faq_entries]).to_csv(faq_csv_path, index=False, encoding="utf-8")

    return {
        "out_faq_json": str(faq_json_path),
        "out_faq_md": str(faq_md_path),
        "out_faq_csv": str(faq_csv_path),
    }
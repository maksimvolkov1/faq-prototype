"""
Run-Artefakte für die Arbeit (Reproduzierbarkeit + Vergleich).

Erzeugt:
- run_summary.md (Konfiguration, Datenbasis, Kennzahlen, Artefaktpfade)
- comparison_table.md/.csv (TF-IDF, Embeddings und Gemma3-Varianten kompakt)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional
import re

import pandas as pd


_SIL_RE = re.compile(r"silhouette\s*\(cosine\)\s*:\s*([0-9]*\.?[0-9]+)", re.IGNORECASE)


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def _path_exists(path_str: str) -> bool:
    return bool(path_str) and Path(path_str).exists()


def parse_silhouette_from_report(report_md_path: str) -> Optional[float]:
    txt = _read_text(Path(report_md_path))
    m = _SIL_RE.search(txt)
    if not m:
        return None
    try:
        return float(m.group(1))
    except Exception:
        return None


def cluster_size_stats(clustered_csv_path: str) -> Dict[str, Any]:
    if not _path_exists(clustered_csv_path):
        return {}

    df = pd.read_csv(clustered_csv_path, dtype=str, keep_default_na=False)
    if "cluster_id" not in df.columns:
        return {"n_tickets": len(df), "n_clusters": None}

    df["cluster_id"] = df["cluster_id"].astype(int)
    sizes = df["cluster_id"].value_counts().sort_index()
    stats = {
        "n_tickets": int(len(df)),
        "n_clusters": int(sizes.shape[0]),
        "min_cluster": int(sizes.min()),
        "max_cluster": int(sizes.max()),
        "avg_cluster": float(sizes.mean()),
        "cluster_sizes": sizes.to_dict(),
        "largest_clusters": sizes.sort_values(ascending=False).head(5).to_dict(),
    }
    return stats


def _md_code(s: str) -> str:
    return f"`{s}`"


def _fmt_min_avg_max(stats: Dict[str, Any]) -> str:
    if not stats or stats.get("avg_cluster") is None:
        return ""
    return f"{stats.get('min_cluster','')}/{stats.get('avg_cluster',''):.1f}/{stats.get('max_cluster','')}"


def _append_if_exists(lines: list[str], label: str, path: Path) -> None:
    if path.exists():
        lines.append(f"  - {label}: {_md_code(str(path))}\n")


def _build_gemma_paths(out: Path, variant: str) -> Dict[str, Path]:
    base = out / "gemma3" / f"gemma3_{variant}"
    return {
        "base": base,
        "faq_md": base / f"faq_gemma3_{variant}.md",
        "faq_json": base / f"faq_gemma3_{variant}.json",
        "faq_csv": base / f"faq_entries_gemma3_{variant}.csv",
        "evaluation_csv": base / f"evaluation_gemma3_{variant}.csv",
    }


def _append_method_section(
    lines: list[str],
    *,
    heading: str,
    k_value: Any,
    method_detail_lines: list[str],
    clustered_csv: str,
    report_md: str,
    sil: Optional[float],
    stats: Dict[str, Any],
    artifacts: list[tuple[str, Path | str]],
) -> None:
    lines.append(heading)
    lines.append(f"- k: {k_value}\n")
    for line in method_detail_lines:
        lines.append(f"- {line}\n")
    if sil is not None:
        lines.append(f"- Silhouette (cosine): **{sil:.3f}**\n")
    if stats:
        lines.append(
            f"- Cluster: {stats.get('n_clusters')} | Tickets: {stats.get('n_tickets')} | "
            f"min/avg/max: {_fmt_min_avg_max(stats)}\n"
        )
        lines.append(f"- Top-5 Clustergrößen: {stats.get('largest_clusters')}\n")
    lines.append("- Artefakte:\n")
    if clustered_csv:
        lines.append(f"  - Clustered CSV: {_md_code(clustered_csv)}\n")
    if report_md:
        lines.append(f"  - Cluster Report: {_md_code(report_md)}\n")
    for label, path in artifacts:
        p = Path(path) if isinstance(path, str) else path
        _append_if_exists(lines, label, p)
    lines.append("\n")



def write_run_summary(
    out_dir: str,
    cfg: dict,
    *,
    tfidf_res: Optional[dict] = None,
    emb_res: Optional[dict] = None,
) -> Dict[str, str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    input_path = str(cfg.get("paths", {}).get("input_tickets", ""))
    seed = cfg.get("project", {}).get("seed", None)
    k_value = cfg.get("clustering", {}).get("k", "")

    lines: list[str] = []
    lines.append("# Run Summary\n\n")
    lines.append("## 1) Datenbasis\n")
    lines.append(f"- Input: {_md_code(input_path)}\n")
    if seed is not None:
        lines.append(f"- Seed: {seed}\n")
    lines.append("\n")

    # TF-IDF
    if tfidf_res:
        clustered_csv = tfidf_res.get("out_clustered_csv", "")
        report_md = tfidf_res.get("out_report_md", "")
        sil = tfidf_res.get("silhouette_cosine", None)
        if sil is None and report_md:
            sil = parse_silhouette_from_report(report_md)
        stats = cluster_size_stats(clustered_csv) if clustered_csv else {}

        tf_cfg = cfg.get("tfidf", {})
        _append_method_section(
            lines,
            heading="## 2) Methode A: TF-IDF + KMeans\n",
            k_value=k_value,
            method_detail_lines=[
                "TF-IDF: "
                f"ngram_range={tf_cfg.get('ngram_range')}, "
                f"max_features={tf_cfg.get('max_features')}, "
                f"min_df={tf_cfg.get('min_df')}, "
                f"max_df={tf_cfg.get('max_df')}, "
                f"sublinear_tf={tf_cfg.get('sublinear_tf')}, "
                f"stopwords={tf_cfg.get('use_stopwords', True)}"
            ],
            clustered_csv=clustered_csv,
            report_md=report_md,
            sil=sil,
            stats=stats,
            artifacts=[
                ("FAQ (MD)", out / "faq_tfidf.md"),
                ("FAQ (JSON)", out / "faq_tfidf.json"),
                ("FAQ (CSV)", out / "faq_entries_tfidf.csv"),
                ("Evaluation", out / "evaluation_tfidf.csv"),
            ],
        )

    # Embeddings
    if emb_res:
        clustered_csv = emb_res.get("out_clustered_csv", "")
        report_md = emb_res.get("out_report_md", "")
        sil = emb_res.get("silhouette_cosine", None)
        if sil is None and report_md:
            sil = parse_silhouette_from_report(report_md)
        stats = cluster_size_stats(clustered_csv) if clustered_csv else {}

        e_cfg = cfg.get("embeddings", {})
        _append_method_section(
            lines,
            heading="## 3) Methode B: Embeddings + KMeans\n",
            k_value=k_value,
            method_detail_lines=[
                f"Model: {_md_code(str(e_cfg.get('model_name')))}",
                f"batch_size: {e_cfg.get('batch_size')} | normalize: {e_cfg.get('normalize')}"
            ],
            clustered_csv=clustered_csv,
            report_md=report_md,
            sil=sil,
            stats=stats,
            artifacts=[
                ("FAQ (MD)", out / "embeddings" / "faq_embeddings.md"),
                ("FAQ (JSON)", out / "embeddings" / "faq_embeddings.json"),
                ("FAQ (CSV)", out / "embeddings" / "faq_entries_embeddings.csv"),
                ("Evaluation", out / "embeddings" / "evaluation_embeddings.csv"),
            ],
        )

    # Gemma3 on TF-IDF clusters
    gemma_tfidf = _build_gemma_paths(out, "tfidf")
    if gemma_tfidf["base"].exists() and tfidf_res:
        clustered_csv = tfidf_res.get("out_clustered_csv", "")
        report_md = tfidf_res.get("out_report_md", "")
        sil = tfidf_res.get("silhouette_cosine", None)
        if sil is None and report_md:
            sil = parse_silhouette_from_report(report_md)
        stats = cluster_size_stats(clustered_csv) if clustered_csv else {}
        llm_cfg = cfg.get("llm_faq", {})
        ollama_cfg = cfg.get("ollama", {})

        _append_method_section(
            lines,
            heading="## 4) Methode C: Gemma3 auf TF-IDF-Clustern\n",
            k_value=k_value,
            method_detail_lines=[
                f"FAQ-Quelle: {_md_code('TF-IDF-Cluster')}",
                f"LLM-Modell: {_md_code(str(ollama_cfg.get('model', llm_cfg.get('model', 'gemma3'))))}",
                "FAQ-Generierung: LLM-gestützt, Clusterbasis aus TF-IDF + KMeans"
            ],
            clustered_csv=clustered_csv,
            report_md=report_md,
            sil=sil,
            stats=stats,
            artifacts=[
                ("FAQ (MD)", gemma_tfidf["faq_md"]),
                ("FAQ (JSON)", gemma_tfidf["faq_json"]),
                ("FAQ (CSV)", gemma_tfidf["faq_csv"]),
                ("Evaluation", gemma_tfidf["evaluation_csv"]),
            ],
        )

    # Gemma3 on embedding clusters
    gemma_embeddings = _build_gemma_paths(out, "embeddings")
    if gemma_embeddings["base"].exists() and emb_res:
        clustered_csv = emb_res.get("out_clustered_csv", "")
        report_md = emb_res.get("out_report_md", "")
        sil = emb_res.get("silhouette_cosine", None)
        if sil is None and report_md:
            sil = parse_silhouette_from_report(report_md)
        stats = cluster_size_stats(clustered_csv) if clustered_csv else {}
        llm_cfg = cfg.get("llm_faq", {})
        ollama_cfg = cfg.get("ollama", {})

        _append_method_section(
            lines,
            heading="## 5) Methode D: Gemma3 auf Embedding-Clustern\n",
            k_value=k_value,
            method_detail_lines=[
                f"FAQ-Quelle: {_md_code('Embedding-Cluster')}",
                f"LLM-Modell: {_md_code(str(ollama_cfg.get('model', llm_cfg.get('model', 'gemma3'))))}",
                "FAQ-Generierung: LLM-gestützt, Clusterbasis aus Embeddings + KMeans"
            ],
            clustered_csv=clustered_csv,
            report_md=report_md,
            sil=sil,
            stats=stats,
            artifacts=[
                ("FAQ (MD)", gemma_embeddings["faq_md"]),
                ("FAQ (JSON)", gemma_embeddings["faq_json"]),
                ("FAQ (CSV)", gemma_embeddings["faq_csv"]),
                ("Evaluation", gemma_embeddings["evaluation_csv"]),
            ],
        )

    lines.append("## 6) Hinweise (Prototyp)\n")
    lines.append("- Ergebnisse basieren auf synthetischen Supporttickets und dienen der prototypischen Evaluation.\n")
    lines.append("- Keine Produktivlösung (kein Monitoring, keine Skalierung, kein kontinuierliches Lernen).\n")
    lines.append("- Gemma3 ist kein eigenes Clustering-Verfahren, sondern eine alternative FAQ-Generierung auf Basis vorhandener Cluster.\n")

    summary_path = out / "run_summary.md"
    summary_path.write_text("".join(lines), encoding="utf-8")

    return {"out_run_summary_md": str(summary_path)}



def _to_markdown_fallback(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    lines = []
    lines.append("| " + " | ".join(cols) + " |\n")
    lines.append("|" + "|".join(["---"] * len(cols)) + "|\n")
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |\n")
    return "".join(lines)



def write_comparison_table(
    out_dir: str,
    cfg: dict,
    *,
    tfidf_res: Optional[dict] = None,
    emb_res: Optional[dict] = None,
) -> Dict[str, str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    rows = []
    k_value = cfg.get("clustering", {}).get("k", "")

    if tfidf_res:
        sil = tfidf_res.get("silhouette_cosine", None)
        if sil is None and tfidf_res.get("out_report_md"):
            sil = parse_silhouette_from_report(tfidf_res["out_report_md"])
        stats = cluster_size_stats(tfidf_res["out_clustered_csv"]) if tfidf_res.get("out_clustered_csv") else {}
        tf = cfg.get("tfidf", {})
        rows.append({
            "Methode": "TF-IDF",
            "Clusterbasis": "TF-IDF + KMeans",
            "FAQ-Typ": "heuristisch",
            "Modell": "-",
            "k": k_value,
            "Silhouette(cosine)": f"{sil:.3f}" if isinstance(sil, (float, int)) else "",
            "Tickets": stats.get("n_tickets", ""),
            "Cluster": stats.get("n_clusters", ""),
            "min/avg/max": _fmt_min_avg_max(stats),
            "Details": f"ng={tf.get('ngram_range')}, maxf={tf.get('max_features')}, min_df={tf.get('min_df')}, max_df={tf.get('max_df')}, sublin={tf.get('sublinear_tf')}",
        })

    if emb_res:
        sil = emb_res.get("silhouette_cosine", None)
        if sil is None and emb_res.get("out_report_md"):
            sil = parse_silhouette_from_report(emb_res["out_report_md"])
        stats = cluster_size_stats(emb_res["out_clustered_csv"]) if emb_res.get("out_clustered_csv") else {}
        e = cfg.get("embeddings", {})
        rows.append({
            "Methode": "Embeddings",
            "Clusterbasis": "Embeddings + KMeans",
            "FAQ-Typ": "heuristisch",
            "Modell": e.get("model_name", ""),
            "k": k_value,
            "Silhouette(cosine)": f"{sil:.3f}" if isinstance(sil, (float, int)) else "",
            "Tickets": stats.get("n_tickets", ""),
            "Cluster": stats.get("n_clusters", ""),
            "min/avg/max": _fmt_min_avg_max(stats),
            "Details": "Labeling/Keywords via TF-IDF",
        })

    gemma_tfidf = _build_gemma_paths(out, "tfidf")
    if gemma_tfidf["faq_md"].exists() and tfidf_res:
        sil = tfidf_res.get("silhouette_cosine", None)
        if sil is None and tfidf_res.get("out_report_md"):
            sil = parse_silhouette_from_report(tfidf_res["out_report_md"])
        stats = cluster_size_stats(tfidf_res["out_clustered_csv"]) if tfidf_res.get("out_clustered_csv") else {}
        ollama_cfg = cfg.get("ollama", {})
        llm_cfg = cfg.get("llm_faq", {})
        rows.append({
            "Methode": "Gemma3 (TF-IDF)",
            "Clusterbasis": "TF-IDF + KMeans",
            "FAQ-Typ": "LLM-gestützt",
            "Modell": ollama_cfg.get("model", llm_cfg.get("model", "gemma3")),
            "k": k_value,
            "Silhouette(cosine)": f"{sil:.3f}" if isinstance(sil, (float, int)) else "",
            "Tickets": stats.get("n_tickets", ""),
            "Cluster": stats.get("n_clusters", ""),
            "min/avg/max": _fmt_min_avg_max(stats),
            "Details": "FAQ aus TF-IDF-Clustern via Gemma3",
        })

    gemma_embeddings = _build_gemma_paths(out, "embeddings")
    if gemma_embeddings["faq_md"].exists() and emb_res:
        sil = emb_res.get("silhouette_cosine", None)
        if sil is None and emb_res.get("out_report_md"):
            sil = parse_silhouette_from_report(emb_res["out_report_md"])
        stats = cluster_size_stats(emb_res["out_clustered_csv"]) if emb_res.get("out_clustered_csv") else {}
        ollama_cfg = cfg.get("ollama", {})
        llm_cfg = cfg.get("llm_faq", {})
        rows.append({
            "Methode": "Gemma3 (Embeddings)",
            "Clusterbasis": "Embeddings + KMeans",
            "FAQ-Typ": "LLM-gestützt",
            "Modell": ollama_cfg.get("model", llm_cfg.get("model", "gemma3")),
            "k": k_value,
            "Silhouette(cosine)": f"{sil:.3f}" if isinstance(sil, (float, int)) else "",
            "Tickets": stats.get("n_tickets", ""),
            "Cluster": stats.get("n_clusters", ""),
            "min/avg/max": _fmt_min_avg_max(stats),
            "Details": "FAQ aus Embedding-Clustern via Gemma3",
        })

    df = pd.DataFrame(rows)

    md_lines = ["# Vergleichstabelle (pro Run)\n\n"]
    if df.empty:
        md_lines.append("_Keine Vergleichsdaten verfügbar._\n")
    else:
        try:
            md_lines.append(df.to_markdown(index=False))
            md_lines.append("\n")
        except Exception:
            md_lines.append(_to_markdown_fallback(df))
            md_lines.append("\n")

    out_md = out / "comparison_table.md"
    out_md.write_text("".join(md_lines), encoding="utf-8")
    out_csv = out / "comparison_table.csv"
    df.to_csv(out_csv, index=False, encoding="utf-8")

    return {"out_comparison_md": str(out_md), "out_comparison_csv": str(out_csv)}

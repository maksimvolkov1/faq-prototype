"""
Evaluation-Sheet Generator (qualitatives Bewertungsraster).

Erzeugt eine CSV mit vorbefüllten Feldern (Cluster/FAQ/Beispiele) und leeren Bewertungsspalten.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import json

import pandas as pd


def _load_faq_json(path: Path) -> List[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def _pick_clusters_by_size(df: pd.DataFrame, n: int) -> List[int]:
    sizes = df["cluster_id"].value_counts()
    return [int(x) for x in sizes.sort_values(ascending=False).head(n).index.tolist()]


def write_evaluation_sheet(
    *,
    method: str,
    clustered_csv_path: str,
    faq_json_path: str,
    out_csv_path: str,
    n_clusters: int = 8,
    examples_per_cluster: int = 3,
) -> Dict[str, str]:
    df = pd.read_csv(clustered_csv_path, dtype=str, keep_default_na=False)
    if "cluster_id" not in df.columns:
        raise ValueError(f"cluster_id missing in {clustered_csv_path}")

    df["cluster_id"] = df["cluster_id"].astype(int)

    faq_entries = _load_faq_json(Path(faq_json_path))
    faq_by_cluster = {int(e["cluster_id"]): e for e in faq_entries if "cluster_id" in e}

    chosen = _pick_clusters_by_size(df, n_clusters)

    rows: List[dict] = []
    for cid in chosen:
        sub = df[df["cluster_id"] == cid].copy()
        size = int(len(sub))

        ex = sub.head(examples_per_cluster)
        ex_ids = ex.get("ticket_id", pd.Series([], dtype=str)).tolist()
        ex_subjects = ex.get("subject", pd.Series([], dtype=str)).tolist()
        ex_requests = ex.get("request_text", pd.Series([], dtype=str)).tolist()

        faq = faq_by_cluster.get(cid, {})
        rows.append({
            "method": method,
            "cluster_id": cid,
            "cluster_size": size,
            "topic_label": faq.get("topic_label", ""),
            "question": faq.get("question", ""),
            "answer_markdown": faq.get("answer_markdown", ""),
            "supporting_ticket_ids": ";".join(faq.get("supporting_ticket_ids", [])) if isinstance(faq.get("supporting_ticket_ids", []), list) else "",
            "example_ticket_ids": ";".join(ex_ids),
            "example_subjects": " | ".join(ex_subjects),
            "example_requests": " | ".join([r[:220] + ("…" if len(r) > 220 else "") for r in ex_requests]),
            "cluster_coherence_1to5": "",
            "question_quality_1to5": "",
            "answer_quality_1to5": "",
            "traceability_1to5": "",
            "notes": "",
        })

    out_path = Path(out_csv_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out_path, index=False, encoding="utf-8")
    return {"out_evaluation_csv": str(out_path)}

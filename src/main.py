from pathlib import Path
import yaml
from datetime import datetime
# import time
# import statistics

from src.io_utils import load_tickets, save_df
from src.preprocess import preprocess_tickets
from src.reporting import write_preprocessing_report
from src.tfidf_cluster import tfidf_cluster_and_report
from src.faq_generate import generate_faq_from_clustered_csv
from src.embed_cluster import embed_cluster_and_report
from src.faq_generate_llm import generate_llm_faq_from_clustered_csv
from src.run_summary import write_run_summary, write_comparison_table
from src.evaluation_sheet import write_evaluation_sheet


# .\.venv\Scripts\python.exe -m src.main

def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_gemma3_for_source(*, label: str, clustered_csv: str, out_dir: Path, cfg: dict):
    safe_label = label.strip().lower()
    llm_subdir = str(cfg.get("llm_faq", {}).get("output_subdir", "gemma3"))

    llm_dir = out_dir / llm_subdir / f"gemma3_{safe_label}"
    llm_dir.mkdir(parents=True, exist_ok=True)

    faq_res = generate_llm_faq_from_clustered_csv(
        clustered_csv,
        str(llm_dir),
        cfg,
        name_suffix=f"gemma3_{safe_label}",
    )

    print(f"[Gemma3/{label}] FAQ JSON: {faq_res['out_faq_json']}")
    print(f"[Gemma3/{label}] FAQ MD:   {faq_res['out_faq_md']}")
    print(f"[Gemma3/{label}] FAQ CSV:  {faq_res['out_faq_csv']}")

    return faq_res, llm_dir


################################################# Zeit Benchmark ##########
# BENCHMARK_MODE = True
# BENCHMARK_SIZES = [100, 200, 300, 400]
# BENCHMARK_REPEATS = 3


# def run_runtime_benchmark(df_clean, cfg, out_dir: Path):
#     seed = int(cfg.get("project", {}).get("seed", 42))

#     print("\n=== Runtime-Benchmark: TF-IDF vs Embeddings ===")
#     print(f"Verfügbare Tickets: {len(df_clean)}")
#     print(f"k = {cfg.get('clustering', {}).get('k', 12)}")
#     print(f"FAQ aktiv: {cfg.get('faq', {}).get('enabled', False)}")
#     print(f"Gemma3 aktiv: {cfg.get('llm_faq', {}).get('enabled', False)}")
#     print(f"Evaluation aktiv: {cfg.get('evaluation', {}).get('enabled', False)}")
#     print("-" * 72)

#     for n in BENCHMARK_SIZES:
#         if n > len(df_clean):
#             print(f"[SKIP] n={n} > verfügbare Tickets ({len(df_clean)})")
#             continue

#         tfidf_times = []
#         emb_times = []

#         for r in range(BENCHMARK_REPEATS):
#             df_sub = (
#                 df_clean
#                 .sample(n=n, random_state=seed + r)
#                 .reset_index(drop=True)
#             )

#             tfidf_out = out_dir / "benchmark" / f"n_{n}" / f"tfidf_r{r+1}"
#             emb_out = out_dir / "benchmark" / f"n_{n}" / f"emb_r{r+1}"

#             t0 = time.perf_counter()
#             tfidf_cluster_and_report(df_sub, str(tfidf_out), cfg)
#             tfidf_times.append(time.perf_counter() - t0)

#             t0 = time.perf_counter()
#             embed_cluster_and_report(df_sub, str(emb_out), cfg)
#             emb_times.append(time.perf_counter() - t0)

#         print(
#             f"n={n:>4} | "
#             f"TF-IDF mean={statistics.mean(tfidf_times):6.2f}s "
#             f"(min={min(tfidf_times):5.2f}, max={max(tfidf_times):5.2f}) | "
#             f"Embeddings mean={statistics.mean(emb_times):6.2f}s "
#             f"(min={min(emb_times):5.2f}, max={max(emb_times):5.2f})"
#         )

#     print("-" * 72)
#     print("Benchmark beendet.\n")

def main():
    cfg = load_config("configs/config.yaml")

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = Path(cfg["paths"]["outputs_dir"]) / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "config_used.yaml").write_text(
        yaml.safe_dump(cfg, sort_keys=False),
        encoding="utf-8",
    )

    df = load_tickets(cfg["paths"]["input_tickets"])
    df_clean = preprocess_tickets(df, cfg)

    ############ Zeit benchmark 
    # if BENCHMARK_MODE:
    #     run_runtime_benchmark(df_clean, cfg, out_dir)
    #     return

    save_df(df_clean, out_dir / "tickets_clean.csv")
    write_preprocessing_report(df_clean, out_dir)

    res = None
    emb_res = None

    faq_res_tfidf = None
    faq_res_emb = None

    faq_res_gemma_tfidf = None
    faq_res_gemma_emb = None
    gemma_tfidf_dir = None
    gemma_emb_dir = None

    if cfg.get("tfidf", {}).get("enabled", False):
        res = tfidf_cluster_and_report(df_clean, str(out_dir), cfg)
        print(f"Clustered CSV: {res['out_clustered_csv']}")
        print(f"Cluster report: {res['out_report_md']}")

        if cfg.get("faq", {}).get("enabled", False):
            faq_res_tfidf = generate_faq_from_clustered_csv(
                res["out_clustered_csv"],
                str(out_dir),
                cfg,
                name_suffix="tfidf",
            )
            print(f"FAQ JSON: {faq_res_tfidf['out_faq_json']}")
            print(f"FAQ MD:   {faq_res_tfidf['out_faq_md']}")
            print(f"FAQ CSV:  {faq_res_tfidf['out_faq_csv']}")

    if cfg.get("embeddings", {}).get("enabled", False):
        emb_dir = out_dir / "embeddings"
        emb_dir.mkdir(parents=True, exist_ok=True)

        emb_res = embed_cluster_and_report(df_clean, str(emb_dir), cfg)
        print(f"[Embeddings] Clustered CSV: {emb_res['out_clustered_csv']}")
        print(f"[Embeddings] Cluster report: {emb_res['out_report_md']}")

        if cfg.get("faq", {}).get("enabled", False):
            faq_res_emb = generate_faq_from_clustered_csv(
                emb_res["out_clustered_csv"],
                str(emb_dir),
                cfg,
                name_suffix="embeddings",
            )
            print(f"[Embeddings] FAQ JSON: {faq_res_emb['out_faq_json']}")
            print(f"[Embeddings] FAQ MD:   {faq_res_emb['out_faq_md']}")
            print(f"[Embeddings] FAQ CSV:  {faq_res_emb['out_faq_csv']}")

    llm_cfg = cfg.get("llm_faq", {})
    if llm_cfg.get("enabled", False):
        # 1) Gemma3 auf TF-IDF-Clustern
        if res:
            faq_res_gemma_tfidf, gemma_tfidf_dir = _run_gemma3_for_source(
                label="tfidf",
                clustered_csv=res["out_clustered_csv"],
                out_dir=out_dir,
                cfg=cfg,
            )
        else:
            print("[Gemma3/TF-IDF] Übersprungen, weil kein TF-IDF-Clustered-CSV vorhanden ist.")

        # 2) Gemma3 auf Embedding-Clustern
        if emb_res:
            faq_res_gemma_emb, gemma_emb_dir = _run_gemma3_for_source(
                label="embeddings",
                clustered_csv=emb_res["out_clustered_csv"],
                out_dir=out_dir,
                cfg=cfg,
            )
        else:
            print("[Gemma3/Embeddings] Übersprungen, weil kein Embeddings-Clustered-CSV vorhanden ist.")

    summary_out = write_run_summary(str(out_dir), cfg, tfidf_res=res, emb_res=emb_res)
    comp_out = write_comparison_table(str(out_dir), cfg, tfidf_res=res, emb_res=emb_res)
    print(f"Run summary: {summary_out['out_run_summary_md']}")
    print(f"Comparison:  {comp_out['out_comparison_md']}")

    ev_cfg = cfg.get("evaluation", {})
    if ev_cfg.get("enabled", True):
        n_clusters = int(ev_cfg.get("n_clusters", 8))
        examples = int(ev_cfg.get("examples_per_cluster", 3))

        if res and faq_res_tfidf:
            ev1 = write_evaluation_sheet(
                method="TF-IDF",
                clustered_csv_path=res["out_clustered_csv"],
                faq_json_path=faq_res_tfidf["out_faq_json"],
                out_csv_path=str(out_dir / "evaluation_tfidf.csv"),
                n_clusters=n_clusters,
                examples_per_cluster=examples,
            )
            print(f"Evaluation (TF-IDF): {ev1['out_evaluation_csv']}")

        if emb_res and faq_res_emb:
            emb_dir = out_dir / "embeddings"
            ev2 = write_evaluation_sheet(
                method="Embeddings",
                clustered_csv_path=emb_res["out_clustered_csv"],
                faq_json_path=faq_res_emb["out_faq_json"],
                out_csv_path=str(emb_dir / "evaluation_embeddings.csv"),
                n_clusters=n_clusters,
                examples_per_cluster=examples,
            )
            print(f"Evaluation (Embeddings): {ev2['out_evaluation_csv']}")

        if res and faq_res_gemma_tfidf and gemma_tfidf_dir:
            ev3 = write_evaluation_sheet(
                method="Gemma3 (TF-IDF)",
                clustered_csv_path=res["out_clustered_csv"],
                faq_json_path=faq_res_gemma_tfidf["out_faq_json"],
                out_csv_path=str(gemma_tfidf_dir / "evaluation_gemma3_tfidf.csv"),
                n_clusters=n_clusters,
                examples_per_cluster=examples,
            )
            print(f"Evaluation (Gemma3 / TF-IDF): {ev3['out_evaluation_csv']}")

        if emb_res and faq_res_gemma_emb and gemma_emb_dir:
            ev4 = write_evaluation_sheet(
                method="Gemma3 (Embeddings)",
                clustered_csv_path=emb_res["out_clustered_csv"],
                faq_json_path=faq_res_gemma_emb["out_faq_json"],
                out_csv_path=str(gemma_emb_dir / "evaluation_gemma3_embeddings.csv"),
                n_clusters=n_clusters,
                examples_per_cluster=examples,
            )
            print(f"Evaluation (Gemma3 / Embeddings): {ev4['out_evaluation_csv']}")


if __name__ == "__main__":
    main()
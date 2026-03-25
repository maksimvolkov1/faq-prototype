import numpy as np
import pandas as pd
import torch
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import TfidfVectorizer


# Stopwords
DE_STOPWORDS = {
    "und","oder","aber","wenn","dann","dass","der","die","das","ein","eine","einer","einem","einen",
    "ist","sind","war","waren","sein","im","in","am","an","auf","aus","bei","für","von","mit","ohne",
    "zu","zum","zur","des","den","dem","ich","du","er","sie","es","wir","ihr","mein","dein","sein",
    "kann","können","bitte","danke","hallo","hi","nicht","mehr","nur","auch","noch","heute","seit",
    "wird","wurde","werden","fehlt","geht","gehen","kommt","komme","mich","mir","uns","euch"
}


def _safe_l2_normalize(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    return v if n == 0 else (v / n)


def embed_cluster_and_report(df: pd.DataFrame, out_dir: str, cfg: dict) -> dict:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    texts = df["clean_text"].fillna("").astype(str).tolist()

    emb_cfg = cfg.get("embeddings", {})
    model_name = emb_cfg.get("model_name", "paraphrase-multilingual-MiniLM-L12-v2")
    batch_size = int(emb_cfg.get("batch_size", 32))
    normalize = bool(emb_cfg.get("normalize", True))

    # 1) Embeddings 
    #model = SentenceTransformer(model_name)
    # model = SentenceTransformer(model_name, device="cuda" if torch.cuda.is_available() else "cpu")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SentenceTransformer(model_name, device=device)
    print(f"[Embeddings] Using device: {device}")
    print(f"[Embeddings] Model: {model_name}")
    print(f"[Embeddings] Embedding dim: {model.get_sentence_embedding_dimension()}")
    
    E = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=normalize,
    )

    # 2) Clustering (KMeans, k aus config)
    cl_cfg = cfg.get("clustering", {})
    k = int(cl_cfg.get("k", 12))
    k = max(2, min(k, E.shape[0]))

    km = KMeans(n_clusters=k, random_state=int(cfg["project"]["seed"]), n_init=10)
    labels = km.fit_predict(E)

    df_out = df.copy()
    df_out["cluster_id"] = labels
    clustered_csv = out / "clustered_tickets_embeddings.csv"
    df_out.to_csv(clustered_csv, index=False, encoding="utf-8")

    # 3) Silhouette (cosine) 
    sil = None
    if len(set(labels)) > 1 and E.shape[0] > len(set(labels)):
        sil = float(silhouette_score(E, labels, metric="cosine"))

    # 4) Keywords pro Cluster
    tf_cfg = cfg.get("tfidf", {})
    ng = tuple(tf_cfg.get("ngram_range", [1, 2]))
    max_features = int(tf_cfg.get("max_features", 5000))

    X_kw = TfidfVectorizer(
        ngram_range=ng,
        max_features=max_features,
        min_df=int(tf_cfg.get("min_df", 1)),
        max_df=float(tf_cfg.get("max_df", 1.0)),
        sublinear_tf=bool(tf_cfg.get("sublinear_tf", False)),
        stop_words=list(DE_STOPWORDS),
    ).fit_transform(df_out["clean_text"].fillna("").astype(str).tolist())
    feature_names = np.array(TfidfVectorizer(
        ngram_range=ng,
        max_features=max_features,
        min_df=int(tf_cfg.get("min_df", 1)),
        max_df=float(tf_cfg.get("max_df", 1.0)),
        sublinear_tf=bool(tf_cfg.get("sublinear_tf", False)),
        stop_words=list(DE_STOPWORDS),
    ).fit(df_out["clean_text"].fillna("").astype(str).tolist()).get_feature_names_out())

    top_kw = int(emb_cfg.get("top_keywords", 6))
    top_ex = int(emb_cfg.get("top_examples", 3))

    # 5) Report schreiben
    lines = []
    lines.append("# Cluster Report (Embeddings + KMeans)\n\n")
    lines.append(f"- Tickets: {len(df_out)}\n")
    lines.append(f"- Cluster (k): {k}\n")
    lines.append(f"- Model: {model_name}\n")
    if sil is not None:
        lines.append(f"- Silhouette (cosine): {sil:.3f}\n")
    lines.append("\n")

    for cid in range(k):
        idx = np.where(labels == cid)[0]
        if len(idx) == 0:
            continue

        # Keywords ( TF-ID Cluster)
        mean_vec = np.asarray(X_kw[idx].mean(axis=0)).ravel()
        kw_idx = np.argsort(mean_vec)[::-1][:top_kw]
        keywords = feature_names[kw_idx].tolist()

        # Repräsentative Tickets
        centroid = E[idx].mean(axis=0)
        if normalize:
            centroid = _safe_l2_normalize(centroid)
            sims = E[idx] @ centroid  # dot == cosine bei normalisierten Vektoren
        else:
            sims = (E[idx] @ centroid) / (np.linalg.norm(E[idx], axis=1) * np.linalg.norm(centroid) + 1e-9)

        top_local = idx[np.argsort(sims)[::-1][:top_ex]]

        lines.append(f"## Cluster {cid} ({len(idx)} Tickets)\n")
        lines.append(f"**Keywords:** {', '.join(keywords)}\n\n")
        lines.append("**Beispiele:**\n")
        for j in top_local:
            tid = df_out.iloc[j]["ticket_id"]
            subj = df_out.iloc[j].get("subject", "")
            txt = df_out.iloc[j]["raw_text"]
            lines.append(f"- `{tid}` – {subj}\n")
            lines.append(f"  - {txt}\n")
        lines.append("\n")

    report_md = out / "cluster_report_embeddings.md"
    report_md.write_text("".join(lines), encoding="utf-8")

    return {
        "k": k,
        "silhouette_cosine": sil,
        "out_clustered_csv": str(clustered_csv),
        "out_report_md": str(report_md),
    }
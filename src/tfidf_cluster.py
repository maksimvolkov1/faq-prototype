import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity


# Stopword-Liste
DE_STOPWORDS = {
    "und","oder","aber","wenn","dann","dass","der","die","das","ein","eine","einer","einem","einen",
    "ist","sind","war","waren","sein","im","in","am","an","auf","aus","bei","für","von","mit","ohne",
    "zu","zum","zur","des","den","dem","ich","du","er","sie","es","wir","ihr","mein","dein","sein",
    "kann","können","bitte","danke","hallo","hi","nicht","mehr","nur","auch","noch","heute","seit",
    "wird","wurde","werden","fehlt","geht","gehen","kommt","komme","mich","mir","uns","euch"
}


def tfidf_cluster_and_report(df: pd.DataFrame, out_dir: str, cfg: dict) -> dict:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    texts = df["clean_text"].fillna("").astype(str).tolist()

    tf_cfg = cfg.get("tfidf", {})
    ng = tuple(tf_cfg.get("ngram_range", [1, 2]))
    max_features = int(tf_cfg.get("max_features", 2000))

    # Stopwords Clustering
    use_stopwords = bool(tf_cfg.get("use_stopwords", True))

    vectorizer = TfidfVectorizer(
        ngram_range=ng,
        max_features=max_features,
        min_df=int(tf_cfg.get("min_df", 1)),
        max_df=float(tf_cfg.get("max_df", 1.0)),
        sublinear_tf=bool(tf_cfg.get("sublinear_tf", False)),
        stop_words=list(DE_STOPWORDS) if use_stopwords else None,
    )
    X = vectorizer.fit_transform(texts)
    feature_names = np.array(vectorizer.get_feature_names_out())

    cl_cfg = cfg.get("clustering", {})
    k = int(cl_cfg.get("k", 6))
    k = max(2, min(k, X.shape[0]))

    model = KMeans(n_clusters=k, random_state=int(cfg["project"]["seed"]), n_init=10)
    labels = model.fit_predict(X)

    df_out = df.copy()
    df_out["cluster_id"] = labels
    df_out.to_csv(out / "clustered_tickets.csv", index=False, encoding="utf-8")

    sil = None
    if len(set(labels)) > 1 and X.shape[0] > len(set(labels)):
        sil = float(silhouette_score(X, labels, metric="cosine"))

    # Keywords pro Cluster über Zentroiden
    centroids = model.cluster_centers_  # shape (k, n_features)
    top_kw = int(tf_cfg.get("top_keywords", 6))
    top_ex = int(tf_cfg.get("top_examples", 3))

    lines = []
    lines.append("# Cluster Report (TF-IDF + KMeans)\n\n")
    lines.append(f"- Tickets: {len(df_out)}\n")
    lines.append(f"- Cluster (k): {k}\n")
    if sil is not None:
        lines.append(f"- Silhouette (cosine): {sil:.3f}\n")
    lines.append("\n")

    for cid in range(k):
        idx = np.where(labels == cid)[0]
        if len(idx) == 0:
            continue

        # Top Keywords
        centroid = centroids[cid]
        kw_idx = np.argsort(centroid)[::-1][:top_kw]
        keywords = feature_names[kw_idx].tolist()

        #  Beispiele
        sims = cosine_similarity(X[idx], centroid.reshape(1, -1)).ravel()
        top_idx_local = idx[np.argsort(sims)[::-1][:top_ex]]

        lines.append(f"## Cluster {cid} ({len(idx)} Tickets)\n")
        lines.append(f"**Keywords:** {', '.join(keywords)}\n\n")
        lines.append("**Beispiele:**\n")
        for j in top_idx_local:
            tid = df_out.iloc[j]["ticket_id"]
            subj = df_out.iloc[j].get("subject", "")
            txt = df_out.iloc[j]["raw_text"]
            lines.append(f"- `{tid}` – {subj}\n")
            lines.append(f"  - {txt}\n")
        lines.append("\n")

    (out / "cluster_report.md").write_text("".join(lines), encoding="utf-8")

    return {
        "k": k,
        "silhouette_cosine": sil,
        "out_clustered_csv": str(out / "clustered_tickets.csv"),
        "out_report_md": str(out / "cluster_report.md"),
    }

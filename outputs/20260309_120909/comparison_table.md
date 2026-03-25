# Vergleichstabelle (pro Run)

| Methode | Clusterbasis | FAQ-Typ | Modell | k | Silhouette(cosine) | Tickets | Cluster | min/avg/max | Details |
|---|---|---|---|---|---|---|---|---|---|
| TF-IDF | TF-IDF + KMeans | heuristisch | - | 12 | 0.121 | 85 | 12 | 3/7.1/13 | ng=[1, 2], maxf=8000, min_df=2, max_df=0.8, sublin=True |
| Embeddings | Embeddings + KMeans | heuristisch | BAAI/bge-m3 | 12 | 0.108 | 85 | 12 | 4/7.1/12 | Labeling/Keywords via TF-IDF |
| Gemma3 (TF-IDF) | TF-IDF + KMeans | LLM-gestützt | gemma3:4b | 12 | 0.121 | 85 | 12 | 3/7.1/13 | FAQ aus TF-IDF-Clustern via Gemma3 |
| Gemma3 (Embeddings) | Embeddings + KMeans | LLM-gestützt | gemma3:4b | 12 | 0.108 | 85 | 12 | 4/7.1/12 | FAQ aus Embedding-Clustern via Gemma3 |


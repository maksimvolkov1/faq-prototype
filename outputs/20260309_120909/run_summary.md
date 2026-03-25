# Run Summary

## 1) Datenbasis
- Input: `data/tickets3.csv`
- Seed: 42

## 2) Methode A: TF-IDF + KMeans
- k: 12
- TF-IDF: ngram_range=[1, 2], max_features=8000, min_df=2, max_df=0.8, sublinear_tf=True, stopwords=True
- Silhouette (cosine): **0.121**
- Cluster: 12 | Tickets: 85 | min/avg/max: 3/7.1/13
- Top-5 Clustergrößen: {1: 13, 2: 12, 8: 10, 3: 8, 7: 8}
- Artefakte:
  - Clustered CSV: `outputs\20260309_120909\clustered_tickets.csv`
  - Cluster Report: `outputs\20260309_120909\cluster_report.md`
  - FAQ (MD): `outputs\20260309_120909\faq_tfidf.md`
  - FAQ (JSON): `outputs\20260309_120909\faq_tfidf.json`
  - FAQ (CSV): `outputs\20260309_120909\faq_entries_tfidf.csv`

## 3) Methode B: Embeddings + KMeans
- k: 12
- Model: `BAAI/bge-m3`
- batch_size: 8 | normalize: True
- Silhouette (cosine): **0.108**
- Cluster: 12 | Tickets: 85 | min/avg/max: 4/7.1/12
- Top-5 Clustergrößen: {1: 12, 7: 11, 10: 8, 2: 7, 11: 7}
- Artefakte:
  - Clustered CSV: `outputs\20260309_120909\embeddings\clustered_tickets_embeddings.csv`
  - Cluster Report: `outputs\20260309_120909\embeddings\cluster_report_embeddings.md`
  - FAQ (MD): `outputs\20260309_120909\embeddings\faq_embeddings.md`
  - FAQ (JSON): `outputs\20260309_120909\embeddings\faq_embeddings.json`
  - FAQ (CSV): `outputs\20260309_120909\embeddings\faq_entries_embeddings.csv`

## 4) Methode C: Gemma3 auf TF-IDF-Clustern
- k: 12
- FAQ-Quelle: `TF-IDF-Cluster`
- LLM-Modell: `gemma3:4b`
- FAQ-Generierung: LLM-gestützt, Clusterbasis aus TF-IDF + KMeans
- Silhouette (cosine): **0.121**
- Cluster: 12 | Tickets: 85 | min/avg/max: 3/7.1/13
- Top-5 Clustergrößen: {1: 13, 2: 12, 8: 10, 3: 8, 7: 8}
- Artefakte:
  - Clustered CSV: `outputs\20260309_120909\clustered_tickets.csv`
  - Cluster Report: `outputs\20260309_120909\cluster_report.md`
  - FAQ (MD): `outputs\20260309_120909\gemma3\gemma3_tfidf\faq_gemma3_tfidf.md`
  - FAQ (JSON): `outputs\20260309_120909\gemma3\gemma3_tfidf\faq_gemma3_tfidf.json`
  - FAQ (CSV): `outputs\20260309_120909\gemma3\gemma3_tfidf\faq_entries_gemma3_tfidf.csv`

## 5) Methode D: Gemma3 auf Embedding-Clustern
- k: 12
- FAQ-Quelle: `Embedding-Cluster`
- LLM-Modell: `gemma3:4b`
- FAQ-Generierung: LLM-gestützt, Clusterbasis aus Embeddings + KMeans
- Silhouette (cosine): **0.108**
- Cluster: 12 | Tickets: 85 | min/avg/max: 4/7.1/12
- Top-5 Clustergrößen: {1: 12, 7: 11, 10: 8, 2: 7, 11: 7}
- Artefakte:
  - Clustered CSV: `outputs\20260309_120909\embeddings\clustered_tickets_embeddings.csv`
  - Cluster Report: `outputs\20260309_120909\embeddings\cluster_report_embeddings.md`
  - FAQ (MD): `outputs\20260309_120909\gemma3\gemma3_embeddings\faq_gemma3_embeddings.md`
  - FAQ (JSON): `outputs\20260309_120909\gemma3\gemma3_embeddings\faq_gemma3_embeddings.json`
  - FAQ (CSV): `outputs\20260309_120909\gemma3\gemma3_embeddings\faq_entries_gemma3_embeddings.csv`

## 6) Hinweise (Prototyp)
- Ergebnisse basieren auf synthetischen Supporttickets und dienen der prototypischen Evaluation.
- Keine Produktivlösung (kein Monitoring, keine Skalierung, kein kontinuierliches Lernen).
- Gemma3 ist kein eigenes Clustering-Verfahren, sondern eine alternative FAQ-Generierung auf Basis vorhandener Cluster.

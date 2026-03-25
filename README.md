# FAQ Generator (Bachelorarbeit)

Dieses Projekt ist ein prototypisches System zur automatisierten Generierung von FAQ-Einträgen aus Supporttickets im Rahmen einer Bachelorarbeit im Studiengang Informatik.

Ziel ist es, mithilfe von Methoden des Natural Language Processing (NLP) wiederkehrende Themen in textbasierten Supportanfragen zu identifizieren und daraus strukturierte FAQ-Einträge abzuleiten.

---

## 🔧 Features

- TF-IDF basierte Textrepräsentation und Clustering
- Embedding-basierte semantische Analyse (z. B. BGE-M3)
- Automatische Generierung von FAQ-Fragen und -Antworten
- Optional: LLM-gestützte Nachbearbeitung (z. B. Gemma3)
- Vergleich und Analyse der Methoden (Qualität & Laufzeit)

---

## 📁 Projektstruktur


```text
faq-prototyp/
│
├── src/         # Hauptlogik (Clustering, FAQ-Generierung, etc.)
├── configs/     # Konfigurationsdateien
├── data/        # Eingabedaten (Supporttickets)
├── outputs/     # Generierte Ergebnisse (Cluster, FAQ, Reports)
├── .gitignore
└── README.md
```

---

## Voraussetzungen
Python 3.x
Installierte Abhängigkeiten
Optional: GPU für schnellere Embedding-Berechnung

##  Nutzung

Ausführung des Prototyps:

```bash
.\.venv\Scripts\python.exe -m src.main


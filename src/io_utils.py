import pandas as pd
from pathlib import Path

# Heuristik
ANS_STARTERS = (
    "Bitte", "Gern", "Hallo", "Hi",
    "Ich habe", "Ich kann", "Für den Zugriff",
    "Tipp", "Hinweis"
)

EXPECTED_COLS = ["ticket_id","created_at","category","priority","status","subject","request_text","answer_text","tags"]

def _looks_misparsed(df: pd.DataFrame) -> bool:
    if "ticket_id" not in df.columns:
        return True
    s = df["ticket_id"].astype(str)
    return not s.str.startswith("TCK-").all()

def load_tickets(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p.resolve()}")

    # Versuch 1: mit pandas
    try:
        df = pd.read_csv(p, dtype=str, keep_default_na=False)
        if _looks_misparsed(df):
            raise ValueError("CSV appears to be misparsed (likely commas inside fields).")
        return df
    except Exception:
        # Fallback
        return load_tickets_robust(p)

def load_tickets_robust(p: Path) -> pd.DataFrame:
    rows = []
    with p.open("r", encoding="utf-8") as f:
        header = f.readline().strip()
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue

            parts = line.split(",")
            if len(parts) < 9:
                continue

            ticket_id, created_at, category, priority, status, subject = parts[:6]
            tags = parts[-1].strip()
            middle = parts[6:-1]  # request + answer

            ans_i = None
            for i in range(1, len(middle)):
                if middle[i].lstrip().startswith(ANS_STARTERS):
                    ans_i = i
                    break

            if ans_i is None:
                ans_i = 1 if len(middle) > 1 else len(middle)

            request_text = ",".join(middle[:ans_i]).strip()
            answer_text = ",".join(middle[ans_i:]).strip()

            rows.append({
                "ticket_id": ticket_id.strip(),
                "created_at": created_at.strip(),
                "category": category.strip(),
                "priority": priority.strip(),
                "status": status.strip(),
                "subject": subject.strip(),
                "request_text": request_text,
                "answer_text": answer_text,
                "tags": tags,
            })

    df = pd.DataFrame(rows)

    for c in df.columns:
        df[c] = df[c].fillna("").astype(str)
    return df

def save_df(df: pd.DataFrame, path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False, encoding="utf-8")
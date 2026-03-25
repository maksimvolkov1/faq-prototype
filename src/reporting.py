from pathlib import Path
import pandas as pd

def write_preprocessing_report(df: pd.DataFrame, out_dir: str) -> str:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    lengths = df["clean_text"].str.len()
    report = []
    report.append("# Preprocessing Report\n")
    report.append(f"- Tickets: {len(df)}\n")
    report.append(f"- Avg length (clean_text): {lengths.mean():.1f}\n")
    report.append(f"- Min/Max length: {lengths.min()} / {lengths.max()}\n\n")

    report.append("## Beispiele (raw -> clean)\n")
    sample = df.sample(min(5, len(df)), random_state=42)[["ticket_id", "raw_text", "clean_text"]]
    for _, row in sample.iterrows():
        report.append(f"### Ticket {row['ticket_id']}\n")
        report.append(f"**Raw:** {row['raw_text']}\n\n")
        report.append(f"**Clean:** {row['clean_text']}\n\n")

    report_path = out / "preprocessing_report.md"
    report_path.write_text("".join(report), encoding="utf-8")
    return str(report_path)

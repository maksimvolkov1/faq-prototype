import re
import pandas as pd

URL_RE = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)
MAIL_RE = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", re.IGNORECASE)
WS_RE = re.compile(r"\s+")

def clean_text(text: str,
               lowercase: bool = True,
               normalize_whitespace: bool = True,
               remove_urls: bool = True,
               remove_emails: bool = True,
               remove_non_alnum: bool = False) -> str:
    t = text or ""
    if lowercase:
        t = t.lower()
    if remove_urls:
        t = URL_RE.sub(" <URL> ", t)
    if remove_emails:
        t = MAIL_RE.sub(" <MAIL> ", t)
    if remove_non_alnum:
        t = re.sub(r"[^0-9a-zA-ZäöüÄÖÜß\s<>\-_/\.]", " ", t)

    if normalize_whitespace:
        t = WS_RE.sub(" ", t).strip()
    return t

def preprocess_tickets(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    df = df.copy()

    in_cfg = cfg.get("input", {})
    title_col = in_cfg.get("title_col", "title")
    body_col = in_cfg.get("body_col", "body")

    if title_col not in df.columns or body_col not in df.columns:
        raise ValueError(f"Missing columns for raw_text: {title_col=}, {body_col=}. Found: {list(df.columns)}")

    df["raw_text"] = (df[title_col].fillna("") + " " + df[body_col].fillna("")).str.strip()

    pp = cfg["preprocessing"]
    df["clean_text"] = df["raw_text"].apply(lambda x: clean_text(
        x,
        lowercase=pp.get("lowercase", True),
        normalize_whitespace=pp.get("normalize_whitespace", True),
        remove_urls=pp.get("remove_urls", True),
        remove_emails=pp.get("remove_emails", True),
        remove_non_alnum=pp.get("remove_non_alnum", False),
    ))

    min_len = int(pp.get("min_text_length", 0))
    if min_len > 0:
        df = df[df["clean_text"].str.len() >= min_len].reset_index(drop=True)

    return df

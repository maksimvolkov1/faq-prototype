import re

SUPPORT = "Der IT-Support"

# Häufige Agenten-Sätze -> neutral/KB-Stil
# Reihenfolge ist wichtig: spezifisch vor allgemein
_PATTERNS = [
    # Konto/Account
    (re.compile(r"^ich habe (dein|ihr|das) konto entsperrt\.?$", re.IGNORECASE),
     "Das Konto wurde entsperrt."),
    (re.compile(r"^ich habe (dein|ihr|das) konto gesperrt\.?$", re.IGNORECASE),
     "Das Konto wurde gesperrt."),
    (re.compile(r"^ich habe (dein|ihr|das) passwort zurückgesetzt\.?$", re.IGNORECASE),
     "Das Passwort wurde zurückgesetzt."),
    (re.compile(r"^ich habe (dein|ihr|das) passwort geändert\.?$", re.IGNORECASE),
     "Das Passwort wurde geändert."),

    # Allgemein: "Ich kann ..." -> Support kann ...
    (re.compile(r"^ich kann\b", re.IGNORECASE),
     f"{SUPPORT} kann"),

    # Allgemein: "Ich habe ..." -> Support hat ...
    (re.compile(r"^ich habe\b", re.IGNORECASE),
     f"{SUPPORT} hat"),

    # Allgemein: "Ich prüfe ..." -> Support prüft ...
    (re.compile(r"^ich prüfe\b", re.IGNORECASE),
     f"{SUPPORT} prüft"),

    # "Ich setze ..." / "Ich ändere ..." / "Ich weise ..." -> Support ...
    (re.compile(r"^ich setze\b", re.IGNORECASE),
     f"{SUPPORT} setzt"),
    (re.compile(r"^ich ändere\b", re.IGNORECASE),
     f"{SUPPORT} ändert"),
    (re.compile(r"^ich weise\b", re.IGNORECASE),
     f"{SUPPORT} weist"),
    (re.compile(r"^ich erstelle\b", re.IGNORECASE),
     f"{SUPPORT} erstellt"),
]

# "Sende/Schicke/Gib mir ..." -> "... dem IT-Support ..."
_TO_SUPPORT_PATTERNS = [
    (re.compile(r"\b(sende|schicke)\s+mir\b", re.IGNORECASE), r"\1 dem IT-Support"),
    (re.compile(r"\b(gib|nenne|bestätige)\s+mir\b", re.IGNORECASE), r"\1 dem IT-Support"),
    (re.compile(r"\b(sende|schicke)\s+uns\b", re.IGNORECASE), r"\1 dem IT-Support"),
    (re.compile(r"\b(gib|nenne|bestätige)\s+uns\b", re.IGNORECASE), r"\1 dem IT-Support"),
]

def neutralize_sentence(s: str) -> str:
    """Wandelt Agenten-Formulierungen in neutralen KB-Stil um."""
    s = (s or "").strip()
    if not s:
        return s

    # 1) Direkte "mir/uns" -> "dem IT-Support"
    for rx, rep in _TO_SUPPORT_PATTERNS:
        s = rx.sub(rep, s)

    # 2) Satzanfang umformen (Ich -> Support/Passiv)
    for rx, rep in _PATTERNS:
        if rx.search(s):
            s = rx.sub(rep, s)
            break

    return s
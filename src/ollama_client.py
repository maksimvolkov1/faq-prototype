from __future__ import annotations

import json
import re
from typing import Any, Dict
from urllib import request, error


class OllamaClientError(RuntimeError):
    pass


_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*(\{.*\}|\[.*\])\s*```", re.DOTALL)


def _extract_json_text(text: str) -> str:
    text = (text or "").strip()
    if not text:
        raise OllamaClientError("Leere Modellantwort erhalten.")

    m = _JSON_BLOCK_RE.search(text)
    if m:
        return m.group(1).strip()

    # Falls das Modell Text vor/nach dem JSON ausgibt
    start = min([i for i in [text.find("{"), text.find("[")] if i != -1], default=-1)
    if start == -1:
        raise OllamaClientError(f"Kein JSON in Modellantwort gefunden: {text[:300]}")

    end_obj = text.rfind("}")
    end_arr = text.rfind("]")
    end = max(end_obj, end_arr)
    if end == -1 or end < start:
        raise OllamaClientError(f"Unvollständiges JSON in Modellantwort gefunden: {text[:300]}")

    return text[start:end + 1].strip()


def chat_json(*, base_url: str, model: str, prompt: str, timeout_sec: int = 120, temperature: float = 0.2) -> Dict[str, Any]:
    url = base_url.rstrip("/") + "/api/chat"
    payload = {
        "model": model,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": temperature,
        },
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }

    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=timeout_sec) as resp:
            body = resp.read().decode("utf-8")
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise OllamaClientError(f"Ollama HTTP {exc.code}: {detail}") from exc
    except error.URLError as exc:
        raise OllamaClientError(
            "Ollama ist nicht erreichbar. Läuft der Dienst lokal unter http://localhost:11434?"
        ) from exc

    try:
        raw = json.loads(body)
    except json.JSONDecodeError as exc:
        raise OllamaClientError(f"Antwort von Ollama ist kein gültiges JSON: {body[:500]}") from exc

    content = raw.get("message", {}).get("content", "")
    json_text = _extract_json_text(content)

    try:
        return json.loads(json_text)
    except json.JSONDecodeError as exc:
        raise OllamaClientError(f"Modellinhalt ist kein gültiges JSON: {json_text[:500]}") from exc

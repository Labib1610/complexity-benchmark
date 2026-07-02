"""Generation backends: ollama (local) and api (Anthropic). Factory: generate()."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

OLLAMA_BASE = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
ANTHROPIC_BASE = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")

_DEFAULT_RETRIES = 3
_BASE_DELAY_S = 2.0
_HTTP_TIMEOUT_S = 300


def _post_json(url: str, payload: dict, extra_headers: dict | None = None) -> dict:
    body = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT_S) as resp:
        return json.loads(resp.read().decode())


def _with_backoff(fn, retries: int = _DEFAULT_RETRIES, base_delay: float = _BASE_DELAY_S) -> str:
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            return fn()
        except Exception as exc:
            last_err = exc
            if attempt < retries - 1:
                time.sleep(base_delay * (2 ** attempt))
    print(f"[backends] hard failure after {retries} attempts: {last_err}")
    return ""


def _ollama(model_string: str, system: str, user: str,
            max_tokens: int, temperature: float) -> str:
    # Stream the response: partial-CPU 32B/20B models can take well over the
    # per-request timeout to finish, and with stream=False Ollama sends nothing
    # until the whole reply is done, so the socket read times out before any
    # bytes arrive. Streaming NDJSON keeps data flowing, so the timeout below
    # acts as an inter-chunk (idle) timeout instead of a whole-response one.
    url = f"{OLLAMA_BASE}/api/chat"
    payload = {
        "model": model_string,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": True,
        "options": {
            "num_predict": max_tokens,
            "num_ctx": max_tokens + 2048,
            "temperature": temperature,
        },
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    parts: list[str] = []
    with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT_S) as resp:
        for line in resp:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line.decode())
            msg = obj.get("message") or {}
            if msg.get("content"):
                parts.append(msg["content"])
            if obj.get("error"):
                raise RuntimeError(f"ollama error: {obj['error']}")
            if obj.get("done"):
                break
    return "".join(parts)


def _api(model_string: str, system: str, user: str,
         max_tokens: int, temperature: float) -> str:
    url = f"{ANTHROPIC_BASE}/v1/messages"
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    payload = {
        "model": model_string,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
        "temperature": temperature,
    }
    resp = _post_json(url, payload, extra_headers=headers)
    return "".join(
        block["text"] for block in resp.get("content", [])
        if block.get("type") == "text"
    )


def generate(
    backend: str,
    model_string: str,
    system: str,
    user: str,
    max_tokens: int,
    temperature: float,
    thinking: bool = False,
) -> str:
    """Call the appropriate backend and return the raw assistant response text."""
    if backend == "ollama":
        fn = lambda: _ollama(model_string, system, user, max_tokens, temperature)
    elif backend == "api":
        fn = lambda: _api(model_string, system, user, max_tokens, temperature)
    else:
        raise ValueError(f"unknown backend: {backend!r}")
    return _with_backoff(fn)

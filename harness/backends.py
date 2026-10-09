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
            max_tokens: int, temperature: float, seed: int | None = None) -> str:
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
            # Audit B9: forward the run seed so generation is reproducible on Ollama.
            **({"seed": seed} if seed is not None else {}),
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


def _resolve_key(name: str) -> str:
    """Resolve an API key from agentic/config/local_secrets.py, then the environment.
    Mirrors agentic.tools.backends.get_key; the key value is never printed."""
    val = ""
    try:
        import agentic.config.local_secrets as _sec  # optional; may not exist
        v = getattr(_sec, name, None)
        if v and not str(v).startswith("PASTE_"):
            val = v
    except Exception:
        pass
    if not val:
        val = os.environ.get(name, "")
    if not val:
        raise RuntimeError(f"API key {name} is not set (local_secrets.py or env var)")
    return val


def _openai_compat(model_string: str, system: str, user: str, max_tokens: int,
                   temperature: float, base_url: str, api_key: str,
                   reasoning: dict | None = None) -> str:
    """OpenAI-compatible /chat/completions (OpenRouter, OpenAI, Gemini-openai, etc.)."""
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model_string,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if reasoning:
        payload["reasoning"] = reasoning         # OpenRouter reasoning control (cap/exclude)
    resp = _post_json(url, payload, extra_headers={"Authorization": f"Bearer {api_key}"})
    choices = resp.get("choices") or []
    if not choices:
        raise RuntimeError(f"openai_compat: empty choices ({str(resp)[:200]})")
    return choices[0].get("message", {}).get("content", "") or ""


def generate(
    backend: str,
    model_string: str,
    system: str,
    user: str,
    max_tokens: int,
    temperature: float,
    thinking: bool = False,
    seed: int | None = None,
    base_url: str | None = None,
    api_key_env: str | None = None,
    reasoning: dict | None = None,
) -> str:
    """Call the appropriate backend and return the raw assistant response text.

    Audit B9: `seed` is forwarded to backends that support deterministic sampling (Ollama).
    The Anthropic Messages API has no seed parameter, so `api` generation stays best-effort
    reproducible via temperature only; that limitation is recorded in gen_meta.
    """
    if backend == "ollama":
        fn = lambda: _ollama(model_string, system, user, max_tokens, temperature, seed=seed)
    elif backend == "api":
        fn = lambda: _api(model_string, system, user, max_tokens, temperature)
    elif backend == "openai_compat":
        if not base_url or not api_key_env:
            raise ValueError("openai_compat backend needs base_url and api_key_env in the registry")
        api_key = _resolve_key(api_key_env)
        fn = lambda: _openai_compat(model_string, system, user, max_tokens, temperature,
                                    base_url, api_key, reasoning=reasoning)
    else:
        raise ValueError(f"unknown backend: {backend!r}")
    return _with_backoff(fn)

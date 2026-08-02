"""Model backends and shared helpers for the agentic phase.

Two backends behind one `chat()` function: an OpenAI-compatible HTTP endpoint
(used for the Gemini teacher/verifier/student) and local Ollama. `chat()` never
raises on failure -- it returns {text, raw, elapsed_s, error} so drivers can record
the failure and continue.

Text post-processing (strip_thinking / extract_code) reuses the existing harness so
we do not reimplement it; extract_json is added here for parsing teacher/verifier
JSON replies.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# --- paths ------------------------------------------------------------------
HERE = Path(__file__).resolve()
AGENTIC = HERE.parents[1]          # .../agentic
ROOT = HERE.parents[2]             # project root (contains dataset/, harness/)
for _p in (str(ROOT), str(AGENTIC)):   # AGENTIC on path so `config` package imports
    if _p not in sys.path:
        sys.path.insert(0, _p)

# Reuse the existing harness text utilities (do not reimplement).
from harness.extract import strip_thinking, extract_code  # noqa: E402

# Local secrets file (gitignored). Optional: keys may also come from the env.
try:
    from config import local_secrets as _secrets  # noqa: E402
except ImportError:
    _secrets = None

CONFIG_DIR = AGENTIC / "config"
SEEDS_DIR = AGENTIC / "seeds"
VERSIONS_DIR = AGENTIC / "versions"
ATTEMPTS_DIR = AGENTIC / "attempts"
REPORTS_DIR = AGENTIC / "reports"
STRATEGIES_DIR = AGENTIC / "strategies"
PROMPTS_DIR = AGENTIC / "prompts"
LOGS_DIR = AGENTIC / "logs"
TESTS_DIR = AGENTIC / "tests"      # universal per-problem test store (adversarial cases)


# --- config -----------------------------------------------------------------
def _load_yaml(path: Path) -> dict:
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)


def load_models() -> dict:
    return _load_yaml(CONFIG_DIR / "models.yaml")


def load_run_config() -> dict:
    return _load_yaml(CONFIG_DIR / "run_config.yaml")


def family_slug(family: str) -> str:
    """Map a family id like '01' to its dataset/seeds directory name."""
    matches = sorted(SEEDS_DIR.glob(f"family_{family}_*"))
    if matches:
        return matches[0].name
    matches = sorted((ROOT / "dataset").glob(f"family_{family}_*"))
    if matches:
        return matches[0].name
    raise FileNotFoundError(f"no family directory for id {family!r}")


def criterion_dirname(n: int) -> str:
    return {1: "criterion_1_npc", 2: "criterion_2_p", 3: "criterion_3_infeasible"}[n]


def list_families(arg: str) -> list[str]:
    """Resolve a --family argument to a list of family ids. 'all' enumerates seeds."""
    if arg != "all":
        return [arg]
    dirs = sorted(SEEDS_DIR.glob("family_*"))
    if not dirs:
        dirs = sorted((ROOT / "dataset").glob("family_*"))
    return [d.name.split("_")[1] for d in dirs]


# --- secrets ----------------------------------------------------------------
def get_key(name: str) -> str:
    """Resolve an API key: local_secrets.py, then env var, then fail loudly.

    A placeholder that was never replaced (PASTE_...) is treated as absent so it
    falls through to the env var and then to a clear error -- never an empty
    Authorization header. The key itself is never printed or logged.
    """
    val = getattr(_secrets, name, None) if _secrets else None
    if not val or str(val).startswith("PASTE_"):
        val = os.environ.get(name, "")
    if not val:
        raise RuntimeError(
            f"{name} is not set. Add it to agentic/config/local_secrets.py "
            f"(copy from local_secrets.example.py) or export {name}."
        )
    return val


def ollama_host() -> str:
    """Resolve the Ollama endpoint: local_secrets, then env, then localhost."""
    val = getattr(_secrets, "OLLAMA_HOST", None) if _secrets else None
    if not val or str(val).startswith("PASTE_"):
        val = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    return val.rstrip("/")


# --- HTTP -------------------------------------------------------------------
def _post_json(url: str, payload: dict, headers: dict, timeout: float) -> dict:
    body = json.dumps(payload).encode()
    h = {"Content-Type": "application/json"}
    h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _openai_compat(cfg: dict, system: str, user: str, timeout: float) -> str:
    base = cfg["base_url"].rstrip("/") + "/"
    url = base + "chat/completions"
    api_key = get_key(cfg["api_key_env"])
    payload = {
        "model": cfg["model_string"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": cfg.get("temperature", 0.7),
        "max_tokens": cfg.get("max_tokens", 4096),
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    # Optional provider headers (e.g. OpenRouter's HTTP-Referer / X-Title ranking
    # headers): set `extra_headers:` on the model entry in models.yaml.
    headers.update(cfg.get("extra_headers") or {})
    resp = _post_json(url, payload, headers, timeout)
    msg = resp["choices"][0]["message"]
    content = msg.get("content") or ""
    # Some providers (OpenRouter/OpenAI reasoning models) return the chain-of-thought
    # in a separate `reasoning` field. Inline it as <think>...</think> so the trace is
    # captured (trace.txt) while extract_code still strips it to get clean code.
    reasoning = msg.get("reasoning") or msg.get("reasoning_content") or ""
    if reasoning:
        content = f"<think>\n{reasoning.strip()}\n</think>\n{content}"
    return content


def _ollama(cfg: dict, system: str, user: str, timeout: float) -> str:
    url = f"{ollama_host()}/api/chat"
    payload = {
        "model": cfg["model_string"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"num_predict": cfg.get("max_tokens", 4096)},
    }
    resp = _post_json(url, payload, {}, timeout)
    return resp["message"]["content"]


def chat(model_cfg: dict, system: str, user: str,
         timeout: float | None = None, retries: int = 3) -> dict:
    """Call the configured backend. Returns {text, raw, elapsed_s, error}.

    Never raises: on hard failure returns text="" and a populated error string.
    """
    backend = model_cfg["backend"]
    timeout = timeout if timeout is not None else 1800
    t0 = time.time()
    last_err = None
    for attempt in range(retries):
        try:
            if backend == "openai_compat":
                raw = _openai_compat(model_cfg, system, user, timeout)
            elif backend == "ollama":
                raw = _ollama(model_cfg, system, user, timeout)
            else:
                return {"text": "", "raw": "", "elapsed_s": 0.0,
                        "error": f"unknown backend {backend!r}"}
            return {"text": raw, "raw": raw,
                    "elapsed_s": round(time.time() - t0, 3), "error": None}
        except Exception as exc:  # noqa: BLE001 - report, never crash the driver
            last_err = exc
            if attempt < retries - 1:
                time.sleep(2.0 * (2 ** attempt))
    return {"text": "", "raw": "", "elapsed_s": round(time.time() - t0, 3),
            "error": f"{type(last_err).__name__}: {last_err}"}


# --- parsing ----------------------------------------------------------------
_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)


def extract_json(text: str) -> dict:
    """Best-effort JSON object from a model reply. Handles ```json fences, extra
    prose, and raw newlines inside string values. Returns {} on failure."""
    text = strip_thinking(text)
    m = _FENCE.search(text)
    if m:                       # take the fenced block's full content (not just up to
        text = m.group(1)       # the first '}', which truncated nested objects before)
    start = text.find("{")
    end = text.rfind("}")       # outermost object
    if start == -1 or end <= start:
        return {}
    candidate = text[start:end + 1]
    # strict=False tolerates raw control chars (literal newlines/tabs) inside strings,
    # common when a model puts multi-line stdin in an "input" field.
    for strict in (True, False):
        try:
            return json.loads(candidate, strict=strict)
        except json.JSONDecodeError:
            continue
    return {}


__all__ = [
    "AGENTIC", "ROOT", "CONFIG_DIR", "SEEDS_DIR", "VERSIONS_DIR", "ATTEMPTS_DIR",
    "REPORTS_DIR", "STRATEGIES_DIR", "PROMPTS_DIR", "LOGS_DIR",
    "load_models", "load_run_config", "family_slug", "criterion_dirname",
    "get_key", "ollama_host",
    "chat", "strip_thinking", "extract_code", "extract_json",
]

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


_NITRO = None


def _openrouter_nitro() -> bool:
    """Cached global toggle for OpenRouter :nitro routing (execution.openrouter_nitro)."""
    global _NITRO
    if _NITRO is None:
        try:
            _NITRO = bool(load_models().get("execution", {}).get("openrouter_nitro", False))
        except Exception:
            _NITRO = False
    return _NITRO


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


# --- LiteLLM backend --------------------------------------------------------
# All model calls go through litellm.completion, which normalizes token usage and cost
# across providers (OpenRouter, OpenAI, Gemini, Ollama). drop_params lets litellm strip
# params a given model rejects (e.g. temperature on OpenAI reasoning models, max_tokens ->
# max_completion_tokens) so we don't hand-maintain per-provider quirks.
import litellm  # noqa: E402

litellm.drop_params = True
litellm.suppress_debug_info = True
litellm.telemetry = False


def _litellm_target(cfg: dict):
    """Map a model entry to (litellm_model, api_key, api_base, extra_body). The provider is
    inferred from base_url so litellm can attach the correct pricing for cost accounting."""
    base = cfg.get("base_url", "") or ""
    ms = cfg["model_string"]
    backend = cfg.get("backend")
    extra_body: dict = {}

    if backend == "ollama":
        return "ollama/" + ms, None, ollama_host(), extra_body

    if "openrouter.ai" in base:
        # :nitro routing (execution.openrouter_nitro or per-model nitro: true)
        if (cfg.get("nitro") or _openrouter_nitro()) and not ms.endswith(":nitro"):
            ms += ":nitro"
        model = "openrouter/" + ms
        # reasoning control: explicit dict passed verbatim (kimi's mandatory reasoning uses
        # {exclude:true, effort:low}); otherwise thinking: -> {enabled: bool}
        if isinstance(cfg.get("reasoning"), dict):
            extra_body["reasoning"] = cfg["reasoning"]
        elif "thinking" in cfg:
            extra_body["reasoning"] = {"enabled": bool(cfg["thinking"])}
        extra_body["usage"] = {"include": True}   # make OpenRouter return actual cost
    elif "generativelanguage" in base:
        model = "gemini/" + ms
    elif "api.openai.com" in base:
        model = ms                                # litellm native OpenAI (has pricing)
    else:
        model = "openai/" + ms                    # generic OpenAI-compatible endpoint

    api_base = base or None if backend != "ollama" else ollama_host()
    # For native openrouter/gemini/openai routes litellm knows the base; only pass api_base
    # for the generic openai-compatible fallback.
    if "openrouter.ai" in base or "generativelanguage" in base or "api.openai.com" in base:
        api_base = None
    key = None if backend == "ollama" else get_key(cfg["api_key_env"])
    return model, key, api_base, extra_body


def _usage_of(resp) -> dict:
    """Pull input/output/thinking tokens and cost out of a litellm response."""
    inp = out = think = cost = None
    u = getattr(resp, "usage", None)
    if u is not None:
        inp = getattr(u, "prompt_tokens", None)
        out = getattr(u, "completion_tokens", None)
        ctd = getattr(u, "completion_tokens_details", None)
        if ctd is not None:
            think = (ctd.get("reasoning_tokens") if isinstance(ctd, dict)
                     else getattr(ctd, "reasoning_tokens", None))
    try:
        cost = litellm.completion_cost(completion_response=resp)
    except Exception:
        cost = None
    if not cost:   # OpenRouter returns the real cost in hidden params
        hp = getattr(resp, "_hidden_params", {}) or {}
        cost = hp.get("response_cost") or cost
    return {"input_tokens": inp, "output_tokens": out,
            "thinking_tokens": think, "cost": cost}


def usage_of(resp: dict) -> dict:
    """Flat usage fields from a chat() result, for callers to merge into their JSON."""
    return {k: resp.get(k) for k in ("input_tokens", "output_tokens",
                                     "thinking_tokens", "cost", "elapsed_s")}


def _empty_usage() -> dict:
    return {"input_tokens": None, "output_tokens": None, "thinking_tokens": None, "cost": None}


def chat(model_cfg: dict, system: str, user: str,
         timeout: float | None = None, retries: int = 3) -> dict:
    """Call the model via litellm. Returns
    {text, raw, elapsed_s, error, input_tokens, output_tokens, thinking_tokens, cost}.
    Never raises: on hard failure returns text="" and a populated error string.
    """
    timeout = timeout if timeout is not None else 1800
    model, key, api_base, extra_body = _litellm_target(model_cfg)
    kwargs = dict(model=model, timeout=timeout,
                  messages=[{"role": "system", "content": system},
                            {"role": "user", "content": user}])
    if key:
        kwargs["api_key"] = key
    if api_base:
        kwargs["api_base"] = api_base
    # Reasoning models (reasoning_effort set, e.g. OpenAI gpt-5.6-*) reject temperature != 1
    # and top_p. litellm only auto-drops these for models it knows in its map; an unknown
    # reasoning model (e.g. gpt-5.6-sol) would still get temperature=0 -> 400. So we simply
    # never send sampling params for reasoning models.
    if model_cfg.get("reasoning_effort"):
        kwargs["reasoning_effort"] = model_cfg["reasoning_effort"]
    else:
        if model_cfg.get("temperature") is not None:
            kwargs["temperature"] = model_cfg["temperature"]
        if model_cfg.get("top_p") is not None:
            kwargs["top_p"] = model_cfg["top_p"]
    if model_cfg.get("max_tokens"):
        kwargs["max_tokens"] = model_cfg["max_tokens"]
    if extra_body:
        kwargs["extra_body"] = extra_body

    t0 = time.time()
    last_err = None
    for attempt in range(retries):
        try:
            resp = litellm.completion(**kwargs)
            msg = resp.choices[0].message
            content = msg.content or ""
            # reasoning is returned separately; inline as <think> so trace.txt captures it
            # while extract_code strips it to get clean code.
            reasoning = getattr(msg, "reasoning_content", None) or getattr(msg, "reasoning", None) or ""
            if reasoning:
                content = f"<think>\n{str(reasoning).strip()}\n</think>\n{content}"
            return {"text": content, "raw": content,
                    "elapsed_s": round(time.time() - t0, 3), "error": None,
                    **_usage_of(resp)}
        except Exception as exc:  # noqa: BLE001 - report, never crash the driver
            last_err = exc
            if attempt < retries - 1:
                time.sleep(2.0 * (2 ** attempt))
    return {"text": "", "raw": "", "elapsed_s": round(time.time() - t0, 3),
            "error": f"{type(last_err).__name__}: {last_err}", **_empty_usage()}


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
    "chat", "usage_of", "strip_thinking", "extract_code", "extract_json",
]

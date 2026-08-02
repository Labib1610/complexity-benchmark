# 44 — Agentic Phase: API Key Handling

> **Build files only. Do not run anything, do not call any API.** The user pastes real
> keys in afterwards.

## Goal

One local file holding all API keys, ignored by git, with obvious placeholders. The
teacher, the verifier, and the closed-source student all currently use the same Gemini
platform, so one key covers all three — but the file is structured so other providers
can be added later without touching code.

## 1. `agentic/config/local_secrets.py` — the real file (gitignored)

Create it with placeholders, not real keys:

```python
# Local API keys. NOT committed - see .gitignore.
# Replace the placeholder strings below with real keys.

# Gemini (OpenAI-compatible endpoint).
# Currently used by: teacher, verifier, and the closed-source student.
GEMINI_API_KEY = "PASTE_GEMINI_KEY_HERE"

# Added later - leave as-is until used.
OPENAI_API_KEY = "PASTE_OPENAI_KEY_HERE"
ANTHROPIC_API_KEY = "PASTE_ANTHROPIC_KEY_HERE"
OPENROUTER_API_KEY = "PASTE_OPENROUTER_KEY_HERE"

# Optional: override the local Ollama endpoint.
OLLAMA_HOST = "http://localhost:11434"
```

## 2. `agentic/config/local_secrets.example.py` — the committed template

Identical file, placeholders only, committed so a collaborator knows the shape. Add a
one-line header: copy this to `local_secrets.py` and fill in your keys.

## 3. `.gitignore`

Append to the project root `.gitignore`:

```
agentic/config/local_secrets.py
```

Keep `local_secrets.example.py` tracked. Verify with `git status` that the real file is
ignored and the example is not.

## 4. Key resolution in `tools/backends.py`

Resolve in this order: local file, then environment variable, then fail with a clear
message. Never print a key.

```python
import os

try:
    from config import local_secrets as _s
except ImportError:
    _s = None

def get_key(name: str) -> str:
    val = getattr(_s, name, None) if _s else None
    if not val or val.startswith("PASTE_"):
        val = os.environ.get(name, "")
    if not val:
        raise RuntimeError(
            f"{name} is not set. Add it to agentic/config/local_secrets.py "
            f"(copy from local_secrets.example.py) or export {name}."
        )
    return val
```

A placeholder that was never replaced falls through to the env var and then to the error,
so a forgotten key fails loudly instead of sending an empty Authorization header.

`models.yaml` already names the variable per model via `api_key_env`. `backends.py` calls
`get_key(model_cfg["api_key_env"])` — so adding a provider is a `models.yaml` entry plus
a line in `local_secrets.py`, never a code change.

## 5. Startup check

Add `tools/check_keys.py`:

```
python tools/check_keys.py
```

For every enabled model in `models.yaml`, report whether its key resolves — printing
`ok` or `missing`, never the key itself. Also report whether Ollama is reachable. The
user runs this once after pasting keys, before the pipeline.

## 6. README note

In `agentic/README.md`, add a short setup step:

```
cp config/local_secrets.example.py config/local_secrets.py
# edit config/local_secrets.py and replace the PASTE_..._HERE placeholders
python tools/check_keys.py
```

## Constraints

- Never write a real key into any file.
- Never log, print, or include a key in an error message.
- Do not commit `local_secrets.py`.

## Done

Create the files, confirm `git status` ignores the real one, run nothing. Then stop.

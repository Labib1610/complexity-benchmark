# Adding or Changing Models

This project has **two independent model registries**. Adding or changing a model is a
**config edit only** — never a code change. Model names never appear in code.

| Registry | File | Used by | Backends supported |
|----------|------|---------|--------------------|
| **Main study** | `models/registry.yaml` | `harness/generate.py`, `harness/evaluate.py` (the 48-problem benchmark) | `ollama`, `api` (Anthropic) |
| **Agentic phase** | `agentic/config/models.yaml` | `agentic/tools/*` (teacher / verifier / students) | `ollama`, `openai_compat` |

After any edit, verify the file parses: `python -c "import yaml;yaml.safe_load(open('<file>'))"`.

---

## Platform 1 — Ollama (local models)

Used in **both** registries. Ollama must be running (`ollama serve`) and the model
pulled locally.

1. Pull the model once:
   ```bash
   ollama pull qwen3:32b
   ollama list                 # confirm the exact "name:tag" string
   ```
2. Add an entry.

**Main study** (`models/registry.yaml`) — the `id` becomes the folder name under
`runs/<date>/generations/<id>/`:
```yaml
  - id: qwen3-32b            # your label (no colons; used as a path)
    display_name: "Qwen3 32B"
    backend: ollama
    model_string: "qwen3:32b"   # EXACT name from `ollama list`
    openness: open
    thinking: true              # true for reasoning models -> <think> stripped, bigger budget
    token_budget: 12288         # reasoning: 12288; standard: 4096
    notes: "reasoning model; strip <think> blocks"
```

**Agentic** (`agentic/config/models.yaml`, under `students:`):
```yaml
  - id: qwen3-32b
    backend: ollama
    model_string: "qwen3:32b"
    thinking: true
    max_tokens: 12288
    enabled: true               # set false to skip without deleting
```

- Non-default host/port: export `OLLAMA_HOST=http://host:port` (agentic) or
  `OLLAMA_BASE_URL=http://host:port` (main study). No file edit needed.
- Ollama students run **sequentially** in the agentic phase until you set
  `execution.ollama_parallel: true` and raise `execution.ollama_max_workers`.

---

## Platform 2 — OpenAI-compatible endpoints (Gemini, and any OpenAI-style API)

Used in the **agentic** registry only (teacher, verifier, students). The backend POSTs
to `{base_url}chat/completions` with an `Authorization: Bearer <key>` header.

1. Put the key in the environment (never in the file):
   ```bash
   export GEMINI_API_KEY=...          # name must match api_key_env below
   ```
2. Add/replace an entry (`agentic/config/models.yaml`):
```yaml
  - id: gemini-3-flash-lite
    backend: openai_compat
    base_url: "https://generativelanguage.googleapis.com/v1beta/openai/"  # note trailing slash
    model_string: "gemini-3-flash-lite"   # the provider's model id
    api_key_env: GEMINI_API_KEY           # env var the key is read from
    thinking: false
    max_tokens: 4096
    enabled: true
```
- To use a different OpenAI-compatible provider (OpenAI, Together, Groq, …): change
  `base_url`, `model_string`, and `api_key_env` (e.g. `OPENAI_API_KEY`). Nothing else.

**OpenRouter** (host the big models in the cloud instead of local Ollama — much faster
than a partly-CPU GPU). Put `OPENROUTER_API_KEY` in `local_secrets.py`, then add students:
```yaml
  - id: qwen3-32b-or                # any label
    backend: openai_compat
    base_url: "https://openrouter.ai/api/v1/"
    model_string: "qwen/qwen3-32b"  # an OpenRouter model id (see openrouter.ai/models)
    api_key_env: OPENROUTER_API_KEY
    thinking: true
    max_tokens: 12288
    enabled: true
    extra_headers:                  # optional, for OpenRouter leaderboard attribution
      HTTP-Referer: "https://your-site"
      X-Title: "complexity-benchmark"
```
Because these run over the API, they can run **concurrently** (`api_parallel: true`,
`api_max_workers`) — no need for the sequential Ollama path.
- The **teacher** and **verifier** are top-level keys (`teacher:`, `verifier:`) with the
  same fields plus `temperature` (teacher 0.9 for diversity, verifier 0.0 for
  consistency). Swapping either is just editing that block.

---

## Platform 3 — Anthropic API (Claude)

Used in the **main study** registry only (`backend: api`).

1. Export the key:
   ```bash
   export ANTHROPIC_API_KEY=...
   ```
2. Fill the entry in `models/registry.yaml` (it ships as a `<FILL>` placeholder):
```yaml
  - id: claude
    display_name: "Claude"
    backend: api
    model_string: "claude-<real-model-id>"   # replace <FILL> with a real id
    openness: closed
    thinking: false
    token_budget: 4096
    notes: ""
```
- Endpoint is `https://api.anthropic.com` by default; override with
  `ANTHROPIC_BASE_URL` if needed.

---

## Field reference

| Field | Where | Meaning |
|-------|-------|---------|
| `id` | both | Your label. In the main study it is also the generations sub-folder, so keep it filesystem-safe (no `:` `/`). |
| `backend` | both | `ollama` \| `api` (main) \| `openai_compat` (agentic). Selects the code path. |
| `model_string` | both | The provider's exact model identifier. |
| `token_budget` / `max_tokens` | main / agentic | Max generation tokens. Reasoning models need ~12288; standard ~4096. |
| `thinking` | both | `true` for reasoning models → `<think>`/`<thinking>` blocks are stripped before extracting code. |
| `api_key_env` | openai_compat | Name of the env var holding the key (key value never stored in the file). |
| `base_url` | openai_compat | Endpoint base (keep the trailing slash). |
| `enabled` | agentic students | `false` skips the student without deleting the entry. |
| `openness` | main | `open` \| `closed` (bookkeeping only). |

## Enable / disable / remove

- **Disable temporarily (agentic student):** set `enabled: false`.
- **Remove:** delete the list entry.
- **Run one model:** `--only <id>` on `harness.generate` / `harness.evaluate` (main) or
  `run_students.py` (agentic).

## After editing — sanity check

```bash
# main study
python -m harness.generate --config runs/<date>/run_config.yaml --only <id> --sample 1

# agentic (renders teacher prompts without any API call)
cd agentic && python tools/generate_versions.py --family 01 --criterion 1 --dry-run
```
If an Ollama call returns empty text, the model name is wrong or Ollama isn't running;
if an API call errors, the key env var is unset or the `base_url`/`model_string` is off.

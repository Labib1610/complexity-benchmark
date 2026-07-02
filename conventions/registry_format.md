# Model Registry Format

`models/registry.yaml` lists every research model. The generation driver reads
it. Two backends: `ollama` (local open-source) and `api` (closed-source).

## Schema
```yaml
models:
  - id: phi4                      # unique short id (used in folder paths)
    display_name: "Phi-4"
    backend: ollama               # ollama | api
    model_string: "phi4"          # ollama tag or API model id
    openness: open                # open | closed
    thinking: false               # true for reasoning models (R1, qwen3, gpt-oss)
    token_budget: 4096            # default max generation tokens
    notes: ""

  - id: claude-sonnet
    display_name: "Claude Sonnet"
    backend: api
    model_string: "claude-sonnet-4-6"
    openness: closed
    thinking: false
    token_budget: 4096
    notes: ""
```

## Rules
- `id` is the directory-safe key used under `generations/<id>/...`.
- `thinking: true` models get elevated `token_budget` and their chain-of-thought
  is stripped before code extraction (handled in the driver).
- Adding a model = adding a list entry. Never edit harness logic to add a model.

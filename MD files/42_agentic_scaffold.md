# 42 — Agentic Hardening Phase: Scaffold

> **You are Claude Code. Build the scaffolding only. Do NOT run any generation, do NOT
> call any API, do NOT execute the pipeline.** The user runs it manually after adding
> API keys, and only for Family 01.

## Scope

A new, self-contained phase folder `agentic/` at the project root. It reads seed
problems from the existing `dataset/` but never writes to it. Family 01 only for now.

Key decisions already made — implement these, don't re-derive:
- Seed test cases are the **small original cases only** (`01`–`04`). Do not copy the
  large scaled cases into this phase.
- Teacher: Gemini via an **OpenAI-compatible endpoint**.
- Students: one Gemini model + Ollama models.
- Ollama runs **sequentially** for now; a config flag flips it to parallel later.
- Target ~30–40 versions per criterion, generated from a strategy library.
- Versions are generated in a batch, then students attempt them, then a human reviews
  and culls. This is not a tight per-edit loop.

## Folder structure

```
agentic/
├── README.md
├── config/
│   ├── models.yaml
│   └── run_config.yaml
├── seeds/                      # copied from dataset, small tests only
│   └── family_01_graph_coloring/
│       ├── criterion_1_npc/{statement.md, meta.yaml, reference.py, tests/}
│       ├── criterion_2_p/...
│       └── criterion_3_infeasible/...
├── strategies/                 # the prompting strategy library (file 43)
├── prompts/                    # teacher / student / verifier prompts (file 43)
├── versions/                   # teacher output
│   └── family_01/criterion_1_npc/v001/
│       ├── statement.md
│       ├── edit.json           # strategy, intensity, rationale, teacher raw
│       └── gate.json           # automated gate result
├── attempts/                   # student output
│   └── family_01/criterion_1_npc/v001/<student_id>/
│       ├── solution.py
│       ├── raw.txt
│       ├── trace.txt           # reasoning trace if the model exposes one
│       └── verdict.json
├── reports/
│   └── family_01_summary.csv
├── tools/
│   ├── seed.py
│   ├── backends.py
│   ├── generate_versions.py
│   ├── gate.py
│   ├── run_students.py
│   └── report.py
└── logs/
```

## config/models.yaml

```yaml
teacher:
  id: gemini-3.6-flash
  backend: openai_compat
  base_url: "https://generativelanguage.googleapis.com/v1beta/openai/"
  model_string: "gemini-3.6-flash"
  api_key_env: GEMINI_API_KEY
  temperature: 0.9          # higher: we want version diversity
  max_tokens: 8192

verifier:                    # separate model, not teacher, not a student
  id: gemini-3-flash-lite-verifier
  backend: openai_compat
  base_url: "https://generativelanguage.googleapis.com/v1beta/openai/"
  model_string: "gemini-3-flash-lite"
  api_key_env: GEMINI_API_KEY
  temperature: 0.0
  max_tokens: 2048

students:
  - id: gemini-3-flash-lite
    backend: openai_compat
    base_url: "https://generativelanguage.googleapis.com/v1beta/openai/"
    model_string: "gemini-3-flash-lite"
    api_key_env: GEMINI_API_KEY
    thinking: false
    max_tokens: 4096
    enabled: true

  - id: qwen3-32b
    backend: ollama
    model_string: "qwen3:32b"
    thinking: true
    max_tokens: 12288
    enabled: true

  - id: gemma3-27b
    backend: ollama
    model_string: "gemma3:27b"
    thinking: false
    max_tokens: 4096
    enabled: true

  - id: gpt-oss-20b
    backend: ollama
    model_string: "gpt-oss:20b"
    thinking: true
    max_tokens: 12288
    enabled: true

held_out: []                 # populated later; teacher must never see these

execution:
  ollama_parallel: false     # sequential for now; flip to true on a bigger GPU
  ollama_max_workers: 1      # raise with the flag above
  api_parallel: true         # API students can run concurrently
  api_max_workers: 3
  request_timeout_s: 1800
  retries: 3
```

`enabled: false` on any student skips it without deleting the entry. Adding a model
is a config edit only — never a code change.

## config/run_config.yaml

```yaml
family: "01"
criteria: [1, 2, 3]
versions_per_criterion: 36     # ~30-40 target
seed_tests: small_only         # cases 01-04; never the scaled ones
strategy_plan: balanced        # see strategies/PLAN.md
seed: 7
stop_on_gate_fail: false       # keep failed versions, mark them, review later
```

## tools/seed.py

Copies Family 01 from `dataset/` into `agentic/seeds/`, taking **only** test cases
`01`–`04`. Copies `statement.md`, `meta.yaml`, `reference.py`, and any `validator.py`.
Prints what it copied and the case count per criterion so the user can confirm no
large cases came along.

Read-only on `dataset/`.

## tools/backends.py

Two backends behind one function:

```python
def chat(model_cfg, system: str, user: str) -> dict:
    """Returns {text, raw, elapsed_s, error}. Never raises on API failure."""
```

- `openai_compat` — POST to `{base_url}chat/completions` with
  `{model, messages:[{role:system},{role:user}], temperature, max_tokens}` and
  `Authorization: Bearer <api_key from env>`. Standard OpenAI response shape.
- `ollama` — POST `http://localhost:11434/api/chat`, `options.num_predict = max_tokens`,
  `stream: false`. Honor `OLLAMA_HOST` env if set.

Retry with backoff per `execution.retries`. On hard failure return
`{text: "", error: "<reason>"}` so the driver records it and continues.

Also provide, reusing the existing harness where possible:
```python
def strip_thinking(text) -> str   # remove <think>/<thinking> blocks
def extract_code(text) -> str     # first ```python fence, else first fence, else all
def extract_json(text) -> dict    # first {...} block; tolerate ```json fences
```

## tools/generate_versions.py

CLI: `python tools/generate_versions.py --family 01 --criterion 1 [--n 36] [--dry-run]`

1. Load the seed statement, `meta.yaml` (the teacher **does** see the true class and
   intended algorithm — it is authoring, not being tested), and the run config.
2. Build the strategy plan: `strategies/PLAN.md` maps N versions across the strategy
   library and intensity levels. Deterministic given `seed`.
3. For each planned version: render the teacher prompt (from `prompts/`), call the
   teacher, parse the JSON response.
4. Write `versions/family_01/criterion_<n>/v###/statement.md` and `edit.json`
   (strategy id, intensity, teacher rationale, raw response, timestamp).
5. Atomic writes, checkpointed — skip a version if `statement.md` already exists
   unless `--reset`.

`--dry-run` renders and prints the prompts without calling the API. The user should
use this first to inspect prompt quality.

## tools/gate.py

CLI: `python tools/gate.py --family 01 [--criterion 1] [--version v003]`

Runs the automated checks on each version and writes `gate.json`:

1. **I/O contract unchanged** — the edited statement's Input and Output sections still
   specify the same format, bounds, and tie-break rule as the seed. If the contract
   changed, the cached `.out` files no longer apply. **Fail.**
2. **Reference still passes** — run `reference.py` against the seed's small tests.
   (Confirms the harness path; it does not prove the *statement* still means the same
   thing — that is the verifier's and the human's job.)
3. **Leakage scan** — reject any forbidden term (`NP-complete`, `polynomial`,
   `bipartite`, `tree`, `DAG`, `2-SAT`, `3-SAT`, `intractable`, reduction names,
   difficulty hints). Deterministic, reliable.
4. **Verifier check** — send the edited statement to the verifier model with the
   verifier prompt. It restates the problem and answers: unambiguous? solvable?
   same task as the seed? Record verdict and reasoning.

Result: `PASS`, `FLAG` (verifier uncertain — needs human), or `FAIL` (contract broken
or leakage). Per `stop_on_gate_fail: false`, failures are recorded, not deleted.

## tools/run_students.py

CLI: `python tools/run_students.py --family 01 [--criterion 1] [--only <student_id>]`

1. For each version that is not `FAIL`, for each enabled student: send the fixed
   student prompt with that version's statement.
2. Save `solution.py`, `raw.txt`, and `trace.txt` (the reasoning trace before
   stripping — this is the feedback signal for later iterations).
3. Score with the existing harness checker against the seed's small tests.
   Write `verdict.json`.
4. Concurrency per `execution`: API students up to `api_max_workers`; Ollama students
   **sequentially** while `ollama_parallel: false`. Implement so flipping the flag and
   raising `ollama_max_workers` is the only change needed later.
5. Checkpointed — skip a (version, student) that already has `verdict.json`.

## tools/report.py

CLI: `python tools/report.py --family 01`

Writes `reports/family_01_summary.csv`, one row per (criterion, version, student):
`criterion, class_label, version, strategy, intensity, gate_result, student, verdict, n_cases, n_passed`

Prints:
- Seed baseline: pass rate per student on `v000` (the unmodified seed).
- Per version: how many students passed, and the **delta from the seed baseline**.
- Versions ranked by delta — the biggest drops first. This is the manual-review queue.
- A per-strategy rollup: which strategies produced the largest average drop.

Keep plotting out. CSV plus a printed table.

## agentic/README.md

Write a short README covering: what this phase does, the folder map, the manual run
order below, and how to add a model (config edit only).

## Manual run order (document this; do not execute)

```bash
export GEMINI_API_KEY=...
python tools/seed.py --family 01
python tools/generate_versions.py --family 01 --criterion 1 --dry-run   # inspect prompts
python tools/generate_versions.py --family 01 --criterion 1
python tools/gate.py --family 01 --criterion 1
python tools/run_students.py --family 01 --criterion 1
python tools/report.py --family 01
```

## Constraints

- Never write to `dataset/`.
- Never copy the large scaled test cases into `seeds/`.
- Reuse the existing harness for running and checking solutions — do not reimplement
  the runner or checker.
- All model choices come from `config/models.yaml`. No model names in code.

## Done

Build the scaffold, print the tree, confirm nothing was executed. Then **stop and wait**
for `43_agentic_prompts_and_strategies.md`.

# 06 — Generation & Evaluation Drivers + Model Registry

> Prerequisite: harness (file `03`) and at least Family 1 (file `04`) exist.

## Goal

Build the **Phase-2 (generate model code)** and **Phase-3 (evaluate)** drivers, plus the model registry and run-config format. After this, you can run the full benchmark end-to-end on whatever families are filled in.

Nothing here touches `dataset/`. Everything writes under `runs/<date>_<name>/`.

---

## Step 1 — Fill `models/registry.yaml`

Per `conventions/registry_format.md`. Seed it with the user's actual models (they run open-source via Ollama on an RTX 5060 Ti, closed-source via API). Provide entries; the user edits ids/strings later:

```yaml
models:
  - id: phi4
    display_name: "Phi-4"
    backend: ollama
    model_string: "phi4"
    openness: open
    thinking: false
    token_budget: 4096
    notes: ""
  - id: gemma3-27b
    display_name: "Gemma 3 27B"
    backend: ollama
    model_string: "gemma3:27b"
    openness: open
    thinking: false
    token_budget: 4096
    notes: ""
  - id: deepseek-r1-14b
    display_name: "DeepSeek-R1 14B"
    backend: ollama
    model_string: "deepseek-r1:14b"
    openness: open
    thinking: true
    token_budget: 12288
    notes: "reasoning model; strip <think> blocks"
  - id: qwen3-14b
    display_name: "Qwen3 14B"
    backend: ollama
    model_string: "qwen3:14b"
    openness: open
    thinking: true
    token_budget: 12288
    notes: ""
  - id: gpt-oss-20b
    display_name: "GPT-OSS 20B"
    backend: ollama
    model_string: "gpt-oss:20b"
    openness: open
    thinking: true
    token_budget: 12288
    notes: ""
  # --- closed-source examples; fill real ids ---
  - id: claude
    display_name: "Claude"
    backend: api
    model_string: "<FILL>"
    openness: closed
    thinking: false
    token_budget: 4096
    notes: ""
```

---

## Step 2 — Run-config format

Create `runs/run_config_template.yaml` (copied per experiment):
```yaml
run_name: main
date: "YYYY-MM-DD"
study: main                 # main | time_budget | token_budget | multiturn
models: [phi4, gemma3-27b, deepseek-r1-14b, qwen3-14b, gpt-oss-20b]  # ids from registry
families: all               # 'all' or list like ["01","02"]
criteria: all               # 'all' or subset of [1,2,3]
samples_per_problem: 1      # pass@1 => 1; raise for pass@k later
seed: 0
generation:
  temperature: 0.2
  # token_budget per-model comes from registry; can be overridden here
evaluation:
  global_timeout_s: 600     # main-study 10-min ceiling; null = use per-problem meta
```

---

## Step 3 — `harness/backends.py`

Abstraction over generation backends. Two implementations + a factory.

```python
def generate(backend, model_string, system, user, max_tokens, temperature, thinking) -> str
```

- **ollama backend:** POST to `http://localhost:11434/api/chat` with the system/user messages, `options.num_predict = max_tokens`, `temperature`, `stream=false`. Return the assistant content. Mirror the user's existing Ollama calling pattern (MODEL_PROFILES-style handling of thinking models with elevated budgets).
- **api backend:** call the Anthropic Messages API (`POST https://api.anthropic.com/v1/messages`) using the model_string, max_tokens, system + user messages. Read the key from env (`ANTHROPIC_API_KEY`). Return concatenated text blocks.
- Wrap both in retry-with-backoff (atomic, fail-soft: on hard failure, return empty string and let the driver record an error).
- Keep network calls isolated so the user can stub them.

> Make the base URL / endpoint configurable via env so it works on the user's machine.

---

## Step 4 — `harness/generate.py` (Phase 2 driver)

CLI: `python -m harness.generate --config runs/<date>_<name>/run_config.yaml`

Behavior:
1. Load run_config + registry + dataset.
2. Resolve the target problem set (families × criteria filters) and model set.
3. For each (model, problem):
   - Build the prompt from `conventions/prompt_template.md` (system + user with `{STATEMENT}` filled from the problem's `statement.md`).
   - Call `backends.generate(...)` with the model's `token_budget` (or override).
   - `strip_thinking` then `extract_code` (from `harness/extract.py`).
   - Write to `runs/<date>_<name>/generations/<model>/family_XX/criterion_n/`:
     - `solution.py`     (extracted code)
     - `raw.txt`         (full raw response, for audit)
     - `gen_meta.json`   (model id, prompt hash, token budget, elapsed, timestamp)
   - **Atomic writes** (write to temp, rename) and **checkpointing**: skip a (model, problem) if `solution.py` already exists, so the run resumes after interruption. (Mirror the user's existing per-model checkpoint + atomic JSON write patterns.)
4. CLI flags to support: `--only <model_id>`, `--reset` (ignore checkpoints), `--sample <n>` (limit problems for a smoke test), `--seed`.

---

## Step 5 — `harness/evaluate.py` (Phase 3 driver)

CLI: `python -m harness.evaluate --config runs/<date>_<name>/run_config.yaml`

Behavior:
1. Load run_config + dataset.
2. For each (model, problem) with a generated `solution.py`:
   - `checker.judge_problem(criterion, solution_path, timeout_override=global_timeout_s)`.
   - Write `runs/<date>_<name>/results/raw/<model>/family_XX/criterion_n/verdict.json`
     containing overall verdict, per-case verdicts, first failure, n_cases/n_passed, class_label.
   - Atomic write + checkpoint (skip if verdict exists unless `--reset`).
3. After all verdicts: call `harness.aggregate` to emit `runs/<date>_<name>/results/summary.csv` and print the per-model pass@1-by-class table and the infeasible confident-wrong rate.

---

## Step 6 — Convenience scripts

`scripts/new_run.sh`:
```bash
#!/usr/bin/env bash
# usage: scripts/new_run.sh <run_name>
set -euo pipefail
name="$1"; date="$(date +%Y-%m-%d)"; dir="runs/${date}_${name}"
mkdir -p "$dir"
sed "s/YYYY-MM-DD/${date}/; s/run_name: main/run_name: ${name}/" \
    runs/run_config_template.yaml > "$dir/run_config.yaml"
echo "created $dir/run_config.yaml — edit it, then run generate + evaluate"
```

`scripts/smoke.sh`:
```bash
#!/usr/bin/env bash
# tiny end-to-end check on family 01 only, one model, 1 sample
set -euo pipefail
python -m harness.generate --config "$1" --only "${2:-phi4}" --sample 3
python -m harness.evaluate --config "$1"
```

Make both executable.

---

## Step 7 — Dry-run wiring test (no live models needed)

To verify the wiring without calling real models:
1. Add a `--dry-run` flag to `generate.py` that, instead of calling a backend, copies the problem's `reference.py` as `solution.py` (so you can confirm the pipeline produces PASS everywhere on filled families).
2. Run dry-run generate + evaluate on Family 1, confirm `summary.csv` shows the reference passing all criteria. This proves generate→evaluate→aggregate end-to-end.

## Done

Confirm the dry-run produces a clean `summary.csv` for Family 1. **Stop and wait** for `07_constraint_studies.md`.

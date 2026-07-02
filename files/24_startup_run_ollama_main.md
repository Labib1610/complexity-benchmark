# 24 — STARTUP RUN: Main Study on the Three Ollama Models

> **You are Claude Code.** The benchmark is fully built (files 00–07) and all 16 families are filled and validated (files 08–23). This file runs the **Main Study** end-to-end on the user's three local Ollama models, across **all families and all criteria**, and reports the results.
>
> Do NOT modify anything under `dataset/`. This run only writes under `runs/`. The user will add more test inputs, more models, and the closed-source API models later — those are separate run files. This is the first real run.

## The models for this run (Ollama, local)

- `qwen3:32b`  — reasoning model (strip `<think>` blocks, elevated token budget)
- `gemma3:27b` — standard model
- `gpt-oss:20b` — reasoning model (strip thinking, elevated token budget)

## Step 0 — Pre-flight (MANDATORY, do not skip)

The results are only trustworthy if the answer key is correct and the model server is reachable.

1. **Validate the whole dataset** (reference passes its own tests, no statement leaks the class):
   ```bash
   for f in dataset/family_*; do python -m harness.reference_check "$f"; done
   ```
   Every family must report clean. If ANY family flags a reference mismatch, missing `.out`, or leakage term, STOP and report it to the user — do not run models against a broken key.

2. **Confirm Ollama is up and the models are present:**
   ```bash
   curl -s http://localhost:11434/api/tags | grep -E "qwen3:32b|gemma3:27b|gpt-oss:20b"
   ollama list
   ```
   If a model is missing, tell the user to `ollama pull <name>` and stop.

3. **Dataset self-consistency dry-run** (references stand in as answers; everything must PASS). Use a throwaway config:
   ```bash
   scripts/new_run.sh preflight
   ```
   Edit `runs/<date>_preflight/run_config.yaml` to:
   ```yaml
   study: main
   models: [qwen3-32b]          # any single registered id; dry-run ignores the model anyway
   families: all
   criteria: all
   samples_per_problem: 1
   evaluation:
     global_timeout_s: 600
   ```
   Then:
   ```bash
   python -m harness.generate --config runs/<date>_preflight/run_config.yaml --dry-run
   python -m harness.evaluate --config runs/<date>_preflight/run_config.yaml
   ```
   Open `runs/<date>_preflight/results/summary.csv` and confirm **all 48 problems show PASS**. If not, a dataset problem is broken — STOP and report which one. This proves the pipeline and key before spending model time.

## Step 1 — Register the three models

Open `models/registry.yaml` and ensure these three entries exist exactly (add or correct them; leave any other entries alone). Use these ids — they become the folder names under `generations/`:

```yaml
models:
  - id: qwen3-32b
    display_name: "Qwen3 32B"
    backend: ollama
    model_string: "qwen3:32b"
    openness: open
    thinking: true
    token_budget: 12288
    notes: "reasoning model; strip <think> blocks"

  - id: gemma3-27b
    display_name: "Gemma 3 27B"
    backend: ollama
    model_string: "gemma3:27b"
    openness: open
    thinking: false
    token_budget: 4096
    notes: ""

  - id: gpt-oss-20b
    display_name: "GPT-OSS 20B"
    backend: ollama
    model_string: "gpt-oss:20b"
    openness: open
    thinking: true
    token_budget: 12288
    notes: "reasoning model; strip thinking"
```

Confirm `backends.py` points at the local Ollama endpoint (`http://localhost:11434/api/chat`). If the user's Ollama runs on a non-default host/port, read it from env (`OLLAMA_HOST`) rather than hard-coding.

## Step 2 — Create the main run

```bash
scripts/new_run.sh main
```
Edit `runs/<date>_main/run_config.yaml`:
```yaml
run_name: main
date: "<date>"
study: main
models: [qwen3-32b, gemma3-27b, gpt-oss-20b]
families: all
criteria: all
samples_per_problem: 1          # pass@1
seed: 0
generation:
  temperature: 0.2
evaluation:
  global_timeout_s: 600         # 10-minute ceiling per problem (from the proposal)
```

## Step 3 — Smoke test before the full sweep

Do NOT launch all 144 generations blind. First confirm one model answers and the wiring holds end-to-end on a tiny slice:

```bash
python -m harness.generate --config runs/<date>_main/run_config.yaml --only gemma3-27b --sample 3
python -m harness.evaluate --config runs/<date>_main/run_config.yaml
```
Check that:
- `runs/<date>_main/generations/gemma3-27b/...` contains real `solution.py` files (not empty),
- `raw.txt` shows a genuine model reply,
- for a reasoning model the `<think>` block was stripped before extraction (spot-check one qwen3/gpt-oss `raw.txt` vs `solution.py` later).
If generation returns empty strings, the Ollama call is failing — report the exact error (timeout, connection refused, model name mismatch) and stop.

## Step 4 — Full generation (Phase 2)

This is 3 models × 16 families × 3 criteria = **144 generations**.

```bash
python -m harness.generate --config runs/<date>_main/run_config.yaml
```
Notes:
- It **checkpoints**: already-written `solution.py` files are skipped, so if it is interrupted just re-run the same command and it resumes.
- The 32B and 20B reasoning models are slow; this may take a while. Let it finish. Do not lower their `token_budget` — they need room for chain-of-thought before the code.
- To regenerate from scratch, add `--reset`. To run one model only, add `--only <id>`.

Output written per (model, problem):
```
runs/<date>_main/generations/<model>/family_XX/criterion_n/
    solution.py    # extracted code (thinking stripped)
    raw.txt        # full raw reply
    gen_meta.json  # tokens, elapsed, timestamp, prompt hash
```

## Step 5 — Evaluation (Phase 3)

```bash
python -m harness.evaluate --config runs/<date>_main/run_config.yaml
```
For each (model, problem) it runs `solution.py` against all that problem's test cases under the 600 s ceiling and writes:
```
runs/<date>_main/results/raw/<model>/family_XX/criterion_n/verdict.json
runs/<date>_main/results/summary.csv     # tidy, one row per (model, family, criterion)
```
It also prints the per-model summary table.

## Step 6 — What to report back to the user

After evaluation, produce a clear written summary (and keep the CSV as the source of truth):

1. **Per-model pass@1 by class** — three numbers each: P, NPC, INFEASIBLE. This is the headline. State whether NPC < P for each model.
2. **Infeasible confident-wrong rate** per model — fraction of infeasible problems where the model returned a confident wrong non-null answer instead of the correct sentinel/certificate.
3. **NPC verdict composition** per model — of the NPC problems, how many PASS / WRONG_ANSWER / TLE / RUNTIME_ERROR. (TLE-heavy ⇒ the model tried an exact exponential algorithm and did not recognize intractability.)
4. **Per-family table** — a 16-row view of pass/fail by class for each model, so the user can see which domains separate cleanly and which don't.
5. **Coverage check** — confirm all 144 (model, problem) cells have both a `solution.py` and a `verdict.json`. Flag any gaps (e.g. a model that returned empty on some problem).

Compute items 1–3 from `summary.csv` (the aggregator already emits 1 and 2; derive 3 by counting `first_failure`/verdict fields). Present them as small tables in your reply, not as files.

## Step 7 — Leave the run intact

Do not delete or overwrite `runs/<date>_main/`. It is the permanent record of this experiment. Later run files (more models, modified dataset, the constraint studies) will create their own dated run folders and will not touch this one.

## Done

Report the six items from Step 6. Then stop — the user will decide next steps (add models, add test inputs, or launch the time-budget / token-budget / multi-turn studies via their own run files).

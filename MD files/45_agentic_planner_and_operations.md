# 45 — Agentic Phase: Open-Ended Planner + Operations Guide

> **Build/edit files only. Run nothing.**

Two changes: make version generation open-ended instead of capped by the strategy count,
and write an operations guide into the repo.

---

# Part A — Open-ended planner

## Problem with the current plan

`strategies/PLAN.md` maps 12 strategies × 3 intensities = 36 fixed cells. That caps
output at 36 per criterion and makes the set closed. Worse, some strategies don't apply
to every class (S04 is NPC-only, S05 is P/INFEASIBLE-only, S06 is INFEASIBLE-only, S12
needs feedback), so a criterion may only have ~30 usable cells.

Version count should be a **target the planner fills**, not a product of the strategy
count.

## Replace `strategies/PLAN.md` with this

```markdown
# Version plan

`versions_per_criterion` in run_config is a target, not a formula. The planner fills it
using four sources in priority order. Version numbering is deterministic given the run
seed.

v000 is reserved for the unmodified seed (report baseline).

## Source 1 — base grid
Every (strategy, intensity) pair applicable to this criterion's class, one sample each.
Strategies declare `classes:` in their file; inapplicable ones are skipped, not
substituted. Typical yield: 27-36 depending on class.

## Source 2 — extra samples
If the target is not met, draw additional samples from cells already used. The teacher
runs at temperature 0.9, so repeated draws from the same (strategy, intensity) produce
genuinely different statements. Distribute round-robin across cells so no single
strategy dominates. Each sample gets a distinct sub-seed.

## Source 3 — composition
Pairs of compatible strategies applied together (both instructions injected, joined by
"Apply both of the following, in combination:"). Skip pairs that conflict — S04 and S05
are mutually exclusive, S12 requires feedback. Composition uses intensity `moderate` or
`aggressive` only; a light composition is indistinguishable from a light single.

## Source 4 — next generation
Derive a version from an **already-accepted** version rather than from the seed. The
parent's statement replaces `{SEED_STATEMENT}` in the teacher prompt; the hidden metadata
block still comes from the original `meta.yaml`. Track `parent` and `generation` in
`edit.json`. Only parents with `gate_result: PASS` are eligible. Generation depth is
capped by `max_generation` in run_config (default 2) so drift stays reviewable.

## Scaling
Raise `versions_per_criterion` and the planner extends automatically through sources 2-4.
There is no upper bound imposed by the strategy library.
```

## run_config.yaml additions

```yaml
versions_per_criterion: 40     # target; planner fills it from sources 1-4
max_generation: 2              # 0 = seed-derived only
composition_enabled: true
samples_seed_stride: 1000      # sub-seed spacing for repeat draws
```

## generate_versions.py changes

- Build the plan from the four sources until the target is met; log which source each
  version came from.
- Record in `edit.json`: `source` (grid | sample | composition | generation),
  `strategies` (list — one id, or two for compositions), `intensity`, `parent`
  (version id or "seed"), `generation`, `sub_seed`.
- Source 4 requires gate results, so it runs in a second pass: generate sources 1-3,
  gate them, then generate source 4 from the passes. Support
  `--sources grid,sample,composition` and `--sources generation` so the user can run the
  two passes explicitly.
- `report.py` gains `source`, `generation`, and `parent` columns, and rolls up mean delta
  by source so the user can see whether compositions and later generations actually
  outperform the base grid.

## Expected volume

Per family: 3 criteria × 40 = 120 versions. Across 16 families: ~1,920. Generation is
the cheap step; gating and student runs are the expensive ones, which is why the human
cull happens after the report ranks them.

---

# Part B — write `agentic/OPERATIONS.md`

Write this file into the repo verbatim.

```markdown
# Operations guide

## Managing models

All model changes are edits to `config/models.yaml`. Never edit code to add, remove, or
change a model.

### Add a model

Append an entry under `students:`:

```yaml
  - id: my-model                    # directory-safe; becomes the folder name
    backend: ollama                 # ollama | openai_compat
    model_string: "my-model:tag"    # ollama tag, or the provider's model id
    thinking: false                 # true for reasoning models
    max_tokens: 4096                # raise to 12288+ for thinking models
    enabled: true
```

For an API model also set `base_url` and `api_key_env`, and add the matching key to
`config/local_secrets.py`.

Then: `python tools/check_keys.py` to confirm it resolves.

### Remove a model

Prefer `enabled: false` over deleting — it keeps past results interpretable and lets you
re-enable later. Delete the entry only if the model will never be used again. Existing
output under `attempts/<model_id>/` is not removed either way; `report.py` reports
whatever it finds.

### Edit a model

Change `max_tokens`, `thinking`, `temperature`, or `model_string` in place. If you change
anything that affects output, the existing attempts are stale — delete that model's
folders under `attempts/` before re-running, or results will mix old and new settings.

### Change the teacher or verifier

Edit the `teacher:` or `verifier:` block. Changing the teacher invalidates comparisons
across versions generated by different teachers, so record it: bump a `teacher_tag` in
run_config and keep old versions in place rather than regenerating over them.

### Concurrency

```yaml
execution:
  ollama_parallel: false     # true when you have the GPU headroom
  ollama_max_workers: 1      # raise with the flag above
  api_parallel: true
  api_max_workers: 3
```

Ollama models are GPU-bound and will 500 or time out if run concurrently on a single
consumer GPU — that failure has already been observed on this project. Leave
`ollama_parallel: false` until the hardware changes.

## Running

### One family (current mode)

```bash
python tools/seed.py               --family 01
python tools/generate_versions.py  --family 01 --criterion 1 --dry-run
python tools/generate_versions.py  --family 01 --criterion 1 --sources grid,sample,composition
python tools/gate.py               --family 01 --criterion 1
python tools/generate_versions.py  --family 01 --criterion 1 --sources generation
python tools/gate.py               --family 01 --criterion 1
python tools/run_students.py       --family 01 --criterion 1
python tools/report.py             --family 01
```

Omit `--criterion` to do all three criteria of the family.

### All families

Every tool accepts `--family all`:

```bash
python tools/seed.py              --family all
python tools/generate_versions.py --family all --sources grid,sample,composition
python tools/gate.py              --family all
python tools/generate_versions.py --family all --sources generation
python tools/gate.py              --family all
python tools/run_students.py      --family all
python tools/report.py            --family all
```

Do not run `--family all` until one family has been completed and reviewed end to end.

### One model at a time

```bash
python tools/run_students.py --family 01 --only qwen3-32b
```

Recommended while Ollama runs sequentially — it keeps each model's runtime isolated and
makes failures easy to attribute.

### Resume and reset

All tools are checkpointed. Re-running the same command skips completed work.

```bash
python tools/run_students.py --family 01              # resumes
python tools/run_students.py --family 01 --reset      # regenerates everything
```

To redo one version only, delete its folder under `versions/` (to regenerate it) or under
`attempts/` (to re-run students on it), then re-run the command.

### Before spending API calls

```bash
python tools/check_keys.py
python tools/generate_versions.py --family 01 --criterion 1 --dry-run
```

The dry run prints the exact prompts without calling anything. Read a few before
committing to a full batch.

## Where things live

| Path | Contents |
|---|---|
| `seeds/` | Family copies from `dataset/`, small test cases only |
| `versions/` | Teacher output: statement + edit.json + gate.json per version |
| `attempts/` | Student output: solution, raw, trace, verdict |
| `reports/` | summary CSVs |
| `logs/` | run logs |

`dataset/` is never written to by this phase.
```

## Done

Apply Part A, write Part B, run nothing. Then stop.

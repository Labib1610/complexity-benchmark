# Agentic Hardening Phase

A self-contained phase that makes Family 01's statements *harder to game* by having a
**teacher** model author many rewritten versions of each seed statement, then having
**student** models attempt them. A human reviews the results and keeps the versions
that most reduce student pass rates.

This phase **reads** seed problems from `dataset/` but **never writes** to it, and
uses **only the small original test cases (01–04)** — never the large scaled cases.

## What it does

1. **seed** — copy Family 01 (statement, meta, reference, validator, small tests) into
   `seeds/`.
2. **generate_versions** — the teacher rewrites each seed statement per a strategy
   library, preserving the exact task and I/O contract. Output → `versions/`.
3. **gate** — automated checks per version (I/O contract unchanged, reference still
   passes, no leakage, verifier model sanity) → `PASS | FLAG | FAIL` in `gate.json`.
4. **run_students** — each enabled student attempts each surviving version; solutions
   are scored with the **existing harness checker** against the seed's small tests.
5. **report** — aggregate into `reports/family_01_summary.csv` and print a review
   queue ranked by how much each version dropped student pass rates.

## Folder map

```
agentic/
├── config/        models.yaml (teacher/verifier/students), run_config.yaml
├── seeds/         Family 01 copied from dataset/ (small tests only)
├── strategies/    strategy library + PLAN.md          (populated by file 43)
├── prompts/       teacher / student / verifier prompts (populated by file 43)
├── versions/      teacher output: statement.md, edit.json, gate.json
├── attempts/      student output: solution.py, raw.txt, trace.txt, verdict.json
├── reports/       family_01_summary.csv
├── tools/         seed, backends, generate_versions, gate, run_students, report
└── logs/
```

## Setup (once)

```bash
cp config/local_secrets.example.py config/local_secrets.py
# edit config/local_secrets.py and replace the PASTE_..._HERE placeholders
python tools/check_keys.py
```

`local_secrets.py` is gitignored; keys may also be provided via environment variables.
`check_keys.py` reports `ok`/`missing` per enabled model and whether Ollama is
reachable — it never prints a key.

## Manual run order

```bash
python tools/seed.py --family 01
python tools/generate_versions.py --family 01 --criterion 1 --dry-run   # inspect prompts
python tools/generate_versions.py --family 01 --criterion 1
python tools/gate.py --family 01 --criterion 1
python tools/run_students.py --family 01 --criterion 1
python tools/report.py --family 01
```

Run the commands from inside `agentic/`. `--dry-run` on `generate_versions` prints the
teacher prompts without calling any API — use it first to inspect prompt quality.

## Adding or disabling a model

Config edit only, never a code change: add an entry to `students:` in
`config/models.yaml`, or set `enabled: false` on an existing one. Ollama students run
sequentially for now; set `execution.ollama_parallel: true` and raise
`ollama_max_workers` on a bigger GPU.

## Notes

- The teacher and verifier see the seed `meta.yaml` (true class, intended algorithm) —
  they are authoring/reviewing, not being tested. Students see only the statement.
- Reuses `harness/` for running and checking solutions — the runner/checker are not
  reimplemented here.
- `strategies/` and `prompts/` are filled by file 43; the tools ship with minimal
  built-in fallbacks so `--dry-run` works before then.

# 01 — Scaffold the Directory Tree

> Prerequisite: you have read `00_START_HERE_project_overview.md`. If you have not, ask the user for it before proceeding.

## Goal

Create the **complete empty skeleton** of the project. No real content yet — just folders, placeholder files, and the top-level README. Later files fill these in.

## Step 1 — Create the root

Create a project root folder named `complexity-benchmark/` in the current working directory. Everything below is relative to that root.

## Step 2 — Create this exact tree

```
complexity-benchmark/
├── README.md
├── .gitignore
├── conventions/                  # filled by file 02
│   └── .gitkeep
├── dataset/                      # filled by files 04 & 05
│   └── .gitkeep
├── models/
│   └── registry.yaml             # placeholder now; filled by file 06
├── runs/                         # produced by drivers; keep empty
│   └── .gitkeep
├── harness/                      # filled by file 03
│   └── .gitkeep
├── studies/                      # filled by file 07
│   └── .gitkeep
└── scripts/                      # small convenience scripts
    └── .gitkeep
```

Use `.gitkeep` files so empty directories are preserved under version control.

## Step 3 — Write `README.md`

Create `complexity-benchmark/README.md` with this content (fill it in as written):

```markdown
# Complexity-Aware Code Generation Benchmark

Benchmarks whether LLMs understand computational complexity structure
(P vs NP-complete vs infeasible) when generating code.

## Layout
- `conventions/` — fixed contracts: I/O format, statement schema, prompt template, checker spec, registry format. Read these first.
- `dataset/` — the benchmark itself (model-agnostic): 16 families × 3 criteria, each with a statement, reference solution, and test cases.
- `models/registry.yaml` — the research models under test (open-source + closed-source).
- `harness/` — shared runner, checker, aggregator.
- `runs/` — one dated, self-contained folder per experiment (generations + results).
- `studies/` — prompt variants for time-budget, token-budget, and multi-turn studies.
- `scripts/` — convenience entry points.

## Dataset structure
Each problem lives at:
`dataset/family_XX_<slug>/criterion_<n>_<label>/`
containing:
- `statement.md`  — shown to the model (never names the complexity class)
- `meta.yaml`     — true class, intended algorithm, reduction notes (model never sees this)
- `reference.py`  — ground-truth solution (Python 3, stdin → stdout)
- `tests/NN.in`, `tests/NN.out` — validated test cases (zero-padded, auto-discovered)

## Conventions (must hold everywhere)
- Python 3 only for all solutions.
- All solutions read stdin, write stdout.
- Test cases are zero-padded `NN.in` / `NN.out`; tooling auto-discovers any number of them.
- Statements never reveal the complexity class.

## Workflow
1. Build dataset (statements, references, tests) — model-free.
2. Generate model code (Phase 2 driver) into `runs/<date>/generations/`.
3. Evaluate code against tests (Phase 3 driver) into `runs/<date>/results/`.
4. Aggregate metrics.
```

## Step 4 — Write `.gitignore`

Create `complexity-benchmark/.gitignore`:

```
__pycache__/
*.pyc
.venv/
runs/*/generations/
runs/*/results/raw/
*.log
.DS_Store
```

> Note: we ignore the heavy per-run model output and raw verdicts, but keep `runs/*/run_config.yaml` and `summary.csv` (do not ignore those).

## Step 5 — Verify

Print the resulting tree (e.g. `find complexity-benchmark -type d` and a listing of top-level files) so the user can confirm the skeleton matches.

## Done

Confirm the scaffold is created, show the tree, then **stop and wait** for `02_conventions.md`.

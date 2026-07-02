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

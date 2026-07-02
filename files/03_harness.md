# 03 — Build the Shared Harness

> Prerequisite: `conventions/` exists from file `02`.

## Goal

Implement the **shared, dataset-aware machinery** in `complexity-benchmark/harness/`. This code is written ONCE and never changes when you add a model or a family. It only knows the dataset layout and the conventions.

Create the following Python modules. Write real, working code (not stubs), Python 3, standard library only where possible (`pyyaml` is allowed and assumed installed).

---

## Module 1 — `harness/dataset.py`

A dataset-loading layer. Responsibilities:

- `discover_families(dataset_dir) -> list[Family]` — scan `dataset/family_*` folders.
- `discover_criteria(family_dir) -> list[Criterion]` — scan `criterion_*` subfolders.
- For each criterion, load `meta.yaml`, the path to `statement.md`, `reference.py`, and **auto-discover all `tests/NN.in` files**, pairing each with its `NN.out`.
- Test-case discovery must be glob-based and sorted, so dropping in `07.in`/`07.out` later requires no code change.

Expose dataclasses:
```python
@dataclass
class TestCase: name: str; in_path: Path; out_path: Path
@dataclass
class Criterion: family_id: str; criterion_id: str; dir: Path; meta: dict;
                 statement_path: Path; reference_path: Path; tests: list[TestCase];
                 validator_path: Path | None
@dataclass
class Family: family_id: str; dir: Path; meta: dict; criteria: list[Criterion]
```
Validator path is `criterion_dir/validator.py` if it exists, else `None`.

Add a helper `iter_problems(dataset_dir)` yielding every `Criterion` across all families (48 when complete).

---

## Module 2 — `harness/runner.py`

Safely runs one Python solution against one test case.

```python
def run_solution(solution_path, input_text, timeout_s) -> RunResult
```
- Use `subprocess.run(["python3", solution_path], input=input_bytes, capture_output=True, timeout=timeout_s)`.
- On `TimeoutExpired` → `RunResult(status="TLE")`.
- On non-zero return code or exception → `status="RUNTIME_ERROR"` with stderr captured.
- Otherwise `status="OK"` with decoded stdout.
- Best-effort memory limiting via `resource.setrlimit` in a `preexec_fn` on Linux (wrap in try/except; skip on unsupported platforms).

`RunResult` dataclass: `status: str; stdout: str; stderr: str; elapsed_s: float`.

---

## Module 3 — `harness/checker.py`

Implements the verdict logic from `conventions/checker_spec.md`.

```python
def normalize(s: str) -> str          # strip per-line trailing ws + trailing blank lines
def judge_exact(produced, expected) -> bool
def judge_custom(validator_path, input_text, produced) -> tuple[bool, str]   # imports validator.validate
def judge_case(criterion, test_case, run_result) -> CaseVerdict
def judge_problem(criterion, solution_path, timeout_override=None) -> ProblemVerdict
```

- `judge_case` maps `RunResult.status` to a verdict: TLE→`TLE`, RUNTIME_ERROR→`RUNTIME_ERROR`, OK→ run `exact` or `custom` per `meta['judge']` → `PASS`/`WRONG_ANSWER`.
- `judge_problem` runs ALL test cases (using per-test `time_limit_s` from meta, unless `timeout_override` given), returns aggregate `PASS` only if every case passed, plus the per-case breakdown.
- Load `validator.validate` dynamically with `importlib.util.spec_from_file_location`.

`ProblemVerdict` dataclass: `family_id; criterion_id; class_label; overall: str; cases: list[CaseVerdict]; first_failure: str | None`.

---

## Module 4 — `harness/extract.py`

Code extraction + thinking-strip used by the generation driver.

```python
def strip_thinking(text: str) -> str   # remove <think>...</think>, <thinking>...</thinking>, and ```reasoning blocks
def extract_code(text: str) -> str     # first ```python fence; else first ``` fence; else whole text
```
These mirror the patterns already used in the user's Ollama evaluation scripts (multi-layer parser that strips chain-of-thought before extracting code).

---

## Module 5 — `harness/aggregate.py`

Turns raw per-problem verdicts into the metrics the proposal needs.

- Read a results directory of `verdict.json` files (one per model/family/criterion).
- Produce a tidy `summary.csv` with columns:
  `model, family_id, family_name, criterion_id, class_label, overall_verdict, first_failure, n_cases, n_passed`.
- Compute and print, per model:
  - pass@1 broken down by `class_label` (P / NPC / INFEASIBLE),
  - the **confident-wrong rate** on INFEASIBLE = fraction of infeasible problems where the model produced a non-null wrong answer (`WRONG_ANSWER`, not the correct infeasibility output),
  - overall pass@1.
- Keep plotting OUT of here; just emit CSV + a printed table. (Plots can be a later notebook.)

---

## Module 6 — `harness/reference_check.py`

A dataset self-test used during dataset construction (file 04/05 will call it).

```python
def check_reference(criterion) -> list[str]   # returns list of problems found (empty = OK)
```
- Runs `reference.py` against every `NN.in`, compares to `NN.out` using the same checker.
- Flags: missing `.out` for an `.in`, reference WRONG_ANSWER vs its own expected output, reference crash, reference TLE at the problem's own time limit.
- Also runs the **leakage check**: scan `statement.md` for forbidden terms from `conventions/statement_schema.md` and flag any hit.

Provide a CLI: `python -m harness.reference_check dataset/family_01_graph_coloring` validates a whole family (or a single criterion path).

---

## Module 7 — `harness/__init__.py`

Empty file to make `harness` a package.

---

## Step — Sanity

After writing, run `python -c "import harness.dataset, harness.runner, harness.checker, harness.extract, harness.aggregate, harness.reference_check"` from the project root to confirm everything imports. If `pyyaml` is missing, `pip install pyyaml --break-system-packages`.

## Done

Confirm all modules import cleanly, list `harness/`, then **stop and wait** for `04_family_template_family01.md`.

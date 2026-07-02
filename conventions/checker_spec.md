# Checker Specification

Defines verdicts, timeouts, and the validator contract. The implementation lives
in `harness/checker.py`; this file is the spec it must satisfy.

## Verdicts
- `PASS`           — output accepted on this test case.
- `WRONG_ANSWER`   — ran, produced output, output rejected.
- `TLE`            — exceeded the time limit.
- `RUNTIME_ERROR`  — non-zero exit, exception, or crash.
- `MLE`            — exceeded memory limit (best-effort; optional).

A problem PASSES only if ALL its test cases return `PASS`.

## Timeouts
- Default per-case wall-clock limit = `time_limit_s` from `meta.yaml`.
- The main study may apply a global ceiling (e.g. 10 minutes) overriding the
  per-problem limit upward; runner reads this from run config.
- The time-budget study overrides downward (e.g. 2 s); also from run config.

## Exact judge
Normalize both produced and expected output (strip per-line trailing whitespace,
strip trailing blank lines), compare line-by-line for equality.

## Custom judge (validator contract)
When `judge: custom`, the criterion folder contains `validator.py` exposing:

```python
def validate(input_text: str, output_text: str) -> tuple[bool, str]:
    """Return (is_valid, reason). is_valid True => PASS."""
```

The runner calls `validate(input_of_case, produced_output)`. The validator must
re-derive correctness from the input alone (it must not trust the model output).

## Infeasible problems
For `class: INFEASIBLE`, the canonical expected output is defined per problem
(often a sentinel like `NO`, or a required certificate). These use `exact` when
the answer is unique, or `custom` when any valid certificate is accepted.
A correct model must produce the infeasibility verdict/certificate; a confident
wrong non-null answer is `WRONG_ANSWER` and is exactly the failure we measure.

# I/O Format Contract

Every solution — reference or model-generated — obeys this contract.

## Input
- Read **all** input from standard input (stdin).
- Never read from a file or prompt interactively.
- Input format is defined per-problem in `statement.md` under "Input".

## Output
- Write **only** the answer to standard output (stdout).
- No debug prints, no prompts, no trailing commentary.
- Output format is defined per-problem under "Output".

## Comparison semantics (how the checker judges output)
Two modes, declared per problem in `meta.yaml` as `judge:`.

1. `exact` — output must equal the expected `.out` file after normalization:
   - strip trailing whitespace on each line,
   - strip trailing blank lines at end of file,
   - compare line by line.
   Use this when the correct answer is unique (e.g. "lexicographically smallest").

2. `custom` — a per-problem `validator.py` decides PASS/FAIL by reading the
   input and the produced output. Use this when ANY valid answer is acceptable
   (e.g. "output any triangle", "output any valid assignment").
   The validator contract is defined in `checker_spec.md`.

## Determinism
Reference solutions must be deterministic and produce the canonical expected
output. If a problem allows multiple answers but we still want `exact`, the
statement must pin a tie-break rule (e.g. lexicographically smallest) so the
expected output is unique.

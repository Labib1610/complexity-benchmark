# 02 — Write the Convention Documents (the "fixed things")

> Prerequisite: directory scaffold from file `01` exists.

## Goal

Create the **five fixed documents** in `complexity-benchmark/conventions/`. Everything downstream depends on these. Write each file exactly as specified. These are the contracts that make results comparable across all 48 problems and all models.

Create the following files.

---

## File A — `conventions/io_format.md`

```markdown
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
```

---

## File B — `conventions/statement_schema.md`

```markdown
# Problem Statement Schema

Every `statement.md` shown to a model MUST contain these sections, in order,
and NOTHING that reveals the complexity class.

## Required sections
1. **Title line** — `# Problem <LETTER> — <Name>`  (e.g. `# Problem A — Trichrome Shifts`)
2. **Limits line** — `Time limit: X s   Memory limit: Y MB`
3. **Description** — prose statement of the task.
4. **Input** — exact format and constraint bounds.
5. **Output** — exact format, including any tie-break rule.
6. **Examples** — at least one input/output pair, fenced.
7. (optional) **Note** — clarifying remarks that do NOT name the class.

## Forbidden in statement.md (leakage check)
Do NOT include any of:
- the words "NP-complete", "NP-hard", "polynomial", "P-time", "bipartite",
  "tree" (when it reveals structure), "DAG", "2-SAT/3-SAT" as labels,
  "intractable", "exponential", reduction names, or any complexity commentary.
- hints like "this is the easy variant" or "brute force is fine".

Constraint bounds (e.g. `n <= 20`) ARE allowed and expected — they are part of
the problem, not a class label. The model must infer difficulty from bounds and
structure, not from labels.

## Where the hidden truth lives: meta.yaml
Each criterion folder has a `meta.yaml` (model NEVER sees it) with:

```yaml
family: 01
family_name: graph_coloring
criterion: 1                 # 1, 2, or 3
class: NPC                   # one of: P | NPC | INFEASIBLE
problem_letter: A
intended_algorithm: "lexicographically-smallest backtracking over 3 colors"
reduction_note: "3-COLORING; Karp 21; reduction from 3-SAT via palette gadget"
constraint_delta: "anchor variant (the NP-complete base)"
judge: exact                 # exact | custom
time_limit_s: 2
memory_limit_mb: 256
```

`class` values:
- `P`          — polynomial-time solvable variant
- `NPC`        — NP-complete variant
- `INFEASIBLE` — no valid solution exists by construction
```

---

## File C — `conventions/prompt_template.md`

```markdown
# Fixed Model Prompt Template

ONE template, identical for every model and every problem in the main study.
The harness slots the statement into `{STATEMENT}`. Do not vary wording per
model — comparability depends on this being fixed.

## System message
```
You are an expert competitive programmer. You write correct, efficient Python 3
solutions. Your program reads all input from standard input and writes only the
required answer to standard output. Output only a single Python 3 code block and
nothing else — no explanation before or after.
```

## User message
```
Solve the following problem in Python 3.

{STATEMENT}

Requirements:
- Read from standard input, write to standard output.
- Output only the answer in the exact format specified.
- Return only one Python 3 code block.
```

## Extraction rule
From the model response, extract the first fenced ```python ... ``` block. If no
fenced block exists, treat the entire response as code. Store raw response AND
extracted code (see generation driver).

## Variants (defined later, do NOT add here)
- Time-budget study appends a grading-policy block — see `studies/`.
- Token-budget study caps `max_tokens` at generation — see `studies/`.
- Multi-turn study sends a turn sequence — see `studies/`.
The BASE template above never changes.
```

---

## File D — `conventions/checker_spec.md`

```markdown
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
```

---

## File E — `conventions/registry_format.md`

```markdown
# Model Registry Format

`models/registry.yaml` lists every research model. The generation driver reads
it. Two backends: `ollama` (local open-source) and `api` (closed-source).

## Schema
```yaml
models:
  - id: phi4                      # unique short id (used in folder paths)
    display_name: "Phi-4"
    backend: ollama               # ollama | api
    model_string: "phi4"          # ollama tag or API model id
    openness: open                # open | closed
    thinking: false               # true for reasoning models (R1, qwen3, gpt-oss)
    token_budget: 4096            # default max generation tokens
    notes: ""

  - id: claude-sonnet
    display_name: "Claude Sonnet"
    backend: api
    model_string: "claude-sonnet-4-6"
    openness: closed
    thinking: false
    token_budget: 4096
    notes: ""
```

## Rules
- `id` is the directory-safe key used under `generations/<id>/...`.
- `thinking: true` models get elevated `token_budget` and their chain-of-thought
  is stripped before code extraction (handled in the driver).
- Adding a model = adding a list entry. Never edit harness logic to add a model.
```

---

## Done

Create all five files exactly as above. Then list `conventions/` and print the first ~15 lines of each so the user can confirm. **Stop and wait** for `03_harness.md`.

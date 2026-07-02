# 07 — Constraint Studies (Time Budget, Token Budget, Multi-Turn)

> Prerequisite: drivers from file `06` work in dry-run on Family 1.

## Goal

Add the three constraint studies as **prompt/run variants on top of the existing dataset**. They reuse all 48 problems, all references, all test cases. They only change the prompt and/or the run config. **No changes to `dataset/`.** This is where the user's "later add token budget and time budget constraint" plugs in cleanly.

Everything lives under `complexity-benchmark/studies/`.

---

## Study 1 — Time Budget (approximation under strict runtime)

Tests RQ4–RQ6: under a tight runtime limit with partial credit, do models switch from exact to heuristic algorithms?

Create `studies/time_budget/`:

### `studies/time_budget/prompt_suffix.md`
A block appended to the fixed user prompt (the base template is unchanged):
```markdown
Constraints for this submission:
- Your program must finish within {RUNTIME_LIMIT_S} seconds per run.
- Grading is partial: you earn credit proportional to solution quality. A run
  that exceeds the time limit earns zero. A correct-but-too-slow exact solution
  scores worse than a fast good-enough approximate one.
- Output the best answer you can within the time limit, in the format specified.
```
`{RUNTIME_LIMIT_S}` is filled from run config.

### `studies/time_budget/scoring.py`
Partial-credit scoring beyond pass/fail:
```python
def approx_ratio(produced_value, optimal_value, minimize: bool) -> float:
    # ratio in [0,1]; 1.0 == optimal. For minimization use optimal/produced.
def score_case(criterion, produced_output, optimal_output, run_result) -> dict:
    # returns {tle: bool, exact: bool, ratio: float, strategy: str|None}
```
- For NPC problems we need the **objective value**, not just pass/fail. Add an optional `objective.py` per criterion (only for problems studied here) exposing `value(input_text, output_text) -> float`. Default behavior: if no `objective.py`, fall back to binary pass/fail.
- `strategy` classification is a stub returning `None` for now (qualitative analysis filled later); leave the hook.

### Run config additions
Reuse `run_config_template.yaml` with `study: time_budget` and an evaluation block:
```yaml
study: time_budget
time_budget:
  runtime_limit_s: 2          # the strict per-run limit shown to the model AND enforced
metrics: [tle_rate, approx_ratio]
```
The evaluate driver, when `study == time_budget`, enforces `runtime_limit_s` as the timeout AND calls `scoring.score_case` to emit ratio/TLE alongside the verdict.

---

## Study 2 — Token Budget

Tests whether generation length caps affect complexity-class performance.

Create `studies/token_budget/`:

### `studies/token_budget/README.md`
```markdown
# Token Budget Study
Same prompts as the main study. The only change is max generation tokens, swept
across levels. We measure how pass@1-by-class degrades as the budget shrinks —
in particular whether NPC and infeasible problems (which may need more reasoning)
degrade faster than P problems.
```

### Mechanism (no new prompt)
- Add to run config:
```yaml
study: token_budget
token_budget:
  levels: [512, 1024, 2048, 4096]   # one run per level, or sweep in one driver pass
```
- The generate driver, when `study == token_budget`, loops the sweep: for each level it overrides every model's `token_budget` to that level and writes generations into a level-suffixed subfolder:
  `generations/<model>/__tok<level>/family_XX/criterion_n/solution.py`
- Evaluate aggregates per (model, level, class). Aggregator gains a `token_level` column when present.

> For thinking models, remember the budget must cover chain-of-thought; the driver should warn if a level is below a model's minimum sensible budget.

---

## Study 3 — Multi-Turn Complexity Transitions

Tests RQ7–RQ9: do models track implicit class shifts across turns?

Create `studies/multiturn/`:

### `studies/multiturn/sequences.yaml`
Defines transition sequences over classes {P, NP, I}, adjacent turns must differ:
```yaml
length_2:
  - [NPC, P]
  - [NPC, INFEASIBLE]
  - [P, NPC]
  - [P, INFEASIBLE]
  - [INFEASIBLE, P]
  - [INFEASIBLE, NPC]
length_3:
  - [P, NPC, INFEASIBLE]
  - [NPC, P, NPC]     # revisiting sequence of interest
  # ... enumerate all adjacent-differ sequences (6 of length 2, 12 of length 3)
conditions:
  - explicit     # the shift names the structure plainly
  - implicit     # the shift is embedded in a constraint, never naming the class
control:
  - same_class   # e.g. NPC -> NPC with a new but still-NPC constraint (isolates context degradation)
```

### `studies/multiturn/turn_templates.md`
For a given family, each turn reuses that family's existing per-criterion `statement.md` as the "problem at this class," wrapped as a conversation:
```markdown
Turn 1: <statement of the first class in the sequence>
Turn k>1 (implicit): "Now assume <constraint that shifts to the next class>, keep solving."
Turn k>1 (explicit): "Now the problem is <named-structure> ; solve it."
```
The implicit constraint phrasings per family come from each family's `constraint_delta` in `meta.yaml` — reworded to NOT name the class (implicit condition) or named plainly (explicit condition).

### `studies/multiturn/driver_notes.md`
```markdown
The multiturn driver extends generate.py:
- Builds a running message history; sends turn t with all prior turns included.
- After each turn, extracts code and evaluates against THAT turn's class problem
  (same family, the criterion matching the class at turn t).
- Records pass@1 per turn => a trajectory per sequence.
- Aggregator computes: direction-of-transition effects (NPC->P improvement,
  P->NPC degradation), infeasibility-detection accuracy when a turn introduces
  INFEASIBLE, and revisit failures (e.g. NPC->P->NPC).
Implement as harness/multiturn.py reusing backends + checker; do not duplicate logic.
```

> Implement `harness/multiturn.py` only the skeleton now (message-history builder + per-turn evaluate loop calling existing checker). Full enumeration of the 18 sequences × conditions can be wired when the user runs it.

---

## Step — Final integration check

1. Confirm `studies/` contains the three subfolders with the files above.
2. Confirm the evaluate driver branches on `study` (main / time_budget / token_budget / multiturn) and that `main` is unchanged.
3. Print a short SUMMARY of the whole project: directory tree (top 3 levels), which families are filled vs placeholder, and the exact commands to run each study:
   - main:        generate + evaluate with `study: main`
   - time budget: set `study: time_budget`, `runtime_limit_s`
   - token budget:set `study: token_budget`, `levels`
   - multiturn:   set `study: multiturn`, point at `sequences.yaml`

## Done — full pipeline is now scaffolded

At this point the user can: fill families 02–16 one at a time (using `dataset/HOW_TO_FILL_A_FAMILY.md` and Family 1 as the template), drop in numbered test cases, register models, and run any of the four studies. Report completion and wait for further instructions from the user.

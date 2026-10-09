# Family 06 (Bin Packing / Cargo Loading) — Rebuild Notes

Rebuilt following the family_04 template, and following the audit's specific guidance for this family:
"use one indivisible **optimisation** contract across conditions ... and require quality scoring."

## What was wrong (audit findings for family 06)

- **B4** — criterion 1 was an indivisible **feasibility decision** (with a k budget) while criterion 2
  was **divisible (fractional)** bin packing without k — a different task, output, and schema. The
  audit also noted the A gap was weak (a single symmetry cut).
- **B7 / gate 3** — no `objective.py`, so the time-budget study could not score packing quality.

Criterion 3 was already an instance-specific certificate (report the smallest oversized item), so it
was never gameable (G7 passed for it).

## What changed

The family is now unified on **minimum bin packing (indivisible)**: minimise the number of
fixed-capacity containers to load all items, reporting the count and one assignment. One schema
(`n C` + weights), one output (count + per-item container) across all three criteria.

### Criterion 1 (NPC) — general min bins
- Reference: from the lower bound `ceil(sum/C)` upward, test feasibility with heaviest-first
  backtracking + empty-container symmetry cut; report the first feasible count and its assignment.
  Instances are `n = 2k` complementary pairs near C/2 (perfect packing → minimum exactly k). n ≤ 28.

### Criterion 2 (P) — every item > C/3 (the one switch)
- Because every item exceeds C/3, at most two fit per container, so the optimum is a **two-pointer
  greedy** (pair the heaviest with the lightest that fits, else the heaviest alone) — exact and
  O(n log n). ~0.14 s at n = 200000.

### Criterion 3 (INFEASIBLE) — unchanged task, hardened tests
- Still the oversized-item certificate (smallest index with weight > C). Regenerated with the
  oversized item at **varied** positions (2, 6, 1, 500, 20000, 1, 123456) so no positional constant
  (e.g. always "print n") can pass.

## B7 approximation scoring (gate 3)

Added `objective.py` (C1 and C2, `MINIMIZE = True`): `value()` recomputes the containers used from
the assignment (0 for an invalid loading). Verified through the real `studies/time_budget/scoring.py`:
optimal loading → ratio 1.0; a valid but wasteful loading (each item alone, 8 vs optimal 4) → ratio
0.50. This is the first minimisation objective in the rebuild (knapsack/LCS were maximisation).

## Correctness testing

Both references were **verified against a brute-force minimum bin packing** on 400 random instances
each — checking the count and a valid assignment. All passed.

## Verification

- `reference_check` passes all 3 criteria.
- References within the declared limit: C1 0.009 s ≤ 5 s, C2 0.14 s ≤ 2 s, C3 0.03 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Same gradeable-NPC ceiling: the reference must compute the exact minimum, so n ≤ 28. The tier
separates a symmetry-blind search from the symmetry-cut search; it does not prove hardness against a
competent solver. True SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_06.py --criterion 1 --k <pairs> --C <C> --seed <s>   # general min bins
python tools/gen_family_06.py --criterion 2 --n <n> --C <C> --seed <s>       # every item > C/3
python tools/gen_family_06.py --criterion 3 --n <n> --C <C> --seed <s> --at <pos>   # oversized
```

# Family 12 (0-1 Knapsack / Portfolio Selection) — Rebuild Notes

Rebuilt following the family_04 template. Knapsack is an **optimization** family, so it also fixes
**B4** (the P-tier had become a different task) and adds **B7** approximation scoring.

## What was wrong (audit findings for family 12)

- **B4** — Criterion 2 was **fractional** knapsack, a *different task* from the 0-1 criterion 1. A
  performance gap between them could not be attributed to the complexity switch.
- **B5** — Criterion 3 used budget **B = 0** and required a constant `NO`; `print("NO")` passed.
- **B7 / gate 3** — this is an optimization family but had **no `objective.py`**, so the
  time-budget/approximation study could not score partial credit.
- **B6** — inputs reused fixed seeds.

## What changed

### Criterion 1 (NPC) — Portfolio Selection (0-1 knapsack, optimization)
- Already non-gameable (reports the max value + a witness subset; a constant cannot fake the exact
  optimum). Kept the meet-in-the-middle O(2^(n/2)) reference; reseeded per case (B6); honest ceiling
  documented (MITM peaks ~137 MB at n=36, OOMs by n=38, so the ramp caps at n=36; statement n≤40).
- Added **`objective.py`** (B7).

### Criterion 2 (P) — Portfolio Selection (Small Costs)
- Rewritten from fractional knapsack to the **same 0-1 knapsack** with the **same schema and
  output** as criterion 1 (audit B4). The one documented switch is a small cost/budget bound
  (costs ≤ 100, B ≤ 2000), which makes the pseudo-polynomial O(n·B) DP polynomial.
- Reference is an O(n·B) budget DP with witness reconstruction — **~0.13 s at n = 2000** vs the 2 s
  limit (gate 12). Added `objective.py` (B7).

### Criterion 3 (INFEASIBLE) — Certify Impossibility
- Redesigned from the constant-`NO`, B=0 design into an **infeasibility-certificate** task: every
  cost strictly exceeds the budget (nothing affordable), and the model must output `MIN m` with
  **B < m ≤ every cost**, checked by `validator.py`. **A constant program fails** (verified: `NO`
  scores WRONG_ANSWER).
- Honest note: unlike partition (three mechanisms), knapsack affordability-infeasibility admits
  essentially **one** cheap certificate (the cheapest item exceeds the budget); non-gameability
  comes from requiring the instance-specific bound m.

## B7 approximation scoring (gate 3) — now working end to end

`objective.py` (in C1 and C2) exposes `value(input_text, output_text)` and `MINIMIZE = False`. It
recomputes the achieved value **from the witness** (it does not trust the claimed number), returning
0 for an infeasible or malformed selection. Verified through the real
`studies/time_budget/scoring.py`:

| model output | score |
|---|---|
| exact optimum | ratio **1.0** |
| feasible but suboptimal | ratio **0.65** (partial credit) |
| infeasible witness | ratio **0.0** |

This is the first family to exercise the full B7 pipeline end to end.

## Verification

- `reference_check` passes all 3 criteria.
- References within the declared limit: C1 0.53 s ≤ 5 s, C2 0.13 s ≤ 2 s, C3 0.01 s ≤ 2 s.
- Constant `NO` fails C3; the old B=0 gaming route now scores WRONG_ANSWER.
- `release_check`: family 12 clean on G7 and G9 (global gameable arms 4→3).

## Honest limitation

Same gradeable-NPC ceiling as family 04/13: a model writing meet-in-the-middle solves every C1 case
in < 1 s. The tier separates naive O(2ⁿ) search / pseudo-poly DP from MITM; it does not prove
hardness against a competent exact solver. True SOTA-resistance needs phases P2–P3.

## Regeneration

```
python tools/gen_family_12.py --criterion 1 --n <n> --seed <s>   # 0-1 knapsack, large values
python tools/gen_family_12.py --criterion 2 --n <n> --seed <s>   # 0-1 knapsack, small budget
python tools/gen_family_12.py --criterion 3 --n <n> --seed <s>   # unaffordable (MIN certificate)
```

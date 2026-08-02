# 37 — Scale Family 12: Investment Portfolios (Knapsack)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_12_knapsack/`.

## Family 12 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | meet-in-the-middle, **O(2^(n/2))** | **naive: 2^n subset search, or O(n·B) DP (blocked by huge B)** | **huge asymptotic gap ✅** |
| 2 | P | greedy by ratio, O(n log n) | naive: O(n²) selection, or DP | asymptotic gap ✅ |
| 3 | INFEASIBLE | B=0 arithmetic check | naive: searches anyway | asymptotic gap ✅ |

**Mirrors Family 04 (subset sum).** Same clean 2^(n/2) vs 2^n separation. Two naive routes
both fail: subset search (2^n) and weight-DP (blocked because B is up to 1e9 → table too big).
Keep costs/values large so the DP route stays blocked — that's the "weakly NP-complete with
large values" design.

## Criterion 1 (NPC) — meet-in-the-middle vs 2^n

1. `tools/naive_family_12_criterion_1.py` — realistic: recursive include/exclude with pruning
   on remaining budget. Natural without meet-in-the-middle.
   - Optionally `..._dp.py` (O(n·B) DP) → confirm MemoryError/TLE given huge B. Report both.
2. Probe `n ∈ [26, 30, 34, 38, 42]`, costs/values up to 1e9, `B ≈ sum(costs)/2` (defeats
   pruning; a tight budget is what makes it hard).
3. Statement says `n ≤ 40`; keep or raise. Check reference memory (sorts 2^(n/2) half-subsets).

## Criterion 2 (P) — fractional, punish O(n²)

Greedy by value/cost ratio is O(n log n). Baseline = O(n²) repeated max-ratio scan → TLE at
n=2e5. Scale `n ∈ [1e3, 1e4, 5e4, 1e5, 2e5]`.

**Watch the output precision:** the statement pins a fixed decimal precision. Confirm the
reference's rounding is stable at large n (floating-point accumulation). If sums get large,
verify the reference's output is deterministic — if precision drifts, flag it, since `exact`
judging depends on byte-identical output.

## Criterion 3 (INFEASIBLE) — B=0, positive costs, must pick ≥1

Reference is an arithmetic check. Baseline searches first → TLEs. Scale n toward the bound.
Answer stays `NO`.

## Procedure

1. `tools/gen_family_12.py` — seeded: `gen_knapsack_large(n, seed)` (large costs/values,
   B≈sum/2), `gen_fractional(n, seed)`, `gen_zero_budget(n, seed)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases; report the DP route's failure mode.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_12_knapsack` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
**Flag any floating-point precision instability in criterion 2.**

Then **stop and wait** for `38_scale_family13_partition.md`.

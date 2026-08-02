# 29 — Scale Family 04: Budget Selection (Subset Sum)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_04_subset_sum/`.

## Family 04 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | meet-in-the-middle, **O(2^(n/2))** | **naive: full subset enumeration or DP over sum, O(2ⁿ) / O(n·T)** | **huge asymptotic gap ✅** |
| 2 | P | DP over sums, O(n·T), T small | naive: O(2ⁿ) subset search ignoring the small bounds | asymptotic gap ✅ |
| 3 | INFEASIBLE | arithmetic check (negative target) | naive: searches subsets anyway | asymptotic gap ✅ |

**This family has the cleanest window in the benchmark.** Meet-in-the-middle is
2^(n/2); naive enumeration is 2ⁿ. At n=40: reference ≈ 2²⁰ ≈ 1M (instant), naive ≈ 2⁴⁰ ≈
10¹² (hopeless). This is the family to point at when explaining the design.

Note the second trap for criterion 1: a model might write **DP over sums** (O(n·T)),
which is *pseudo-polynomial*. With `T` up to 4·10¹⁰ that DP is impossible (memory and
time). Both plausible naive routes fail — good. Keep values large so the DP route is
genuinely blocked; that is the whole point of the "weakly NP-complete with large values"
design in `meta.yaml`.

## Criterion 1 (NPC) — exploit 2^(n/2) vs 2ⁿ

1. Write `tools/naive_family_04_criterion_1.py` — realistic: recursive
   include/exclude subset search with basic pruning (stop if running sum exceeds target).
   This is the natural solution when a model doesn't think of meet-in-the-middle.
   - Optionally also write `tools/naive_family_04_criterion_1_dp.py` (DP over sums) and
     confirm it fails on **memory/time** given the huge `T`. Report both.
2. Probe the baseline across `n ∈ [26, 30, 34, 38, 42]` with large values (up to 1e9).
   **Hard instances = no valid subset exists** (forces full exploration) or targets that
   are just barely unreachable. Pruning helps most when the target is small, so keep
   `T ≈ sum/2` to defeat it.
3. Expect the baseline to TLE around **n ≈ 30–36**; the reference at n=42 is 2²¹ ≈ 2M —
   still fast. You have a lot of room here.
4. `chosen_max_size`: the statement says `n ≤ 40`; you can likely keep or raise it.
   Check the reference's memory at large n (it sorts 2^(n/2) half-sums).

## Criterion 2 (P) — the small-bounds arm

The point: with small values the DP is genuinely polynomial. The baseline must be a
solution that **ignores the small bounds** and does subset search (2ⁿ) → TLEs, while the
O(n·T) DP reference is comfortable.

Scale `n` up (statement says `n ≤ 1000`, costs ≤ 100, `T ≤ 500`). At n=1000 the DP table
is 1000×500 = 500K — trivial. A 2ⁿ search at n=1000 is beyond hopeless, so this arm bites
easily. Also add a case where a **correct but O(n·T) with poor constants** (e.g. Python
list-of-lists instead of a rolling boolean array) strains — that is the realistic
inefficiency to punish here.

## Criterion 3 (INFEASIBLE) — negative target

Reference is an arithmetic check. Baseline = a solution that searches subsets before
concluding → TLEs at large n. Scale `n` toward the bound with large values and a negative
`T`. The answer stays `NO`.

## Procedure

1. `tools/gen_family_04.py` — seeded. Generators:
   - `gen_subsetsum_large(n, seed, reachable=None)` — values up to 1e9; when
     `reachable=False`, choose T deliberately unreachable (e.g. sum/2 shifted by 1 with
     all-even values → parity-unreachable, forcing full search).
   - `gen_subsetsum_small(n, seed, reachable=True)` — costs ≤ 100, T ≤ 500.
   - `gen_negative_target(n, seed)` — positive costs, negative T.
2. Write the realistic baselines.
3. **Probe with the baseline.** Confirm exponential blow-up.
4. Emit a 5-case ramp straddling the threshold; keep anchors, append.
5. **Generate `.out` with the reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 at `time_limit_s` on the largest cases. If you
   wrote the DP variant baseline, report its failure mode (MemoryError or TLE).
7. Update `statement.md` bounds to match.
8. Append `scaling:` provenance.
9. `python -m harness.reference_check dataset/family_04_subset_sum` → clean.

## Report

Probe curve, threshold, ramp, proof exit codes (both naive routes if applicable),
reference gen times, bound changes, reference_check clean.

**Also note for the user:** this family should show the widest, cleanest gap — if it
doesn't, something is wrong with the size selection, since the asymptotic separation here
is unambiguous.

Then **stop and wait** for `30_scale_family05_three_dim_matching.md`.

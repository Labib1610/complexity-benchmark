# 38 — Scale Family 13: Workload Partitioning (Partition Problem)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_13_partition/`.

## Family 13 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | meet-in-the-middle for sum=S/2, **O(2^(n/2))** | **naive: 2^n subset search / blocked DP** | **huge asymptotic gap ✅** |
| 2 | P | DP over sums, O(n·S), S small | naive: 2^n search ignoring small values | asymptotic gap ✅ |
| 3 | INFEASIBLE | parity check (odd sum) | naive: searches anyway | asymptotic gap ✅ |

**Mirrors Families 04 and 12.** Clean separation.

## Criterion 1 (NPC) — the hard instances matter

1. `tools/naive_family_13_criterion_1.py` — realistic: recursive include/exclude with pruning.
2. Probe `n ∈ [26, 30, 34, 38, 42]` with durations up to 1e9.
   **Hardest instances: even total sum, but NO valid equal partition exists** — forces
   exhaustive refutation. Construct these deliberately (e.g. values where S/2 is unreachable
   by a parity/gcd argument, while S stays even). A random even-sum instance is usually
   *satisfiable* and easy — do not rely on random.
3. Statement says `n ≤ 40`; keep or raise.

## Criterion 2 (P) — small durations

Small values (≤100), `n ≤ 2000`, `S ≤ 2e5` → DP table is polynomial. Baseline = 2^n search →
dead instantly at n=2000. Also add a realistic-inefficiency case: an O(n·S) DP with poor
constants (list-of-lists instead of a rolling bitset/bytearray) should strain.

Scale `n ∈ [200, 500, 1000, 2000]`. Include splittable and non-splittable even-sum cases.

## Criterion 3 (INFEASIBLE) — odd sum

Reference sums and checks parity, O(n). Baseline searches subsets first → TLEs at large n.
Scale n toward the bound with a guaranteed odd total. Answer stays `NO`.

## Procedure

1. `tools/gen_family_13.py` — seeded: `gen_partition_large(n, seed, splittable=None)` (must
   support constructing hard even-sum-but-unsplittable instances), `gen_partition_small(n, seed)`,
   `gen_odd_sum(n, seed)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_13_partition` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
**Explicitly confirm the hard NPC cases are even-sum-but-unsplittable**, not random.

Then **stop and wait** for `39_scale_family14_steiner_tree.md`.

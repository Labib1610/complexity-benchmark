# 39 — Scale Family 14: Network Extension (Steiner Tree)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_14_steiner_tree/`.

## Family 14 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | Dreyfus-Wagner DP, **O(3^t·n + 2^t·n²)** | **naive: enumerate subsets of optional nodes + MST, O(2^(n−t)·m log m)** | **asymptotic gap ✅** |
| 2 | P | MST (Kruskal/Prim), O(m log m) | naive: O(n²) Prim w/o heap, or O(m·n) union-find without compression | asymptotic gap ✅ |
| 3 | INFEASIBLE | degree scan, O(n+m) | naive: attempts the tree build first | asymptotic gap ✅ |

**Criterion 1's window comes from the terminal/node asymmetry:** the reference is exponential
in `t` (terminals, kept ≤ 10 → 3¹⁰ ≈ 59K, fine), while a naive solution is exponential in the
number of **optional nodes** (n − t). **Hold `t` small and grow `n`.** That asymmetry is the
whole window — the same trick as Family 11.

## Criterion 1 (NPC) — hold t, grow n

1. `tools/naive_family_14_criterion_1.py` — realistic: enumerate subsets of optional (Steiner)
   nodes, build an MST on terminals ∪ subset, take the minimum. Natural without Dreyfus-Wagner.
2. Probe with `t ∈ [8, 10]` fixed and `n ∈ [24, 30, 36, 42]` (so optional nodes = n − t grows).
   The baseline is 2^(n−t) → dies fast. The reference stays ~3^t·n → fine.
3. Statement says `n ≤ 100, t ≤ 10`. Keep `t ≤ 10`; the baseline should TLE well before n=100,
   so pick the max where the baseline decisively fails and the reference is still tractable.
4. Hard instances: graphs where an optional relay genuinely lowers cost (so the answer isn't
   just the terminal MST), with many near-tie relay choices.

## Criterion 2 (P) — MST, punish the O(n²)

Scale toward bounds: `n ∈ [1e3 … 2e5]`, `m ≤ 2e5`, guaranteed connected. Baseline = Prim
without a heap (O(n²)) or Kruskal with a naive union-find (no path compression / no union by
rank) → TLE at n=2e5, while the reference is O(m log m). Include equal-weight-edge cases
(tests tie handling) and a sparse tree-like graph.

## Criterion 3 (INFEASIBLE) — isolated required node

Reference scans degrees, O(n+m). Baseline attempts a Steiner/MST build first → TLEs. Scale n,
m toward bounds; one case with the isolated terminal at a **high index**.

## Procedure

1. `tools/gen_family_14.py` — seeded: `gen_steiner(n, m, t, seed)` (relays that genuinely help),
   `gen_mst(n, m, seed)` (connected, with equal-weight cases), `gen_isolated_terminal(n, m, t, seed, at)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up. Remember: hold `t`, grow `n`.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_14_steiner_tree` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
Note that criterion 1's window comes from **fixing t while growing n**.

Then **stop and wait** for `40_scale_family15_lcs.md`.

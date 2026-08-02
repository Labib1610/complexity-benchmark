# 35 — Scale Family 10: Sensor Placement (Dominating Set)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_10_dominating_set/`.

## Family 10 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | branch-and-bound / pruned search | **naive: all C(n,k) subsets, check domination** | **asymptotic gap ✅** |
| 2 | P | tree DP (3 states), O(n) | **naive: exponential search ignoring tree structure** | **huge gap ✅** |
| 3 | INFEASIBLE | isolated-vertex scan, O(n+m) | naive: searches placements first | asymptotic gap ✅ |

**Criterion 2 is notable:** the reference is O(n) tree DP; a model that doesn't recognize the
structure may attempt exponential search. At n=2e5 that's instant death. This arm should bite
hard — and it directly tests whether the model *recognizes* the tractable structure, which is
exactly the paper's thesis.

## Criterion 1 (NPC) — subset enumeration dies

1. `tools/naive_family_10_criterion_1.py` — realistic: iterate over combinations of k vertices,
   check every vertex is dominated. Natural without B&B.
2. Probe `n ∈ [24, 28, 32, 36]` with `k` near the true minimum dominating set (hardest).
   **NO instances (k one below minimum) force exhaustive search.** Sparse-ish random graphs
   at average degree 3–5 are hard here.
3. Statement says `n ≤ 30`; raise to the new max. Keep the reference tractable offline.

## Criterion 2 (P) — tree DP vs exponential

Scale `n ∈ [1e3, 1e4, 5e4, 1e5, 2e5]`. Use varied tree shapes: a **path** (deep recursion —
also tests that solutions use iterative post-order, since recursive DFS will hit Python's
recursion limit at n=2e5 → RUNTIME_ERROR, a legitimate and interesting failure), a **star**, a
**balanced binary tree**, and a **random tree**.

Baseline = exponential subset search → TLE. Also worth noting: a *recursive* tree DP will
RuntimeError on the path case — report that as a distinct, realistic failure mode.

## Criterion 3 (INFEASIBLE) — isolated vertex, k=0

Reference scans degrees. Baseline attempts placement search → TLEs. Scale n toward the bound;
one case with the isolated vertex at a **high index**.

## Procedure

1. `tools/gen_family_10.py` — seeded: `gen_domset(n, m, k, seed, dominatable=None)`,
   `gen_tree(n, seed, shape="path"|"star"|"balanced"|"random")`, `gen_isolated_k0(n, m, seed, at)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_10_dominating_set` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
**Explicitly note the recursion-depth failure mode on the path-shaped tree case** — it's a
realistic model failure worth documenting.

Then **stop and wait** for `36_scale_family11_set_cover.md`.

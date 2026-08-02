# 28 — Scale Family 03: Delivery Routing (Hamiltonian Path)

> Follow `25_START_test_case_scaling.md` (corrected). Family 01 is the proven template.
> Target: `dataset/family_03_hamiltonian_path/`.

## Family 03 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | Hamiltonian path, bitmask DP O(2ⁿ·n²) | **naive DFS with backtracking, O(n!)** | **huge asymptotic gap ✅** |
| 2 | P | unique-topological-order check, O(n+m) | naive: try permutations / O(n²) repeated scans | asymptotic gap ✅ |
| 3 | INFEASIBLE | scan degrees, O(n+m) | naive: search for a path before concluding | asymptotic gap ✅ |

**Criterion 1 has the best window in the whole benchmark so far.** The reference is
bitmask DP (2ⁿ·n²); a naive model solution is very plausibly **recursive DFS
backtracking (n!)**. At n=14, 2ⁿ·n² ≈ 3.2M (instant) while n! ≈ 87 billion (hopeless).
That is a genuine asymptotic gap — expect this family to scale easily.

## Criterion 1 (NPC) — exploit the DP-vs-permutation gap

1. Write `tools/naive_family_03_criterion_1.py` — realistic: recursive DFS from each
   start vertex, marking visited, backtracking. This is the natural, obvious solution a
   competent model writes when it does **not** think of bitmask DP. Include the standard
   "visited" pruning (that's realistic); do not add memoization (that would BE the DP).
2. Probe the baseline across `n ∈ [12, 14, 16, 18, 20, 22]`. **Hard instances for
   DFS backtracking are graphs with NO Hamiltonian path but high connectivity** — the
   search explores enormously before failing. Also dense graphs where many partial paths
   look viable. Hunt adversarial seeds.
3. Expect the baseline to TLE around **n ≈ 16–20** on hard NO instances, while the
   bitmask-DP reference stays fast well past that (2²⁰·400 ≈ 4·10⁸ — minutes offline,
   which is fine).
4. `chosen_max_size`: push to where the reference is still tractable offline. The
   statement currently says `n ≤ 18` (chosen for Held-Karp); you can likely raise it.
   Note memory: bitmask DP at n=24 needs 2²⁴·24 states — check RAM before committing.

## Criterion 2 (P) — punish inefficiency

Baseline `tools/naive_family_03_criterion_2.py` = correct but inefficient: e.g. repeatedly
scan all vertices to find in-degree-0 each step (O(n²)) instead of maintaining a queue, or
build an adjacency matrix. Must TLE at n=2·10⁵ while the O(n+m) Kahn reference is fast.

Scale `n ∈ [1e3, 1e4, 5e4, 1e5, 2e5]`, `m ≈ 2n` (respect `m ≤ 2e5`), graph guaranteed
acyclic. Include a large YES (unique topological order = a forced chain) and a large NO
(two simultaneous in-degree-0 vertices).

## Criterion 3 (INFEASIBLE) — scale toward the bound

Baseline = a solution that actually searches for a Hamiltonian path before noticing the
isolated vertex (exponential) → TLEs. The reference just scans degrees, O(n+m).

Scale toward the stated bound. Ensure at least one large case where the isolated vertex
is at a **high index**, so "print the first isolated vertex found while scanning from 1"
is still correct but a solution that reports a *non-smallest* one fails.

## Procedure

1. `tools/gen_family_03.py` — seeded. Generators:
   - `gen_ham(n, m, seed, has_path=None)` — general graph; hard NO instances = dense,
     well-connected, but Hamiltonicity destroyed (e.g. plant a cut vertex or an
     unbalanced bipartition).
   - `gen_dag_unique(n, seed, unique=True)` — DAG with a forced unique topological order
     (a chain plus forward edges) or with two sources when `unique=False`.
   - `gen_isolated(n, m, seed, iso_at)` — graph with a planted degree-0 vertex.
2. Write the three realistic baselines.
3. **Probe with the baseline.** Confirm exponential blow-up on criterion 1.
4. Emit a 5-case ramp straddling the threshold; keep existing anchors, append numbers.
5. **Generate `.out` with the reference, unlimited time.** Record elapsed (provenance only).
6. **Mandatory proof:** baseline exit=124 at `time_limit_s` on the largest cases.
7. Update `statement.md` bounds to match new max sizes.
8. Append `scaling:` provenance to each `meta.yaml`.
9. `python -m harness.reference_check dataset/family_03_hamiltonian_path` → clean.

## Report

Probe curve, threshold, ramp with pass/TLE, proof exit codes, reference gen times,
bound changes, reference_check clean. Flag the memory ceiling if bitmask DP limits size.

Then **stop and wait** for `29_scale_family04_subset_sum.md`.

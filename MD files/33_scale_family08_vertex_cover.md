# 33 — Scale Family 08: Security Guard Placement (Vertex Cover)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_08_vertex_cover/`.

## Family 08 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | bounded-search-tree branching, **O(2^k·m)** | **naive: try all C(n,k) vertex subsets** | **asymptotic gap ✅** |
| 2 | P | Hopcroft-Karp (König), O(E√V) | naive: Kuhn's O(V·E), or brute-force cover search | asymptotic gap ✅ |
| 3 | INFEASIBLE | greedy matching of size k+1, O(m) | naive: searches for a cover before concluding | asymptotic gap ✅ |

**Criterion 1 has a real gap:** the FPT branching is 2^k (k = budget), while a naive subset
search is C(n,k). At n=40, k=18: 2¹⁸ ≈ 262K vs C(40,18) ≈ 10¹¹. Exploit that.

## Criterion 1 (NPC) — 2^k vs C(n,k)

1. `tools/naive_family_08_criterion_1.py` — realistic: iterate over combinations of k
   vertices, check if each covers all edges (with early exit). This is the natural solution
   when a model doesn't know the FPT branching trick.
   - A second plausible baseline: greedy/heuristic cover — but that gives *wrong answers*,
     not TLE. Note if you see that; it's a WRONG_ANSWER signal, also interesting.
2. Probe `n ∈ [30, 36, 40, 46]` with `k` set near the true minimum cover (hardest — the
   answer is barely achievable or barely not). **NO instances (k one below the true minimum)
   force exhaustive search** — hunt those.
3. Keep `k ≤ 18` so the reference's 2^k stays tractable; raise `n` freely (that's what kills
   the C(n,k) baseline). Update the statement bounds accordingly.

## Criterion 2 (P) — bipartite, König

Scale toward the bound: `nA,nB ∈ [1e3 … 1e5]`, `m ≤ 2e5`. Baseline = Kuhn's O(V·E) or an
adjacency-matrix approach → TLE, while Hopcroft-Karp is fast. As with Family 05, Kuhn's is
often fast in practice — use **adversarial structures with long augmenting chains**. If the
gap stays too narrow, report it.

## Criterion 3 (INFEASIBLE) — matching lower bound

Reference greedily collects k+1 disjoint edges, O(m). Baseline attempts to find a cover of
size k first (exponential) → TLEs. Scale n, m toward bounds with a large planted matching.
**judge is `custom`** here — verify the validator still works at scale (it checks the printed
edges are real, disjoint, and exactly k+1).

## Procedure

1. `tools/gen_family_08.py` — seeded: `gen_vc(n, m, k, seed, coverable=None)`,
   `gen_bipartite_vc(nA, nB, m, seed)`, `gen_big_matching(n, m, k, seed)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_08_vertex_cover` → clean (confirm the custom validator runs).

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
Flag if criterion 2's Kuhn-vs-HK gap is too narrow.

Then **stop and wait** for `34_scale_family09_clique_independent_set.md`.

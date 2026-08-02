# 34 — Scale Family 09: Social Network Analysis (Clique / Independent Set)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_09_clique_independent_set/`.

## Family 09 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | Bron-Kerbosch w/ pivoting or bitset B&B | **naive: check all C(n,k) subsets** | **asymptotic gap ✅** |
| 2 | P | Hopcroft-Karp (König), O(E√V) | naive: brute-force independent set search | asymptotic gap ✅ |
| 3 | INFEASIBLE | pigeonhole check (r > n), O(1) | naive: searches subsets anyway | asymptotic gap ✅ |

## Criterion 1 (NPC) — pivoting vs subset enumeration

1. `tools/naive_family_09_criterion_1.py` — realistic: iterate over combinations of k vertices,
   verify all pairs adjacent (early exit on first non-edge). Natural without the
   Bron-Kerbosch/bitset insight.
2. Probe `n ∈ [30, 36, 40, 46]`. **Hard clique instances: random graphs at edge probability
   ~0.5 with k just above the true max clique** (forces exhaustive refutation). The
   max-clique size in G(n, 0.5) is ≈ 2·log₂(n) — set k just above that for hard NO instances.
3. Keep the reference tractable (bitset B&B handles n=46 at p=0.5 in seconds-to-minutes
   offline — fine). Statement says `n ≤ 40`; raise to the new max.

## Criterion 2 (P) — two-sided independent set

Answer = `(nA+nB) − maxMatching`. Scale toward bounds: `nA,nB ∈ [1e3 … 1e5]`, `m ≤ 2e5`.
Baseline = brute-force / greedy independent set search → TLE (or wrong answer). Include an
edgeless case (independent set = n) as an edge case.

## Criterion 3 (INFEASIBLE) — pigeonhole (r > n)

Reference is O(1) after reading. Baseline searches subsets → TLEs at large n. Scale n toward
the bound with `r > n` guaranteed. The answer stays the sentinel.

## Procedure

1. `tools/gen_family_09.py` — seeded: `gen_clique(n, p, k, seed, has_clique=None)`,
   `gen_bipartite_is(nA, nB, m, seed)`, `gen_oversize_request(n, m, seed)` (r > n).
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_09_clique_independent_set` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.

Then **stop and wait** for `35_scale_family10_dominating_set.md`.

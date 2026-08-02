# 30 — Scale Family 05: Team & Resource Alignment (3-Dimensional Matching)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_05_three_dim_matching/`.

## Family 05 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | backtracking with pruning over triples | backtracking, weaker/no pruning | **same shape** — hardness from instance structure |
| 2 | P | Hopcroft-Karp, O(E√V) | **naive: Kuhn's augmenting path, O(V·E)** | asymptotic gap ✅ |
| 3 | INFEASIBLE | scan for empty compatibility row, O(E) | naive: attempt full matching search first | asymptotic gap ✅ |

## Criterion 1 (NPC) — instance structure carries it

Like Families 01/02, reference and baseline share shape, so **hardness must come from the
instance**. Hard 3DM instances: near-critical triple density where many partial matchings
look viable but no perfect matching exists. **NO instances force exhaustive search** — hunt
those seeds.

1. `tools/naive_family_05_criterion_1.py` — realistic: pick the lowest uncovered X element,
   try its allowed triples in order, recurse, backtrack. Standard, competent.
2. Probe `k ∈ [14, 16, 18, 20, 22]` with triple count tuned so instances are near-critical
   (roughly `t ≈ 3k` to `5k`; tune empirically). Seeds 1..8.
3. Find where the baseline exceeds `time_limit_s`. Statement says `k ≤ 18` — raise to match
   the new max if needed.

## Criterion 2 (P) — Hopcroft-Karp vs Kuhn

Real gap: Kuhn's is O(V·E), Hopcroft-Karp O(E√V). At k=1000 with dense-ish edges, Kuhn's
can be pushed to TLE. **Tune E upward** (statement allows `e ≤ 1e5`) and use worst-case
structures for Kuhn's (long augmenting chains). If Kuhn's still passes, increase k/e or
report that the gap is too narrow — Kuhn's is often fast in practice, so this arm may need
adversarial structure, not just size.

Scale `k ∈ [200, 500, 1000]`, `e` near its cap. Include a perfect-matching case and a NO case.

## Criterion 3 (INFEASIBLE) — scale toward the bound

Baseline = runs a full matching search before noticing the empty row → TLEs at scale.
Reference scans rows, O(E). Ensure one large case where the partnerless X element has a
**high index**.

## Procedure

1. `tools/gen_family_05.py` — seeded: `gen_3dm(k, t, seed, perfect=None)`,
   `gen_bipartite(k, e, seed, perfect=True)`, `gen_empty_row(k, e, seed, empty_at)`.
2. Write the realistic baselines.
3. **Probe with the baseline**; confirm blow-up (criterion 1) / TLE (criteria 2,3).
4. 5-case ramp straddling the threshold; keep anchors, append.
5. **Generate `.out` with the reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 at `time_limit_s` on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `python -m harness.reference_check dataset/family_05_three_dim_matching` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes,
reference_check clean. **Flag if criterion 2's Kuhn-vs-HK gap proves too narrow.**

Then **stop and wait** for `31_scale_family06_bin_packing.md`.

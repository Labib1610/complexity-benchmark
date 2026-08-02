# 36 — Scale Family 11: Skill Coverage (Set Cover)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_11_set_cover/`.

## Family 11 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | bitmask DP over covered-skill sets, **O(2^u·s)** | **naive: all C(s,k) consultant subsets** | **asymptotic gap ✅** |
| 2 | P | matching → edge cover (König), O(E√V) | naive: exponential cover search | asymptotic gap ✅ |
| 3 | INFEASIBLE | uncovered-skill scan, O(total set size) | naive: searches covers first | asymptotic gap ✅ |

## Criterion 1 (NPC) — bitmask DP vs subset enumeration

Reference is 2^u·s (u = universe size ≤ 20 → 1M·s, tractable). A naive solution enumerating
C(s,k) consultant subsets explodes as `s` grows. **Key insight: keep `u` moderate (the
reference's cost) but push `s` up (the baseline's cost).** That asymmetry is your window.

1. `tools/naive_family_11_criterion_1.py` — realistic: iterate over combinations of k
   consultants, union their skills, check coverage. Natural without bitmask DP.
2. Probe with `u ∈ [18, 20]` fixed and `s ∈ [40, 60, 80, 120]`, `k` near the true minimum
   cover. **NO instances (k one below minimum) force exhaustive search.**
3. Statement says `u ≤ 20, s ≤ 200`. Raise `s` toward 200 if needed; keep `u ≤ 20` so the
   reference's 2^u stays fine.

## Criterion 2 (P) — size-2 sets = edge cover

Per the design note in the original build file, this arm may have been constrained to a
bipartite structure to avoid needing Blossom. **Check `meta.yaml` / `statement.md` for what
was decided and keep it consistent.**

Scale toward bounds: `u ∈ [1e3 … 1e5]`, `s ≤ 2e5`. Baseline = exponential cover search or an
O(V·E) matching → TLE. Include a path-of-skills and a star structure with known minimum covers.

## Criterion 3 (INFEASIBLE) — uncoverable skill

Reference scans, O(total). Baseline searches covers first → TLEs. Scale u, s toward bounds;
one case with the uncoverable skill at a **high id**.

## Procedure

1. `tools/gen_family_11.py` — seeded: `gen_setcover(u, s, k, seed, coverable=None)`,
   `gen_size2_sets(u, s, seed)`, `gen_uncoverable(u, s, seed, skill_at)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up. Remember: hold `u` fixed, grow `s`.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_11_set_cover` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
Note explicitly that criterion 1's window comes from **fixing u while growing s**.

Then **stop and wait** for `37_scale_family12_knapsack.md`.

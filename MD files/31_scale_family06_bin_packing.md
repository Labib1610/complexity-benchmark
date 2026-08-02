# 31 — Scale Family 06: Cargo Loading (Bin Packing)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_06_bin_packing/`.

## Family 06 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | backtracking with symmetry pruning | backtracking, weaker pruning / no symmetry breaking | **same shape** — instance structure + symmetry |
| 2 | P | sum + ceil division, O(n) | naive: simulates packing item-by-item, O(n·k) or worse | asymptotic gap ✅ |
| 3 | INFEASIBLE | scan for oversized item, O(n) | naive: attempts packing first | asymptotic gap ✅ |

## Criterion 1 (NPC) — symmetry is the weapon

Bin packing's hardness for backtracking comes from **symmetry**: identical items and
interchangeable empty bins create astronomically many equivalent branches. A competent
baseline without symmetry breaking explodes; the reference (with "don't open a new empty bin
beyond the first") survives much longer. **That is a real gap even without an asymptotic
difference — exploit it.**

Hard instances: many **identical or near-identical** item weights, capacity such that items
*almost* fit in k bins (e.g. total = k·C exactly, requiring a perfect packing — these are
brutal for naive search). Also weights near C/3 or C/2.

1. `tools/naive_family_06_criterion_1.py` — realistic: try placing each item into every bin
   1..k with the capacity check, recurse. No symmetry breaking (a competent but not expert
   solution). This is genuinely what many models write.
2. Probe `n ∈ [16, 18, 20, 22, 24]` with the "total = k·C, perfect packing required"
   structure and duplicate weights. Seeds 1..8.
3. Statement says `n ≤ 18` — raise to the new max.

## Criterion 2 (P) — fractional, punish the simulator

The answer is `ceil(sum/C)` in O(n). A naive solution that literally simulates filling bins
one unit/item at a time can be made to TLE by pushing `n` to 2e5 and using large weights.
Scale `n ∈ [1e3, 1e4, 5e4, 1e5, 2e5]`. Include an exact-multiple case (tests ceil edge).

## Criterion 3 (INFEASIBLE) — oversized item

Reference scans, O(n). Baseline attempts a packing search first → TLEs. Scale n toward the
bound; ensure one case where the oversized item has a **high index**.

## Procedure

1. `tools/gen_family_06.py` — seeded: `gen_binpack_hard(n, k, C, seed)` (perfect-packing
   structure, duplicate weights), `gen_fractional(n, C, seed)`, `gen_oversized(n, C, seed, at)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with the reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_06_bin_packing` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.
Note in the report that criterion 1's gap comes from **symmetry breaking**, not asymptotics.

Then **stop and wait** for `32_scale_family07_shortest_common_superstring.md`.

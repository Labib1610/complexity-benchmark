# 32 — Scale Family 07: DNA/Log Assembly (Shortest Common Superstring)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_07_shortest_common_superstring/`.

## Family 07 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | bitmask DP over orderings, **O(2^k·k²)** | **naive: try all k! permutations** | **huge asymptotic gap ✅** |
| 2 | P | max suffix-prefix overlap via KMP/Z, O(n) | naive: O(n²) overlap check per position | asymptotic gap ✅ |
| 3 | INFEASIBLE | substring scan, O(k·|F|) | naive: attempts assembly first | asymptotic gap ✅ |

**Criterion 1 has an excellent window** — same shape as Family 03. At k=12: DP = 2¹²·144 ≈
590K (instant); k! = 479M (dead). Expect easy scaling.

## Criterion 1 (NPC) — DP vs permutations

1. `tools/naive_family_07_criterion_1.py` — realistic: recursively try each unused fragment
   next, merging on max overlap, tracking the best (i.e. permutation search with pruning on
   current length). Natural solution without the bitmask-DP insight.
2. Probe `k ∈ [10, 12, 14, 16]`, fragment length ≤ 20. **Hard instances = fragments with many
   partial overlaps** (shared prefixes/suffixes across many fragments), which defeat pruning
   because many orderings look promising. Random strings over a **small alphabet** (e.g.
   {a,b}) maximize spurious overlaps — use that.
3. Statement says `k ≤ 12`; the DP handles k=18 (2¹⁸·324 ≈ 85M — slow but fine offline).
   Raise the bound to the new max.

## Criterion 2 (P) — two strings, punish O(n²)

Reference uses Z/KMP for O(n) overlap. Baseline = the natural O(n²): for each candidate
overlap length, compare character by character. Push string length to 1e5 (statement bound) —
O(n²) = 1e10 → decisive TLE.

Include: strings with a long overlap, no overlap, identical strings, and a **worst case for
naive** (e.g. `aaaa...a` + `aaaa...ab`, which makes naive comparison do maximal work).

## Criterion 3 (INFEASIBLE) — forbidden substring

Reference scans fragments for F, O(k·|F|). Baseline attempts assembly first → TLEs. Scale k
and fragment lengths; ensure one case where the offending fragment is at a **high index**.

## Procedure

1. `tools/gen_family_07.py` — seeded: `gen_scs(k, len, seed, alphabet="ab")`,
   `gen_two_strings(n, seed, overlap=None)`, `gen_forbidden(k, len, seed, F, at)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm factorial blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_07_shortest_common_superstring` → clean.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check.

Then **stop and wait** for `33_scale_family08_vertex_cover.md`.

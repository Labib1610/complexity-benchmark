# Family 05 (3-Dimensional Matching / Crew Assembly) — Rebuild Notes

Rebuilt per the audit's per-family guidance ("preserve the hypergraph schema/output and introduce one
tractable structural promise; use an independent exact oracle") and the V5 reference-timing flag.

## What was wrong (audit findings for family 05)

- **B4** — criterion 1 was 3-dimensional matching (triples), but criterion 2 and criterion 3 had been
  switched to plain **bipartite matching** (worker–task *pairs*, an assignment vector) — a different
  task, schema, and output.
- **V5 / B1 (reference too slow)** — the criterion-1 backtracking reference **TLE'd at the declared
  5 s limit** on the hunted-hard k=22 cases.

## What changed

The family is now unified on the **3-dimensional matching triple schema** (`k t` + `x y z` triples,
output k crews) across all three criteria. The A/B switch is a tractable structural promise.

### Criterion 1 (NPC) — general 3DM
- Kept the specialist-order backtracking reference and its validator (recomputes feasibility by
  backtracking). **Sizes capped at k ≤ 20** so the reference always finishes well under 5 s (was TLE
  at k=22). NO cases sit at small k (sparse instances the search refutes instantly); YES cases at
  k = 10..20 (planted matchings). All solve in < 0.03 s.

### Criterion 2 (P) — functional promise (the one switch)
- Rewritten from bipartite worker–task matching to **3DM on the triple schema** with the promise that
  each specialist is tied to exactly one machine and the machines are all distinct (a bijection
  X→Y). The only freedom is the time slot, so it reduces to a **bipartite matching between
  specialists and slots** (Hopcroft-Karp). Output: k crews (same as criterion 1). ~0.02 s at k=1200.

### Criterion 3 (INFEASIBLE) — triple-schema certificate
- Rewritten from a bipartite "unassignable worker" to the **3DM missing-specialist** certificate:
  some specialist appears in no allowed crew, so no plan exists. Report the smallest such specialist.
  Positions varied (2, high, low, 100, high, 1, 345) so no positional constant passes.

## Correctness testing

The C2 functional-3DM reference was **verified against a brute-force 3DM solver** on 400 random
instances (YES/NO verdict) and its output accepted by the validator. C1's backtracking oracle and
validator are the original (unchanged) logic.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: **C1 0.02 s ≤ 5 s (was TLE 5.01 s)**, C2 0.02 s ≤ 2 s,
  C3 0.01 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Family 05 has a narrow gradeable window (like family 16): a genuinely hard 3DM instance makes the
backtracking oracle TLE, so gradeable cases are ones the oracle solves quickly — the NPC tier here
separates a weak search from the ordered backtracking, not competent-from-competent. Strong hardness
needs a stronger oracle / the sealed P2–P3 evaluation.

## Regeneration

```
python tools/gen_family_05.py --criterion 1 --k <k> --t <t> --seed <s> --perfect <yes|no|>   # general (k<=20)
python tools/gen_family_05.py --criterion 2 --k <k> --seed <s> --kind <yes|no>               # functional 3DM
python tools/gen_family_05.py --criterion 3 --k <k> --seed <s> --at <pos>                     # missing specialist
```

# Family 01 (Graph 3-Colouring / Shift Assignment) — Rebuild Notes

This is the family whose diagnosis started the whole audit: the criterion-1 reference was the **naive
index-order backtracking** that made n=40 look "hard" (it TLE'd at the declared 2 s), while
forward-checking solves the same instance in ~0.01 s. The rebuild fixes exactly that, plus the
lex-min canonicalization.

## What was wrong

- **B2 / V5 (reference too slow — the core bottleneck)** — the criterion-1 reference tried colours
  1,2,3 in vertex order and returned the first (lexicographically smallest) colouring. On the n=40
  cases this **TLE'd at the 2 s limit** (2.004 s), so the answer-key case was ungradeable — and the
  "hardness" was purely an artefact of the weak reference, not the problem.
- **B4 (canonicalization)** — it demanded the lexicographically smallest colouring; the audit flags
  lex-min output contracts.

Criterion 2 (2-colouring, bipartite check) and criterion 3 (odd-cycle / triangle certificate — its
outputs are triangles like `1 2 3`, `998 999 1000`, hardened during the dedup pass) were already
fine and are unchanged.

## What changed

### Criterion 1 (NPC) — 3-colouring
- Reference rewritten to **forward-checking + the most-constrained-vertex (MRV) heuristic**, returning
  **any** proper 3-colouring (or NO). Judge switched to **custom**: any valid colouring is accepted
  (lex-min removed). Statement relaxed accordingly. **All cases now solve in ~0.01 s (was TLE 2 s at
  n=40)** — the same 200x speedup the original diagnosis identified.

## Correctness testing

The C1 validator's 3-colourability check is the same forward-checking solver; the reference passes
its own validator on every case (reference_check). (Correctness of forward-checking 3-colouring is
standard; feasibility is cross-checked by the validator recomputing it.)

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: **C1 0.01 s ≤ 2 s (was TLE 2.004 s)**, C2 0.28 s ≤ 1 s,
  C3 0.17 s ≤ 2 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Forward-checking solves these n≤40 instances trivially — which is the whole point: this tier only
ever separated the *naive index-order* baseline from a competent solver, and now the reference IS the
competent solver. It does not demonstrate hardness against a good colourer (DSATUR / SAT); the audit's
B2 note (calibrate hidden graphs against DSATUR / bitset B&B / SAT) is the P2–P3 research step.

## Regeneration

```
python tools/gen_family_01.py --criterion 1 --n <n> --m <m> --seed <s> [--sat yes|no]  # 3-colouring
python tools/gen_family_01.py --criterion 2 --n <n> --m <m> --seed <s> --sat <yes|no>  # 2-colouring
python tools/gen_family_01.py --criterion 3 --n <n> --m <m> --seed <s> --plant <low|high>  # triangle
```

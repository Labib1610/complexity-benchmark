# Family 02 (Boolean Satisfiability) — Rebuild Notes

Rebuilt per the audit's per-family guidance ("use the same witness rule; mix hidden SAT/UNSAT
generators") and the V5 reference-timing flag.

## What was wrong

- **B4 (canonicalization)** — criterion 1 (3-SAT) demanded the **lexicographically smallest**
  satisfying assignment while criterion 2 (2-SAT) accepted **any** — the exact inconsistency the
  audit called out ("SAT A requires the lexicographically smallest assignment, while SAT B accepts
  any").
- **V5 / B1 (reference too slow)** — the criterion-1 DPLL re-scanned **every clause each propagation
  round** and searched for the lex-min assignment; on the n=90 threshold cases it **TLE'd at the 2 s
  limit** (2.004 s).

Criterion 2 (2-SAT via SCC) and criterion 3 (2-SAT contradiction certificate) were already fine and
are unchanged.

## What changed

### Criterion 1 (NPC) — 3-SAT
- Statement relaxed to **any satisfying assignment** (lex-min removed), matching criterion 2 — fixes
  the B4 canonicalization inconsistency. Judge switched to **custom** (the validator checks the
  assignment satisfies every clause; for UNSAT it recomputes satisfiability).
- Reference rewritten from the clause-rescanning lex-min DPLL to an **efficient any-assignment DPLL**
  with **variable-indexed unit propagation** (BCP touches only clauses containing a newly-assigned
  variable). **n=90 UNSAT now solves in 0.74 s (was TLE 2.004 s)**; all cases well under 2 s.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: **C1 0.74 s ≤ 2 s (was TLE 2.004 s)**, C2 0.58 s ≤ 1 s,
  C3 0.58 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

3-SAT at the m/n ≈ 4.26 phase transition is genuinely hard, but a gradeable case must be solvable by
the reference within the limit, so n is capped at 90 (efficient DPLL < 1 s there). The tier separates
naive backtracking (no propagation) from DPLL-with-BCP; it does not prove hardness against a modern
CDCL solver — the audit's "calibrate against modern SAT solvers" is the P2–P3 step.

## Regeneration

```
python tools/gen_family_02.py --criterion 1 --n <n> --seed <s> --ratio 4.26          # 3-SAT (threshold)
python tools/gen_family_02.py --criterion 2 --n <n> --m <m> --seed <s> --sat <yes|no> # 2-SAT
python tools/gen_family_02.py --criterion 3 --n <n> --m <m> --seed <s> --contra <low|high>  # contradiction
```

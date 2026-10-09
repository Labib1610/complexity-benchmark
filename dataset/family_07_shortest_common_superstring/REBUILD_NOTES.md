# Family 07 (Shortest Common Superstring) — Rebuild Notes

Rebuilt following the family_04/15 template. An optimization/string family, so it fixes a **B4**
schema+canonicalization mismatch and adds a **B7** objective, per the audit's guidance to "keep k in
all schemas" and "score feasible superstrings by length."

## What was wrong (audit findings for family 07)

- **B4** — criterion 1 (k fragments) had a `k` header while criterion 2 (two fragments) used a bare
  two-line schema (no header). Both also demanded the **lexicographically smallest** shortest
  superstring — a canonicalization burden the audit flags (like SAT's lex-min-vs-any inconsistency).
- **B7 / gate 3** — no `objective.py`, so the time-budget study could not score superstring quality.

Criterion 3 was already an instance-specific certificate (smallest fragment index containing the
forbidden string F), so it was never gameable (G7 passed for it).

## What changed

The family is unified on **shortest common superstring**: output *any* string of minimum length that
contains every fragment. One schema (`k` header + k fragments), one output contract across criteria 1
and 2. The A/B switch is the fragment count.

### Criterion 1 (NPC) — k ≥ 3 fragments
- Reference rewritten as a **length-only Held-Karp** over suffix-prefix overlaps + order
  reconstruction (was: a Held-Karp that stored the full string in every DP cell, ~335 MB at k=16;
  the length-DP is ~8 MB, so k=16 fits comfortably — 0.61 s). Judge switched to **custom**: any
  shortest superstring is accepted (the lex-min requirement is removed). k ≤ 16.

### Criterion 2 (P) — k = 2 fragments (the one switch)
- Unified `k`-header schema. Reference is the O(n) overlap merge (prefix-function). Judge custom;
  any shortest accepted. ~0.20 s at n = 500000.

### Criterion 3 (INFEASIBLE) — unchanged task, hardened tests
- Still the forbidden-pattern certificate (smallest fragment index containing F). Regenerated with
  the F-containing fragment at **varied** positions (2, high, low, 500, high, 1, 12345) so no
  positional constant can pass.

## B7 approximation scoring (gate 3)

Added `objective.py` (C1 and C2, `MINIMIZE = True`): `value()` returns the output length if it is a
valid superstring of every fragment, else 0. Verified through the real `studies/time_budget/scoring.py`:
optimal → ratio 1.0; a plain concatenation (length 112 vs optimal 86) → ratio 0.77.

## Correctness testing

- The C1 validator's Held-Karp min-length was **verified against a brute-force permutation SCS** on
  200 instances; the rewritten C1 reference and the C2 reference both pass their validators on 200
  instances each, and the C2 length matches the brute-force minimum.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.61 s ≤ 5 s (k=16), C2 0.20 s ≤ 1 s, C3 0.03 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Same gradeable-NPC ceiling: the Held-Karp reference is O(2^k), so k ≤ 16. The tier separates a
permutation search (defeated by spurious overlaps over a small alphabet) from the bitmask DP; it does
not prove hardness against a competent solver. True SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_07.py --criterion 1 --k <k> --len <L> --seed <s> --alphabet ab   # k>=3
python tools/gen_family_07.py --criterion 2 --n <n> --seed <s> --mode <worst|long|none|identical>  # k=2
python tools/gen_family_07.py --criterion 3 --k <k> --len <L> --F <F> --at <pos> --seed <s>   # forbidden
```

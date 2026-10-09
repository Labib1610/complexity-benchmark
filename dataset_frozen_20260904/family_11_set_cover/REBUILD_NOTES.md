# Family 11 (Set Cover / Consultant Hiring) — Rebuild Notes

Rebuilt following the family_04/08/09/10 template. Its polynomial arm is minimum **edge cover**
(set cover restricted to 2-element sets), matching-based like the rest of the graph cluster.

## What was wrong (audit findings for family 11)

- **B4** — criterion 1 was general set-cover **decision + witness** (`u s k`), while criterion 2 was
  minimum-edge-cover **SIZE** on a two-side (`uA uB s`) schema with integer-only output — a different
  task, output, and schema.
- **B6** — criterion inputs were byte-identical to family 08 (resolved earlier in the dedup pass by
  reseeding family 11's colliding P-tier cases).

Criterion 3 was already an instance-specific certificate (report the smallest skill no consultant
brings — an uncoverable element), so it was never gameable (G7 passed for it).

## What changed

The family is now unified on **set cover: decide whether k hires cover every skill, and report
them** — one schema (`u s k` + sets), one output (`YES` + consultant indices / `NO`) across criteria
1 and 2. The A/B switch is exactly the set size.

### Criterion 1 (NPC) — arbitrary-size sets
- Kept the 2^u bitmask-DP decision + witness reference. u ≤ 20.

### Criterion 2 (P) — 2-element sets = edge cover (the one switch)
- Rewritten from min-edge-cover SIZE (`uA uB s` schema) to the **same set-cover decision + witness**
  on the unified `u s k` schema, restricted to 2-element sets. Reference: treat each 2-skill set as
  an edge, 2-colour to recover the two skill kinds, Hopcroft-Karp matching, **Gallai** minimum edge
  cover `= u − matching`, build the witness (matching edges + one incident set per still-uncovered
  skill), decide `size ≤ k`. **~1.1 s at u = 100000** vs the 2 s limit (gate 12).

### Criterion 3 (INFEASIBLE) — unchanged
- Already a certificate (smallest skill brought by no consultant). Non-gameable; left as is.

## Correctness testing

The C2 edge-cover reference (matching + Gallai witness) was **verified against a brute-force minimum
set cover** on 400 random instances, across all k values — checking YES witnesses (a valid cover of
size ≤ k) and NO decisions. All passed.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.04 s ≤ 5 s, C2 1.1 s ≤ 2 s, C3 0.04 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Same gradeable-NPC ceiling: the bitmask-DP C1 reference (u ≤ 20) is fast. The tier separates a
C(s,k) subset baseline from the DP; it does not prove hardness against a competent solver. True
SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_11.py --criterion 1 --u <u> --s <s> --k <k> --seed <sd> --coverable <yes|no>  # arbitrary sets
python tools/gen_family_11.py --criterion 2 --u <u> --seed <sd> --kind <yes|no>                        # 2-element sets
python tools/gen_family_11.py --criterion 3 --u <u> --s <s> --seed <sd> --at high                      # certificate
```

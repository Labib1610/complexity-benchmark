# Family 13 (Partition / Balanced Machines) — Rebuild Notes

Rebuilt following the **family_04 template** (`dataset/family_04_subset_sum/REBUILD_NOTES.md`).
Partition is subset sum with target = total/2, so C1/C2 mirror family 04; C3 gains an extra
certificate mechanism (a dominant element).

## What was wrong (audit findings for family 13)

- **B2/B3** — C1/C2 hard-NO instances were "all-even durations, total ≡ 2 (mod 4)" → a **parity/gcd
  shortcut** (divide out gcd = 2, get an odd total, answer NO instantly). Straw baseline.
- **gate 12** — the C2 (P-tier) reference was a boolean-**list** DP taking ~2.1 s at n = 2000, i.e.
  it **missed the 2 s limit** (audit V5 flagged partition B).
- **B5** — C3 made every instance infeasible via an **odd total** and required a constant `NO`; a
  one-line `print("NO")` passed every test.
- **B6** — several inputs duplicated inputs elsewhere.

## What changed

### Criterion 1 (NPC) — Balanced Machines
- Hard-NO now **genuine**: random **coprime** durations, **even** total (so the odd-total refutation
  cannot be used), no single element > half, no subset summing to total/2 (MITM-verified).
  Constructible only for n ≤ ~32; the top of the ramp uses **hard-YES** planted balanced splits that
  a naive O(2ⁿ) search TLEs finding while MITM solves instantly.
- **Ceiling n = 38** (MITM reference ≈ 148 MB; ≈ 296 MB at n = 40, over the 256 MB limit).

### Criterion 2 (P) — same task, small values
- Reference rewritten as an efficient **bitset DP** (`dp |= dp << c`) — **~0.03 s at n = 2000** vs the
  2 s limit, a comfortable margin (gate 12 fixed).
- NO instances now **genuine** (coprime, even total, DP-verified); genuine small-value NO exists only
  at small n, so NO cases sit at n ≤ 12 and large n (to 2000) demonstrates the polynomial DP via YES.

### Criterion 3 (INFEASIBLE) — infeasibility-CERTIFICATE task (B5)
- Every instance is infeasible for a **machine-checkable reason** from **three mechanisms**:
  - `ODD` — the total is odd;
  - `MAX` — one task exceeds half the total (2·max > total);
  - `MOD d` — an even d ≥ 2 divides every duration but not half the total.
- Output is the **certificate**, checked by `validator.py`. **A constant program fails** — verified:
  constant `NO`, `ODD`, and `MAX` all score WRONG_ANSWER; only a correct per-instance certificate
  passes. `complexity_switch`: input schema unchanged; output contract becomes diagnosis.

## Verification

- `reference_check` passes all 3 criteria.
- Every reference solves **within the declared model limit**: C1 0.21 s ≤ 5 s, C2 0.03 s ≤ 2 s,
  C3 0.02 s ≤ 2 s.
- Constant / single-mechanism programs all fail C3; the old `NO` baseline now scores WRONG_ANSWER.
- `release_check`: family 13 is clean on G7 and G9 (global counts dropped 5→4 gameable arms,
  22→21 duplicate groups).

## Honest limitation (same as family 04)

The gradeable-NPC ceiling applies: a case must be solvable by the reference, so it can never be hard
for an equally competent solver. A model writing meet-in-the-middle solves every C1 case in < 0.5 s.
This tier separates naive O(2ⁿ) search from MITM; it does not prove hardness against a competent
exact solver. True SOTA-resistance needs the sealed hidden-generator evaluation of phases P2–P3.

## Regeneration

```
python tools/gen_family_13.py --criterion 1 --n <n> --seed <s> --kind <yes|no|rand>
python tools/gen_family_13.py --criterion 2 --n <n> --seed <s> --kind <yes|no>
python tools/gen_family_13.py --criterion 3 --n <n> --seed <s> --kind <odd|mod|max>
```

# Family 03 (Hamiltonian Path / Delivery Routing) — Rebuild Notes

Rebuilt per the audit's per-family guidance ("accept any valid path; add hard YES cases; scale past
the bitmask-DP deadline") and the general B4 canonicalization rule.

## What was wrong (audit findings for family 03)

- **B4 (canonicalization)** — criterion 1 demanded the **lexicographically smallest** route while
  criterion 2 accepted any — an inconsistent output contract across the pair.
- **V5 / B1 (reference too slow)** — the criterion-1 reference **TLE'd at the declared 5 s limit**
  (n = 20, bytearray DP, ~5.01 s), so the "answer key" case was not solvable within the model
  deadline by anyone.
- **family.yaml** had a `<FILL: ...>` placeholder for `base_problem`.

Criterion 3 was already an instance-specific certificate (smallest isolated location; the generator
even supports a second isolated vertex so a non-smallest answer is wrong), and its outputs already
vary across cases (1, 4, 1, 1000, 1, 50000, 7). Left as is.

## What changed

The pair is unified on **Hamiltonian path: output ANY valid route** (the lex-smallest requirement is
removed). The A/B switch is the road network: criterion 1 is a general two-way network (NPC),
criterion 2 is a one-way acyclic hierarchy (a DAG, P — the route is the unique topological order).

### Criterion 1 (NPC)
- **Reference rewritten** from a `bytearray` DP (O(2ⁿ·n²), TLE at n=20) to a **bitset DP**
  (`dp[mask]` = bitmask of possible path ends) with backward reconstruction of any one path. Judge
  switched to **custom**: any valid route is accepted. Tests **capped at n ≤ 18** so the reference
  finishes comfortably under 5 s (measured: n=17 → 1.3 s, n=18 → 0.65 s; n=20 would be ~8.6 s). The
  statement bound n ≤ 20 is kept as the truthful problem class.

### Criterion 2 (P)
- Kept the DAG reference (unique topological order + consecutive-edge check). Judge switched to
  **custom** accepting any valid route (the DAG route is unique anyway). ~0.34 s at n = 200000.

### Criterion 3 (INFEASIBLE) — unchanged
- Isolated-location certificate; already instance-specific and position-varied.

## Correctness testing

The C1 validator's Hamiltonian-path feasibility DP was **verified against a brute-force permutation
search** on 600 random graphs. Both references pass their custom validators (reference_check).

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: **C1 1.33 s ≤ 5 s (was TLE 5.01 s)**, C2 0.34 s ≤ 1 s,
  C3 0.11 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Gradeable-NPC ceiling: the bitmask DP is O(2ⁿ), so gradeable cases cap at n ≤ 18. The tier separates
naive DFS backtracking from the bitmask DP; it does not prove hardness against a competent solver.
True SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_03.py --criterion 1 --n <n> --m <m> --seed <s> --path <yes|no>   # general (n<=18)
python tools/gen_family_03.py --criterion 2 --n <n> --seed <s> --unique <yes|no>          # DAG
python tools/gen_family_03.py --criterion 3 --n <n> --m <m> --seed <s> --iso <pos>        # isolated
```

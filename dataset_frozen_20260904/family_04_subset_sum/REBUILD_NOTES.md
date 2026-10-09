# Family 04 (Subset Sum / Budget Selection) — Rebuild Notes

This family is the **template** for the P1–P3 dataset rebuild the audit
(`MD files/COMPLEXITY_BENCHMARK_AUDIT.md`) requires. It shows, on one family, how the audit's
research-level blockers (B2, B3, B4, B5, B6) are addressed concretely and verifiably. The same
pattern is to be applied to families 01–03 and 05–16.

## What was wrong (audit findings for family 04)

- **B2/B3** — Criterion 1's hard-NO instances used *all-even values + an odd target*. That is a
  **parity-trivial** NO: a solver that checks the gcd answers NO instantly with no search, so the
  tier was calibrated against a straw baseline, not a competent one.
- **B5** — Criterion 3 made every instance infeasible via a *negative target* and required a
  constant `NO`. A one-line `print("NO")` passed every test (verified: it did).
- **B6** — Several inputs were byte-identical to inputs in other criteria/families.

## What changed

### Criterion 1 (NPC) — Exact Budget Selection
- Hard-NO instances are now **genuine**: random **coprime** values (gcd = 1, so no modular/parity
  shortcut) with the target **verified infeasible by meet-in-the-middle**. Constructible only for
  n ≤ ~32 (above that, random subset sums densely cover the range, so a true NO cannot be sampled).
- The top of the ramp uses **hard-YES** instances — a single deep large-value witness that a naive
  O(2ⁿ) search TLEs finding while the MITM reference locates instantly (non-gameable even by a
  "search-then-fallback-to-NO" heuristic).
- **Honest ceiling:** the MITM reference materialises 2^(n/2) entries per half; under the 256 MB
  limit it validates through **n = 38** (0.28 s) but **exceeds 256 MB at n = 40**. Ramp tops at 38.
- Same I/O schema as B (audit B4: the A/B pair already shared schema; preserved).

### Criterion 2 (P) — same task, small values
- NO instances are now **genuine** (coprime small values, DP-verified unreachable). Genuine
  small-value NO exists only at small n, so NO cases sit at n ≤ 12; large n (to 1000) shows the
  O(n·T) DP staying polynomial via YES cases. Reference DP runs ~0.02 s at n = 1000 vs the 2 s
  limit — a **>90× margin** (acceptance gate 12).

### Criterion 3 (INFEASIBLE) — redesigned as an infeasibility-CERTIFICATE task (B5)
- Every instance is infeasible for a **machine-checkable reason**, drawn from **two mechanisms**:
  - `SUM` — the target exceeds the total of all costs;
  - `MOD d` — an integer d ≥ 2 divides every cost but not the target.
- The required output is the **certificate**, not `NO`. `validator.py` checks it against the input.
- **A constant program can no longer pass** — verified: constant `NO`, constant `SUM`, and constant
  `MOD 2` all score WRONG_ANSWER; only a correct per-instance certificate passes.
- The `complexity_switch` (audit B4) for this arm: input schema unchanged; the output contract
  becomes *diagnosis* (certify impossibility) instead of *decide + witness*.

## Baseline matrix (audit B2 closure evidence)

Measured on the target machine (Python 3.12), per-case reference vs. the realistic naive baseline
(`tools/naive_family_04_criterion_1.py`, recursive include/exclude O(2ⁿ) with sum-pruning):

| Criterion | size | kind | reference | ref memory | naive O(2ⁿ) |
|---|---|---|---|---|---|
| 1 NPC | 26 | NO  | 0.016 s | < 256 MB | TLE (>4 s) |
| 1 NPC | 32 | NO  | 0.038 s | < 256 MB | TLE (>4 s) |
| 1 NPC | 36 | YES | 0.143 s | < 256 MB | TLE (>4 s) |
| 1 NPC | 38 | YES | 0.275 s | < 256 MB | TLE (>4 s) |
| 1 NPC | 40 | YES | 0.444 s | **> 256 MB** | TLE — *excluded (OOM)* |
| 2 P   | 1000 | YES | ~0.02 s | < 256 MB | (DP; search TLEs from n~25) |

Pseudo-polynomial DP over sums is also blocked for criterion 1 by large targets (T up to ~4·10¹⁰
needs a ~20 GB array → TLE/OOM).

## Honest limitation (must be reported)

This is the inherent **gradeable-NPC ceiling** the audit describes: a case must be solvable by the
reference to have an answer key, so it can **never** be hard for an equally competent solver. A model
that writes meet-in-the-middle solves every criterion-1 case here in < 0.5 s. This tier separates
**naive O(2ⁿ) search (and pseudo-poly DP) from MITM** — it does **not** demonstrate hardness against
a competent exact solver, and must not be reported as such. Genuine SOTA-resistance requires the
sealed, hidden-generator, multi-baseline evaluation of audit phases P2–P3.

## Regeneration

```
python tools/gen_family_04.py --criterion 1 --n <n> --seed <s> --kind <yes|no|rand>
python tools/gen_family_04.py --criterion 2 --n <n> --seed <s> --kind <yes|no>
python tools/gen_family_04.py --criterion 3 --n <n> --seed <s> --kind <sum|mod>
```

All references reproduce their `.out` under `harness.reference_check`, and every reference solves
within the declared model limit (C1 0.20 s ≤ 5 s, C2/C3 ≤ 0.02 s ≤ 2 s).

# 11 — Fill Family 04: Budget Selection (Subset Sum)

> Follow `08_START_family_filling.md`. Target: `dataset/family_04_subset_sum/`.

## Domain framing

Choose a subset of purchasable items so their total cost hits an exact target budget. Same framing across all three; only the number ranges and the target change the regime.

## Criterion 1 — NP-complete (Subset Sum, large values)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given `n` item costs and a target `T`, decide whether some subset sums to exactly `T`; output the chosen item indices or `NO`.
- **Input:** `n` then `n` costs then `T`. `1 ≤ n ≤ 40`, costs up to `1e9`, `T` up to `4e10`. Large values make pseudo-polynomial DP infeasible (exponential in bit-length); meet-in-the-middle (2^(n/2)) is the intended route.
- **Output:** `YES` + chosen indices (lexicographically smallest index set: prefer the subset that is smallest when its sorted index list is compared), else `NO`. (To keep tie-break tractable you MAY instead require "any valid subset" with `judge: custom` + validator summing the chosen costs. Pick one; keep consistent.)
- **Reference:** meet-in-the-middle. Deterministic.

## Criterion 2 — P (poly-bounded values)

- **Class:** P. **Letter:** B.
- **Problem:** identical task, but costs and target are **small** (`cost ≤ 100`, `T ≤ 500`, `n ≤ 1000`), making the DP table polynomial in input size.
- **Input:** `n`, `n` costs, `T` with the small bounds above.
- **Output:** `YES` + lexicographically smallest subset (or `judge: custom` "any valid subset"), else `NO`. Choose same convention as C1.
- **Reference:** classic boolean DP over reachable sums with predecessor tracking for reconstruction. O(n·T). Do NOT mention "pseudo-polynomial" or "polynomially bounded" in the statement — just give small bounds.

## Criterion 3 — Infeasible (negative target)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** all item costs are **positive integers**, but the target is **negative**. No subset (including empty, which sums to 0) can reach a negative total. The task is to recognize and report impossibility.
- **Input:** `n`, `n` positive costs, a negative `T`.
- **Output:** a single line `NO`. (Crisp sentinel — a model returning any subset is WRONG_ANSWER.)
- **Judge:** `exact`.
- **Reference:** if `T < 0` (and all costs positive), print `NO`. (Keep it honest: the reference reads input and prints `NO`.)

## Test cases

- C1: a reachable target (`YES`), an unreachable one (`NO`), n=1.
- C2: small reachable and unreachable cases, the empty-subset target T=0 (`YES`, empty set).
- C3: two instances with negative targets (both `NO`).

Generate `.out` from references, run `reference_check`, fix flags, report, wait for `12`.

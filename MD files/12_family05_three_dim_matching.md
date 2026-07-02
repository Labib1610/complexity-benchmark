# 12 — Fill Family 05: Team & Resource Alignment (3-Dimensional Matching)

> Follow `08_START_family_filling.md`. Target: `dataset/family_05_three_dim_matching/`.

## Domain framing

Form complete operating teams by pairing/tripling people and resources so each entity is used exactly once. NPC variant needs three simultaneous roles; P variant needs only two.

## Criterion 1 — NP-complete (3-Dimensional Matching)

- **Class:** NPC. **Letter:** A.
- **Problem:** Three disjoint sets X, Y, Z each of size `k`. A list of allowed triples `(x,y,z)`. Decide whether `k` triples can be chosen so every element of X, Y, Z is covered exactly once; output the chosen triples or `NO`.
- **Input:** `k t` (set size, number of allowed triples); then `t` lines `x y z` (1-indexed within each set). `1 ≤ k ≤ 18`.
- **Output:** `YES` + `k` chosen triples (sorted, lexicographically smallest selection), else `NO`. If lexicographic selection is heavy, use `judge: custom` "any perfect 3D matching" with a validator checking exact cover. Pick one; keep consistent.
- **Reference:** backtracking with pruning (assign the lowest uncovered X element, try its allowed triples in order). Deterministic.

## Criterion 2 — P (bipartite 2-dimensional matching)

- **Class:** P. **Letter:** B.
- **Problem:** Only **two** sets X and Y of size `k`, allowed pairs `(x,y)`. Decide whether a perfect matching exists; output it or `NO`.
- **Input:** `k e` then `e` lines `x y`. `1 ≤ k ≤ 1000`, `e ≤ 1e5`.
- **Output:** `YES` + for each x its matched y (the matching that is lexicographically smallest by x's partner), else `NO`. Output can be made unique via a deterministic augmenting order; or `judge: custom` "any perfect matching". Choose one.
- **Reference:** Hopcroft–Karp or Kuhn's augmenting-path matching. O(E√V) or O(VE). Never say "bipartite matching" in the statement; describe two groups and allowed pairings.

## Criterion 3 — Infeasible (empty compatibility row, Hall violation)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** two sets X, Y of size `k`, but **some element of X has no allowed partner at all**. A perfect matching cannot exist (Hall's condition violated for that singleton). Certify by naming the unmatchable element.
- **Input:** `k e` then `e` allowed pairs; guaranteed at least one X element with zero allowed partners.
- **Output:** the smallest index in X that has no allowed partner.
- **Judge:** `exact` (optionally `validator.py` confirming that X element indeed appears in no pair).
- **Reference:** read pairs, mark which X elements have any partner, print smallest with none.

## Test cases

- C1: a 3D instance with a perfect matching, one without (`NO`), k=1.
- C2: a 2-set instance with a perfect matching, one without (`NO`).
- C3: two instances each with a known partnerless X element.

Generate `.out`, run `reference_check`, fix, report, wait for `13`.

# 16 — Fill Family 09: Social Network Analysis (Clique / Independent Set)

> Follow `08_START_family_filling.md`. Target: `dataset/family_09_clique_independent_set/`.

## Domain framing

Find a group of users who are all mutually connected (a clique) or all mutually unconnected (an independent set). NPC: clique of size k in a general network. P: maximum independent set when the network is two-sided. Infeasible: requesting a group larger than the user count.

## Criterion 1 — NP-complete (Clique of size k)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given a graph and `k`, decide whether `k` mutually-adjacent vertices exist; output one such clique or `NO`.
- **Input:** `n m k` then `m` edges. `1 ≤ n ≤ 40` (use bitset adjacency + branch-and-bound; keeps it feasible for moderate n).
- **Output:** `YES` + the clique vertices (lexicographically smallest size-k clique), else `NO`. If heavy, `judge: custom` "any size-k clique". Pick one.
- **Reference:** Bron–Kerbosch with pivoting, or bitset branch-and-bound, searching for the lexicographically smallest clique of size k. Deterministic.

## Criterion 2 — P (max independent set on a two-sided network)

- **Class:** P. **Letter:** B.
- **Problem:** the network is two-sided (every connection joins side A to side B). Find the **size** of the largest independent set.
- **Theorem:** in a bipartite graph, max independent set = n − max matching (König).
- **Input:** `nA nB m` then `m` edges. `sizes ≤ 1e5`, `m ≤ 2e5`.
- **Output:** the maximum independent-set size = `(nA+nB) − maxMatching`. Unique → `exact`.
- **Reference:** Hopcroft–Karp matching; output `n − matching`. No "König"/"bipartite" labels in statement.

## Criterion 3 — Infeasible (size exceeds universe, pigeonhole)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** the network has `n` users, but the request asks for a group of size `r > n`. No subset of an `n`-element set has more than `n` members — impossible regardless of structure. Report impossibility.
- **Input:** `n m r` then `m` edges, with `r > n` guaranteed.
- **Output:** a single line `NO` (or `IMPOSSIBLE`; pick one sentinel and state it). `judge: exact`.
- **Reference:** if `r > n` print the sentinel.

## Test cases

- C1: a graph with a k-clique (`YES`), one without (`NO`), k=1.
- C2: small two-sided graphs with known independent-set sizes, an edgeless graph (independent set = n).
- C3: two instances with r > n.

Generate `.out`, run `reference_check`, fix, report, wait for `17`.

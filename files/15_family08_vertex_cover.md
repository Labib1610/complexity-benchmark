# 15 — Fill Family 08: Security Guard Placement (Vertex Cover)

> Follow `08_START_family_filling.md`. Target: `dataset/family_08_vertex_cover/`.

## Domain framing

Place guards on junctions so every corridor (edge) is watched by a guard at one of its two ends. NPC: general layout, budget k. P: layout splits into two sides (bipartite). Infeasible: too many disjoint corridors for the budget.

## Criterion 1 — NP-complete (Vertex Cover decision)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given a graph and integer `k`, decide whether `k` vertices can cover all edges; output such a set or `NO`.
- **Input:** `n m k` then `m` edges. `1 ≤ n ≤ 40`, but keep `k` small (≤ 18) so branching `O(2^k · m)` works (branch on an uncovered edge: include u or v).
- **Output:** `YES` + the cover (lexicographically smallest vertex set of size ≤ k), else `NO`. If lexicographic-smallest is heavy, `judge: custom` "any cover of size ≤ k". Pick one.
- **Reference:** bounded-search-tree branching on edges. Deterministic.

## Criterion 2 — P (bipartite vertex cover via König)

- **Class:** P. **Letter:** B.
- **Problem:** the junctions split into two groups and every corridor connects one group to the other (describe operationally: "each junction is colored A or B and every corridor joins an A to a B"). Find the **minimum** number of guards covering all corridors.
- **Theorem:** by König's theorem, min vertex cover = max matching in a bipartite graph.
- **Input:** `nA nB m` then `m` edges (a-side, b-side). `sizes ≤ 1e5`, `m ≤ 2e5`.
- **Output:** the minimum number of guards (= maximum matching size). Unique number → `exact`. (Optionally also output the actual cover via König's construction; if so, pin lexicographic order or use custom.)
- **Reference:** Hopcroft–Karp maximum matching; output its size. Don't write "König" or "bipartite" as labels in the statement.

## Criterion 3 — Infeasible (matching lower bound exceeds budget)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** general graph with `k` guards, but the layout contains **`k+1` or more pairwise vertex-disjoint corridors** (a matching larger than `k`). Each disjoint corridor needs its own guard, so `k` guards cannot cover all — impossible. Certify by outputting `k+1` disjoint corridors (a matching of size k+1).
- **Input:** `n m k` then `m` edges; guaranteed a matching of size ≥ k+1 exists.
- **Output:** `k+1` lines, each a disjoint edge `u v` (output a greedily-found matching of size k+1; define ordering, e.g. edges in input order, vertices not reused).
- **Judge:** `custom` — `validator.py` checks the printed edges are all real edges, pairwise vertex-disjoint, and number exactly k+1.
- **Reference:** greedy matching collecting edges whose endpoints are unused until k+1 collected.

## Test cases

- C1: a coverable graph (`YES`), an uncoverable-within-k graph (`NO`), a single edge.
- C2: small two-sided graphs with known min cover sizes (triangle-free), including a perfect matching case.
- C3: two graphs each with a known large disjoint-corridor set.

Generate `.out`, run `reference_check`, fix, report, wait for `16`.

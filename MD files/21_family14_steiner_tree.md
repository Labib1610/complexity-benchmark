# 21 — Fill Family 14: Network Extension (Steiner Tree)

> Follow `08_START_family_filling.md`. Target: `dataset/family_14_steiner_tree/`.

## Domain framing

Connect a set of required sites with cabling at minimum total cost; optional junction nodes may be used as relays. NPC: choose which optional relays to include. P: every node is required (becomes a minimum spanning tree). Infeasible: a required site with no cabling options (isolated).

## Criterion 1 — NP-complete (Steiner Tree in graphs)

- **Class:** NPC. **Letter:** A.
- **Problem:** Weighted graph; a subset of nodes are **required (terminals)**, the rest optional. Find the minimum-cost connected subgraph linking all terminals (may use optional nodes). Output the minimum cost.
- **Input:** `n m t` (nodes, edges, number of terminals); then `t` terminal ids; then `m` lines `u v w`. Keep `t ≤ 10` (Dreyfus–Wagner / Erickson DP over terminal subsets, O(3^t · n + 2^t · n^2)). `n ≤ 100`.
- **Output:** the minimum total cabling cost (a number). Unique → `exact`. (Outputting the actual edge set would need a tie-break; keep output = cost for cleanliness.)
- **Reference:** Dreyfus–Wagner DP (or bitmask-over-terminals + Dijkstra relaxation). Deterministic.

## Criterion 2 — P (all nodes required → MST)

- **Class:** P. **Letter:** B.
- **Problem:** **every** node is required (no optional relays). The minimum connected subgraph linking all nodes is a minimum spanning tree. Output its total cost.
- **Input:** `n m` then `m` lines `u v w`; graph guaranteed connected. `n ≤ 2e5`, `m ≤ 2e5`.
- **Output:** the MST total cost. Unique → `exact`.
- **Reference:** Kruskal (union-find) or Prim. O(m log m). Never say "Steiner" or "spanning tree" as a difficulty label — just "connect all sites at minimum total cost".

## Criterion 3 — Infeasible (isolated required site)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** a required site has **no incident cabling option** (degree 0) while other sites exist. It cannot be connected to anything — impossible. Report it.
- **Input:** `n m t`, `t` terminals, `m` edges; guaranteed some terminal has degree 0 (and n ≥ 2).
- **Output:** the smallest id among required sites that have no incident edge.
- **Judge:** `exact` (optionally validator confirming degree 0 and that it is a terminal).
- **Reference:** compute degrees, print smallest terminal with degree 0.

## Test cases

- C1: a graph where an optional relay lowers cost (known optimum), a graph with no useful relay, t=1 (cost 0).
- C2: small connected graphs with known MST costs (a triangle, a path), including equal-weight edges.
- C3: two instances with an isolated required site.

Generate `.out`, run `reference_check`, fix, report, wait for `22`.

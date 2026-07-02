# 17 — Fill Family 10: Sensor Placement (Dominating Set)

> Follow `08_START_family_filling.md`. Target: `dataset/family_10_dominating_set/`.

## Domain framing

Place sensors at nodes so every node is either a sensor or adjacent to one. NPC: general network with budget k. P: the network is a tree (each node has exactly one parent, no cycles). Infeasible: an isolated node with zero budget.

## Criterion 1 — NP-complete (Dominating Set decision)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given a graph and `k`, decide whether `k` nodes can be chosen so every node is chosen or adjacent to a chosen one; output the set or `NO`.
- **Input:** `n m k` then `m` edges. `1 ≤ n ≤ 30` (subset search with pruning, or DP over a small structure).
- **Output:** `YES` + the dominating set (lexicographically smallest of size ≤ k), else `NO`. If heavy, `judge: custom` "any dominating set of size ≤ k". Pick one.
- **Reference:** branch-and-bound / greedy-guided exhaustive search for the smallest valid set. Deterministic.

## Criterion 2 — P (minimum dominating set on a tree)

- **Class:** P. **Letter:** B.
- **Problem:** the network is a **tree**: node 1 is the root and every other node lists exactly one parent; there are no cycles (describe operationally, never say "tree"). Find the **minimum** number of sensors dominating all nodes.
- **Input:** `n` then `n−1` lines `child parent` (or a parent array). `1 ≤ n ≤ 2e5`.
- **Output:** the minimum number of sensors. Unique → `exact`.
- **Reference:** classic leaf-to-root tree DP with three states per node (has sensor / dominated-without-own-sensor / not-yet-dominated). O(n). Use iterative post-order to avoid recursion limits at n=2e5.

## Criterion 3 — Infeasible (isolated node, zero budget)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** budget `k = 0`, and the network contains an **isolated node** (degree 0). With no sensors placeable, that node can never be dominated — impossible. Report it.
- **Input:** `n m k` (k=0) then `m` edges; guaranteed an isolated node.
- **Output:** the smallest index of an isolated node.
- **Judge:** `exact` (optionally validator confirming degree 0).
- **Reference:** print smallest degree-0 vertex.

## Test cases

- C1: a dominatable-within-k graph (`YES`), one not (`NO`), n=1.
- C2: small trees with known minimum dominating-set sizes (a path, a star, a balanced binary tree).
- C3: two instances with k=0 and an isolated node.

Generate `.out`, run `reference_check`, fix, report, wait for `18`.

# 10 — Fill Family 03: Delivery Routing (Hamiltonian Path)

> Follow `08_START_family_filling.md`. Target: `dataset/family_03_hamiltonian_path/`.

## Domain framing

A delivery vehicle must visit a set of locations connected by one-way or two-way roads, passing through every location exactly once. Keep this framing across all three.

## Criterion 1 — NP-complete (Hamiltonian Path, general graph)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given a graph, decide whether a route visits every vertex exactly once; output such a route or `NO`.
- **Input:** `n m` then `m` edges (`u v`). Keep `1 ≤ n ≤ 18` so a Held–Karp style bitmask DP fits (2^n · n). State it as a plain road network; do not hint at hardness.
- **Output:** `YES` + a permutation of all `n` vertices forming a valid path (lexicographically smallest such path by the sequence of vertices), else `NO`.
- **Reference:** bitmask DP over subsets reconstructing the lexicographically smallest Hamiltonian path, O(2^n · n^2). Deterministic.

## Criterion 2 — P (Hamiltonian path in a DAG via unique topological order)

- **Class:** P. **Letter:** B.
- **Problem:** Same routing task, but roads are strictly one-way and there are **no cycles** (describe operationally: "every road goes from a lower-stage location to a higher-stage one; you can never return to a location once left"). Decide existence and output the route or `NO`.
- **Theorem to use:** a DAG has a Hamiltonian path iff its topological order is unique, i.e. at every step of Kahn's algorithm exactly one vertex has in-degree 0; the unique order IS the path (check each consecutive pair is an edge).
- **Input:** `n m`, then `m` directed edges; guaranteed acyclic. `1 ≤ n ≤ 2e5`, `1 ≤ m ≤ 2e5`.
- **Output:** `YES` + the route (the forced order), else `NO`. Output is unique, so `judge: exact`.
- **Reference:** Kahn's algorithm; if at any step the in-degree-0 set has size ≠ 1, output `NO`; else verify consecutive edges exist. O(n+m). Never write "DAG" or "topological" in the statement.

## Criterion 3 — Infeasible (isolated vertex)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** Same routing task on a graph with **more than one vertex** where one location has **no roads at all**. A route covering every location is impossible because the isolated location can never be entered or left. Certify impossibility by naming the unreachable location.
- **Input:** `n m` (`n ≥ 2`), `m` edges; guaranteed at least one degree-0 vertex.
- **Output:** the smallest index of a location with no incident roads. (Define exactly in statement.)
- **Judge:** `exact` (smallest isolated vertex is unique). Optionally add `validator.py` confirming the printed vertex truly has degree 0.
- **Reference:** read edges, mark degrees, print smallest vertex with degree 0.

## Test cases

- C1: a graph with a Hamiltonian path, one without (`NO`), a 2-vertex case.
- C2: a unique-order chain (`YES`), a graph where two vertices are simultaneously sources (`NO`).
- C3: two graphs each with a known isolated vertex.

Generate `.out` from references, run `reference_check`, fix flags, report, wait for `11`.

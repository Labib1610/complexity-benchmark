# 04 — Build Family 1 End-to-End (The Worked Template)

> Prerequisite: harness from file `03` imports cleanly.

## Goal

Build **Family 1 (Shift Assignment / Graph Coloring)** completely — all three criteria, statements, references, validators, and a few sample test cases — and validate it with the harness. This proves the whole pipeline on one family before we scale to 16. **Every later family is a copy of this shape.**

Family 1 is already designed (it exists in the user's notebook). Reproduce it into the dataset layout. The three criteria:

- **Criterion 1 (NPC):** 3-coloring with `n ≤ 20` — backtracking, lexicographically smallest.
- **Criterion 2 (P):** 2-coloring / bipartiteness with `n ≤ 2·10⁵` — BFS, lexicographically smallest.
- **Criterion 3 (INFEASIBLE):** triangle certificate — graph guaranteed to contain a triangle; output the lexicographically smallest triangle (proves 2-coloring impossible).

## Step 1 — Create the family folder

```
dataset/family_01_graph_coloring/
├── family.yaml
├── criterion_1_npc/
│   ├── statement.md
│   ├── meta.yaml
│   ├── reference.py
│   └── tests/
├── criterion_2_p/
│   ├── statement.md
│   ├── meta.yaml
│   ├── reference.py
│   └── tests/
└── criterion_3_infeasible/
    ├── statement.md
    ├── meta.yaml
    ├── reference.py
    ├── validator.py
    └── tests/
```

`family.yaml`:
```yaml
family: "01"
name: graph_coloring
display_name: "Shift Assignment (Graph Coloring)"
base_problem: "Assign workers to shifts so no conflicting pair shares a shift."
anchor: 3-COLORING
```

## Step 2 — Criterion 1 (NPC): statement, meta, reference

`criterion_1_npc/statement.md` (NO class names — bounds only):
```markdown
# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A factory runs three shifts labeled 1, 2, 3. There are n workers. Some pairs of
workers are in conflict and must not be placed on the same shift. Assign every
worker to exactly one of the three shifts so that no conflicting pair shares a
shift, or report that it is impossible.

## Input
The first line contains two integers n and m — the number of workers and the
number of conflict pairs (1 ≤ n ≤ 20, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the shift of worker i. Among all valid
assignments output the lexicographically smallest sequence (compare s₁ first,
then s₂, and so on).

## Example 1
Input:
4 5
1 2
1 3
2 3
1 4
2 4
Output:
YES
1 2 3 3

## Example 2
Input:
4 6
1 2
1 3
1 4
2 3
2 4
3 4
Output:
NO
```

`criterion_1_npc/meta.yaml`:
```yaml
family: "01"
family_name: graph_coloring
criterion: 1
class: NPC
problem_letter: A
intended_algorithm: "lexicographically-smallest backtracking over 3 colors"
reduction_note: "3-COLORING; Karp 21; reduction from 3-SAT via palette gadget; NP-complete even for max-degree 4"
constraint_delta: "anchor variant (NP-complete base)"
judge: exact
time_limit_s: 2
memory_limit_mb: 256
```

`criterion_1_npc/reference.py` — use the notebook's `A.py` (backtracking DFS, tries colors 1,2,3 in index order, prints YES + assignment or NO). Reproduce it faithfully.

## Step 3 — Criterion 2 (P): statement, meta, reference

`criterion_2_p/statement.md` (note: never write the word that names the structure — describe two shifts and bounds only):
```markdown
# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The same factory now runs only two shifts, labeled 1 and 2. With n workers and m
conflict pairs, assign each worker a shift so that no conflicting pair shares a
shift, or report impossibility.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 2·10⁵, 0 ≤ m ≤ 2·10⁵).
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with n integers s₁ … sₙ (each in {1,2}),
the lexicographically smallest valid assignment.

## Example 1
Input:
4 4
1 2
2 3
3 4
1 4
Output:
YES
1 2 1 2

## Example 2
Input:
3 3
1 2
1 3
2 3
Output:
NO
```

`criterion_2_p/meta.yaml`:
```yaml
family: "01"
family_name: graph_coloring
criterion: 2
class: P
problem_letter: B
intended_algorithm: "BFS 2-coloring; assign shift 1 to lowest-indexed unvisited node per component; O(n+m)"
reduction_note: "2-COLORING = bipartiteness testing; only obstruction is an odd cycle"
constraint_delta: "shifts reduced 3->2; removes NP-hardness entirely"
judge: exact
time_limit_s: 1
memory_limit_mb: 256
```

`criterion_2_p/reference.py` — use the notebook's `B.py` (BFS coloring, lexicographically smallest, prints YES/assignment or NO).

## Step 4 — Criterion 3 (INFEASIBLE): statement, meta, reference, validator

`criterion_3_infeasible/statement.md`:
```markdown
# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be
hopeless. Your job is not to schedule — it is to certify the impossibility. It is
guaranteed that the conflict graph contains at least one set of three workers who
pairwise conflict. Any such set proves two shifts cannot suffice. Output one such set.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000,
3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next m lines contains two integers u v — a conflicting pair.
It is guaranteed that at least one such triple exists.

## Output
Print three integers a b c on one line with a < b < c such that all three pairs
a–b, a–c, b–c are conflicts. Output the lexicographically smallest such triple
(smallest a; ties by smallest b; then smallest c).

## Example 1
Input:
4 5
1 2
1 3
2 3
2 4
3 4
Output:
1 2 3

## Example 2
Input:
5 6
1 2
1 4
2 4
3 4
3 5
4 5
Output:
1 2 4
```

`criterion_3_infeasible/meta.yaml`:
```yaml
family: "01"
family_name: graph_coloring
criterion: 3
class: INFEASIBLE
problem_letter: C
intended_algorithm: "bitset adjacency; iterate a asc, neighbor b>a asc, c=lowest set bit of adj[a]&adj[b], c>b; O(n*m/64)"
reduction_note: "triangle (K3) is 3-chromatic; its presence makes 2-coloring impossible; certificate-style infeasibility"
constraint_delta: "guarantee a triangle exists; task becomes 'prove no 2-coloring'"
judge: exact
time_limit_s: 2
memory_limit_mb: 256
```

> The expected output is unique (lexicographically smallest triple), so `judge: exact` is correct. We ALSO add a `validator.py` as a defensive cross-check and as the template for future "any valid certificate" problems.

`criterion_3_infeasible/reference.py` — implement the bitset triangle search returning the lexicographically smallest triple (matches the notebook's intended approach for Problem C).

`criterion_3_infeasible/validator.py`:
```python
def validate(input_text: str, output_text: str):
    lines = input_text.split()
    n = int(lines[0]); m = int(lines[1])
    edges = set()
    idx = 2
    for _ in range(m):
        u = int(lines[idx]); v = int(lines[idx+1]); idx += 2
        edges.add((min(u, v), max(u, v)))
    toks = output_text.split()
    if len(toks) != 3:
        return False, "expected exactly three integers"
    a, b, c = (int(t) for t in toks)
    if not (a < b < c):
        return False, "not strictly increasing"
    for x, y in ((a, b), (a, c), (b, c)):
        if (x, y) not in edges:
            return False, f"pair {x}-{y} is not a conflict"
    return True, "valid triangle"
```

## Step 5 — Add sample test cases

For each criterion, create at least the two examples from the statement as `tests/01.in`/`01.out` and `tests/02.in`/`02.out`, plus 1–2 small hand-made edge cases (e.g. minimal n, no edges, all-conflict). Keep them tiny and correct. The user will add MORE numbered cases later; the harness auto-discovers them.

> Generate `.out` files by **running the reference** on each `.in`, not by hand — see Step 6.

## Step 6 — Generate outputs from references & validate

1. For every `.in`, run the corresponding `reference.py` and write its stdout to the matching `.out`. (This guarantees `.out` is exactly what the reference produces.)
2. Run the dataset self-test:
   `python -m harness.reference_check dataset/family_01_graph_coloring`
3. Fix anything it flags (reference mismatch, missing `.out`, leakage terms in a statement).

## Step 7 — Report

Show the final tree of `dataset/family_01_graph_coloring/`, the reference-check output (should be clean), and confirm the leakage check passed. This family is now the **canonical template**.

## Done

**Stop and wait** for `05_remaining_families_scaffold.md`.

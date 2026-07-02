# Problem Statement Schema

Every `statement.md` shown to a model MUST contain these sections, in order,
and NOTHING that reveals the complexity class.

## Required sections
1. **Title line** — `# Problem <LETTER> — <Name>`  (e.g. `# Problem A — Trichrome Shifts`)
2. **Limits line** — `Time limit: X s   Memory limit: Y MB`
3. **Description** — prose statement of the task.
4. **Input** — exact format and constraint bounds.
5. **Output** — exact format, including any tie-break rule.
6. **Examples** — at least one input/output pair, fenced.
7. (optional) **Note** — clarifying remarks that do NOT name the class.

## Forbidden in statement.md (leakage check)
Do NOT include any of:
- the words "NP-complete", "NP-hard", "polynomial", "P-time", "bipartite",
  "tree" (when it reveals structure), "DAG", "2-SAT/3-SAT" as labels,
  "intractable", "exponential", reduction names, or any complexity commentary.
- hints like "this is the easy variant" or "brute force is fine".

Constraint bounds (e.g. `n <= 20`) ARE allowed and expected — they are part of
the problem, not a class label. The model must infer difficulty from bounds and
structure, not from labels.

## Where the hidden truth lives: meta.yaml
Each criterion folder has a `meta.yaml` (model NEVER sees it) with:

```yaml
family: 01
family_name: graph_coloring
criterion: 1                 # 1, 2, or 3
class: NPC                   # one of: P | NPC | INFEASIBLE
problem_letter: A
intended_algorithm: "lexicographically-smallest backtracking over 3 colors"
reduction_note: "3-COLORING; Karp 21; reduction from 3-SAT via palette gadget"
constraint_delta: "anchor variant (the NP-complete base)"
judge: exact                 # exact | custom
time_limit_s: 2
memory_limit_mb: 256
```

`class` values:
- `P`          — polynomial-time solvable variant
- `NPC`        — NP-complete variant
- `INFEASIBLE` — no valid solution exists by construction

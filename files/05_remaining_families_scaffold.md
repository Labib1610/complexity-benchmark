# 05 — Scaffold Families 02–16 (Empty, Correctly-Structured, With Fill Guide)

> Prerequisite: Family 1 is complete and validated (file `04`).

## Goal

Create the **folder skeletons for families 02–16** matching the Family 1 shape exactly, pre-fill each `family.yaml` and each `meta.yaml` from the known design (the user's 16-family validation document), and leave `statement.md` / `reference.py` / `tests/` as **clearly-marked placeholders** the user fills in later. This is what lets the user "add data as a number followed and it does as it is."

> Do NOT invent problem statements or reference solutions for families 02–16 now. Only scaffold structure + metadata + placeholder markers. The user (with you, later, one family at a time) will fill the actual statements/references following the Family 1 template.

## The 16 families (canonical list)

Use these slugs and anchors. They come directly from the validated design.

| # | slug | display name | NPC anchor | P variant | Infeasible trigger |
|---|------|--------------|-----------|-----------|--------------------|
| 01 | graph_coloring | Shift Assignment | 3-COLORING | 2-COLORING (bipartite) | triangle certificate |
| 02 | sat | Task Scheduling | 3-SAT | 2-SAT | contradiction cycle (x and ¬x same SCC) |
| 03 | hamiltonian_path | Delivery Routing | HAMILTONIAN PATH | unique-topo-order DAG | isolated vertex |
| 04 | subset_sum | Budget Selection | SUBSET SUM (large values) | poly-bounded values | negative target |
| 05 | three_dim_matching | Team & Resource Alignment | 3-DIMENSIONAL MATCHING | bipartite matching (Hopcroft-Karp) | empty compatibility row (Hall) |
| 06 | bin_packing | Cargo Loading | BIN PACKING | fractional bin packing | item bigger than any bin |
| 07 | shortest_common_superstring | DNA/Log Assembly | SCS (k≥3) | 2-string overlap | forbidden substring contradiction |
| 08 | vertex_cover | Security Guard Placement | VERTEX COVER | bipartite (König) | matching lower bound > budget |
| 09 | clique_independent_set | Social Network Analysis | CLIQUE | bipartite independent set (König) | size > |V| (pigeonhole) |
| 10 | dominating_set | Sensor Placement | DOMINATING SET | tree DP | isolated vertex with budget 0 |
| 11 | set_cover | Skill Coverage | SET COVER | size-2 sets = edge cover (König) | uncoverable element |
| 12 | knapsack | Investment Portfolios | 0-1 KNAPSACK | fractional knapsack (greedy) | budget 0, positive costs |
| 13 | partition | Workload Partitioning | PARTITION | small-integer DP | odd total sum |
| 14 | steiner_tree | Network Extension | STEINER TREE | all-required = MST | isolated required node |
| 15 | lcs | Bioinformatics Alignment | MULTIPLE-SEQ LCS (k≥3) | 2-sequence LCS DP | disjoint alphabets |
| 16 | job_shop | Factory Scheduling | JOB-SHOP (m≥3) | 2-machine flow-shop (Johnson) | deadline < min job time |

## Step 1 — Generate the skeletons

For each family 02–16, create:

```
dataset/family_XX_<slug>/
├── family.yaml
├── criterion_1_npc/
│   ├── statement.md          # placeholder
│   ├── meta.yaml             # PRE-FILLED from the table + design doc
│   ├── reference.py          # placeholder
│   └── tests/.gitkeep
├── criterion_2_p/
│   ├── statement.md          # placeholder
│   ├── meta.yaml             # PRE-FILLED
│   ├── reference.py          # placeholder
│   └── tests/.gitkeep
└── criterion_3_infeasible/
    ├── statement.md          # placeholder
    ├── meta.yaml             # PRE-FILLED
    ├── reference.py          # placeholder
    └── tests/.gitkeep
```

Assign `problem_letter` sequentially per family if you like (A/B/C within a family), or globally — pick one scheme and apply it consistently. Recommended: A/B/C reset per family for readability.

## Step 2 — Pre-fill every `meta.yaml`

Fill `class`, `intended_algorithm`, `reduction_note`, and `constraint_delta` from the table above and the design document. Leave `judge`, `time_limit_s`, `memory_limit_mb` at sensible defaults (`exact`, family-appropriate seconds, 256). Mark `judge: custom` ONLY where "any valid answer" is accepted (you can default everything to `exact` now and flip later).

Example for `family_02_sat/criterion_1_npc/meta.yaml`:
```yaml
family: "02"
family_name: sat
criterion: 1
class: NPC
problem_letter: A
intended_algorithm: "<FILL: backtracking / DPLL-style for 3-SAT assignment>"
reduction_note: "3-SAT; Cook-Levin (1971); canonical NP-complete"
constraint_delta: "anchor variant (NP-complete base)"
judge: exact
time_limit_s: 2
memory_limit_mb: 256
```

## Step 3 — Placeholder content for `statement.md` and `reference.py`

Each placeholder `statement.md`:
```markdown
# Problem <LETTER> — <FILL TITLE>

Time limit: <X> s   Memory limit: 256 MB

<!--
PLACEHOLDER — fill following conventions/statement_schema.md and the Family 1 template.
RULES:
- Describe the task in plain words. Bounds allowed. NEVER name the complexity class.
- This is the <CLASS> variant of family <XX> (<slug>). Anchor: <anchor>.
- Required sections: Description, Input, Output (with tie-break), at least one Example.
-->
```

Each placeholder `reference.py`:
```python
# PLACEHOLDER reference solution for family <XX> (<slug>), criterion <n> (<CLASS>).
# Fill with a deterministic Python 3 solution: read stdin, write stdout.
# Intended algorithm (from meta.yaml): <intended_algorithm>
import sys
def main():
    data = sys.stdin.buffer.read().split()
    # TODO: implement
    raise NotImplementedError
main()
```

## Step 4 — Write a fill-in guide

Create `dataset/HOW_TO_FILL_A_FAMILY.md`:

```markdown
# How to Fill a Family

Each family is filled by copying the shape of family_01_graph_coloring.

For each of the three criteria:
1. Write statement.md per conventions/statement_schema.md. NEVER name the class.
   Add 1–2 worked examples in the statement.
2. Write reference.py: deterministic, stdin->stdout, matches intended_algorithm in meta.yaml.
3. Add test cases:
   - Put the statement's example inputs as tests/01.in, tests/02.in, ...
   - Add small edge cases (minimal sizes, empty, the infeasible sentinel case).
   - GENERATE every .out by RUNNING reference.py on the .in (never hand-write outputs).
4. If "any valid answer" is acceptable, set judge: custom in meta.yaml and add validator.py
   (contract in conventions/checker_spec.md). Otherwise pin a tie-break so judge: exact works.
5. Validate: python -m harness.reference_check dataset/family_XX_<slug>
   Fix any reference mismatch, missing .out, or leakage-term flag.

Adding MORE test cases later: just drop tests/NN.in and generate tests/NN.out from the
reference. The harness auto-discovers them — no code change needed.
```

## Step 5 — Report

List the dataset tree (families 01–16 present), confirm every `meta.yaml` is filled with the correct `class`, and confirm placeholders are clearly marked. Note that references for 02–16 are intentionally `NotImplementedError` until filled.

## Done

**Stop and wait** for `06_generation_and_evaluation_drivers.md`.

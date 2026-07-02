# 09 — Fill Family 02: Task Scheduling (SAT)

> Follow the fixed procedure in `08_START_family_filling.md`. Target: `dataset/family_02_sat/`.

## Domain framing (use this cover story consistently across all three)

A set of tasks must each be assigned a time window. Compatibility rules constrain which windows tasks may take, expressed as clauses ("at least one of these task–window choices must hold"). This is SAT dressed as scheduling. Keep the same vocabulary in all three statements; only the structure changes.

## Criterion 1 — NP-complete (3-SAT)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given Boolean variables and clauses of **exactly 3 literals**, decide satisfiability and output a satisfying assignment or `NO`. Frame variables as task on/off decisions; each clause lists 3 literals.
- **Input:** `n m` (variables, clauses); then `m` lines each with 3 signed integers (e.g. `1 -2 3` means x1 OR ¬x2 OR x3). `1 ≤ n ≤ 40`, clauses arbitrary.
- **Output:** `YES` + a line of `n` values in {0,1} (the lexicographically smallest satisfying assignment by variable index), else `NO`.
- **Reference:** backtracking / DPLL with unit propagation, exploring variable values 0 then 1 in index order to guarantee lexicographically smallest. Deterministic.

## Criterion 2 — P (2-SAT)

- **Class:** P. **Letter:** B.
- **Problem:** identical framing, but clauses have **exactly 2 literals**. Decide satisfiability, output an assignment or `NO`.
- **Input:** `n m`; then `m` lines of 2 signed integers. `1 ≤ n ≤ 1e5`, `1 ≤ m ≤ 2e5`.
- **Output:** `YES` + lexicographically smallest satisfying assignment in {0,1}, else `NO`. (To get lexicographically smallest in 2-SAT: build the implication graph, Tarjan/Kosaraju SCC; a formula is satisfiable iff no variable shares an SCC with its negation; then choose values greedily from lowest variable preferring 0 when free, respecting forced implications. If full lexicographic-smallest is too intricate, the statement may instead require "any satisfying assignment" and you set `judge: custom` with a validator that checks all clauses — choose ONE approach and make statement + meta consistent.)
- **Reference:** implication graph + SCC (Tarjan), O(n+m).
- **Note:** never write "2-SAT" or "implication graph" in the statement; just say each clause has two literals.

## Criterion 3 — Infeasible (contradiction cycle)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** the same 2-literal-clause setting, but it is **guaranteed unsatisfiable** by a contradiction. The task is to certify it: output a variable that is forced both true and false. Equivalent to: some variable x and ¬x lie in the same SCC of the implication graph.
- **Input:** `n m` then `m` 2-literal clauses; guaranteed unsatisfiable.
- **Output:** a single integer — the smallest-indexed variable that the implication structure forces into contradiction. (Define precisely in the statement: "print the smallest index i such that asserting xi true and asserting xi false each lead, by the implication rules, back to the other.")
- **Judge:** `custom` is cleanest — add `validator.py` that rebuilds the implication graph from the clauses and confirms the printed variable is genuinely in a contradictory SCC. Alternatively pin "smallest such index" and use `exact`. Pick one; keep statement + meta consistent.
- **Reference:** implication-graph SCC; report the smallest variable index whose two literals are in the same SCC.

## Test cases (per criterion: examples + edges)

- C1: one satisfiable instance, one unsatisfiable (→ `NO`), one tiny (n=1).
- C2: an even cycle of implications (satisfiable), a clearly satisfiable small set, one `NO`.
- C3: at least two instances each with a known forced-contradiction variable.

Generate all `.out` by running the references. Then run `python -m harness.reference_check dataset/family_02_sat` and fix flags. Report and wait for `10`.

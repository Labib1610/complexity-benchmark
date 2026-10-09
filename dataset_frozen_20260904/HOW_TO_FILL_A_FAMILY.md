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

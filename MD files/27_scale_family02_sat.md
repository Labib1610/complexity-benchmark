# 27 — Scale Family 02: Task Scheduling (SAT)

> Follow the corrected rule in `25_START_test_case_scaling.md`. Family 01 is the
> proven template — open it if unsure. Target: `dataset/family_02_sat/`.
>
> **Rule reminder:** ground truth = unlimited offline time. Size is chosen by where a
> **realistic competent baseline** exceeds the model's `time_limit_s`.

## Family 02 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | 3-SAT, DPLL-style backtracking | plain backtracking + unit propagation | **same shape (2^n)** — hardness from instance structure |
| 2 | P | 2-SAT, implication graph + SCC, O(n+m) | naive: try assignments / repeated propagation, O(n·m) | asymptotic gap ✅ |
| 3 | INFEASIBLE | implication-graph SCC contradiction | naive: brute-force search for the contradiction | asymptotic gap ✅ |

Criterion 1 is like Family 01 — no asymptotic gap, so **hardness must come from
instance structure**. See below.

## Criterion 1 (NPC) — the phase transition is everything

Random 3-SAT has a sharp, well-known phase transition at **clause-to-variable ratio
m/n ≈ 4.26**. Instances at that ratio are exponentially hard; away from it they are
trivially easy (satisfiable below, trivially refutable above). **Generate at m ≈ 4.26·n.**
Size alone will not create hardness — the ratio will.

**UNSAT instances are the expensive ones** (they force exhaustive refutation), just as
hard NO instances were in Family 01. Hunt for adversarial seeds; hardness varies
enormously seed to seed.

1. Write `tools/naive_family_02_criterion_1.py` — realistic: backtracking with unit
   propagation, variables in index order. NOT a strawman (no removing propagation).
2. Probe with the **baseline** across `n ∈ [30, 40, 50, 60, 70]` at m ≈ 4.26n, seeds
   1..8. Find where it exceeds `time_limit_s`. Expect the wall somewhere around
   **n ≈ 40–60** (3-SAT DPLL is efficient; you may need to go higher than Family 01).
3. Confirm exponential blow-up in the curve before committing.

## Criterion 2 (P) — punish the inefficient-but-correct

Real asymptotic gap here. Baseline `tools/naive_family_02_criterion_2.py` = a
**correct but O(n·m)** approach (e.g. repeatedly propagate implications until fixpoint
for each variable, or try both polarities per variable with full propagation). It must
TLE while the O(n+m) SCC reference is comfortable.

Scale toward the statement bound: `n ∈ [1e3, 1e4, 5e4, 1e5]`, `m ≈ 2n` (respect
`m ≤ 2e5`). Include a large satisfiable case, a large unsatisfiable case, and one with
many disconnected components.

## Criterion 3 (INFEASIBLE) — scale toward the bound

Baseline = brute-force search for the contradictory variable (e.g. for each variable,
try asserting it and fully explore implications, O(n·m)) → must TLE. The SCC-based
reference is O(n+m).

Scale `n` and `m` toward the stated bounds. Ensure at least one large case where the
contradictory variable is at a **high index**, so a solution that scans and reports the
first thing it finds (rather than the smallest index) fails.

## Procedure (same as Family 01)

1. Write `tools/gen_family_02.py` — seeded, deterministic. Generators:
   - `gen_3sat(n, ratio=4.26, seed, force_unsat=None)` — clauses of exactly 3 distinct
     literals, no duplicate/tautological clauses.
   - `gen_2sat(n, m, seed, satisfiable=True)` — 2-literal clauses; plant a contradiction
     cycle when `satisfiable=False`.
   - `gen_2sat_contradiction(n, m, seed, contra_var)` — guaranteed unsatisfiable with a
     known forced-contradiction variable.
2. Write the three realistic baselines (`tools/naive_family_02_criterion_{1,2,3}.py`).
3. **Probe with the baseline**, not the reference. Record the curve; confirm the wall.
4. Emit a **ramp of 5 cases straddling the threshold** (≈2 pass, ≈3 TLE), appended
   after the existing anchors (keep 01–04, do not renumber).
5. **Generate every `.out` with the reference, unlimited time** (background if slow).
   Record elapsed as provenance only.
6. **Mandatory proof:** realistic baseline exits 124 (TLE) at `time_limit_s` on the
   largest cases; report exit codes:
   ```bash
   timeout 2 python tools/naive_family_02_criterion_1.py < <largest .in>; echo "exit=$?"
   # exit=124 = TLE = SUCCESS. This is the whole point.
   ```
7. Update each `statement.md` bound to match the new max size (bounds must be truthful).
8. Append the `scaling:` provenance block to each `meta.yaml` (schema in file 25).
9. `python -m harness.reference_check dataset/family_02_sat` → clean.

## Report

Baseline probe curve (showing exponential blow-up on criterion 1), threshold and
chosen max, the ramp with pass/TLE per case, the mandatory proof exit codes, reference
generation times (informational), statement bound changes, and reference_check clean.

Then **stop and wait** for `28_scale_family03_hamiltonian_path.md`.

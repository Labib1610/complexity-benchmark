# Complexity Benchmark: Verified Audit and Repair Plan

**Re-audit date:** 2026-09-01  
**Source archive:** `/Users/nzabir/Downloads/complexity-benchmark-main.zip`  
**Archive SHA-256:** `70b3478452d905638b5d8086322a0c0cb0d4e121b83c3ba42032422c1edc606f`  
**ZIP revision:** `67f92cecb59e1e02a067a09dd81b57467625829e`  
**Analysis copy:** `complexity-benchmark-main/`

Source paths are relative to the analysis copy unless prefixed with
`complexity-benchmark-main/`.

## Executive verdict

The repository is a useful benchmark-development prototype, but the current release cannot
support a claim that models distinguish P from NP-complete behavior or switch to
approximation under a deadline.

The decisive failures are:

1. **The evaluated deadline is not the stated deadline.** The main run gives every program
   600 seconds instead of the declared 1, 2, or 5 seconds.
2. **Several "hard" arms are deliberately tractable by standard exact algorithms.** The
   benchmark often keeps the exponential parameter small and grows a different variable
   that only defeats one weaker baseline.
3. **The tests are static, small, correlated, and public to executed code.** They measure
   conformance to a few constructions, not robustness on a hidden hard distribution.
4. **`INFEASIBLE` is a promised condition, not a third complexity class.** Six arms accept a
   constant `NO` or `NONE` on every test, and several statements print the answer explicitly.
5. **The approximation study is nonfunctional.** Its prompt, output plumbing, objective
   modules, input plumbing, and aggregation are all incomplete or incorrect.
6. **The hardening evidence is invalid for runtime hardness.** It ignores task limits,
   records cumulative retirement as defeat, and has only been run on family 01.
7. **The retained main result is stale and unauditable.** It uses fewer tests than the
   current dataset and contains no model generations or raw verdicts.

These are release blockers, not minor limitations.

## Evidence standard

This report uses three claim types:

- **Source fact:** directly cited to repository file and line numbers.
- **Measured fact:** recomputed from this archive; the exact method and result are recorded in
  the verification log.
- **Supported inference:** an explanation consistent with source and measurements, but not a
  claim about an unobserved model strategy.

One important limit follows from that standard: the main run's generated code is absent.
Therefore this audit does **not** claim that a specific main-run model used meet-in-the-middle,
FPT, branch-and-bound, or a constant shortcut. It proves that the benchmark permits those
fast strategies and that its retained results cannot distinguish among them.

Timing measurements are machine-specific. File counts, hashes, source behavior, stored JSON
counts, duplicate groups, and output diversity are not.

## Why SOTA models can solve it

NP-completeness is a worst-case property of an unbounded decision problem. It does not imply
that every finite instance is hard, that `n > 40` is hard, or that a restricted parameter
range prevents fast exact solving.

The repository's own metadata gives the direct explanation:

| Arm | Verified exact route | Why the selected cases remain manageable |
|---|---|---|
| Subset sum A | Meet-in-the-middle, `O(2^(n/2))`; largest selected `n=36`, recorded at about 0.10 s (`dataset/family_04_subset_sum/criterion_1_npc/meta.yaml:13-45`). | The half-space is `2^18`, not `2^36`. The benchmark defeats `O(2^n)` recursion, not meet-in-the-middle. |
| Shortest superstring A | Held-Karp `O(2^k k^2)`; selected maximum `k=16`, recorded at about 1.02 s (`dataset/family_07_shortest_common_superstring/criterion_1_npc/meta.yaml:13-43`). | The reference is intentionally capped where its bitmask DP fits; the baseline enumerates `k!` permutations. |
| Vertex cover A | Bounded search tree `O(2^k m)`; `k` remains at most 18 (`dataset/family_08_vertex_cover/criterion_1_npc/meta.yaml:13-46`). | The generator raises `n` and places a unique P3 cover late for a `C(n,k)` baseline while leaving the FPT parameter small. |
| Clique A | Bitset branch-and-bound; `n=46,k=14` is recorded at about 0.01 s (`dataset/family_09_clique_independent_set/criterion_1_npc/meta.yaml:13-44`). | Heavy pruning solves these planted/random constructions while the selected baseline enumerates all `k`-subsets. |
| Set cover A | Bitmask DP over skills with `u<=20`; selected `s=200` is recorded at about 0.03 s (`dataset/family_11_set_cover/criterion_1_npc/meta.yaml:13-45`). | The exponential space is at most `2^20`; growing consultants `s` mainly hurts the `C(s,k)` baseline. |
| Steiner A | Dreyfus-Wagner exponential in terminals with `t<=10`; recorded probes are about 0.02--0.16 s (`dataset/family_14_steiner_tree/criterion_1_npc/meta.yaml:13-42`). | The generator explicitly holds `t` small while growing optional nodes. |
| Multi-LCS A | Memoized `O(L^k)` DP with `k<=5`; `k=5,L=16` is recorded at 2.54 s (`dataset/family_15_lcs/criterion_1_npc/meta.yaml:13-46`). | For fixed `k<=5`, this is polynomial in `L`; the baseline is the same recursion without memoization. |
| Graph coloring A | Metadata states that forward checking solves the selected cases sub-second, although index-order backtracking times out (`dataset/family_01_graph_coloring/criterion_1_npc/meta.yaml:32-39`). | `n<=40` defeats one variable ordering, not all competent exact coloring algorithms. |

Fresh execution confirms the distinction. On the highest-numbered available test of each
criterion under the declared limit, 42/48 references passed and six timed out; all 48
designated naive solvers timed out. The six reference failures were graph coloring A, SAT A,
Hamiltonian path A, 3D matching A, partition B, and job shop A. See Verification V5.

Thus the references fall into three groups:

1. exact algorithms that are fast because the decisive parameter is small;
2. exact algorithms that are fast on the selected construction because of pruning,
   memoization, symmetry breaking, or meet-in-the-middle; and
3. slow references that pass only in offline validation or evaluation with expanded limits.

This fully explains why fast exact solutions are possible without implying `P = NP`.

## Release blockers

### B1. Resource limits are not enforced

**Evidence**

- Every criterion declares 1, 2, or 5 seconds (Verification V1).
- The retained run config sets `global_timeout_s: 600`
  (`runs/2026-07-01_main/run_config.yaml:1-12`).
- Evaluation forwards that override (`harness/evaluate.py:80-93,148-149`).
- The checker chooses the override instead of `meta.yaml`
  (`harness/checker.py:87-103`).
- The run template recommends the same 600-second value
  (`runs/run_config_template.yaml:1-13`).
- Hardening explicitly says not to enforce the task limit and uses a separate ceiling
  (`agentic/tools/harden_loop.py:211-226`).
- Frontier evaluation states that "TLE is NOT a verdict" and uses a 3,600-second runaway
  guard (`agentic/tools/frontier_eval.py:10-14,94-112`).

**Consequence**

A 2-second task receives 300 times its stated budget in the main run. A correct exponential
program can be reported as a pass even when it fails the research condition being tested.
Stored hardening data contains 1,633 `PASS` cases above the declared limit, including one
2-second case at 283.024 seconds (Verification V8).

**Required action**

Use one submitted-solution budget in main, hardening, frontier, and held-out evaluation. A
global setting may reduce a task budget but must never expand it. Offline oracle generation
must be reported separately and never enter model pass/fail.

**Closure evidence**

- An integration test submits a program that sleeps for `limit + epsilon` and receives TLE
  in every evaluation path.
- Every raw case record stores declared limit, effective limit, elapsed CPU/wall time, and
  verdict.
- A release check fails if any `PASS` has `elapsed > effective_limit`.

### B2. Difficulty is calibrated against weak baselines

**Evidence**

All 48 designated naive programs timed out on the highest-numbered available case, but
metadata often defines a baseline that omits the central algorithm or promise:

- subset sum compares `O(2^n)` recursion against `O(2^(n/2))` meet-in-the-middle
  (`dataset/family_04_subset_sum/criterion_1_npc/meta.yaml:13-31`);
- bin packing omits one empty-bin symmetry cut
  (`dataset/family_06_bin_packing/criterion_1_npc/meta.yaml:13-28`);
- vertex cover compares `C(n,k)` enumeration with `O(2^k m)` branching
  (`dataset/family_08_vertex_cover/criterion_1_npc/meta.yaml:13-27`);
- set cover fixes `u<=20` and grows `s` to break `C(s,k)` enumeration
  (`dataset/family_11_set_cover/criterion_1_npc/meta.yaml:13-27`);
- infeasible subset sum intentionally uses a baseline that ignores a negative target
  (`dataset/family_04_subset_sum/criterion_3_infeasible/meta.yaml:13-29`);
- infeasible LCS intentionally uses memo-less LCS despite disjoint alphabets
  (`dataset/family_15_lcs/criterion_3_infeasible/meta.yaml:13-33`).

Job shop is an especially strong counterexample to the current calibration method: its
metadata says the weaker solver is sometimes faster and that only one hunted seed creates a
gap (`dataset/family_16_job_shop/criterion_1_npc/meta.yaml:13-28,40-46`).

**Consequence**

"Naive solver timed out" proves only that one implementation is weak on that construction.
It does not show that a standard contest algorithm, optimized exact solver, SOTA-generated
solver, or timeout-aware hybrid is challenged.

**Required action**

Calibrate every hard arm against a portfolio:

- naive and textbook;
- optimized exact;
- FPT/parameterized;
- SAT/CP-SAT/MIP or other solver-backed oracle;
- heuristic and approximation;
- timeout-aware exact/heuristic hybrid;
- several SOTA development models.

Retain a hard distribution only when the optimized exact portfolio cannot saturate it under
the real deadline and useful heuristics produce a nontrivial score spread.

**Closure evidence**

Publish a baseline matrix by generator, size, seed, YES/NO status, runtime, feasibility, and
objective quality. No criterion may be accepted from one baseline comparison.

### B3. The hard tier often scales the wrong parameter

**Evidence**

- set cover says the window comes from "FIXING u" while growing `s`
  (`dataset/family_11_set_cover/criterion_1_npc/meta.yaml:13-27,40-45`);
- Steiner says "HOLD t SMALL AND GROW n"
  (`dataset/family_14_steiner_tree/criterion_1_npc/meta.yaml:13-27,38-42`);
- vertex cover raises `n`, not `k`, because that breaks the selected enumeration baseline
  (`dataset/family_08_vertex_cover/criterion_1_npc/meta.yaml:40-46`);
- clique raises `n` while its branch-and-bound reference remains at about 0.01 s
  (`dataset/family_09_clique_independent_set/criterion_1_npc/meta.yaml:20-44`);
- multi-LCS keeps `k<=5`, although the cited hardness depends on variable sequence count
  (`dataset/family_15_lcs/criterion_1_npc/meta.yaml:6-20`).

**Consequence**

Large surface dimensions such as `n=46` or `s=200` create the appearance of scale while the
best known exact state space remains small.

**Required action**

For each task, identify the controlling parameter of the strongest known exact contestant
algorithm and scale that parameter across the deadline. Examples:

- raise set-cover universe size `u`, not only number of sets;
- raise Steiner terminal count `t`, not only relay nodes;
- raise LCS sequence count `k` if variable `k` is the claimed hard regime;
- move subset sum beyond the meet-in-the-middle half-space that fits the deadline;
- calibrate coloring against DSATUR/forward checking and SAT encodings, not index order.

**Closure evidence**

Each criterion must ship a complexity profile naming the strongest baseline, controlling
parameter, measured transition region, and hidden generator distributions. The hard split
must cross that baseline's measured resource boundary on repeated target-machine runs.

### B4. The three conditions do not isolate one semantic switch

**Evidence**

The README claims the variants differ by a "minimal semantic change"
(`README.md:7-11,32-48`). The statements often change several variables:

- 3D matching changes triples and `k` printed triples into bipartite pairs and one assignment
  vector (`dataset/family_05_three_dim_matching/criterion_1_npc/statement.md:15-28`;
  `dataset/family_05_three_dim_matching/criterion_2_p/statement.md:14-27`);
- bin packing changes indivisible feasibility with given `k` into divisible optimization
  without `k` (`dataset/family_06_bin_packing/criterion_1_npc/statement.md:5-20`;
  `dataset/family_06_bin_packing/criterion_2_p/statement.md:5-18`);
- clique becomes maximum independent set on a bipartite graph, then criterion C becomes a
  constant `NO` task (`dataset/family_09_clique_independent_set/criterion_1_npc/statement.md:7-22`;
  `dataset/family_09_clique_independent_set/criterion_2_p/statement.md:7-20`;
  `dataset/family_09_clique_independent_set/criterion_3_infeasible/statement.md:7-20`);
- job shop becomes two-machine flow shop with a different schema, then C adds a deadline
  (`dataset/family_16_job_shop/criterion_1_npc/statement.md:7-23`;
  `dataset/family_16_job_shop/criterion_2_p/statement.md:7-22`;
  `dataset/family_16_job_shop/criterion_3_infeasible/statement.md:7-22`).

A descriptive token comparison gives median A/B similarity 0.652; 11/16 pairs are below
0.70, and only subset sum and partition exceed 0.90 (Verification V4).

Canonicalization also changes independently. SAT A requires the lexicographically smallest
assignment, while SAT B accepts any assignment
(`dataset/family_02_sat/criterion_1_npc/statement.md:19-24`;
`dataset/family_02_sat/criterion_2_p/statement.md:14-17`).

The `NPC` label also conflates task types. NP-completeness formally classifies decision
languages, while current A arms include lexicographically canonical search, optimum value
plus witness, and optimum scalar output. Examples are graph-coloring canonical search,
knapsack optimization, and job-shop makespan
(`dataset/family_01_graph_coloring/criterion_1_npc/statement.md:15-20`;
`dataset/family_12_knapsack/criterion_1_npc/statement.md:16-19`;
`dataset/family_16_job_shop/criterion_1_npc/statement.md:13-23`). Their metadata cites the
related generalized decision problem, not a proof that the exact output contract is
NP-complete (`dataset/family_01_graph_coloring/criterion_1_npc/meta.yaml:6-8`;
`dataset/family_12_knapsack/criterion_1_npc/meta.yaml:6-8`;
`dataset/family_16_job_shop/criterion_1_npc/meta.yaml:6-8`).

**Consequence**

A performance difference cannot be attributed to complexity recognition. It may come from
different input schema, output burden, objective, representation, scale, or promise.

**Required action**

Use one task and one I/O schema per family. Across conditions preserve:

- objective and optimization direction;
- witness and canonicalization requirements;
- input fields and meanings;
- narrative and examples;
- broad scale.

Change only one documented promise or parameter. Record the pair contract in machine-readable
metadata and reject variants that violate it. Record decision/search/optimization/canonical
task type separately, and reserve `NP-complete` for the decision language actually justified
by the reduction note.

**Closure evidence**

An automated pair gate compares schema, objective, output type, canonicalization, and scale.
Every difference must be listed in a single approved `complexity_switch` field. A human audit
must confirm that the switch, not a new task, explains tractability.

### B5. `INFEASIBLE` is inherently gameable in its current form

**Evidence**

The repository defines it as "No valid solution exists by construction"
(`README.md:37-42`; `conventions/statement_schema.md:43-46`). It is not undecidability and is
not disjoint from P.

Six of 16 infeasible arms have one normalized expected answer on every test:

| Families | Constant answer | Passing tests |
|---|---:|---:|
| 04, 09, 12, 13, 16 | `NO` | 35/35 |
| 15 | `NONE` | 7/7 |

This was recomputed from all criterion-C outputs (Verification V2). The metadata confirms
that constant output passes by design, for example family 09
(`dataset/family_09_clique_independent_set/criterion_3_infeasible/meta.yaml:31-35`) and family
15 (`dataset/family_15_lcs/criterion_3_infeasible/meta.yaml:36-39`).

Several statements also explain and print the answer:

- `r > n`, then "Print ... `NO`"
  (`dataset/family_09_clique_independent_set/criterion_3_infeasible/statement.md:7-20`);
- mutually disjoint alphabets, then "Print ... `NONE`"
  (`dataset/family_15_lcs/criterion_3_infeasible/statement.md:7-20`);
- one operation exceeds the deadline, then "Print ... `NO`"
  (`dataset/family_16_job_shop/criterion_3_infeasible/statement.md:9-22`).

**Consequence**

If a condition promises that every input is infeasible and the required output is only
`NO`, a constant program is correct by construction. Wording hardening cannot remove this
failure.

**Required action**

Choose one of two defensible designs:

1. **Feasibility-recognition track:** use one statement and mix feasible and infeasible
   hidden instances. The model must decide per instance; there is no all-NO criterion.
2. **Certificate track:** require a machine-checkable certificate, use the same certificate
   burden across paired conditions, and mix multiple hidden infeasibility mechanisms.

Report infeasibility as a promise/distribution condition, not a complexity class.

**Closure evidence**

A constant-output suite must fail. Hidden tests must cover multiple certificate mechanisms,
and the validator must verify the certificate from the input rather than compare a literal.

### B6. Test cases are conformance tests, not hardness tests

**Evidence**

- There are only 7--11 tests per criterion (Verification V1).
- All tests are static; evaluation discovers existing files and never generates a hidden
  post-submission input (`harness/evaluate.py:101-105,122-149`).
- 39 of 43 metadata `gen_command` entries hard-code `--seed 1` (Verification V3).
- SHA-256 grouping finds 23 exact duplicate-input groups covering 52/430 files
  (Verification V3).
- Vertex cover and dominating set share byte-identical NPC inputs; vertex cover, clique, and
  set cover share byte-identical P inputs (Verification V3).
- The executed program runs in the repository context with no isolated working directory
  (`harness/runner.py:36-54`), so code can read tests, references, and validators.

All 430 inputs do have outputs, and all references reproduce them under the 3,600-second
reference ceiling (Verification V6). That is useful integrity, but the check reruns the same
reference that generated the output (`harness/reference_check.py:50-75`). LCS even re-derives
the optimum with the same k-dimensional DP in its validator
(`dataset/family_15_lcs/criterion_1_npc/validator.py:12-30`).

**Consequence**

The suite can be passed by recognizing a few constructions, exploiting shared structure, or
overfitting visible data. Reference agreement proves self-consistency, not independent
correctness.

**Required action**

- Keep only examples and small conformance cases public.
- Generate scored inputs after model code is frozen, from secret seeds.
- Use multiple independent generators per family: random, structured, adversarial, hard
  YES, hard NO, near-threshold, planted, and distribution-shift.
- Deduplicate exact and near-duplicate inputs before splitting.
- Reserve a final generator family and seed range untouched by teachers, students, models,
  and benchmark designers during tuning.
- Validate every oracle with a second implementation or proof-producing solver; exhaustively
  cross-check small cases and use metamorphic tests at scale.

**Closure evidence**

Publish, after evaluation, a manifest containing generator commit, seed commitment, input
hash, distribution tag, oracle version, and split. Report uncertainty by independent
generator/seed cluster, not only aggregate pass rate.

### B7. Approximation scoring is broken end to end

**Evidence**

1. The intended policy exists in `prompt_suffix.md`
   (`studies/time_budget/prompt_suffix.md:1-6`), but generation constructs the prompt from
   only the statement (`harness/generate.py:184-203`).
2. The scorer expects `objective.py` (`studies/time_budget/scoring.py:30-38`), but the dataset
   contains zero such modules (Verification V1).
3. Evaluation discards actual stdout and passes checker diagnostics as produced output
   (`harness/evaluate.py:168-178`).
4. The scorer passes a directory name instead of the test input to an objective
   (`studies/time_budget/scoring.py:71-79`).
5. Aggregation has no score or ratio fields
   (`harness/aggregate.py:12-15,28-83`).

A controlled call reproduced the plumbing failure:

```text
score_case(criterion, "",   "NO", OK) -> exact=False, ratio=0.0
score_case(criterion, "NO", "NO", OK) -> exact=True,  ratio=1.0
```

The first form matches the effective PASS path because `cv.reason` is empty.

**Consequence**

Models are not told to approximate; no objective implementation exists; correct stdout does
not reach the scorer; and ratios cannot affect reported metrics.

**Required action**

Use optimization tasks with a verifiable candidate:

1. parse the candidate;
2. reject infeasible candidates;
3. recompute objective value from input and candidate;
4. compare against an independently proven optimum or bound;
5. aggregate feasibility, quality ratio, runtime, timeout rate, and anytime curve.

For decision/search tasks, use success over many hidden instances. Do not call a wrong
decision an approximation ratio.

**Closure evidence**

End-to-end tests must prove that the deadline appears in the actual prompt, exact and
non-optimal stdout reach the objective, infeasible witnesses score zero, a valid non-optimal
witness receives partial credit, TLE receives zero, and aggregate metrics reproduce case
scores.

### B8. Agentic hardening does not establish hardness

**Evidence**

The current 42 lineage files are all family 01, 14 per condition. No current lineage exists
for families 02--16 (Verification V8).

The loop retires a student after one defeat and later stops when too few active students
remain (`agentic/tools/harden_loop.py:719-772`). Retired students are retested and can regain
PASS, but are not reactivated. Recomputed results:

- zero depths defeat all four students simultaneously;
- zero depths have zero raw passers;
- five lineages are labeled `all_defeated`;
- every such final depth still has three raw passers;
- 32/42 lineages contain regressions;
- 87 depths restore at least one model, for 97 restoration events;
- 1,633/6,804 scaled case records are `PASS` above the declared limit.

See Verification V8.

Frontier results are also evaluated without task deadlines. GPT-5.6 Sol solves 41/42 final
statements and Gemini 3.7 Flash solves 40/42. All three unsolved pairs fail by wrong answer,
not timeout; one solved Gemini case takes 919.175 seconds on a 2-second problem
(Verification V9).

**Consequence**

The stored outcomes do not show simultaneous panel defeat, deadline hardness, or
generalization beyond one family.

**Required action**

- Determine defeat from the current raw panel, not cumulative retirement.
- Stop only on simultaneous current-panel failure, or reactivate a model that regains PASS.
- Use the task deadline for scientific pass/fail; run eventual-correctness diagnostics
  separately.
- Harden instances and generators, not only prose.
- Freeze development models and versions; evaluate untouched frontier models only after the
  statement and generator are frozen.
- Expand to all families before reporting benchmark-level results.

**Closure evidence**

Unit tests must simulate fail-then-pass regression and prove the model is active again. A
lineage may be called defeated only when its final raw panel has zero passers within the
declared limit. Reports must be regenerated from one immutable run ID.

### B9. Results are stale and irreproducible

**Evidence**

Current criteria contain 7--11 tests and 430 inputs. The retained summary contains 144 rows
but records only 2--5 tests per row (Verification V7). It therefore predates the current
suite.

The summary says `gpt-oss-20b` passed all 16 NPC rows, but:

- the run used the 600-second override;
- no `solution.py`, `raw.txt`, `gen_meta.json`, or raw `verdict.json` remains;
- `.gitignore` explicitly excludes generations and raw results
  (`.gitignore:11-14`);
- the documented seed is recorded but not used
  (`harness/generate.py:6-11,101-108`);
- model identifiers include mutable tags
  (`models/registry.yaml:38-53`);
- dependencies have lower bounds and omit `litellm`, although agentic code imports it
  (`requirements.txt:1-9`; `agentic/tools/backends.py:132-141`).

The shipped `test_gate_bounds.py` still fails at import with
`ModuleNotFoundError: litellm` (Verification V6).

**Consequence**

The headline result cannot be re-evaluated for algorithm, extraction, timeout, checking, or
current-test correctness.

**Required action**

Store immutable run artifacts: archive/test hashes, prompt text/hash, exact model provider
and revision, decoding settings, dependency lock, container digest, CPU/OS, generated text,
extracted code, stdout/stderr, resource measurements, per-case verdict, and aggregate
derivation.

**Closure evidence**

A clean environment must reproduce every published summary row from raw artifacts with one
command. The reproduction must fail on any hash or schema mismatch.

### B10. Generated code is not sandboxed

**Evidence**

`runner.py` invokes `python3 solution_path` with inherited filesystem, environment, working
directory, and network. It has no process namespace, filesystem isolation, environment
scrubbing, output cap, or process-group kill (`harness/runner.py:19-83`). The memory rlimit
is best effort and silently ignores failure (`harness/runner.py:19-33`).

**Consequence**

Generated code can inspect benchmark answers or secrets, access the network, emit unbounded
captured output, or leave descendants. This is both a host-security and benchmark-integrity
failure.

**Required action**

Run every submission in an ephemeral container or VM with:

- no repository or answer-key mount;
- only the current input and executable interface;
- no network or secrets;
- read-only runtime plus bounded scratch space;
- CPU, wall, memory, process, file, and output limits;
- process-group termination;
- fixed interpreter/compiler image.

**Closure evidence**

Adversarial integration tests must fail to read another test, reference, environment secret,
or network endpoint; forked children must die at timeout; oversized output must be capped.

## Per-family correction map

This table identifies the first concrete redesign needed in each family. It is not a claim
that a single listed change is sufficient; every family must also pass the common hidden-test
and solver-portfolio gates.

| Family | Verified breakability/confound | First correction |
|---:|---|---|
| 01 Coloring | Forward checking is recorded sub-second, while reference generation takes 9--105 s (`dataset/family_01_graph_coloring/criterion_1_npc/meta.yaml:32-64`). | Keep one coloring output contract; calibrate hidden graphs against DSATUR, bitset B&B, and SAT; enforce 2 s. |
| 02 SAT | A and its baseline share DPLL+UP; A requires lexicographic minimum while B accepts any witness (`dataset/family_02_sat/criterion_1_npc/meta.yaml:13-18`; `dataset/family_02_sat/criterion_1_npc/statement.md:19-24`; `dataset/family_02_sat/criterion_2_p/statement.md:14-17`). | Use the same witness rule; mix hidden SAT/UNSAT generators and calibrate against modern SAT solvers. |
| 03 Hamiltonian | `n<=20` bitmask DP is the intended exact route; hard cases are mainly constructed NO instances and timeout-fallback-to-NO is acknowledged (`dataset/family_03_hamiltonian_path/criterion_1_npc/meta.yaml:13-49`). | Accept any valid path; add independently generated hard YES cases and scale past the bitmask-DP deadline. |
| 04 Subset sum | `n=36` is inside meet-in-the-middle range; hard NO cases use even values and odd target (`dataset/family_04_subset_sum/criterion_1_npc/meta.yaml:26-45`). | Scale the MITM half-space; reject parity/gcd/range-trivial cases; retain the otherwise strong same-schema A/B design. |
| 05 3D matching | A changes triples and `k` output rows into bipartite pairs and one vector in B; A reference misses 5 s (`dataset/family_05_three_dim_matching/criterion_1_npc/statement.md:19-28`; `dataset/family_05_three_dim_matching/criterion_2_p/statement.md:18-27`; Verification V5). | Preserve the hypergraph schema/output and introduce one tractable structural promise; use an independent exact oracle. |
| 06 Bin packing | The A gap is one symmetry cut and hard scaled cases are predominantly NO; B changes divisibility, objective, and schema (`dataset/family_06_bin_packing/criterion_1_npc/meta.yaml:13-49`; `dataset/family_06_bin_packing/criterion_2_p/statement.md:5-18`). | Use one indivisible optimization contract across conditions; diversify constructions and require quality scoring. |
| 07 Superstring | Held-Karp is intentionally capped at `k=16`, about 1 s (`dataset/family_07_shortest_common_superstring/criterion_1_npc/meta.yaml:13-43`). | Raise the true bitmask parameter beyond exact saturation; score feasible superstrings by length; keep `k` in all schemas. |
| 08 Vertex cover | FPT `2^k` remains fast; instances are repeated disjoint P3s, and A/B change decision+witness to optimum size (`dataset/family_08_vertex_cover/criterion_1_npc/meta.yaml:13-46`; `dataset/family_08_vertex_cover/criterion_2_p/statement.md:7-20`). | Increase `k`, diversify graph families, and use minimum-cover witness output in both general and bipartite conditions. |
| 09 Clique | Bitset B&B is recorded at 0.01 s; C prints constant `NO` (`dataset/family_09_clique_independent_set/criterion_1_npc/meta.yaml:13-44`; `dataset/family_09_clique_independent_set/criterion_3_infeasible/statement.md:15-20`). | Calibrate against maximum-clique solvers and keep the clique objective/output across all conditions. |
| 10 Dominating set | Instances reuse unique-center P3 constructions and exact inputs from family 08 (`dataset/family_10_dominating_set/criterion_1_npc/meta.yaml:13-42`; Verification V3). | Use independent graph generators, raise the real branch parameter, and preserve a minimum dominating-set objective. |
| 11 Set cover | Universe `u<=20` leaves at most `2^20` masks while decoy consultants increase `s` (`dataset/family_11_set_cover/criterion_1_npc/meta.yaml:13-45`). | Raise and vary `u`, diversify set systems, and keep minimum set-cover output across conditions. |
| 12 Knapsack | MITM is capped at `n=36`; B changes 0/1 selection into fractional knapsack and C is constant `NO` (`dataset/family_12_knapsack/criterion_1_npc/meta.yaml:13-41`; `dataset/family_12_knapsack/criterion_2_p/statement.md:5-18`; `dataset/family_12_knapsack/criterion_3_infeasible/meta.yaml:30-32`). | Use one 0/1 objective/witness contract; choose a genuine tractable promise and score value on larger hard cases. |
| 13 Partition | MITM is capped at `n=38`; hard NO instances have an immediate parity proof; P reference misses 2 s (`dataset/family_13_partition/criterion_1_npc/meta.yaml:13-48`; Verification V5). | Remove parity-trivial hard cases, increase the exact half-space, and require a comfortable P-reference timing margin. |
| 14 Steiner | Terminals stay `t<=10`, so `3^t` remains small; B changes to all vertices (`dataset/family_14_steiner_tree/criterion_1_npc/meta.yaml:13-42`; `dataset/family_14_steiner_tree/criterion_2_p/statement.md:5-19`). | Raise `t`; keep terminal schema; use a tractable structural promise such as tree topology without changing the objective. |
| 15 LCS | `k<=5` makes stated `O(L^k)` polynomial in `L`; C prints constant `NONE` (`dataset/family_15_lcs/criterion_1_npc/meta.yaml:13-46`; `dataset/family_15_lcs/criterion_3_infeasible/statement.md:15-20`). | Make `k` variable in the hard arm, preserve schema, and score any valid common subsequence by length. |
| 16 Job shop | Metadata explicitly says the gap is unreliable and only one hunted seed separates solvers (`dataset/family_16_job_shop/criterion_1_npc/meta.yaml:13-46`). | Rebuild with CP-SAT/SAT-backed calibration and a same-schema tractable promise, or remove the family. |

## Ordered repair plan

### P0. Restore measurement validity

1. Enforce declared limits everywhere.
2. Repair stdout/input/objective/aggregation for approximation.
3. Replace cumulative retirement with simultaneous current-panel defeat.
4. Sandbox generated code.
5. Preserve raw immutable artifacts and lock dependencies.

**Evidence required:** deadline conformance tests, approximation integration tests, hardening
regression tests, sandbox escape tests, and one fully reproducible dry run.

### P1. Repair the research construct

1. Rename the conditions `GENERAL_HARD`, `TRACTABLE_PROMISE`, and
   `INFEASIBILITY_DIAGNOSIS`.
2. Record task type separately: decision, search, optimization, or canonical output.
3. Build same-schema/same-objective pairs with one documented complexity switch.
4. Remove canonical output unless canonicalization is itself the target.
5. Replace all-NO tasks with mixed feasibility or validated certificate tasks.

**Evidence required:** machine-readable pair manifests, automatic schema-diff results, and a
human proof sketch for each promise and algorithmic consequence.

### P2. Rebuild tests and hardness

1. Create multiple hidden generators per family.
2. Scale the controlling parameter of the strongest exact algorithm.
3. Calibrate against competent exact, solver-backed, heuristic, and approximation baselines.
4. Use independent/proof-producing oracles.
5. Reserve untouched generators, seeds, and models for final evaluation.

**Evidence required:** baseline matrix, generator/seed manifest, oracle agreement report,
shortcut audit, duplicate/near-duplicate audit, and target-machine runtime profiles.

### P3. Run a sealed SOTA-resistant evaluation

1. Freeze statements, generators, scoring, container, and development model panel.
2. Pre-register a non-saturation difficulty band for development models.
3. Generate final tests only after code generation.
4. Run held-out models once; do not tune on their outcome.
5. Report per-distribution confidence intervals, feasibility, quality, runtime, and timeout
   rates, not only pass@1.

**Evidence required:** signed/frozen manifest, held-out split commitment, raw artifacts, and
an independently reproduced report.

No finite benchmark can guarantee that future SOTA models will not solve it. The defensible
goal is narrower: demonstrate that the frozen hidden distribution resists a specified
contemporary solver/model portfolio under an actually enforced resource budget while still
providing meaningful partial-score separation.

## Release acceptance gates

Do not use a revised release for research claims until all gates pass:

1. No evaluation path expands a declared task limit.
2. No `PASS` exceeds the effective limit.
3. Every optimization criterion has a tested feasibility parser and objective evaluator.
4. Exact, partial, malformed, infeasible, runtime-error, and TLE cases are covered end to end.
5. Every pair preserves schema, objective, and output burden except for one approved switch.
6. No criterion is called NP-complete solely from a related task or variable-parameter form.
7. A constant output cannot pass an infeasibility condition.
8. Hidden tests are generated after code freeze from multiple held-out distributions.
9. Exact and near-duplicate leakage across splits is zero.
10. Two independent or proof-producing oracles agree on every scored case.
11. Hard tiers are calibrated against optimized exact and heuristic portfolios.
12. P tiers pass with a pre-registered timing margin on the target environment.
13. Hardening requires zero current-panel passers within the declared limit.
14. Final models, generators, and seeds are untouched by development.
15. Raw artifacts reproduce every reported number.
16. Generated code passes sandbox-isolation tests.

## Positive assets to preserve

- The 16-family/48-criterion directory layout is consistent.
- All 430 inputs have outputs.
- The dataset includes 17 custom validators for witness-bearing outputs.
- Metadata documents generators, scaling intent, baseline timings, and known weaknesses in
  unusual detail.
- Several hard arms mix YES and NO instances.
- Family 16 candidly records that its separation failed.
- Teacher, verifier, student, and frontier roles are separated in configuration.

These are strong foundations for a rebuild, but they do not offset the release blockers.

## Verification log

### V1. Archive and inventory

Recomputed from the ZIP and extracted tree:

```text
SHA-256: 70b3478452d905638b5d8086322a0c0cb0d4e121b83c3ba42032422c1edc606f
ZIP revision: 67f92cecb59e1e02a067a09dd81b57467625829e
families: 16
criteria/references: 48/48
input/output files: 430/430
custom validators: 17
objective.py files: 0
declared limits: 1, 2, 5 seconds
tests per criterion: 7 (13), 8 (2), 9 (8), 10 (24), 11 (1)
tests by label: NPC 158, P 156, INFEASIBLE 116
```

### V2. Infeasible output diversity

Normalized every criterion-C `.out` file. Families 04, 09, 12, 13, and 16 each have one
unique output, `NO`, over seven tests. Family 15 has one unique output, `NONE`, over seven
tests. The remaining ten infeasible criteria have multiple certificate outputs.

### V3. Static-generator and duplication audit

Parsed all metadata and SHA-256 grouped all inputs:

```text
metadata gen_command entries: 43
gen_command entries containing literal --seed 1: 39
exact duplicate-input groups: 23
files in duplicate groups: 52/430
```

Verified examples:

```text
f096e1d6893f49f96f508bbec11f75c7fb537f4905676315849bd7f16207a088
  dataset/family_08_vertex_cover/criterion_2_p/tests/08.in
  dataset/family_09_clique_independent_set/criterion_2_p/tests/08.in
  dataset/family_11_set_cover/criterion_2_p/tests/08.in

109007648ecbb56ffb88fa567cebb89f2b2b4fb5079696d5afd81a805083baf7
  dataset/family_08_vertex_cover/criterion_1_npc/tests/10.in
  dataset/family_10_dominating_set/criterion_1_npc/tests/10.in
```

### V4. Statement-pair comparison

Lowercased A/B statements, tokenized words/numbers/punctuation, and ran
`difflib.SequenceMatcher(autojunk=False)`:

```text
median A/B similarity: 0.651525
pairs below 0.70: 11/16
pairs above 0.90: family 04 subset sum, family 13 partition
```

This is descriptive corroboration, not a semantic proof; the schema/objective inspection is
the primary evidence.

### V5. Fresh strict-limit execution

On Apple M3 Pro, macOS 26.6.2, Python 3.9.6, reran the highest-numbered available test of
every reference and designated naive solver with each criterion's declared wall-clock and
memory limit:

```text
reference: OK 42, TLE 6
designated naive: TLE 48

reference TLE:
  family 01 coloring A
  family 02 SAT A
  family 03 Hamiltonian A
  family 05 3D matching A
  family 13 partition B
  family 16 job shop A
```

### V6. Integrity and executable checks

```text
all 16 family-level harness.reference_check runs: PASS
python3 -m compileall -q harness agentic/tools tools dataset: PASS
agentic/tools/test_gate_bounds.py: FAIL before tests
failure: ModuleNotFoundError: No module named 'litellm'
```

Reference checks use the repository's 3,600-second override and therefore establish output
self-consistency, not submitted-solution timing.

### V7. Retained main results

Parsed `runs/2026-07-01_main/results/summary.csv` and run directories:

```text
summary rows: 144
recorded tests per row: 2--5
current tests per criterion: 7--11
gpt-oss-20b NPC rows marked PASS: 16/16
generation/raw/verdict artifacts retained: 0
```

### V8. Hardening lineages

Parsed all 42 current `lineage.json` files:

```text
coverage: family 01 only; 14 lineages per condition
outcomes: exhausted 22, max_depth 15, all_defeated 5
depths with all four raw-defeated: 0
depths with zero raw-passers: 0
false all_defeated final raw-passers: 3 in each of 5 lineages
lineages with regressions: 32/42
regression depths: 87
restored-model events: 97
scaled case records with limit and elapsed time: 6,804
PASS records above declared limit: 1,633
maximum over-limit PASS: 283.024 s on a 2 s task
```

### V9. Frontier results

Parsed all 84 current frontier `result.json` files:

```text
coverage: family 01 only; 42 statements x 2 evaluators
GPT-5.6 Sol: NPC 13/14, P 14/14, infeasible 14/14
Gemini 3.7 Flash: NPC 12/14, P 14/14, infeasible 14/14
unsolved pairs: 3, all containing WRONG_ANSWER
maximum accepted case runtime: 919.175 s
```

## Final conclusion

The current dataset is too easy for strong coder models for identifiable, verified reasons:
resource limits are expanded, exact parameters are capped, baselines are weak, statements
expose shortcuts, tests are static and correlated, and approximation is not actually scored.

The correct remedy is not more wording hardening. It is a rebuild around:

1. one enforced resource contract;
2. same-schema paired tasks;
3. hidden multi-distribution instance generation;
4. strong exact/heuristic baseline calibration;
5. independent oracles;
6. valid objective-based partial scoring;
7. sealed held-out evaluation with reproducible raw artifacts.

Until those gates pass, model pass rates from this repository should be treated as prototype
debugging results, not evidence about complexity awareness.

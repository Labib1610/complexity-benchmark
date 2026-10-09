# AgentGAN — Complexity-Class-Aware Benchmark: Full Workflow & Methodology

*Living design document for the paper. Describes the project, the agentic pipeline, and every
component in detail. **No experimental results here** — results are added after the runs.*

Last updated: 2026-09-11.

---

## 1. Motivation & Core Idea

**The capability claim.** Recognising the *computational complexity class* of a problem — and
choosing an algorithm appropriate to it — is a genuine reasoning capability, distinct from pattern-
matching a textbook problem to a memorised solution. A model that truly "understands" a task should:
(a) solve a **P** problem efficiently, (b) recognise an **NP-complete (NPC)** problem and not waste
effort trying to beat its intractability, and (c) not be fooled when the *surface* of a problem is
disguised to look like the other class.

**The gap.** Existing code/reasoning benchmarks do not **control the complexity class while holding
the problem surface (the seed) fixed**. They also saturate: strong models pass because the problems
are common (memorised). Nothing measures whether a model tracks the class rather than the phrasing.

**Our approach — AgentGAN.** A GAN-style *adversarial, evolving* benchmark generator. A **teacher**
(generator) rewrites a fixed **seed** problem into many **variants** that preserve the ground-truth
answer and complexity class but strip the surface cues a model uses to recall the textbook solution.
A **student panel** provides the discriminator signal (which variants they still solve). A **validity
gate** guarantees each variant is still a well-posed, solvable, faithful instance. A **hardening loop**
iterates: each variant becomes a *lineage* that is re-edited against live student behaviour until the
students fail — surfacing the point at which surface manipulation, and then genuine instance hardness,
defeats the model.

**Contributions (itemised for the paper):**
1. A framework (AgentGAN) that hardens a benchmark adversarially while a **validity gate** keeps every
   generated instance well-posed, faithful, and solvable (executable checks + LLM-judged criteria).
2. A **complexity-class-controlled** dataset: for each seed family, matched **P** and **NPC** variants
   with class-disguise edits, so accuracy can be measured *per class* on the *same surface*.
3. A **hardening loop with agentic memory and a fallback ladder**, plus an **instance-hardness /
   worst-case tier** that pushes NPC problems into the regime where they must raise **TLE** (the
   intractability signal) — while remaining gradeable via cheap witnesses.
4. **Transfer to a held-out model** never seen by the pipeline, showing the task (not one model's
   quirk) was hardened; plus a **directional asymmetry** analysis (P→NPC vs NPC→P).

---

## 2. Problem Formulation

- **Seed** `s`: an original, well-formed competitive-programming-style problem for a family (statement +
  reference solver + test cases + metadata). Version id `v000` is always the untouched seed.
- **Criteria (classes) per seed.** Each family ships parallel *criteria* that pose the family's task
  under a controlled complexity class:
  - `criterion_1_npc` — the **NP-complete** decision/search form.
  - `criterion_2_p`   — a **polynomial** relative of the same surface (e.g., 2-colouring vs 3-colouring).
  - `criterion_3_infeasible` — *(DROPPED 2026-09-11; see §11)* a certificate-of-impossibility form.
- **Variant** `v` of a criterion: a teacher-rewritten statement that **preserves the answer and the
  class** but changes the surface. `v_P` / `v_NPC` denote variants of the P / NPC criteria.
- **Edit operator** (a *strategy* `S01…S12`, at an *intensity* light/moderate/aggressive): the
  transformation the teacher applies to produce a variant (see §4.2). Composition applies compatible
  pairs together.
- **Hardening depth** `d`: within a lineage, `d=0` is the base variant; each increment re-edits the
  previous statement against the students that still pass.
- **What the teacher optimises:** maximise the number of panel students that FAIL the variant, subject
  to the gate accepting it.
- **What the teacher is forbidden from doing** (enforced by the gate, §3.3): changing the answer,
  changing the complexity class, dropping/altering numeric bounds or tie-break rules, leaking the class
  name / algorithm name, or producing an ill-posed/unsolvable statement.

---

## 3. The AgentGAN Framework

Pipeline driver: `run_agentic_family01.sh` (family-parameterised via `FAM=NN`). Eight stages:
1. `generate_versions` (sources: grid, sample, composition) → 2. `gate` → 3. `generate_versions`
(source: generation, derives from accepted variants) → 4. `gate` → 5. `gen_tests` (adversarial corner
cases) → 6. `run_students` (baseline attempts) → 7. `harden_loop` (lineage/depth) → 8. `reports`.
All stages are **checkpointed and resumable** (existing `verdict.json` / `gate.json` / `progress.json`
are skipped); nothing is deleted (`stop_on_gate_fail: false`).

### 3.1 Teacher (Generator) Agent
- Model: **gemini-3.1-pro** (`temperature 0.7` for variant diversity, `max_tokens 32768`).
- Input: seed statement + the chosen strategy/intensity + (in the loop) the agentic memory block and
  the observed student shortcut. Output: a tag-delimited rewrite (`<STATEMENT>…</STATEMENT>` plus
  rationale/preserved-answer/preserved-class/risk tags) — tag-delimited, not JSON, for robust multi-line
  markdown parsing with truncation salvage.
- The teacher is the **sole author** of final statement text. It never grades and never validates.
- `versions_per_criterion` (target 40) is filled by a **planner** from four sources in priority order
  (`strategies/PLAN.md`): (1) **grid** — every applicable (strategy, intensity) cell, one sample;
  (2) **sample** — extra distinct sub-seed draws from used cells; (3) **composition** — compatible
  strategy pairs applied together (moderate/aggressive); (4) **generation** — derive a new variant from
  an already-**accepted** variant (a second pass; capped by `max_generation`).

### 3.2 Student Panel (Discriminator Signal)
- The panel are the models we harden *against*; their pass/fail on each variant is the GAN discriminator
  signal. Identical decoding across the panel (`temperature 0.0, top_p 1.0, max_tokens 32768`) so
  differences are attributable to the model, not sampling.
- Current panel (OpenRouter): **deepseek-v4-flash, gpt-oss-120b, qwen3-coder, glm-5**
  (kimi-k2.7-code is a staged/disabled alternate). Some models mandate reasoning tokens; those are
  capped (`reasoning: {max_tokens: 4000, exclude: true}`) so code still fits in the budget.
- A student is **excluded from a variant's baseline** if it already fails the *unmodified seed*
  (`skip_students_failing_seed: true`) — we only harden against students the seed didn't already defeat.
- Grading uses `harness.checker.judge_problem` against the criterion's test tiers (§4.3). Verdicts:
  `PASS / WRONG_ANSWER / RUNTIME_ERROR / TLE / MLE`.

### 3.3 Validity Gate
Two independent parts — **hard constraints** (binary, fatal) and **graded criteria** (0–5, thresholded).
They measure different things and are never merged. Source: `agentic/tools/gate.py`.

**Hard constraints (H*, executed where noted):**
- **H1 example consistency** — run `reference.py` on each example input embedded in the rewritten
  statement; its output must match the stated example output. *Executed.*
- **H2 I/O contract** — Input/Output sections present; every numeric bound and any tie-break rule
  matches the seed (bounds compared numerically). *(This is the check that flagged the empty 429
  statements — no I/O section, bounds dropped.)*
- **H3 no class leakage** — deterministic forbidden-term scan (no "NP-complete", algorithm names, etc.).
- **H4 S09 constraint** — only when strategy S09 (added non-binding constraints) was used: evaluate the
  teacher's formal constraint against every seed test input; any violation → fail. *Executed.*
- **H5 solver round-trip** — hand the rewrite to a **strong solver model NOT in the student panel**; its
  solution must pass the seed's **anchor+corner** tests. *Executed.* Solver: **gemini-3.1-flash-lite**
  (cheap, non-reasoning — a reasoning model wastes its budget "thinking" about a 4-node graph).
  This is the check that keeps a variant **solvable** (raises the difficulty ceiling without breaking
  gradeability).

**Graded criteria (G1–G4, verifier at temperature 0, each with a one-sentence justification):**
- **G1 unambiguity · G2 completeness · G3 faithfulness · G4 naturalness.**
- Verifier: **gpt-5.6-luna** on the OpenAI API — deliberately a **different provider than the teacher**
  (Gemini) to avoid self-enhancement bias.

**Acceptance / selection:**
- `ACCEPT` iff all H pass **AND** `G1≥4 AND G2≥4 AND G3≥5 AND G4≥3`.
- `FLAG` if hard checks pass but a graded score is exactly one below threshold (or a hard check couldn't
  be verified). `REJECT` otherwise.
- **Composite (for selection among accepted candidates):** `0.40·G3 + 0.30·G1 + 0.20·G2 + 0.10·G4`.

### 3.4 Agentic Memory & Hardening Loop
Source: `agentic/tools/harden_loop.py`. Each selected base version becomes a **lineage** hardened
iteratively against live student behaviour.

Per lineage, at each depth `d`:
1. Run **all** students on the current statement (retired ones re-run to confirm continued defeat).
2. Active passers = still-active students that passed. If none → `all_defeated`.
3. The **verifier** summarises the single shared **shortcut** the passers exploited, flagging whether
   it is *mutable* (rewordable away) or a **structural floor** (the shortcut *is* the task and cannot be
   hidden by wording).
4. **Edit** via a **fallback ladder** — `[S12_primary → S12_secondary → S07 → S02_aggressive]` — each
   candidate gate-validated; the highest-composite ACCEPTED candidate is kept
   (`candidates_per_depth: 2`).
5. Failed active students are **retired** (still re-tested each depth, but no longer steer the teacher).
6. `depth += 1`, up to `max_depth: 10`.

- **Agentic memory** (`memory.json` per lineage, aggregated into `criterion_memory.json`): depth history,
  which strategies newly defeated/regressed which students, dead-ends, and per-student profiles
  (`resistant_to`, `defeated_by`, `never_defeated_by_depth`). A capped **memory block**
  (`memory_block_max_tokens: 1500`) is fed back to the teacher so it doesn't repeat dead-ends.
- **Aggressive mode** from `aggressive_from_depth: 3` once the strategy library is exhausted; requires
  the teacher to invent and name a novel method (persisted under `strategies/discovered/`).
- **Adversarial corner engine** (`adversarial_corner`): when rewording is exhausted (structural floor),
  pivot from surface attack to **instance attack** — generate candidate inputs (`candidate_pool: 40`),
  keep the `cases_per_survivor: 4` that break survivors via differential testing.
- **Defeat definition** (`hardening_target: wrong_or_slow`): a student is defeated on
  `WRONG_ANSWER / RUNTIME_ERROR / MLE` **or** on **TLE** beyond `tle_ceiling_s: 300` (the NP-hard
  intractability signal — a correct-but-exponential solution that cannot finish in time is defeated).
  `elapsed_s` is always recorded.
- **Lineage normalisation:** `target_lineages: 14` fixes the lineage count per criterion across families
  for comparability (`top_k: 10` hardest by student-delta + `include_random: 4`, topped up randomly if
  the ranking under-fills). Lineages are independent → run `lineage_workers: 4` concurrently.

### 3.5 Expert Co-Author (Double Authoring / 3-Way Negotiation)
- Model: **gpt-5.3-codex** (OpenAI), `invoke_when: on_reject`.
- When the gate **rejects** a teacher draft, the expert **critiques** it and proposes concrete
  alternatives; the teacher then revises (`gate_negotiation_rounds: 4`, full transcript persisted to
  `negotiation.json`). The expert **never writes final statement text** (teacher is sole author) and
  **never validates** (that is the gate).
- **Role separation is enforced in code:** the expert must not be the teacher, the verifier, the H5
  solver, any student, or the held-out model (and must be a different provider than the teacher).

---

## 4. The P↔NP-Hardened Dataset

### 4.1 Seed Problem Families
16 families (each with matched NPC + P criteria), spanning classic and uncommon NP-complete problems:
`01 graph_coloring · 02 sat · 03 hamiltonian_path · 04 subset_sum · 05 three_dim_matching ·
06 bin_packing · 07 shortest_common_superstring · 08 vertex_cover · 09 clique_independent_set ·
10 dominating_set · 11 set_cover · 12 knapsack · 13 partition · 14 steiner_tree · 15 lcs · 16 job_shop`.
Each family: `statement.md`, `reference.py` (ground-truth solver), `tests/`, `meta.yaml` (declares the
`class`, judge type, time/memory limits). Seeds live in `agentic/seeds/…` (working copy for the pipeline)
and `dataset/…` (release copy).

### 4.2 Class-Flipping / Class-Disguise Edits
Twelve strategies (`strategies/`, applied at light/moderate/aggressive intensity):
- **S01** remove textbook-recall wording · **S02** same structure, new real-world scenario ·
  **S03** describe special structure by mechanics, never by name · **S04** make a *hard* problem look
  like it has an easy shortcut · **S05** make an *easy* problem look like it needs heavy machinery ·
  **S06** hide the reason no solution exists · **S07** state bounds indirectly (reader must derive) ·
  **S08** embed in a scenario where every detail is load-bearing · **S09** add true non-binding
  constraints (answer-preserving) · **S10** present the task as one step in a larger workflow ·
  **S11** reorder so the objective arrives after the constraints · **S12** attack the specific shortcut
  seen in student reasoning traces (the loop's primary lever; `S12_primary/secondary`).
- **Bidirectional class disguise:** S04 disguises NPC-as-easy; S05 disguises P-as-hard. Example pair
  (graph colouring): NPC criterion = 3-colouring ("assign 3 shifts so no conflicting pair shares one");
  P criterion = 2-colouring ("two shifts") — same surface, one is intractable, one is BFS-polynomial.
  The point is whether the model tracks the class through the disguise.

### 4.3 Ground-Truth and Test Cases (three tiers)
Every criterion is graded on separately-scored tiers (`scoring_tier: all` requires all to pass):
- **anchor** — the small seed cases `01–04` (trivial; sanity/base).
- **corner** — generated adversarial edge cases (`gen_tests`, `agentic/tests/…`, prefixed `u*`/`adv_*`).
- **scaled / worst-case** — large or near-threshold instances that force the **intractability (TLE)**
  signal for NPC (see §4.4). Tiers are always scored and recorded separately.

Judging: `judge: exact` (match reference `.out`) or `judge: custom` (a `validator.py`, e.g. witness
verification for colouring). Ground truth is produced by the family's `reference.py`; where the exact
optimum is NP-hard to certify at scale, grading uses **witness verification** instead (see §4.4).

### 4.4 Instance-Hardness / Worst-Case Tier (the TLE lever)
Surface hardening (rewording) plateaus at the **structural floor**: once the model recognises the task,
no phrasing hides it. Genuine NPC difficulty therefore comes from **instances**, not words. The
worst-case tier plants **near-threshold** instances that are hard to *find* a solution for but whose
answer is verifiable by a **cheap witness**, so grading needs no reference solve — escaping the
"gradeable ceiling" (a gradeable NPC case must be solvable by the reference to make the key, so it can
never be hard for an equally-good solver *unless* graded by witness).
- **Colouring (family 01):** planted 3-colourable graphs at edge ratio ≈2.3 (the 3-colouring phase
  transition), `n` up to ~1200; grade = verify the model's colouring (`tools/worstcase_coloring.py`).
  Near-threshold + large `n` ⇒ search TLEs though a witness exists.
- **3-D matching (family 05):** plant a perfect matching + decoy triples; grade = verify the k triples
  (`tools/worstcase_3dm.py`). Confirmed SOTA-resistant TLE regime: **`k≥100` at ratio ≥6.0** — every
  current solver (incl. frontier gpt-5.6 & gemini) TLEs, while the planted witness guarantees a solution.
  NOTE: high ratio (not low) is the hard region — more triples/element ⇒ higher backtracking branching
  factor ⇒ search explodes though many matchings exist. Ratio ≈4 was in the *easy* (planted-CSP) region.
- **Key limitation (a reportable finding):** **optimisation** families (e.g., job-shop makespan) do
  **not** cheaply support a gradeable TLE worst-case tier — certifying the optimum is itself NP-hard
  (the reference TLEs at the same scale), and there is no cheap "hard-to-find but feasible" witness
  (perfect job-shop schedules are greedy-findable). Only families whose YES-answer has a **cheap witness
  for a hard-to-find solution** support the TLE tier (colouring, 3-D matching, subset-sum/partition/
  knapsack, vertex-cover/independent-set/clique, Hamiltonian). This is a per-family property worth
  reporting.
- For **P** criteria, the "worst case" is a **scale-stress** tier (large inputs): a correct polynomial
  solver always passes, so it only catches non-polynomial/naïve solutions — never SOTA-resistant (this
  is a definitional property of P, not a weakness of the method).

### 4.5 Dataset Statistics (to fill after runs)
Per family/criterion: #accepted variants, #lineages (14), depth-to-defeat distribution, #corner cases,
worst-case tier sizes, gate ACCEPT/FLAG/REJECT counts.

---

## 5. Experimental Setup

### 5.1 Models & Roles (all `openai_compat`; role separation enforced in code)
| Role | Model | Provider / notes |
|---|---|---|
| Teacher (generator) | gemini-3.1-pro | Gemini; temp 0.7 (diversity) |
| Verifier (graded gate) | gpt-5.6-luna | OpenAI; temp 0 (deterministic); ≠ teacher provider |
| Gate H5 solver | gemini-3.1-flash-lite | cheap non-reasoning; not a student/teacher/verifier/held-out |
| Student panel | deepseek-v4-flash, gpt-oss-120b, qwen3-coder, glm-5 | OpenRouter; temp 0 identical decoding |
| Expert co-author | gpt-5.3-codex | OpenAI; critiques on gate reject; never authors/validates |
| Held-out (transfer) | kimi-k3 | never seen by teacher/pipeline; run once at the end |
| Frontier evaluators | gpt-5.6-sol, gemini-3.7-flash-frontier | strong models outside the panel; independent assessment |

Budgets/decoding/timeouts/resumability: students/held-out `temp 0, top_p 1, max_tokens 32768`; reasoning
models send `reasoning_effort` instead of temperature. `execution`: `api_parallel: true`,
`api_max_workers: 4`, `request_timeout_s: 1800`, `retries: 3`. Every stage is checkpointed/resumable;
long runs are launched detached (`nohup … &`) and survive restarts. Secrets are read from
`agentic/config/local_secrets.py` / env; key *values* are never logged.

### 5.2 Metrics
- **Accuracy per class** (NPC vs P) per model, over the hardened variant pool ("test cases") and over
  the worst-case tier — reported **with vs without** the worst-case tier.
- **The gap metric** — per-model NPC↔P accuracy difference on the same surface.
- **Hardening depth-to-defeat** — the depth at which each lineage first defeats all students
  (`all_defeated_simultaneously`); shallow = the seed was already hard.
- **Transfer** — held-out model accuracy on final-depth statements (`held_out_check`, `scope:
  final_depth_only`).
- **Failure-type breakdown** — PASS / WRONG_ANSWER / RUNTIME_ERROR / **TLE** (the intractability share).

---

## 6. Analysis Dimensions (methodology; results later)
- **Failure taxonomy:** over-engineering P (heavy machinery on a polynomial task), under-engineering NPC
  (a heuristic/greedy that is wrong or times out), and — historically — confident-wrong on infeasible
  (now dropped). Distinguish **WRONG_ANSWER** (mis-recognised class / buggy solver) from **TLE**
  (correct approach, genuine intractability).
- **Directional asymmetry (uniquely ours):** do models fail more on P→NPC (disguised-hard) or NPC→P
  (disguised-easy)? Enabled by the matched criteria and S04/S05 disguises.
- **Ablations:** no gate / no memory / no aggressive mode / single-direction edits only / no worst-case
  tier — to isolate each component's contribution to the hardening drop.
- **Validity-gate reliability:** ACCEPT/FLAG/REJECT rates, hard-check catch rate (e.g., it correctly
  rejected the empty 429-truncated statements), and verifier agreement with human spot-checks
  (`tools/judge_agreement.py`, `tools/human_annotation.py`).

---

## 7. Directory Map (where things live)
```
dataset/family_NN_*/criterion_{1_npc,2_p}/    release seeds (statement, reference, tests, meta, validator)
agentic/seeds/…                               pipeline working copy of the seeds
agentic/versions/family_NN/criterion_*/vNNN/  teacher variants (statement.md, edit.json, gate.json)
agentic/attempts/family_NN/criterion_*/vNNN/<model>/  student solutions + verdict.json
agentic/lineages/family_NN/criterion_*/L*/    hardening lineages (plan.json, per-depth statements, memory)
agentic/tests/family_NN/criterion_*/          generated corner cases (u*/adv_*)
agentic/strategies/                           S01–S12 catalogue + discovered methods + PLAN.md
agentic/reports/                              per-family summary/lineage CSVs
agentic/config/{run_config.yaml,models.yaml,local_secrets.py}   all knobs & model roles
tools/worstcase_*.py                          witness generators+graders for the worst-case tiers
run_agentic_family01.sh                       8-stage driver (FAM=NN)
```

---

## 8. Key Design Decisions & Findings (workflow-level, for the paper's rationale)
- **Verifier ≠ teacher provider** (self-enhancement bias); **H5 solver is cheap & non-reasoning**
  (reasoning models waste budget on trivial anchor tests); **held-out has zero prior pipeline contact**
  (valid transfer); **expert critiques but never authors/validates** (clean role separation).
- **Surface hardening plateaus (structural floor); instance hardening (worst-case) is the real NPC
  lever** — and only witness-gradeable families support a TLE tier.
- **Seeds are the bottleneck:** common/memorised families have ~0% seed failure; **uncommon families
  carry real seed difficulty** and respond to hardening. Seed *selection/difficulty* dominates the
  teacher-student pipeline's ability to raise the failure rate.
- **Fixed 14 lineages/family** for cross-family comparability.

---

## 8b. Dataset Packaging (TODO — release organization)
Once a family's runs are done, its artifacts (currently scattered across `agentic/versions`,
`agentic/lineages`, `agentic/tests`, `dataset/`, `tools/worstcase_*`) must be consolidated into a clean,
released dataset layout. Proposed structure (to build with an automated packager):
```
dataset_release/family_NN_<slug>/criterion_{1_npc,2_p}/
    statement_seed.md                      # v000 base statement
    statements/{vNNN.md, lineage_L*_d*.md} # the accepted hardened statements (+ provenance)
    reference.py  validator.py  meta.yaml  # ground-truth solver + judge + limits
    tests/anchor/    (4 base cases)        # the three test tiers, EQUAL fixed sizes across families
    tests/scaled/    (>100/>200)
    tests/worstcase/ (near-threshold, witness-graded, size == hardening size)
    solutions/<model>/{vNNN.py, verdict.json}   # student + frontier solutions, per statement
    MANIFEST.json                          # counts, tier sizes, provenance, gate results
```
Requirements: every statement paired with its ground-truth + tests + all model solutions/verdicts;
tiers equal-sized and fixed across families; fully reproducible provenance (which strategy/depth
produced each statement). Builder script is pending.

## 9. Reproducibility / How to Run
```bash
# full pipeline for one family (NN)
FAM=NN nohup bash run_agentic_family01.sh > agentic/logs/pipeline_family_NN.log 2>&1 &
# resume an interrupted hardening stage
python agentic/tools/harden_loop.py --family NN --resume
# held-out transfer (after the campaign)   |   frontier eval over variants
python agentic/tools/frontier_eval.py --family NN --depths all
FAM=NN python run_frontier_variants.py
```

---

## 10. Related Work (threads to develop)
(a) **Adversarial / evolving benchmarks** — dynamic and contamination-resistant benchmark generation,
GAN-style data generation, self-play. (b) **Complexity-aware code generation** — reasoning about
algorithmic complexity, hardness-aware evaluation, and program synthesis under resource limits.

---

## 11. Change Log
- **2026-09-11 — Infeasible criterion dropped.** `criterion_3_infeasible` was non-discriminating
  (always ~100%; hardening ran to `max_depth` and never defeated any student because impossibility
  certificates are trivially findable). All active infeasible artifacts moved to
  `_archive_infeasible_dropped_20260911/` (restorable, paths preserved); `run_config.criteria: [1,2]`;
  tool CLI `choices` and defaults changed `[1,2,3]→[1,2]`. INFEASIBLE class-handling code left intact
  (dead code, harmless). The pipeline now hardens **NPC (1)** and **P (2)** only.
- **2026-09-11 — Lineage count normalised** to a fixed 14 per criterion (`target_lineages`).
- **2026-09-11 — Seed-failing students no longer dropped** (`skip_students_failing_seed: false`): keep
  every student's feedback even where it fails the unmodified seed (e.g. gpt-oss on job-shop). Lineage
  seed selection remains hardest-first (biggest student-drop), now computed over the full panel.
- **2026-09-11 — Equal-weight tier scheme:** hardening tier (anchor 4 + corner 12 = 16) and the
  worst-case tier are held to the SAME fixed size (16) across all families, so the combined score
  weights them 50/50. Reporting order: (1) anchor+scaled accuracy — a large NPC↔P gap = the seed
  hardened most; (2) add worst-case at equal weight; (3) worst-case as the model-dropping tier. The
  automated **scaled (>100/>200)** tier builder is pending (project item #2).
- **2026-09 — Worst-case tiers** added (`tools/worstcase_coloring.py`, `tools/worstcase_3dm.py`); the
  optimisation-family limitation (job-shop) documented in §4.4.

# Final Evaluation Dataset — P↔NPC Complexity-Class Benchmark

This folder is the **release dataset** for complexity-class-awareness evaluation: **12 problem
families**, each posed under two controlled complexity classes on the *same problem surface* — an
**NP-complete (NPC)** criterion and a **polynomial (P)** relative. Every family was hardened by the
AgentGAN pipeline (a teacher rewrites the seed to strip textbook cues; a student panel + validity gate
drive iterative hardening) and probed with a worst-case tier.

## The 12 families

| Family | Problem | NPC / P | Worst-case | Tests | Tests kept |
|---|---|---|---|---|---|
| `family_01_graph_coloring` | Graph colouring | 3-colouring (NPC) / 2-colouring (P) | witness | 290 | curated |
| `family_02_sat` | Boolean satisfiability | 3-SAT (NPC) / 2-SAT (P) | witness | 32 | curated |
| `family_05_three_dim_matching` | 3-D matching | 3DM (NPC) / bipartite matching (P) | witness | 32 | curated |
| `family_09_clique_independent_set` | Independent set / clique | IS size k (NPC) / (P relative) | witness | 32 | curated |
| `family_14_steiner_tree` | Steiner tree | general (NPC) / trees (P) | scale | 48 | curated |
| `family_16_job_shop` | Job-shop scheduling | ≥2 machines (NPC) / (P) | scale | 55 | curated |
| `family_17_exact_cover` | Exact cover | X3C (NPC) / bipartite 2-set matching (P) | witness | 60 | all 30/crit |
| `family_18_linear_arrangement` | Minimum linear arrangement | general (NPC) / trees (P) | scale | 60 | all 30/crit |
| `family_19_multicommodity_flow` | Multicommodity flow | k-commodity integer (NPC) / max-flow (P) | scale | 60 | all 30/crit |
| `family_20_edge_colouring` | Edge colouring | 3-edge-colour cubic (NPC) / bipartite König (P) | witness | 60 | all 30/crit |
| `family_21_multiway_cut` | Multiway cut | ≥3 terminals (NPC) / s–t min-cut (P) | scale | 60 | all 30/crit |
| `family_22_precedence_scheduling` | Precedence scheduling | ≥2 machines (NPC) / single machine (P) | scale | 60 | all 30/crit |

**Worst-case column:** `witness` = a genuine SOTA-resistant TLE tier (a planted YES-instance with a
cheap-to-verify certificate that is hard to *find* — large instances time out even strong/frontier
solvers). `scale` = an optimization family where certifying the optimum is itself NP-hard, so the
worst-case is a scale-stress tier (breaks naïve/exact solvers, not heuristic ones — see per-family notes).

## Per-family folder layout
Each `family_NN_<slug>/` contains, for both criteria (`criterion_1_npc`, `criterion_2_p`):

```
family_NN_<slug>/
├── seed/<criterion>/
│     statement.md      the (hardened, disguised) problem statement — the base version v000
│     reference.py      ground-truth solver (reads stdin, writes stdout)
│     validator.py      judge: validate(input_text, output_text) -> (ok: bool, message: str)
│     meta.yaml         class (NPC/P), intended algorithm, reduction note, limits, tier info
├── tests/<criterion>/
│     *.in / *.out      the evaluation test cases (see "Test tiers" below)
├── versions/<criterion>/vNNN/
│     statement.md      a teacher-generated variant of the seed
│     edit.json         provenance: strategy, intensity, parent, teacher id, rationale
│     gate.json         validity-gate result (ACCEPT/FLAG/REJECT + hard checks H1–H5 + graded G1–G4)
├── attempts/<criterion>/vNNN/<model>/
│     solution.py       the model's code for that variant
│     verdict.json      per-case pass/fail + overall + tokens/cost/time
└── lineages/<criterion>/L*/
      lineage.json      the hardening chain (depth 0 = base variant … up to max depth)
      d000..dNN/        per-depth hardened statement + gate + student results
      memory.json       agentic memory (which strategies defeated which students)
      plan.json / criterion_memory.json   lineage plan + aggregated memory
```

Only **ACCEPT** and **FLAG** versions are included (REJECTs are dropped). Each kept version ships with the
full **attempt** set (every panel model's solution + verdict), so the dataset is self-contained for
re-grading and analysis.

## Test tiers (what's in `tests/`)
- **Obscure families (17–22):** the full **30-case** tier per criterion — `01–05` anchor (tiny),
  `06–15` scaled, `16–30` worst/near-threshold — all witness-graded.
- **Original families (01, 02, 05, 09, 14, 16):** curated for discrimination — trivially-passed small
  anchors are dropped; kept are the `corner_*` adversarial cases (generated to be hard), any `seed_*`
  case that at least one model failed, and the `worst_*` scaled/near-threshold instances where present.
  (family_01 additionally ships its large phase-transition worst-case tier, hence its high count.)

File naming in `tests/`: `NN.in/.out` (obscure tiers), `seed_NN.*` (kept seed cases),
`corner_NN.*` (adversarial cases), `worst_NN.*` (worst-case tier).

## How to grade a model output
For a test case `X.in`, run the model's program on it, then call the family's
`seed/<criterion>/validator.py:validate(input_text, model_stdout)` — it returns `(ok, message)`.
NPC criteria use **witness/certificate checking** (verify the model's answer, e.g. a colouring, a
matching, a satisfying assignment, a schedule) so grading is cheap even where solving is intractable.

## Provenance & scores
- `_manifest.json` — machine-readable per-family counts.
- Complexity of each variant is preserved (`edit.json` records the class-preserving transformation).
- The methodology is documented in `../agentic/WORKFLOW.md`; the run procedure in `../RUN_GUIDE.md`.

## Notes & honest caveats
- **Witness vs scale worst-case.** Only families whose YES-answer has a cheap witness for a *hard-to-find*
  solution admit a SOTA-resistant TLE tier (colouring, SAT, 3-D matching, exact cover, edge colouring,
  vertex-cover, dominating-set, set-cover, partition, independent-set). Pure optimization families
  (job-shop, Steiner, MinLA, multicommodity, multiway-cut, precedence, bin-packing, SCS, knapsack, LCS)
  cannot be cheaply graded at the intractable scale, so their worst-case is a scale-stress tier.
- **P relatives are polynomial** and included to measure whether models track the class through the
  disguise (an over-engineered P solution is itself a signal).
- Statements are deliberately **disguised** (no textbook problem names) to defeat pattern-matching.

# Adversarial Complexity-Class Benchmark

Benchmarking whether large language models understand **computational-complexity
structure** when they generate code, or whether their coding ability is surface-level
pattern matching.

Each problem **family** pairs an **NP-complete (NPC)** variant with a **polynomial-time
(P)** relative posed over the same surface, so that a single structural change moves the
instance across the class boundary. Statements are then **adversarially hardened** (a
teacher LLM rewrites them to be harder while a validity gate keeps them well-posed and
answer-preserving), and an independent panel of models is evaluated on the result.

> **Current setup (this is the live configuration).**
> - **12 families**, **2 criteria** each: `criterion_1_npc` and `criterion_2_p`.
> - The released benchmark lives in **`final_dataset/`**: seeds, all hardened statement
>   versions, full hardening lineages, stored model attempts, and curated tests.
> - Evaluation is done by **`evaluate.py`** (NPC, with a 1/2/5/10 s time-constraint
>   sweep) and **`evaluate_p.py`** (P, at each statement's own stated limit), scored by a
>   family of **report scripts**.

---

## Table of contents
- [The core idea](#the-core-idea)
- [The twelve families](#the-twelve-families)
- [Repository layout](#repository-layout)
- [The dataset (`final_dataset/`)](#the-dataset-final_dataset)
- [How a statement is hardened](#how-a-statement-is-hardened)
- [Evaluating models](#evaluating-models)
- [The report variants](#the-report-variants)
- [Model panel](#model-panel)
- [Quick start](#quick-start)
- [Paper analysis docs](#paper-analysis-docs)
- [Glossary](#glossary)

---

## The core idea

For every family we author two problem statements that look almost identical on the
surface but live in different complexity classes:

| Criterion | Class | Meaning | Example (Family 01: graph colouring) |
|---|---|---|---|
| `criterion_1_npc` | **NPC** | NP-complete, no known polynomial algorithm | 3-colouring |
| `criterion_2_p` | **P** | polynomial-time solvable | 2-colouring / bipartiteness |

**A statement never names its complexity class.** No "NP-complete", no "bipartite", no
algorithm or reduction name. The model must infer difficulty from structure and bounds
alone; the hidden truth (class, intended algorithm, reduction) lives in a `meta.yaml` the
model never sees. A model that truly understands algorithmic difficulty should do markedly
worse on the NPC side than on its near-identical P twin. That **P to NPC gap** is the
headline measurement.

On top of that, statements are **hardened** so difficulty cannot come from recognising a
textbook problem: the problem is disguised as a domain scenario, class vocabulary is
stripped, and the reduction-critical constraints are embedded in prose, while the answer,
I/O contract, and complexity class are provably preserved.

---

## The twelve families

| # | Family | NPC criterion | P relative |
|---|---|---|---|
| 01 | graph colouring | 3-colouring | 2-colouring |
| 02 | satisfiability | 3-SAT | 2-SAT |
| 03 | matching | 3-D matching | bipartite matching |
| 04 | clique / independent set | general graphs | interval graphs |
| 05 | Steiner tree | terminal subset | spanning tree (MST) |
| 06 | job-shop | makespan | two-machine flow shop |
| 07 | exact cover | exact cover by 3-sets | exact cover by 2-sets |
| 08 | linear arrangement | general graphs | trees |
| 09 | multicommodity flow | k-commodity (integer) | single commodity |
| 10 | edge colouring | cubic graphs | bipartite graphs |
| 11 | multiway cut | at least 3 terminals | s-t min cut |
| 12 | precedence scheduling | at least 2 machines | single machine |

(Family numbering is the original dataset id; families 03, 04, 06 to 08, 10 to 13, and 15
exist in `dataset/` but are not part of the released 12-family `final_dataset/`.)

---

## Repository layout

```
complexity-benchmark/
├── README.md                     ← you are here
│
├── final_dataset/                ← THE RELEASED BENCHMARK (12 families)
│   └── family_NN_<slug>/
│       ├── seed/<crit>/          statement.md · reference.py · validator.py · meta.yaml
│       ├── tests/<crit>/         curated test cases (NN.in/.out, worst_*, corner_*, seed_*)
│       ├── versions/<crit>/vNNN/ accepted/flagged hardened statements (+ edit.json, gate.json)
│       ├── lineages/<crit>/LNNN/ hardening chains: dNNN/statement.md + per-depth attempts
│       ├── attempts/<crit>/vNNN/<model>/  stored generation-time solutions + verdicts
│       ├── README.md  _manifest.json
│
├── agentic/                      ← the hardening pipeline
│   ├── config/
│   │   ├── models.yaml           teacher / verifier / students / held-out / frontier
│   │   ├── eval_models.yaml      the EVALUATION panel + time_limits + execution
│   │   └── run_config.yaml       gate thresholds, lineage/feedback-loop settings
│   ├── prompts/                  teacher / student / verifier / expert / analyst prompts
│   ├── tools/                    generate_versions · gate · gen_tests · run_students ·
│   │                             harden_loop · report · backends.py (LiteLLM) · family modules
│   ├── seeds/, versions/, lineages/, attempts/, tests/, reports/, logs/
│
├── evaluate.py                   ← NPC evaluation (1/2/5/10 s sweep, derive mode)
├── evaluate_p.py                 ← P evaluation (statement's own stated limit)
├── eval_report*.py               ← 6 report variants (see below)
├── build_final_dataset.py        ← (re)builds final_dataset/ from agentic/ + dataset/
├── run_family_full.sh            ← per-family hardening driver (FAM=NN)
├── EVAL_GUIDE.md, RUN_GUIDE.md   ← how to run evaluation / hardening
│
├── dataset/                      ← original per-family seeds (16-family superset)
├── tools/                        ← family generators + worst-case witness graders
├── models/, conventions/, docs/, scripts/, studies/   ← supporting material
└── _archive_* , *_frozen_*       ← archived earlier states (incl. dropped INFEASIBLE)
```

Output of the evaluation goes to a **sibling** directory, never inside this repo:
```
../evaluation/
├── grades/   family_NN/criterion_1_npc/<stmt>/<model>/{1,2,5,10}s.json   (NPC)
├── grades_p/ family_NN/<stmt>/<model>/result.json                        (P)
├── solutions/ , solutions_p/     cached generated programs
└── reports/  summary*.{md,json}
```

---

## The dataset (`final_dataset/`)

A *statement* is one problem text a model is evaluated on. The released set contains, per
family and criterion, **all generated versions plus every hardening-lineage depth**
(about 2,100 statements total). Each family folder has:

- **`seed/`**: the canonical statement, `reference.py` (ground truth), `validator.py`
  (witness checker, where applicable), and `meta.yaml` (hidden class/algorithm/limits).
- **`tests/`**: curated test cases. Obscure families (17 to 22) keep all 30 (`01` to `15`
  anchor+scaled, `16` to `30` worst); curated originals keep `seed_*`, `corner_*`, and
  `worst_*` cases.
- **`versions/`**: every ACCEPT/FLAG hardened variant (with its gate score and edit).
- **`lineages/`**: the hardening chains (`d000` to `d0NN`), each depth with the statement
  and the per-model attempts that drove the next edit.
- **`attempts/`**: generation-time model solutions + verdicts per version.

Grading uses either the family's **`validator.py`** (`validate(input, output) -> (ok, msg)`,
a witness/constraint check) or, for the optimisation families with no validator (14, 16,
and the P side of 01), **exact match** against the reference `.out`.

---

## How a statement is hardened

Per family, per criterion, the pipeline (`agentic/tools/`) runs:

1. **generate_versions**: expand the seed into many paraphrase and structural **versions**.
2. **gate**: the validity gate runs hard checks `H1` to `H4` (well-posed, solvable,
   I/O-consistent) plus graded criteria `G1` to `G4` scored by the **verifier**. Accept
   only if all hard checks pass and `G1>=4, G2>=4, G3>=5, G4>=3`. (The former H5
   round-trip LLM solve is disabled in the current configuration.)
3. **harden_loop**: the hardest versions seed **lineages**. At each depth `d0` to `d10` the
   **teacher** rewrites the statement harder; the **student panel** attempts it; a student
   is *defeated* when it is wrong or too slow (`wrong_or_slow`, 300 s TLE ceiling); an
   **analyst** reads all traces to pick the shared shortcut to remove next. The loop
   continues until all students are defeated or depth 10 is reached.

Roles are kept on separate providers to avoid self-enhancement bias. All prompts are
documented verbatim in `../paper_files/prompts.md`.

---

## Evaluating models

Two harnesses write to `../evaluation/` and are **checkpointed, resumable, and
crash-proof** (a failed family/task is logged and skipped; the run continues).

**NPC (`evaluate.py`).** The statement's `Time limit:` is set and a strict scoring note is
appended; the model is told its program must finish within the limit or score 0 on that
test. The default **`derive` mode** generates one solution per (statement, model), runs it
once at the max limit while recording each test's elapsed time, then **derives** the result
at every limit (a case passes at limit L if it is correct and finished within L seconds).
This is about 4x cheaper than regenerating per limit and gives identical numbers for the
hardened tiers.

```bash
cd complexity-benchmark
python evaluate.py                         # all families, NPC, limits 1/2/5/10 s
FAM=17 python evaluate.py                  # one family
FAM=02,05,09 python evaluate.py            # several
EVAL_MODELS=gemma-3-4b python evaluate.py  # one model (e.g. local Ollama)
```

**P (`evaluate_p.py`).** No time sweep; each P statement is evaluated once at the limit
already written in its statement (the strict note is "only for NP"). Same flags.
```bash
python evaluate_p.py          # all families, P
FAM=17 python evaluate_p.py
```

Knobs (env): `FAM`, `EVAL_MODELS`, `EVAL_CRIT`, `LIMITS`, `EVAL_WORKERS`, `EVAL_MODE`
(`derive` or `per_limit`), `EVAL_SCOPE` (`all`, `versions`, or `lineages`), `EVAL_MAX_STMTS`.
Failure handling: API errors and empty replies are **retried** on re-run (not stored);
genuine wrong/TLE results are kept; after `EVAL_MAX_GEN_RETRIES` (4) a persistent failure
is stored as a real 0. Stop with `pkill -f evaluate`; re-run the same command to resume.
See **`EVAL_GUIDE.md`** for the full walkthrough.

---

## The report variants

All are read-only, safe to run mid-run, and write to `../evaluation/reports/`.

| Script | Metric |
|---|---|
| `eval_report.py` / `eval_report_p.py` | **test-case** pass % (micro-avg over cases), per family + overall |
| `eval_report_statement.py` / `_p_statement.py` | **statement** pass % (a statement counts only if all its tests pass) |
| `eval_report_tiered.py` / `_p_tiered.py` | **TEST, WORST, OVERALL** (anchor+scaled vs worst tier; OVERALL = equal-weight average) |

NPC reports show one column per time limit (1/2/5/10 s); P reports are single-column (each
statement at its own stated limit).

---

## Model panel

Defined in `agentic/config/eval_models.yaml`; decoding is uniform (temperature 0.0,
top-p 1.0, reasoning off). Current active panel (10 models):

- **OpenRouter:** gemma-3-12b, gemma-3-27b, qwen3.8-flash, qwen3.8-27b, qwen3.8-omni-flash,
  deepseek-v4.1-flash, mistral-medium-3.5, llama-4-scout
- **Google API:** gemini-3.8-flash
- **Local Ollama:** gemma-3-4b (`gemma3:4b`), moved local because the OpenRouter free pool
  rate-limited it

Held or commented for budget: `kimi-k3` (held-out transfer model), `qwen3.8-2.4t-a95b`, and
the OpenRouter copy of gemma-3-4b. Keys: `OPENROUTER_API_KEY`, `GEMINI_API_KEY` (in
`agentic/config/local_secrets.py` or env); Ollama needs none. All calls route through
LiteLLM (`agentic/tools/backends.py`).

---

## Quick start

```bash
cd complexity-benchmark
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt        # pyyaml, litellm, ...
# set OPENROUTER_API_KEY / GEMINI_API_KEY; `ollama pull gemma3:4b` for the local model

# sanity check on a tiny slice (a few cents):
EVAL_MAX_STMTS=2 FAM=17 python evaluate.py

# full NPC + P (checkpointed; survives restarts):
nohup python evaluate.py   > ../evaluation/run_np.log 2>&1 &
nohup python evaluate_p.py > ../evaluation/run_p.log  2>&1 &

# read results anytime:
python eval_report_tiered.py
python eval_report_p.py
```

To (re)build the released dataset from the pipeline outputs: `python build_final_dataset.py`.
To harden a new or updated family end-to-end: `FAM=NN bash run_family_full.sh` (see `RUN_GUIDE.md`).

---

## Paper analysis docs (`../paper_files/`)

| File | Contents |
|---|---|
| `dataset_statistics.md` | counts, word-length stats per family + overall (+ `compute_stats.py`, figures via `make_figures.py`) |
| `evaluation_methodology.md` | metric definitions, grading, time-constraint semantics, full model config |
| `prompts.md` | every pipeline prompt, verbatim, with role and step |
| `hardening_effectiveness.md` | before/after accuracy drop per class, with tables |
| `per_layer_accuracy_drop.md` | per-hardening-depth accuracy curves per family |
| `failure_taxonomy.md` | wrong-answer / crash / TLE breakdown with measured percentages |
| `qualitative_examples.md` | annotated real failures (full code, error lines marked) |

---

## Glossary

- **NPC / P**: the two complexity classes each family spans (`criterion_1_npc`, `criterion_2_p`).
- **Seed / version / lineage depth**: the base statement, a generated variant, and a
  rewrite step in the hardening chain (`d0` to `d10`).
- **Hardening**: the teacher rewrites a statement harder while the gate preserves the
  answer, the I/O contract, and the class; a student is *defeated* when wrong or slower
  than the 300 s ceiling.
- **Validity gate**: hard checks `H1` to `H4` plus graded criteria `G1` to `G4` (scored by
  the verifier).
- **Verdict / why**: PASS, or FAIL tagged `wrong_answer`, `tle`, or `runtime_error`.
- **Derive mode**: grade once at the max limit, then derive every tighter limit from the
  recorded elapsed times.
- **Worst tier**: the large, near-threshold test cases engineered to defeat even 300 s
  solvers (`worst_*`, or numeric id at least 16 for the obscure families).
- **Held-out model**: `kimi-k3`, never used anywhere in the pipeline; its evaluation is the
  transfer / anti-overfitting check.
```

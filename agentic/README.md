# Agentic Hardening Phase

This folder holds Phase 3 of the benchmark: an agentic loop that rewrites problem
statements to defeat pattern-matching, guided by student models' own reasoning traces.

It **reads** `../dataset/` and **never writes to it**. Everything it produces stays here.

---

## 1. What this phase does

We have 48 problems (16 families × 3 criteria: NP-complete, P, infeasible). Static
benchmarks invite the objection that models memorised the classic problems. This phase
answers that by continuously **re-authoring** the statements:

1. A **teacher** model rewrites a statement so a careful reasoner still succeeds but a
   pattern-matcher fails.
2. **Student** models attempt it; their code and reasoning traces are saved.
3. An **analyser** reads the traces of the models that *passed* and names the single
   shared shortcut they used.
4. The teacher rewrites again to remove exactly that shortcut.
5. A **validity gate** rejects any rewrite that changes the answer, changes the
   complexity class, becomes ambiguous, or names the class.

Repeat until nobody passes, the depth limit is hit, or no valid harder rewrite exists.

---

## 2. Folder map

```
agentic/
├── config/
│   ├── models.yaml               teacher, verifier, students. Add a model here — never in code.
│   ├── run_config.yaml           family, depths, seed counts, scoring tier, ladder.
│   ├── local_secrets.py          API keys. GITIGNORED. Create from the .example file.
│   └── local_secrets.example.py  template, committed.
│
├── seeds/                        problems copied from ../dataset (regenerate with seed.py)
│   └── family_XX_slug/criterion_N_class/
│       ├── statement.md          the v0 problem shown to students
│       ├── meta.yaml             hidden truth: class, intended algorithm, scaling provenance
│       ├── reference.py          ground-truth solution
│       ├── tests/                anchor cases 01–04 (small, hand-verifiable)
│       └── tests_scaled/         scaled cases (large; where intractability bites)
│
├── strategies/                   the rewrite playbook
│   ├── PLAN.md                   how N versions are allocated across sources
│   ├── INTENSITY.md              light / moderate / aggressive
│   └── S01…S12.md                one file per strategy (see §6)
│
├── prompts/
│   ├── teacher_system.md         hard constraints every rewrite must satisfy
│   ├── teacher_user_template.md  slots: seed, metadata, strategy, intensity, feedback
│   ├── teacher_feedback_block.md the S12 block naming the observed shortcut
│   ├── student_system.md         fixed; identical to the main study for comparability
│   ├── verifier_system.md        gate's ambiguity / same-task judge
│   └── shortcut_summarizer.md    names the shared affordance from passers' traces
│
├── versions/                     batch-generated rewrites (input to the loop)
│   └── family_XX/criterion_N/vNNN/{statement.md, edit.json, gate.json}
│
├── lineages/                     the loop's output — the important artefact
│   └── family_XX/criterion_N/
│       ├── plan.json             which seeds and students were selected
│       └── LNNN/
│           ├── lineage.json      per-depth passers, retirements, shortcut, outcome
│           └── dNNN/
│               ├── statement.md          the statement at this depth
│               ├── edit.json             strategy, rung, teacher raw output, rationale
│               ├── gate.json             gate verdict and reasons
│               ├── shortcut.json         analyser output that drove this edit
│               ├── teacher_attempt_N.txt raw teacher reply (kept even on failure)
│               └── attempts/<student>/
│                   ├── solution.py  raw.txt  trace.txt  verdict.json
│
├── tests/                        corner cases generated per problem (see gen_tests.py)
├── reports/                      summary CSVs
├── logs/                          harden_loop.log and run logs
├── archive/                      snapshots of superseded runs (v2, v3, …)
├── tools/                        see §4
└── OPERATIONS.md                 day-to-day command reference
```

---

## 3. Scoring: three tiers

A solution is scored against three separate tiers. **They are never merged** — each
measures something different, and merging makes results uninterpretable.

| tier | source | measures | typical size |
|---|---|---|---|
| `anchor` | `seeds/.../tests/` (01–04) | basic correctness | tiny, hand-verifiable |
| `corner` | `tests/` from `gen_tests.py` | edge-case coding correctness | small |
| `scaled` | `seeds/.../tests_scaled/` | **intractability** | large (Phase 2 sizes) |

`run_config.yaml → feedback_loop.scoring_tier` decides which tiers drive retirement
(`all` by default).

**Why the scaled tier matters.** The anchor and corner tiers are small enough that any
correct algorithm finishes instantly, so recognising the problem costs nothing. The
scaled tier is sized so a *realistic but naive* solver exceeds the time limit while a
genuinely good one does not. That is what separates models by mechanism.

**Ground truth is generated offline with no time limit.** The reference may take
minutes; the time limit applies only to student solutions. These two are deliberately
decoupled.

---

## 4. Tools

| tool | what it does | costs tokens |
|---|---|---|
| `seed.py` | Copy problems from `../dataset` into `seeds/`, including `tests_scaled/`. Run once after cloning. | no |
| `check_keys.py` | Verify every enabled model's key resolves and Ollama is reachable. Never prints keys. | no |
| `gen_tests.py` | Teacher invents corner-case inputs; the **reference** computes their outputs. See §4a. | **yes** |
| `generate_versions.py` | Batch-generate base versions from the strategy library. See §4b. | **yes** |
| `gate.py` | Run the validity gate over generated versions. | yes (verifier) |
| `harden_loop.py` | **The main driver** — the feedback loop described in §1. | **yes** |
| `report_lineage.py` | Survival curves, per-tier verdicts, shortcut taxonomy, per-student scaled rates. | no |
| `report.py` | Older batch report over `versions/` (superseded by `report_lineage.py`). | no |

---

## 4a. Corner-case generation (`gen_tests.py`)

### Why it exists

The anchor tier is only four tiny hand-verified cases, and the scaled tier probes
intractability. Neither reliably catches **ordinary coding bugs** — an off-by-one, a
mishandled empty input, a tie-break rule applied in the wrong order. A model can pass
four small examples by luck.

The corner tier fills that gap: a dozen small but adversarial inputs per problem,
designed to break plausible-but-wrong implementations.

### How it works

1. The teacher receives the problem statement and is asked to invent inputs that would
   break a subtly incorrect solution — boundary sizes, degenerate structures, cases where
   a greedy or first-found answer differs from the required one.
2. It returns **inputs only**, in a tag-delimited format (not JSON — models are
   unreliable at JSON for multi-line content), at low temperature for consistency.
3. Each input is validated against the statement's constraints. Invalid ones are dropped.
4. **The reference computes every expected output**, run offline with no time limit.

> The teacher never writes an expected output. It proposes inputs; ground truth always
> comes from `reference.py`. This is non-negotiable — a model-authored answer key would
> silently corrupt every downstream result.

### Running it

```bash
python tools/gen_tests.py --family 01                # all three criteria
python tools/gen_tests.py --family 01 --criterion 1  # one criterion
```

Output lands in `tests/family_XX/criterion_N/` as `NN.in` / `NN.out` plus a provenance
record (which model generated it, when, the raw reply). Roughly 12 cases per criterion.

Cost is small — a handful of calls per problem — and it is a **one-time** cost per
problem. Once the corner tests exist they are reused by every later run, so do not
regenerate them unless the statement's I/O contract changes.

### Checking they are useful

A corner tier that every model passes is telling you nothing. After generating, confirm
the cases actually discriminate — if all students score 12/12 on every problem, the
generated inputs are too easy and are worth regenerating with a stronger prompt.

---

## 4b. Base version generation (`generate_versions.py`)

### What it produces

This is the **batch** step that creates the pool of rewritten statements. The hardening
loop later picks a subset of these as its starting points (lineage seeds).

`run_config.yaml → versions_per_criterion` sets the target — 80 was used for Family 01,
giving 240 versions across its three criteria. The number is a *target the planner
fills*, not a formula, so raising it simply extends generation.

### The four sources

The planner fills the target from four sources, in priority order:

| source | what it is |
|---|---|
| `grid` | every (strategy, intensity) pair applicable to this criterion's class — one sample each. Typically 27–36 versions. |
| `sample` | repeat draws from cells already used. The teacher runs at high temperature, so repeats differ. |
| `composition` | two compatible strategies applied together in one rewrite. Moderate/aggressive only. |
| `generation` | a rewrite **derived from an already-accepted version** rather than from the seed. Versions form a tree, not a flat list. Depth capped by `max_generation`. |

Not every strategy applies to every class — S04 is NP-complete only, S05 is P/infeasible
only, S06 is infeasible only, S12 requires feedback. Inapplicable strategies are skipped,
so the grid yield varies by criterion.

`generation` requires gate results, so it runs as a **second pass**:

```bash
# pass 1 — seed-derived versions
python tools/generate_versions.py --family 01 --criterion 1 --sources grid,sample,composition
python tools/gate.py --family 01 --criterion 1

# pass 2 — derived from versions that passed the gate
python tools/generate_versions.py --family 01 --criterion 1 --sources generation
python tools/gate.py --family 01 --criterion 1
```

### Always dry-run first

```bash
python tools/generate_versions.py --family 01 --criterion 1 --dry-run
```

This renders and prints the exact prompts without calling the API. Read a few before
committing to 80 generations — prompt quality is the single biggest determinant of
version quality, and this check is free.

### What gets saved

```
versions/family_01/criterion_1_npc/v017/
├── statement.md     the rewritten problem
├── edit.json        source, strategies, intensity, parent, generation, sub-seed,
│                    the teacher's rationale / preserved-answer / preserved-class / risk,
│                    and its full raw reply
└── gate.json        gate verdict with reasons (written even when rejected)
```

The `risk` field is the teacher's own assessment of how the rewrite might be judged
ambiguous. **Any version where `risk` is not "none" deserves a human read** — it is the
cheapest signal for the review queue.

### Cost and volume

For Family 01: 240 versions cost roughly $0.30 in teacher calls plus verifier calls at
the gate. Generation is the cheap step; the expensive steps are student attempts and the
hardening loop.

Versions are **reusable across model sets** — if you change the student panel, the
existing versions stay valid and only the loop needs re-running.

### Gate outcomes to expect

Roughly, for Family 01: about half passed, a handful were flagged for verifier
uncertainty, and a small number failed — mostly on leakage (the teacher writing
"NP-complete" or "bipartite" into the statement despite the constraint) or on a broken
I/O contract. Failed versions are kept on disk with their reason, not deleted.

---

## 5. Running it

### One-time setup

```bash
cd agentic
cp config/local_secrets.example.py config/local_secrets.py
# edit config/local_secrets.py — replace the PASTE_..._HERE placeholders
python tools/check_keys.py
python tools/seed.py --family all      # seeds/ is gitignored; regenerate after cloning
```

### Per family

Four stages. Stages 1 and 2 are one-time per problem; their output is reused by every
later run.

```bash
# STAGE 1 — corner-case tests (§4a). One-time. Skip if tests/ already populated.
python tools/gen_tests.py --family 01

# STAGE 2 — base versions (§4b). One-time. Reusable across model sets.
python tools/generate_versions.py --family 01 --criterion 1 --dry-run   # free; read the prompts
python tools/generate_versions.py --family 01 --criterion 1 --sources grid,sample,composition
python tools/gate.py               --family 01 --criterion 1
python tools/generate_versions.py --family 01 --criterion 1 --sources generation
python tools/gate.py               --family 01 --criterion 1

# STAGE 3 — the hardening loop. Re-run whenever the student panel or scoring changes.
python tools/harden_loop.py --family 01 --criterion 1 --reset

# STAGE 4 — read the result (free)
python tools/report_lineage.py --family 01
```

**What each stage costs:** stage 1 is a handful of calls per problem; stage 2 is roughly
$0.30 per family; stage 3 is the expensive one at $1–2 and several hours per criterion;
stage 4 is free.

**When to repeat what:** changing the student panel or the scoring tier means re-running
**stage 3 only** — the corner tests and base versions stay valid. Changing a problem's
statement or I/O contract invalidates its corner tests and versions, so stages 1 and 2
must be redone for that problem.

Omit `--criterion` for all three. `--family all` exists but should not be used before one
family has been completed and reviewed.

### Smoke test before spending

```bash
python tools/harden_loop.py --family 01 --criterion 1 --only-lineage L001 --max-depth 1 --reset
cat lineages/family_01/criterion_1_npc/L001/d001/teacher_attempt_1.txt
```

If `d001/statement.md` exists, the teacher step works. If only the raw attempt file
exists, read it — it shows exactly what the teacher returned.

### Resume / reset

Everything is checkpointed. Re-running the same command resumes. `--reset` clears the
lineage's depth directories and starts over.

---

## 6. The strategy library

Twelve rewrite strategies × three intensities. Some apply only to certain classes.

| id | idea |
|---|---|
| S01 | remove lexical cues that trigger textbook recall |
| S02 | transplant to a different real-world domain |
| S03 | describe special structure operationally, never by name |
| S04 | make a hard problem look tractable (NPC only) |
| S05 | make an easy problem look intractable (P / infeasible) |
| S06 | camouflage the contradiction (infeasible only) |
| S07 | state bounds indirectly through the scenario |
| S08 | embed in a realistic scenario where every detail is load-bearing |
| S09 | add true but non-binding constraints |
| S10 | present the task as one step in a larger workflow |
| S11 | give constraints before revealing the objective |
| S12 | target the shortcut observed in student traces (feedback-driven) |

The loop uses **S12**, falling back through `S12_secondary → S07 → S02_aggressive` when
the gate rejects an edit.

---

## 7. The validity gate

Every rewrite must pass before any student sees it:

1. **Answers unchanged** — the reference still produces the correct output.
2. **Class unchanged** — the teacher may make the class harder to *recognise*, never
   change what it is.
3. **Unambiguous** — a separate verifier model confirms same-task, unambiguous, solvable,
   and example-consistent. Returns `pass` / `flag` / `fail`.
4. **No class vocabulary** — deterministic keyword scan.

Rejected edits are saved with their reason, then the ladder tries the next strategy.

> The gate is what separates this from generic adversarial paraphrasing. Without it the
> teacher drifts problems into something the answer key no longer matches.

---

## 8. Reading the results

`report_lineage.py` prints:

- **Survival curves** — `raw` (all students, the scientific metric), `steer` (non-retired
  pool), `a+c` (anchor+corner), `scaled`.
- **Verdict breakdown per depth per tier** — TLE on the scaled tier is on-thesis;
  WRONG_ANSWER on anchor/corner is coding noise.
- **Per-student scaled pass rate** and first timing-out case.
- **Shortcut taxonomy** — which affordances models rely on most.
- **Structural floor** — how many named shortcuts are the core task itself.

### Interpreting outcomes

- `all_defeated` means no model passed. With the scaled tier active this usually means
  **instance hardness** defeated them, not that hardening succeeded. Do not read the
  label as success without checking the tier breakdown.
- Sample size shrinks with depth (lineages terminate early). Report depth counts
  alongside the curve; deep points can rest on one or two lineages.

---

## 9. Adding or changing models

Edit `config/models.yaml` only.

```yaml
  - id: my-model                 # directory-safe; becomes the folder name
    backend: openai_compat       # openai_compat | ollama
    base_url: "https://..."      # API models only
    model_string: "provider/model"
    api_key_env: OPENROUTER_API_KEY
    thinking: false              # true for reasoning models
    max_tokens: 4096             # raise for thinking models
    enabled: true
```

Then add the key to `config/local_secrets.py` and run `check_keys.py`.

- Prefer `enabled: false` over deleting — keeps past results interpretable.
- Changing `max_tokens` or `thinking` makes existing attempts stale; delete that model's
  folders under `lineages/.../attempts/` before re-running.
- Local Ollama models must run **sequentially** on a single consumer GPU
  (`execution.ollama_parallel: false`); running them concurrently causes HTTP 500s.

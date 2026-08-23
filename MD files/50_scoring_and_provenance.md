# 50 — Strategy fixes, gate scoring, and provenance tracking

> **Build/edit only. Run nothing.** Three independent parts. Apply all three, then the
> user runs the full Family 01 campaign.

---

# PART A — Strategy file fixes

## A1. Rename

`strategies/s02_dpmain_transplant.md` → `strategies/s02_domain_transplant.md`.

## A2. Add a `perturbation_family` field to every strategy file

Insert after `classes:`. This is the literature mapping and becomes a table in the paper.

| file | perturbation_family |
|---|---|
| S01 | `lexical_substitution` |
| S02 | `paraphrase_domain` |
| S03 | `logical_equivalence` |
| S04 | `misleading_cue` (complexity-directed) |
| S05 | `misleading_cue` (complexity-directed) |
| S06 | `novel` (complexity-directed) |
| S07 | `logical_equivalence` |
| S08 | `semantic_expansion` |
| S09 | `semantic_expansion` |
| S10 | `semantic_expansion` |
| S11 | `structural_reorder` |
| S12 | `adversarial_feedback` |

## A3. Rewrite `s12_feedback_targeted.md` — it is stale

The current file predates the immutable-element fix and can still instruct the teacher to
remove bounds or tie-break rules, which the gate always rejects. Replace its body with:

```
id: S12
summary: Attack the specific shortcut observed in student reasoning traces.
classes: all
perturbation_family: adversarial_feedback
requires: feedback

Only for rounds where student traces are available.

Read the shared reasoning pattern in the feedback block, identify the single step that
let the models bypass the intended reasoning, and remove exactly that affordance with the
smallest possible edit. Leave the rest of the statement alone.

IMMUTABLE ELEMENTS. If the identified affordance is a numeric bound, an input or output
format, a tie-break rule, or an example value, you may NOT remove it. You may only change
how it is PRESENTED — for example, expressing a bound through the scenario rather than as
a bare inequality. If the affordance cannot be re-presented, say so rather than producing
an edit that will be rejected.
```

## A4. Strengthen `s08_narrative_embedding.md`

Append:

```
JUSTIFICATION REQUIRED. For every sentence of context you add, it must do one of three
things: specify a constraint, clarify the objective, or define the data. In your
rationale, list each added detail and which of the three it does. A detail you cannot
place in one of those categories is padding and must be removed.

This is not distractor injection. Adding irrelevant-but-plausible clauses is a known and
separately-studied effect; if we added those we would be measuring distraction rather
than reasoning. Every detail must be load-bearing.
```

## A5. Strengthen `s09_nonbinding_constraints.md`

Append:

```
FORMAL STATEMENT REQUIRED. State each added constraint formally in your rationale, in a
form that can be checked against a concrete input — for example "sum of all weights <=
10^6" or "no vertex has degree > n-1". The gate will evaluate your constraint against
every existing test input; if any input violates it, the constraint is binding, the
answer may change, and the rewrite is rejected.

Prefer constraints that follow arithmetically from the seed's own bounds. Do not invent a
constraint you cannot state precisely.
```

## A6. Promote the truth requirement in `s04` and `s05`

Move "Every statement you make must be true" to its own emphasised line at the top of the
instruction body in both files, phrased:

```
TRUTH CONSTRAINT (non-negotiable): every claim you make about the problem must be
factually correct. You are shaping emphasis, salience, and expectation — never facts. A
statement that is misleading because it is false is invalid and will be rejected.
```

## A7. Note the empirical result in `PLAN.md`

Append to Source 2:

```
Empirical note: in the Family 01 batch, this source was the least effective (mean delta
+0.12, the worst of the four). Temperature alone produces paraphrase, not genuine
diversity. Persona conditioning of the teacher prompt is the intended fix.
```

---

# PART B — Gate scoring

Replace the binary verdict with a two-part scheme: **hard constraints** (binary, fatal)
and **graded criteria** (0–5, thresholded). They measure different things and must not be
merged.

## B1. Hard constraints — binary, fatal, mostly executable

| id | check | how |
|---|---|---|
| H1 | **Example consistency** | Run `reference.py` on each example input in the rewritten statement. Its output must equal the stated example output. **Fully executable.** |
| H2 | **I/O contract preserved** | Parse Input/Output sections; format, every numeric bound, and any tie-break rule must match the seed. Bounds compared numerically, not textually. |
| H3 | **No class leakage** | Deterministic keyword scan. |
| H4 | **S09 constraint non-binding** | *Only when S09 was used.* Evaluate the teacher's formally-stated constraint against every existing test input. Any violation → reject. **Executable.** |
| H5 | **Solver round-trip** | Give the rewritten statement to a strong solver model **not in the student panel**; its solution must pass the seed's anchor tests. **Executable evidence that the task is unchanged.** |

H1, H4, H5 are the strong ones because they are *executed*, not judged. H5 is the single
best answer to "how do you know the rewrite preserved meaning?"

Run H5 once per version, on anchor tests only (cheap and fast).

## B2. Graded criteria — 0–5, scored by the verifier

| id | criterion | 0 | 5 |
|---|---|---|---|
| G1 | **Unambiguity** | multiple defensible readings | exactly one reading |
| G2 | **Completeness** | information needed to solve is missing | fully specified |
| G3 | **Faithfulness** | asks a materially different question | provably the same question |
| G4 | **Naturalness** | reads as machine-generated or contrived | reads as a problem a person would write |

Each score requires a one-sentence justification. Verifier temperature 0.

## B3. Acceptance rule

```
ACCEPT  iff  H1..H5 all pass
        AND  G1 >= 4  AND  G2 >= 4  AND  G3 >= 5  AND  G4 >= 3
FLAG    if hard constraints pass but a graded score is one below its threshold
REJECT  otherwise
```

G3 requires a full 5 because faithfulness is effectively a hard constraint expressed on a
scale — a rewrite that asks a different question is worthless. G4 is permissive because
naturalness is a quality signal, not a validity one.

Record the threshold vector in `gate.json` so a sensitivity analysis can be re-run
without re-judging.

## B4. Composite score for *selection*, not just filtering

```
composite = 0.40*G3 + 0.30*G1 + 0.20*G2 + 0.10*G4
```

The gate becomes a **selector**, not just a filter. Where multiple candidate rewrites
exist at one depth (the fallback ladder, or `candidates_per_depth > 1`), take the
highest-composite accepted candidate rather than the first that passes.

Add to `run_config.yaml`:

```yaml
gate:
  thresholds: {G1: 4, G2: 4, G3: 5, G4: 3}
  composite_weights: {G3: 0.40, G1: 0.30, G2: 0.20, G4: 0.10}
  solver_roundtrip:
    enabled: true
    model_id: <a model NOT in the student panel>
    tests: anchor
feedback_loop:
  candidates_per_depth: 3      # generate N, gate all, keep the best
```

## B5. `gate.json` schema

```json
{
  "result": "ACCEPT | FLAG | REJECT",
  "hard": {
    "H1_example_consistency": {"pass": true, "detail": "2/2 examples reproduce"},
    "H2_io_contract":         {"pass": true, "bounds_seed": {...}, "bounds_new": {...}},
    "H3_leakage":             {"pass": true, "hits": []},
    "H4_s09_nonbinding":      {"pass": null, "detail": "not applicable"},
    "H5_solver_roundtrip":    {"pass": true, "solver": "...", "anchor": "4/4"}
  },
  "graded": {
    "G1_unambiguity": {"score": 5, "justification": "..."},
    "G2_completeness": {"score": 5, "justification": "..."},
    "G3_faithfulness": {"score": 5, "justification": "..."},
    "G4_naturalness":  {"score": 4, "justification": "..."}
  },
  "composite": 4.80,
  "thresholds_applied": {"G1": 4, "G2": 4, "G3": 5, "G4": 3},
  "judge": {"model": "...", "temperature": 0},
  "attempt": 1,
  "rung": "S12_primary"
}
```

## B6. Rewrite `prompts/verifier_system.md`

It must emit the four graded scores with justifications, tag-delimited (not JSON —
consistent with the teacher path). Keep the existing same-task reasoning but express it
as G3.

## B7. New tool — `tools/judge_agreement.py`

```
python tools/judge_agreement.py --family 01 --sample 100 --judges <id1> <id2>
```

Re-judges a stratified random sample (stratified by strategy, intensity, and composite
score band) with two additional judges **from different providers**, temperature 0, same
prompt. Computes pairwise Cohen's κ (quadratic-weighted for the 0–5 scales) and the
unanimous-agreement rate. Writes `reports/judge_agreement.json`.

This also mitigates the current same-provider exposure: teacher and verifier are both
Gemini.

## B8. New tool — `tools/human_annotation.py`

Exports a stratified sample of ~100 versions to a CSV with blank score columns, blinded
(no verifier scores shown, version ids hashed). A second mode ingests two completed
sheets and computes Krippendorff's α between annotators plus judge-vs-human accuracy and
F1 at the configured threshold.

## B9. Report the gate

Extend `report_lineage.py` (or add `tools/report_gate.py`) with a table:

| strategy | intensity | n | accept % | H-fail breakdown | mean G1..G4 | mean composite |

Plus a threshold-sensitivity table at G1/G2 ≥ 3, 4, 5.

---

# PART C — Provenance tracking

Every version has a parent; lineages have depth chains. Currently that is spread across
many `edit.json` files and is unreadable. Build a consolidated record.

## C1. `tools/build_provenance.py`

```
python tools/build_provenance.py --family 01
```

Walks `versions/` and `lineages/`, emits **one file per criterion**:
`reports/provenance/family_01_criterion_1_npc.json`

```json
{
  "family": "01",
  "criterion": "criterion_1_npc",
  "generated_at": "...",
  "seed": {"id": "v000", "statement_path": "seeds/.../statement.md"},

  "versions": {
    "v017": {
      "parent": "v000",
      "generation": 0,
      "source": "grid",
      "strategies": ["S01"],
      "intensity": "moderate",
      "gate": {"result": "ACCEPT", "composite": 4.8},
      "used_as_lineage_seed": "L003",
      "path": "versions/family_01/criterion_1_npc/v017"
    },
    "v054": {
      "parent": "v017",
      "generation": 1,
      "source": "generation",
      "...": "..."
    }
  },

  "lineages": {
    "L003": {
      "base_version": "v017",
      "outcome": "all_defeated",
      "final_depth": 4,
      "depths": [
        {"depth": 0, "parent": null,   "statement": "d000/statement.md",
         "raw_passers": ["qwen3.5-flash"], "shortcut": "graph coloring recall"},
        {"depth": 1, "parent": "d000", "strategy": "S12", "rung": "S12_primary",
         "gate": {"result": "ACCEPT", "composite": 4.6},
         "raw_passers": ["qwen3.5-flash"], "shortcut": "..."}
      ]
    }
  },

  "edges": [["v000","v017"], ["v017","v054"], ["v017","L003/d000"], ["L003/d000","L003/d001"]],

  "stats": {
    "versions_total": 80, "accepted": 44, "flagged": 6, "rejected": 30,
    "by_source": {"grid": 31, "sample": 16, "composition": 19, "generation": 14},
    "by_generation": {"0": 66, "1": 14},
    "lineages": 14, "max_depth_reached": 4
  }
}
```

## C2. Human-readable tree

Also emit `reports/provenance/family_01_criterion_1_npc.md`:

```
v000  (seed)
├── v001  S01/light          grid         ACCEPT  4.9
├── v017  S01/moderate       grid         ACCEPT  4.8   → seed of L003
│   └── v054  S07/moderate   generation   ACCEPT  4.5
└── v023  S03/aggressive     grid         REJECT  (H3 leakage: np-complete)

L003  base=v017  outcome=all_defeated  depth=4
  d000  passers=[qwen]              shortcut="graph coloring recall"
  d001  S12  ACCEPT 4.6  passers=[qwen]   shortcut="3-coloring mapping"
  d002  S12  ACCEPT 4.4  passers=[]       → all_defeated
```

## C3. Graph export

Emit `reports/provenance/family_01_criterion_1_npc.dot` (Graphviz) so the tree can be
rendered:
- node colour by gate result (accept / flag / reject)
- solid edges for version derivation, dashed for lineage depth steps
- lineage seeds outlined

## C4. Consistency check mode

```
python tools/build_provenance.py --family 01 --check
```

Flags: a version whose `parent` does not exist; a lineage whose `base_version` is missing
or was not gate-accepted; a depth whose `parent` is not the previous depth; `generation`
inconsistent with the parent chain; orphaned directories on disk with no record.

Run this after generation and after the loop.

---

# Order of work

1. Part A (strategy files) — smallest, no dependencies.
2. Part B1–B6 (gate scoring) — the core change.
3. Part C (provenance) — independent of B.
4. Part B7–B9 (agreement tooling, reporting) — can follow after the run.

Run nothing. Report what changed.

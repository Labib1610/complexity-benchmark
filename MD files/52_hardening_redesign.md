# 52 — Hardening Redesign: Memory, Simultaneous Defeat, Aggressive Mode

> **Build only. Run nothing.** Six changes to `harden_loop.py` and its prompts.

---

## Motivation

Frontier evaluation of the final statements:

| criterion | gemini-3.7-flash | gpt-5.6-sol |
|---|---|---|
| NPC | 86% | 93% |
| P | **100%** | **100%** |
| INFEASIBLE | **100%** | **100%** |

The statements are well-formed but not hard enough. Six changes follow.

---

# CHANGE 1 — Target WRONG_ANSWER, not TLE

## Rationale

TLE conflates reasoning failure with runtime/language artifacts: a model can understand a
problem perfectly and still time out. WRONG_ANSWER is unambiguously a reasoning failure.
From now on hardening targets correctness only.

## Implementation

Add to `run_config.yaml`:

```yaml
feedback_loop:
  hardening_target: wrong_answer_only   # wrong_answer_only | all_failures
  tle_ceiling_s: 300                    # runaway guard only, NOT the difficulty signal
```

When `hardening_target: wrong_answer_only`:

- A student counts as **DEFEATED** only on `WRONG_ANSWER` or `RUNTIME_ERROR`.
- A student that produces a correct answer counts as **NOT DEFEATED**, regardless of how
  long it took.
- Do **not** enforce the problem's `time_limit_s` during the loop. Use `tle_ceiling_s`
  purely to kill runaways.
- **Still record `elapsed_s` for every case.** Timing remains reported; it just no longer
  decides defeat.

`verdict.json` gains `defeated: true|false` alongside the existing verdict, so reports can
show both views.

> **Note for the report:** the scaled tier now measures *runtime*, not difficulty. Update
> `report_lineage.py` so the scaled curve is labelled as a timing measure and a new
> correctness-only curve becomes the primary metric.

---

# CHANGE 2 — Agentic memory

## Rationale

Each depth currently starts blind: the summarizer sees only the current depth's traces.
Knowledge of what was already tried, what worked, and each student's characteristic
weakness is discarded. The teacher therefore repeats failed strategies and, worse,
re-enables students it had already defeated.

## Store

`lineages/<family>/<criterion>/<L>/memory.json`, rebuilt and appended at every depth:

```json
{
  "lineage": "L008",
  "criterion": "criterion_1_npc",
  "depth_history": [
    {
      "depth": 1,
      "strategy": "S12",
      "shortcut_targeted": "recognizes task as graph triangle",
      "edit_summary": "replaced explicit triple-conflict wording with pairwise phrasing",
      "defeated_before": [],
      "defeated_after": ["deepseek-v4-flash"],
      "regained": [],
      "gate_composite": 4.8,
      "outcome": "partial - 1 of 4 defeated"
    }
  ],
  "student_profiles": {
    "kimi-k2.7-code": {
      "times_defeated": 1,
      "defeated_by": ["hidden infeasibility in a nested constraint"],
      "resistant_to": ["domain transplant", "lexical cue removal"],
      "characteristic_failure": "WRONG_ANSWER on tie-break rules",
      "never_defeated_by_depth": 4
    }
  },
  "strategies_tried": [
    {"name": "S12/pairwise-rephrase", "depth": 1, "net_defeated": 1, "verdict": "weak"},
    {"name": "S06/nested-contradiction", "depth": 3, "net_defeated": 3, "verdict": "strong"}
  ],
  "dead_ends": [
    "renaming the domain - no student affected at depths 1, 2, 5"
  ]
}
```

**Also maintain a criterion-level memory** at
`lineages/<family>/<criterion>/criterion_memory.json`, aggregating across lineages: which
strategies ever defeated which students, and which never did. Lineages run in parallel, so
guard this file with a lock and merge rather than overwrite.

## Feeding it to the teacher

Add a `{MEMORY_BLOCK}` slot to `teacher_user_template.md`:

```
PRIOR ATTEMPTS ON THIS PROBLEM
------------------------------
Depths so far: {N}
Currently defeated: {DEFEATED_LIST}
Still solving it: {SURVIVOR_LIST}

What has already worked:
{STRATEGIES_THAT_WORKED}

What has already failed - do not repeat these:
{DEAD_ENDS}

Per-student profile of the survivors:
{SURVIVOR_PROFILES}

Warning: an edit that defeats a survivor must not restore any student already defeated.
Previous regressions: {REGRESSIONS}
```

**Cap the memory block at ~1,500 tokens.** Summarize older depths; keep the most recent
two verbatim. Unbounded memory becomes the dominant token cost.

---

# CHANGE 3 — Target simultaneous defeat

## Rationale

Different students fail on different things. Defeating them one at a time produces a
statement hard for whoever was last targeted, not hard in general. The goal is a single
statement that defeats **all** students at once.

## Implementation

1. **The summarizer now reads ALL students' traces**, not only passers'. Understanding why
   the already-defeated failed is what prevents accidentally un-defeating them.

2. Its output gains fields:

```json
{
  "survivor_shortcuts": [
    {"student": "kimi-k2.7-code", "shortcut": "...", "affordance": "..."}
  ],
  "common_affordance": "the single affordance ALL survivors rely on, or null",
  "defeated_student_causes": [
    {"student": "deepseek-v4-flash", "why_failed": "...", "fragile": true}
  ],
  "recommended_edit": "...",
  "regression_risk": "which defeated students this edit might restore"
}
```

3. `common_affordance` is the priority target when non-null — that is the single edit that
   defeats everyone at once. Fall back to per-survivor targeting only when it is null.

4. Track **regressions** explicitly. If depth *d* defeats A but restores B, record it in
   memory as a regression and instruct the teacher to avoid that edit shape.

5. New stop condition: `all_defeated_simultaneously` — every student defeated **at the same
   depth**, not cumulatively. Report this separately from the existing `all_defeated`.

---

# CHANGE 4 — Aggressive mode after depth 3

## Rationale

The fixed 12-strategy library is exhausted by depth 3. Beyond that the teacher should
devise its own approaches.

## Implementation

```yaml
feedback_loop:
  aggressive_from_depth: 3
  aggressive_requires_named_method: true
```

From depth 3 onward, append to the teacher prompt:

```
AGGRESSIVE MODE

The standard strategy library has not defeated the remaining models. You are no longer
restricted to it. Devise your own approach.

You may combine, extend, or invent methods freely. All hard constraints still apply
without exception: identical answers for every input, unchanged complexity class,
unchanged I/O contract, unambiguous statement, no complexity-class vocabulary.

You MUST name and describe your method. Report:

<METHOD_NAME>a short label for the technique you invented</METHOD_NAME>
<METHOD_DESCRIPTION>what it does and why you expect it to defeat the survivors</METHOD_DESCRIPTION>
<METHOD_NOVEL>yes if this is not one of S01-S12, no if it is a variant</METHOD_NOVEL>
```

Persist every invented method to `strategies/discovered/<criterion>/<method_slug>.json`
with the name, description, the depth and lineage that produced it, the survivors it
targeted, and whether it succeeded.

Add `tools/report_discovered.py`: lists every invented method, how often it was used, and
its net defeat rate. **Post-hoc, map each discovered method onto the established
perturbation taxonomy** (lexical / structural / semantic / misdirection / novel) so the
taxonomy remains principled — an agent-discovered strategy that maps to a known family is
a validation, one that does not is a contribution.

---

# CHANGE 5 — Gate negotiation instead of exhaustion

## Rationale

`ladder_exhausted` currently discards a lineage when the gate rejects every fallback. The
gate's rejection reasons are actionable and should be used.

## Critical constraint — read before implementing

**The gate must never write statement content.** If it co-authors, it cannot
independently validate, and every acceptance becomes self-approval. The negotiation is
*structured feedback*, not co-creation:

```
teacher writes  ->  gate rejects WITH REASONS  ->  teacher revises using those reasons
                ->  FRESH gate call validates  ->  accept or repeat
```

The gate produces only diagnostics. The teacher produces all text.

## Implementation

```yaml
feedback_loop:
  gate_negotiation_rounds: 4        # replaces gate_retry: 2
  negotiation_transcript: true
```

On rejection, the gate returns structured, actionable feedback:

```json
{
  "rejected_because": ["H2", "G1"],
  "H2_detail": "bound 'n <= 40' present in seed, absent in rewrite",
  "G1_detail": "the phrase '...' admits two readings",
  "actionable_advice": "restore the missing bound; disambiguate the quoted phrase",
  "do_not_change": ["the scenario framing, which scored well on G4"]
}
```

The teacher receives this in a `{GATE_FEEDBACK}` block and revises. Loop up to
`gate_negotiation_rounds`. Only after all rounds fail does the lineage end as
`negotiation_failed` (replacing `ladder_exhausted`).

Save the full exchange to `d<NNN>/negotiation.json` — every teacher attempt and every gate
response, in order. This is provenance and it is also a finding in itself: *how many
rounds does it take to produce a valid hard problem?*

---

# CHANGE 6 — Depth 6 → 10

```yaml
feedback_loop:
  max_depth: 10
```

Justified by the last-change data: pass counts were still moving at depths 5–6, so the
previous ceiling was truncating.

---

# Cost

Roughly **2.5–3× the previous loop**, driven by depth 6→10, up to 4 negotiation rounds
instead of 2, and the memory block enlarging every teacher prompt.

Estimate **$25–35 per family**. Run Family 01 first and measure before committing to the
rest.

Cost controls if needed: cap the memory block hard at 1,500 tokens, and reduce
`candidates_per_depth` to 1 once negotiation is doing the quality work.

---

# Order of work

1. Change 1 (scoring target) — smallest, unblocks correct measurement.
2. Change 2 (memory) — needed by 3 and 4.
3. Change 3 (simultaneous defeat).
4. Change 5 (negotiation).
5. Change 4 (aggressive mode).
6. Change 6 (depth) — one line.

Then a single-lineage smoke test at `--max-depth 4` to confirm memory populates,
aggressive mode triggers at depth 3, and a negotiation transcript is written.

Run nothing beyond that smoke test.

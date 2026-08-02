# 46 — Feedback-Driven Hardening Loop (the missing piece)

> **Build only. Run nothing.** The user executes manually, Family 01 first.

## What went wrong

The current pipeline is a **batch generator**: it produced 80 versions per criterion from
the strategy library, ran students once on each, and reported deltas. Every version was
tested once and abandoned.

The `generation` source came closest to iteration but it applied a *fresh strategy* to a
prior version — it never read student reasoning traces. So the feedback arrow was never
wired. `feedback.py` exists but is not driven as a loop.

The result is visible in the report: 70% of versions sit at delta +0, best case −3, and
per-strategy effects are within noise.

## What to build instead

The 240 existing versions become **starting points**, not the product. Each selected
version enters a lineage that is hardened iteratively against live student behaviour
until every student fails or hardening is exhausted.

```
for each base version B:
    depth 0 = B
    active = all students          # students whose traces drive hardening
    loop:
        run ALL students on the current version
        passers = students that passed
        if passers is empty  -> lineage complete, all defeated
        collect reasoning traces from PASSERS ONLY
        summarizer names the single shared shortcut those passers used
        teacher rewrites (strategy S12) to remove exactly that shortcut
        gate validates
        if gate rejects  -> retry teacher with the gate's reason (bounded);
                            if still rejected, lineage stops as "exhausted"
        students that just failed are RETIRED from the feedback pool
            (their traces no longer drive hardening, but they are still re-run
             on every later depth to confirm they stay defeated)
        depth += 1, repeat
```

Retirement is the key mechanic the user asked for: once a model is defeated it stops
steering the teacher, because its shortcut is already gone. Hardening then targets only
the models still passing.

---

## 1. Archive the current run first

Move existing attempts and reports to `archive/v3/` before starting. Keep `versions/`
in place — those are the lineage seeds. Print what was archived.

## 2. Config — add to `run_config.yaml`

```yaml
feedback_loop:
  seed_selection: top_k        # top_k | all | explicit
  top_k: 10                    # base versions per criterion to harden
  include_random: 4            # plus this many random non-top versions, for diversity
  explicit: []                 # version ids when seed_selection: explicit

  max_depth: 6
  stop_when_all_fail: true
  retire_failed_students: true # defeated students stop driving hardening
  retest_retired: true         # but are still run at every later depth
  min_passers_to_continue: 1

  gate_retry: 2                # teacher retries when the gate rejects
  skip_students_failing_seed: true   # exclude a student from a problem's baseline
                                     # if it already fails the unmodified seed
```

`skip_students_failing_seed` fixes a real defect in the current data: gemma-4-31b scores
2/3 on the v000 seed for one criterion, so its "failures" on hardened versions are not
attributable to hardening. Such a student is recorded but excluded from that problem's
survival statistics.

Cost control: 10+4 seeds × 3 criteria × ~6 depths × 5 students ≈ 1,260 student calls and
~250 teacher calls per family. Raise `top_k` only after reviewing one family.

## 3. `tools/harden_loop.py` — the driver

CLI:
```
python tools/harden_loop.py --family 01 [--criterion 1] [--resume] [--reset]
                            [--max-depth N] [--only-lineage L003]
```

Behaviour:

1. **Select seeds.** Read `reports/family_01_summary.csv`. Take the `top_k` base versions
   by most-negative delta, plus `include_random` others sampled deterministically from
   the remaining PASS-gated versions. Record the selection in `lineages/.../plan.json`.

2. **For each seed, run the loop above.** At every depth:
   - Run all enabled students on the current statement, scored by the existing harness
     against the seed's small tests **plus** the universal corner-case tests from
     `gen_tests.py`.
   - Save per student: `solution.py`, `raw.txt`, `trace.txt`, `verdict.json`.
   - Partition into passers and failers. Update the retirement set.
   - If no passers remain → stop, outcome `all_defeated`.
   - If depth would exceed `max_depth` → stop, outcome `max_depth`.

3. **Summarize the shortcut.** Send the passers' traces and solutions to the summarizer
   (verifier model, temperature 0) using `prompts/shortcut_summarizer.md` below. It
   returns one named shortcut plus the evidence.

4. **Harden.** Call the teacher with strategy S12, the current statement as
   `{SEED_STATEMENT}`, the hidden metadata from the original `meta.yaml`, and the
   populated `{FEEDBACK_BLOCK}` (the shortcut summary, passer/failer counts).

5. **Gate.** Run the existing gate. On `FAIL` or `FLAG`, retry the teacher up to
   `gate_retry` times, appending the gate's reason to the prompt. If still rejected,
   stop the lineage with outcome `exhausted` and keep the last valid depth as final.

6. **Record and continue.**

## 4. Output layout

```
lineages/family_01/criterion_1_npc/L001/
├── lineage.json          # base version id, per-depth summary, outcome
├── d000/                 # the base version (copied, not symlinked)
│   ├── statement.md
│   └── attempts/<student>/{solution.py,raw.txt,trace.txt,verdict.json}
├── d001/
│   ├── statement.md
│   ├── edit.json         # S12, shortcut targeted, teacher raw, parent, gate retries
│   ├── gate.json
│   ├── shortcut.json     # summarizer output for the depth that produced this
│   └── attempts/<student>/...
└── d002/ ...
```

`lineage.json` per depth: `depth, passers[], failers[], retired[], n_active,
shortcut_name, gate_result`. Plus a top-level `outcome` of `all_defeated` |
`max_depth` | `exhausted`, and `depth_to_defeat` mapping each student to the depth where
it first failed (null if never).

## 5. `prompts/shortcut_summarizer.md`

```
You are analysing why several models solved a programming problem correctly.

You will see the problem statement, and for each model that solved it: its reasoning
trace and its final solution.

Find the SINGLE most important shortcut these models shared - the specific step, cue, or
recognition that let them reach a correct approach without deeply reasoning about the
problem's structure. Look for: a word or phrase that triggered recall of a known problem,
a number that revealed the structure, a phrasing that let them skip analysis.

If the models genuinely reasoned from first principles and you find no shortcut, say so.

Respond with a single JSON object and nothing else:

{
  "shortcut_found": "yes" | "no",
  "shortcut_name": "a short label, e.g. 'two-category phrasing triggers bipartite recall'",
  "evidence": "the specific phrases from the traces that show this, quoted briefly",
  "affordance_in_statement": "the exact text in the statement that enables it",
  "removal_suggestion": "how to remove this affordance without changing the task"
}
```

Feed `affordance_in_statement` and `removal_suggestion` into the teacher's feedback block
so the edit is targeted rather than vague.

## 6. Feedback block (replaces the placeholder in `teacher_user_template.md`)

```
OBSERVED STUDENT BEHAVIOUR ON THE CURRENT VERSION
-------------------------------------------------
{N_ACTIVE} models still solve this problem. {N_RETIRED} have already been defeated by
earlier versions and no longer steer these edits.

Shared shortcut used by the models that still succeed:
  {SHORTCUT_NAME}
Evidence from their reasoning:
  {EVIDENCE}
The text in the current statement that enables it:
  {AFFORDANCE}
Suggested removal:
  {REMOVAL_SUGGESTION}

Remove exactly this affordance with the smallest edit that works. Do not rewrite parts of
the statement that are not implicated. All hard constraints still apply.
```

## 7. `tools/report_lineage.py`

CLI: `python tools/report_lineage.py --family 01`

Writes `reports/family_01_lineages.csv`: one row per (criterion, lineage, depth, student)
with `verdict, retired_flag, shortcut_name, gate_result`.

Prints:
- **Survival curve** per criterion: number of students still passing at depth 0,1,2,…
  This is the headline — it should decline. If it is flat, hardening is not working.
- **Depth-to-defeat** per student: the median depth at which each model first fails.
  A robust model survives deeper; this is a per-model difficulty ranking.
- **Lineage outcomes**: how many reached `all_defeated` vs `max_depth` vs `exhausted`.
- **Shortcut taxonomy**: the most frequent `shortcut_name` values across lineages —
  which affordances models rely on most. This is a genuine finding on its own.
- **Base-version yield**: which starting versions produced lineages that fully defeated
  the panel, grouped by their original strategy.

Replace delta as the primary metric. Delta over 5 binary outcomes is too coarse — that is
why 70% of the current results are +0. Survival depth is continuous, monotone, and
directly meaningful.

## 8. Manual run order

```bash
python tools/harden_loop.py   --family 01 --criterion 1        # start with one criterion
python tools/report_lineage.py --family 01
```

Resume after interruption with the same command; add `--reset` to rebuild. Use
`--only-lineage L001 --max-depth 2` for a cheap smoke test before committing to the full
selection.

## Constraints

- Never write to `dataset/`.
- Retired students are still executed at every later depth (`retest_retired: true`);
  only their traces are withheld from the teacher.
- The gate is unchanged and remains mandatory at every depth.
- Teacher sees the hidden metadata; students never do.

## Done

Build the archive step, config, `harden_loop.py`, the summarizer prompt, the feedback
block, and `report_lineage.py`. Run nothing. Then stop.

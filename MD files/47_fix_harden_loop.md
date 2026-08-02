# 47 — Fix: harden_loop dies before the gate, silently

> **Build/edit only. Run nothing.**

## Evidence

All 14 lineages returned `outcome: exhausted, final_depth: 0`. In `lineage.json`:
`gate_result: null`, and no `d001/` directory exists anywhere. `grep` over `logs/` found
only rejections from the earlier batch run (`family01_run.log`, version ids `v007`…),
none from `harden_loop`.

The summarizer succeeded — `shortcut_name` is populated. So the loop died between
"shortcut named" and "d001 written", and left no record of why.

Two problems: a **silent failure** (no diagnostics) and whatever **caused** it.

---

## Part A — Instrumentation (do this first, it is why we are blind)

Nothing in the teacher/gate step is persisted on failure. Fix that.

1. **Write `logs/harden_loop.log`.** One line per step per lineage/depth:
   `lineage, depth, step (students|summarize|teacher|gate), status, detail`.
   `harden_loop.py` currently logs nothing to file.

2. **Persist every teacher attempt, including failures.** Create the depth directory
   *before* calling the teacher, and write:
   ```
   d001/teacher_attempt_1.txt     # raw response, verbatim, always
   d001/teacher_attempt_1.json    # {parsed: bool, parse_error, elapsed_s}
   d001/teacher_attempt_2.txt     # on retry
   ```
   A depth directory containing only failed attempts and no `statement.md` is a valid,
   informative end state.

3. **Persist gate results even when rejecting** — `d001/gate.json` with the verdict and
   full reason, on every attempt.

4. **Record why the lineage stopped.** Add to `lineage.json`:
   ```json
   "stop_reason": "teacher_parse_failure" | "teacher_api_error" | "gate_rejected"
                  | "all_defeated" | "max_depth" | "no_shortcut_found",
   "stop_detail": "…"
   ```
   `exhausted` with no detail is not actionable.

---

## Part B — The likely cause: output format mismatch

`generate_versions.py` works and uses **tag-delimited** teacher output, because strict
JSON is unreliable for multi-line markdown statements. `harden_loop.py` is new and
requests JSON. That would fail identically on every lineage — matching what we observe.

**Fix: make the S12 teacher call use the same tag-delimited format that already works.**
Do not maintain two output contracts. Replace the JSON instruction in the teacher prompt
used by `harden_loop.py` with:

```
Respond using exactly these tags, with no other text:

<STATEMENT>
the complete rewritten statement in markdown
</STATEMENT>
<RATIONALE>
two or three sentences on what you changed and which reasoning step it now forces
</RATIONALE>
<PRESERVED_ANSWER>
one sentence on why every answer is unchanged
</PRESERVED_ANSWER>
<PRESERVED_CLASS>
one sentence on why the complexity class is unchanged
</PRESERVED_CLASS>
<RISK>
the most likely way this could be judged ambiguous, or "none"
</RISK>
```

Reuse the existing tag parser and salvage path from `generate_versions.py` — import it,
do not reimplement. If `<STATEMENT>` is present and non-empty, treat the attempt as
usable even if other tags are missing.

**Verify before anything else:** run the loop for one lineage at depth 1 with the
instrumentation from Part A and read `teacher_attempt_1.txt`. That file will show
immediately whether the teacher is returning prose, JSON, tags, or an API error.

---

## Part C — The summarizer names affordances the teacher may not touch

From the taxonomy:

```
n=40 constraint triggers backtracking recall
n <= 40 constraint triggers backtracking
lexicographical requirement maps to greedy backtracking order
```

Bounds and tie-break rules are **immutable** under the gate's I/O-contract rule. The
summarizer is telling the teacher to remove things the gate will always reject. Even
after Part B, this produces guaranteed-failing edits.

Add to `prompts/shortcut_summarizer.md`, before the response format:

```
IMMUTABLE ELEMENTS. These cannot be changed and must NOT be proposed for removal:
- numeric bounds and their values (n, m, limits)
- the input format and the output format
- any tie-break rule (for example "lexicographically smallest")
- the examples' values

If the shortcut you identify depends on an immutable element, do not propose removing
it. Instead, either (a) propose changing how that element is PRESENTED - stated
indirectly through the scenario rather than as a bare inequality - or (b) look for the
next most important shortcut that is in mutable text, or (c) report shortcut_found: "no"
if the only affordances are immutable.
```

Add a field to the response:
```
"affordance_is_mutable": "yes" | "no"
```
`harden_loop.py` must skip an edit attempt where this is `"no"` and re-request the next
shortcut, rather than sending a doomed instruction to the teacher.

---

## Part D — One rejection must not kill the lineage

Currently a failed S12 ends the lineage at depth 0. Add a fallback ladder: on failure at
a depth, try in order —

1. **S12** with the named shortcut (as now).
2. **S12 with the next-ranked shortcut**, if the summarizer offered one.
3. **S07 (constraint indirection)** — the correct tool when the affordance is a bound:
   restate the bound through the scenario without changing its value.
4. **S02 or S08** at `aggressive` — a general reframe with no specific target.

Only after the ladder is exhausted does the lineage stop, with
`stop_reason: "ladder_exhausted"`. Config:

```yaml
feedback_loop:
  fallback_ladder: [S12_primary, S12_secondary, S07, S02_aggressive]
  ladder_attempts_per_depth: 4
```

---

## Part E — What the data already tells us (report this, do not try to fix it)

Half the taxonomy is structural:

```
graph 3-coloring recall
3-coloring problem identification
graph coloring problem identification
```

Models recognise 3-coloring from *three categories + pairwise conflict + cannot share*.
That structure **is** the problem. It cannot be removed by rewording, at any intensity.

This is a genuine finding and a real limit on surface hardening. Record it: add a
`structural_floor` flag to any shortcut whose `affordance_in_statement` is the core task
description rather than incidental wording, and report the proportion. It belongs in the
paper's limitations, not in another round of prompt tuning.

Also note the panel is thin: `gemini-3-flash-lite` passed all 14 lineages and was never
defeated; `gpt-oss-20b` fell in 1 of 14; `qwen3.5-flash` and `gpt-4o-mini` already fail
many base versions at depth 0; `gemma-4-31b` is skipped for failing the seed. Effectively
two strong students and two weak ones.

---

## Order of work

1. Part A (instrumentation).
2. Part B (output format).
3. Re-run one lineage, depth 1, and read `teacher_attempt_1.txt`. **Report what it
   contains before continuing.** If Part B was the cause, a `d001/statement.md` now
   appears.
4. Parts C and D only after the teacher step is confirmed working.

## Done

Apply Parts A–D, add the Part E flag, run nothing. Then stop and report what changed.

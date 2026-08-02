# 43 — Agentic Phase: Prompts and Strategy Library

> **Build files only. Do not call any API.** Write these files verbatim into
> `agentic/prompts/` and `agentic/strategies/`.

Prompt quality determines version quality, so these are specified exactly rather than
described. Write them as given.

---

## prompts/teacher_system.md

```
You are an expert problem author for a computational-complexity benchmark. You rewrite
programming problem statements so that models which genuinely reason about algorithmic
structure still succeed, while models that rely on surface pattern matching fail.

You are given a seed problem, its true complexity class, and its intended algorithm.
You know the truth because you are authoring, not being tested.

HARD CONSTRAINTS. A rewrite that violates any of these is worthless and will be
discarded:

1. IDENTICAL ANSWERS. For every possible input, the correct output must be exactly what
   it was for the seed. You are changing how the problem is presented, never what it
   asks. The existing reference solution must remain correct without modification.

2. IDENTICAL I/O CONTRACT. Input format, output format, all numeric bounds, and any
   tie-break rule (for example "lexicographically smallest") must carry over exactly.
   Reword them freely; never change what they specify.

3. UNCHANGED COMPLEXITY CLASS. The rewritten problem stays in the same class as the
   seed. You may make the class harder to recognise. You may never change what it is.

4. NO CLASS VOCABULARY. Never write: NP-complete, NP-hard, polynomial, exponential,
   intractable, bipartite, tree, DAG, acyclic, 2-SAT, 3-SAT, matching, clique, cover,
   knapsack, or any reduction or algorithm name. Never hint at difficulty. Describe
   structure through its mechanics instead.

5. UNAMBIGUOUS. A careful, competent reader must still arrive at exactly one correct
   interpretation. Difficulty must come from the reasoning required, never from vague
   wording, missing information, or contradiction. If you cannot make it harder without
   making it unclear, make a smaller edit.

6. WORKED EXAMPLE. Keep at least one input/output example, rewritten to match your new
   framing. Its values must stay consistent with the seed.

Required sections in the rewritten statement, in order: title, time and memory limits,
description, Input, Output, at least one Example.

Respond with a single JSON object and nothing else:

{
  "statement": "the complete rewritten statement in markdown",
  "rationale": "two or three sentences on what you changed and which reasoning step it now forces",
  "preserved_answer": "one sentence explaining why every answer is unchanged",
  "preserved_class": "one sentence explaining why the complexity class is unchanged",
  "risk": "the single most likely way this rewrite could be judged ambiguous, or 'none'"
}
```

---

## prompts/teacher_user_template.md

```
SEED PROBLEM
------------
{SEED_STATEMENT}

HIDDEN METADATA (you see this; the models being tested never do)
----------------------------------------------------------------
True complexity class: {CLASS}
Intended algorithm: {INTENDED_ALGORITHM}
Why this class: {REDUCTION_NOTE}

STRATEGY FOR THIS VERSION
-------------------------
Strategy: {STRATEGY_NAME}
{STRATEGY_INSTRUCTION}

Intensity: {INTENSITY}
{INTENSITY_INSTRUCTION}

{FEEDBACK_BLOCK}

Produce the rewritten statement now, as a single JSON object.
```

`{FEEDBACK_BLOCK}` is empty on the first round. On later rounds it is:

```
OBSERVED STUDENT BEHAVIOUR ON THE CURRENT VERSION
-------------------------------------------------
{N} models attempted this problem. {N_PASSED} passed.

Shared reasoning pattern in their traces:
{TRACE_SUMMARY}

Target this pattern. Remove whatever let them shortcut to the answer, while keeping
every hard constraint intact.
```

---

## prompts/student_system.md

Must match the main study's fixed prompt, so hardened versions are comparable to the
baseline. Copy it verbatim from `conventions/prompt_template.md` — do not write a new
one. If that file has a system and a user part, mirror both here.

---

## prompts/verifier_system.md

```
You are checking whether a rewritten programming problem statement is well formed. You
are not solving it.

You will see an ORIGINAL statement and a REWRITTEN statement.

Answer these four questions independently:

1. SAME TASK. Does the rewritten statement ask for exactly the same thing as the
   original, for every possible input? Consider the input format, the output format,
   the bounds, and any tie-break rule.

2. UNAMBIGUOUS. Could a careful reader arrive at more than one reasonable
   interpretation? Quote the specific phrase if so.

3. SOLVABLE. Is all information needed to solve it present?

4. EXAMPLE CONSISTENT. Does each worked example agree with the rules as stated?

Respond with a single JSON object and nothing else:

{
  "same_task": "yes" | "no" | "unsure",
  "same_task_reason": "...",
  "unambiguous": "yes" | "no" | "unsure",
  "ambiguity_quote": "the offending phrase, or ''",
  "solvable": "yes" | "no",
  "example_consistent": "yes" | "no" | "unsure",
  "overall": "pass" | "flag" | "fail"
}

Use "flag" whenever you are unsure. A human reviews every flag.
```

---

## strategies/PLAN.md

```markdown
# Strategy plan

12 strategies × 3 intensities = 36 versions per criterion, matching
`versions_per_criterion: 36`. Version numbering is deterministic given the run seed:
v001..v012 light, v013..v024 moderate, v025..v036 aggressive, strategies in id order
within each block.

v000 is reserved for the unmodified seed, used as the baseline in reports.

Not every strategy fits every class. Where a strategy is marked "class:" it is only
planned for those criteria; the planner substitutes the next applicable strategy so the
count stays at 36.

Adjust the count by editing `versions_per_criterion`; the planner scales by dropping
from the aggressive block first.
```

## strategies/INTENSITY.md

```markdown
# Intensity levels

**light** — Minimal edit. Change only the specific words or phrases the strategy
targets. The statement should read as a close variant of the seed. Lowest risk of
ambiguity; use as the control point for how much surface change matters.

**moderate** — Rewrite the description freely while keeping the same scenario domain.
Restructure sentences, reorder information, replace terminology throughout. The Input
and Output sections may be reworded but must specify the same thing.

**aggressive** — Full re-authoring. New scenario, new vocabulary, new narrative
structure. The reader should not recognise it as a variant of the seed. All hard
constraints still apply, and clarity is still mandatory — aggressive means thoroughly
rewritten, never vague.
```

## strategies/ — one file per strategy

Each file has an id, a one-line summary, the instruction text injected into
`{STRATEGY_INSTRUCTION}`, and which classes it applies to.

### S01_lexical_cue_removal.md
```
id: S01
summary: Remove the words that let a model recall the textbook problem.
classes: all

Identify every word or number in the seed that acts as a direct trigger for recalling a
known problem — the count of categories, a named structure, a characteristic phrase.
Replace each with wording that specifies the same thing without the trigger. The reader
must derive from the mechanics what they previously got from the keyword.
```

### S02_domain_transplant.md
```
id: S02
summary: Same structure, entirely different real-world scenario.
classes: all

Move the problem into a different domain that is a genuine structural fit — the
entities, relations, and constraints must map one to one onto the seed. Do not merely
rename; rebuild the scenario so the new domain's own logic explains each constraint. A
reader who knows the seed should not recognise it from the setting.
```

### S03_operational_structure.md
```
id: S03
summary: Describe the special structure through its mechanics, never by name.
classes: all

Where the seed relies on a structural property, state that property as a set of
operational rules about how the data is built or behaves. The reader must infer the
structure by reasoning about the rules. Never state the property itself, and do not make
the rules so indirect that the structure becomes uncertain — a careful reader must be
able to establish it.
```

### S04_downward_misdirection.md
```
id: S04
summary: Make a hard problem present as if it had an easy shortcut.
classes: NPC

Frame the problem so its surface features resemble a tractable variant: emphasise
regularity, suggest the data is well behaved, foreground properties that would matter if
a shortcut existed. Every statement you make must be true and every constraint must
remain exactly as in the seed. You are shaping emphasis and expectation, never facts. A
model that reasons carefully will still see the real difficulty.
```

### S05_upward_misdirection.md
```
id: S05
summary: Make an easy problem present as if it needed heavy machinery.
classes: P, INFEASIBLE

Frame the problem so it appears to require exhaustive search: emphasise the size of the
space, describe the objective in general terms, avoid foregrounding the restriction that
makes it tractable. State that restriction plainly but without emphasis — it must be
present and unambiguous. A careful reader finds it and takes the efficient route.
```

### S06_infeasibility_camouflage.md
```
id: S06
summary: Hide the reason no solution exists.
classes: INFEASIBLE

Present the problem as an ordinary task to be solved, with the contradiction distributed
across separate constraints rather than stated in one place. Never claim a solution
exists. The impossibility must remain fully derivable from the stated constraints; you
are removing the signposts, not the evidence.
```

### S07_constraint_indirection.md
```
id: S07
summary: State bounds indirectly so the reader must derive them.
classes: all

Express numeric bounds through the scenario rather than as bare inequalities — a
capacity, a headcount, a physical limit that implies the number. The derived value must
be exact and unambiguous, and every bound in the seed must still be recoverable. Do not
force arithmetic that could plausibly be done two ways.
```

### S08_narrative_embedding.md
```
id: S08
summary: Embed in a realistic scenario where every detail is load-bearing.
classes: all

Write the problem as a situation someone would actually face, with enough context that
the constraints feel motivated. Every detail you add must be relevant — it either
specifies a constraint, clarifies the objective, or defines the data. Do not pad with
irrelevant description; that measures distraction, not reasoning.
```

### S09_nonbinding_constraints.md
```
id: S09
summary: Add true constraints that do not change the answer.
classes: all

Add one or two constraints that are genuinely satisfied by every valid input under the
seed's bounds, so the answer is unchanged for every input. The reader must determine
that they are not binding. Verify carefully that your added constraints cannot exclude
any input the seed permitted — if in doubt, do not add it.
```

### S10_compositional_framing.md
```
id: S10
summary: Present the task as one step inside a larger workflow.
classes: all

Situate the problem as a stage in a bigger process, with the preceding and following
stages described briefly. What is actually required — the input, the computation, the
output — must remain exactly the seed's. The reader must isolate the real task from its
surroundings.
```

### S11_inverted_presentation.md
```
id: S11
summary: Reorder so the objective arrives after the constraints.
classes: all

Restructure the description so the reader encounters the data model and constraints
before learning what is being asked. This prevents matching a known problem from the
first sentence and forces the constraints to be read on their own terms. Section order
(title, limits, description, Input, Output, Example) is fixed; reorganise within the
description.
```

### S12_feedback_targeted.md
```
id: S12
summary: Attack the specific shortcut observed in student reasoning traces.
classes: all
requires: feedback

Only for rounds where student traces are available. Read the shared reasoning pattern in
the feedback block, identify the single step that let the models bypass the intended
reasoning, and remove exactly that affordance with the smallest possible edit. Leave the
rest of the statement alone.
```

---

## Wiring notes

- `generate_versions.py` loads a strategy file, injects its instruction into
  `{STRATEGY_INSTRUCTION}` and the intensity text into `{INTENSITY_INSTRUCTION}`.
- Teacher temperature is 0.9 for diversity; verifier is 0.0 for consistency.
- If the teacher returns unparseable JSON, retry once with a short reminder to return
  only JSON, then record the failure and move on.
- `edit.json` stores strategy id, intensity, all five teacher JSON fields, the raw
  response, and the timestamp. The `risk` field feeds the human-review queue: any
  version where `risk` is not "none" is worth a closer read.

## Done

Write the files. Confirm the tree under `agentic/prompts/` and `agentic/strategies/`.
Run nothing. The user executes the pipeline manually for Family 01.

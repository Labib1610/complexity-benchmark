# Multi-Turn Prompt Templates

For a given family, each turn uses that family's per-criterion `statement.md` as the
"problem at this class," wrapped as a conversation turn.

## Turn 1 (all conditions)
Send the statement of the first class in the sequence verbatim, using the same
system prompt and user message format as the main study.

## Turn k > 1 — Implicit condition
The shift is embedded in a constraint change; the class name is never mentioned.
The constraint wording is derived from the `constraint_delta` field in `meta.yaml`,
reworded to describe only the mechanical change:

```
Turn k (implicit):
"Now assume the following change to the problem: {CONSTRAINT_DELTA_REWORDED}.
Keep solving in the same format."
```

`CONSTRAINT_DELTA_REWORDED` strips any complexity labels from `meta.yaml`'s
`constraint_delta` and rephrases it as a neutral constraint change.

Example (family 01, NPC -> P transition):
  meta.yaml constraint_delta: "shifts reduced 3->2; removes NP-hardness entirely"
  Reworded: "The factory now runs only two shifts instead of three."

## Turn k > 1 — Explicit condition
The new structure is named directly:

```
Turn k (explicit):
"The problem has now changed. {CRITERION_STATEMENT_FULL}
Solve this new version."
```

Here CRITERION_STATEMENT_FULL is the full `statement.md` of the target criterion,
identical to what is sent in a fresh main-study prompt.

## Control condition (same_class)
Turn 1 and Turn 2 use different instances of the SAME criterion (same class,
different graph/input parameters). This isolates whether any performance change
is due to context accumulation rather than class shift.

## Recording
After each turn the driver:
1. Extracts code from the assistant response.
2. Evaluates the extracted code against the target criterion's test cases.
3. Records (turn_index, class_label, condition, verdict) as one row.

This produces a per-sequence trajectory:
  family -> model -> sequence -> [turn_1_verdict, turn_2_verdict, ...]

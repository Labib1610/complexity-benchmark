You are analysing why several models solved a programming problem correctly.

You will see the problem statement, and for each model that solved it: its reasoning
trace and its final solution.

Find the SINGLE most important shortcut these models shared - the specific step, cue, or
recognition that let them reach a correct approach without deeply reasoning about the
problem's structure. Look for: a word or phrase that triggered recall of a known problem,
a number that revealed the structure, a phrasing that let them skip analysis.

If the models genuinely reasoned from first principles and you find no shortcut, say so.

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

Respond with a single JSON object and nothing else:

{
  "shortcut_found": "yes" | "no",
  "shortcut_name": "a short label, e.g. 'two-category phrasing triggers bipartite recall'",
  "evidence": "the specific phrases from the traces that show this, quoted briefly",
  "affordance_in_statement": "the exact text in the statement that enables it",
  "affordance_is_mutable": "yes" | "no",
  "structural_floor": "yes" | "no",
  "secondary_shortcut_name": "the next most important shortcut in MUTABLE text, or ''",
  "removal_suggestion": "how to remove or re-present this affordance without changing the task"
}

Set "affordance_is_mutable" to "no" when the affordance is an immutable element above.
Set "structural_floor" to "yes" when the affordance IS the core task description itself
(the intrinsic structure of the problem) rather than incidental wording - such a shortcut
cannot be removed by any rewording.

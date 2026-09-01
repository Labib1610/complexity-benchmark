You are analysing how several models attempted one programming problem, to help make the
statement hard for ALL of them AT ONCE.

You will see the problem statement, and for EVERY model: its verdict (solved / wrong /
error), its reasoning trace, and its solution. Read the ones that FAILED as carefully as
the ones that solved it — understanding why a model already failed is what stops a future
edit from accidentally making it succeed again (a regression).

Your goal is to find the SINGLE affordance that ALL surviving (still-solving) models rely
on, so one edit can defeat them together. Only if no such common affordance exists should
you fall back to per-survivor shortcuts.

IMMUTABLE ELEMENTS — cannot be changed, must NOT be proposed for removal:
- numeric bounds and their values (n, m, limits)
- the input format and the output format
- any tie-break rule (e.g. "lexicographically smallest")
- the examples' values

If an affordance depends on an immutable element, propose changing how it is PRESENTED
(indirectly through the scenario, not as a bare inequality), or target the next affordance
in mutable text, or report shortcut_found: "no".

Respond with a single JSON object and nothing else:

{
  "shortcut_found": "yes" | "no",
  "shortcut_name": "short label for the primary affordance to target",
  "evidence": "the specific phrases from the traces that show it, quoted briefly",
  "affordance_in_statement": "the exact statement text that enables it",
  "affordance_is_mutable": "yes" | "no",
  "structural_floor": "yes" | "no",
  "secondary_shortcut_name": "next most important shortcut in MUTABLE text, or ''",
  "removal_suggestion": "how to remove or re-present the affordance without changing the task",

  "survivor_shortcuts": [
    {"student": "<id>", "shortcut": "what let this survivor solve it", "affordance": "the enabling text"}
  ],
  "common_affordance": "the SINGLE affordance ALL survivors rely on, or null if none is shared",
  "defeated_student_causes": [
    {"student": "<id>", "why_failed": "the specific reasoning error", "fragile": true|false}
  ],
  "recommended_edit": "the one edit most likely to defeat all survivors at once",
  "regression_risk": "which already-defeated students this edit might accidentally restore, or ''"
}

Set "affordance_is_mutable" to "no" when the affordance is an immutable element.
Set "structural_floor" to "yes" when the affordance IS the core task itself (intrinsic
structure) rather than incidental wording — such a shortcut cannot be reworded away.
Set "common_affordance" to null unless every surviving model genuinely depends on the same
thing. When it is non-null it is the priority target: one edit defeats everyone.
For each defeated model set "fragile": true if a small wording change could flip it back to
solving (so the teacher knows to protect that defeat).

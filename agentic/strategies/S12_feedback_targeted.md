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

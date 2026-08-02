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

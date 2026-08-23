You are grading a rewritten programming problem statement on four independent quality
criteria. You are NOT solving it.

You will see an ORIGINAL statement and a REWRITTEN statement. Judge the REWRITTEN one,
using the ORIGINAL only as the reference for what the task is supposed to be.

Score each criterion on an integer scale from 0 to 5, and give exactly one sentence of
justification for each. Be strict: reserve 5 for statements that leave no room for doubt.

G1 — UNAMBIGUITY.  Could a careful reader arrive at more than one reasonable
     interpretation? 0 = several defensible readings; 5 = exactly one reading.

G2 — COMPLETENESS.  Is every piece of information needed to solve it present (bounds,
     formats, tie-break rules, edge cases)? 0 = information is missing; 5 = fully specified.

G3 — FAITHFULNESS.  Does the rewrite ask for exactly the same thing as the original, for
     every possible input — same input meaning, same output meaning, same bounds, same
     tie-break rule? This is the same-task judgement. 0 = it asks a materially different
     question; 5 = it is provably the same question. Do not award 5 if any bound, format,
     or tie-break rule differs in substance from the original.

G4 — NATURALNESS.  Does it read like a problem a person would write? 0 = machine-generated
     or contrived; 5 = natural and idiomatic.

Respond with EXACTLY these tags and nothing else. Put a single integer inside each score
tag and one sentence inside each justification tag:

<G1_unambiguity>N</G1_unambiguity>
<G1_justification>one sentence</G1_justification>
<G2_completeness>N</G2_completeness>
<G2_justification>one sentence</G2_justification>
<G3_faithfulness>N</G3_faithfulness>
<G3_justification>one sentence</G3_justification>
<G4_naturalness>N</G4_naturalness>
<G4_justification>one sentence</G4_justification>

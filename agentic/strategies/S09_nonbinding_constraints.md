id: S09
summary: Add true constraints that do not change the answer.
classes: all
perturbation_family: semantic_expansion

Add one or two constraints that are genuinely satisfied by every valid input under the
seed's bounds, so the answer is unchanged for every input. The reader must determine
that they are not binding. Verify carefully that your added constraints cannot exclude
any input the seed permitted — if in doubt, do not add it.

FORMAL STATEMENT REQUIRED. State each added constraint formally in your rationale, in a
form that can be checked against a concrete input — for example "sum of all weights <=
10^6" or "no vertex has degree > n-1". The gate will evaluate your constraint against
every existing test input; if any input violates it, the constraint is binding, the
answer may change, and the rewrite is rejected.

Prefer constraints that follow arithmetically from the seed's own bounds. Do not invent a
constraint you cannot state precisely.

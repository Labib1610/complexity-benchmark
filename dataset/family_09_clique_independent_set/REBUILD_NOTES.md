# Family 09 (Clique / Independent Set) — Rebuild Notes

Rebuilt following the family_04 template. This is a **graph** family, so it also required the
biggest structural change so far: the three arms are now **unified on one task** (independent set),
fixing the audit's B4 semantic-switch violation.

## What was wrong (audit findings for family 09)

- **B4** — the three arms were three *different* things: criterion 1 was **clique** (decision +
  witness), criterion 2 was **maximum independent set on a bipartite graph** (a different task, a
  two-campus schema, integer-only output), criterion 3 was a **clique** decision. A performance gap
  could not be attributed to a single complexity switch.
- **B5** — criterion 3 asked for a clique of size **r > n** and required a constant `NO`;
  `print("NO")` passed every test.
- **B6** — criterion-2 inputs were byte-identical to inputs in families 08 and 11.

## What changed

The family is now unified on **INDEPENDENT SET** — "find a group of *k* users, no two of whom are
friends (an all-strangers group), and report one" — with **one input schema** (`n m k` then edges)
and **one output contract** (`YES` + k vertices / `NO`) across all three criteria. The A/B switch is
now exactly the graph class.

### Criterion 1 (NPC) — general graph
- Reference: an independent set of size k is a clique of size k in the **complement**; solved by
  bitset branch-and-bound on the complement. Genuine hard-NO = dense graph with k = maxIS+1;
  hard-YES = planted independent set on the highest-indexed vertices (found last by a C(n,k)
  baseline). Ground truth (max IS) computed in the generator, so k is always correct. n ≤ 46.

### Criterion 2 (P) — bipartite graph (the one switch)
- Same task/schema/output; the switch is that the graph is bipartite (the "two-camp" structure),
  which makes independent set polynomial. Reference: 2-colour to recover the two sides,
  Hopcroft-Karp matching, **König's theorem** for the max independent set, and a **constructive
  König witness** (MIS = V minus the min vertex cover from alternating reachability). ~0.42 s at
  n = 50000 vs the 2 s limit (gate 12).
- The word describing the graph class is kept out of the statement (leakage rule); the two-camp
  wording conveys it and the solver recovers the structure by 2-colouring.

### Criterion 3 (INFEASIBLE) — certificate task (B5)
- Redesigned into an infeasibility-certificate task with **two mechanisms**: `SIZE` (k > n) and
  `COMPLETE` (the graph is complete, so the max independent set is 1 < k). Output is the certificate,
  checked by `validator.py`. **A constant program fails** — verified: constant `NO`, `SIZE`, and
  `COMPLETE` all score WRONG_ANSWER.

## Correctness testing

The C1 (complement B&B) and C2 (König matching + witness) references were **verified against a
brute-force independent-set solver** on 200 random graphs each, across all k values — checking both
YES witnesses (independent, exactly k vertices) and NO decisions (against the brute-force maximum).
All passed.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.012 s ≤ 5 s, C2 0.42 s ≤ 2 s, C3 0.015 s ≤ 2 s.
- Constant / single-mechanism programs all fail C3.
- `release_check`: family 09 clean on G7 and G9 (global gameable arms 3→2, duplicate groups 21→20).

## Honest limitation

Same gradeable-NPC ceiling as the other families: the branch-and-bound reference (a competent exact
solver) solves every C1 case in ~0.01 s. The tier separates C(n,k) subset enumeration from B&B; it
does not prove hardness against a competent solver. True SOTA-resistance needs phases P2–P3.

## Regeneration

```
python tools/gen_family_09.py --criterion 1 --n <n> --seed <s> --kind <yes|no>       # general
python tools/gen_family_09.py --criterion 2 --n <n> --seed <s> --kind <yes|no>       # bipartite
python tools/gen_family_09.py --criterion 3 --n <n> --seed <s> --kind <size|complete> # certificate
```

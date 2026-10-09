# Family 08 (Vertex Cover / Guard Placement) — Rebuild Notes

Rebuilt following the family_04/09 template. Vertex cover is the dual of independent set, so the
polynomial (bipartite) arm reuses the same Koenig matching machinery verified for family 09.

## What was wrong (audit findings for family 08)

- **B4** — the arms were inconsistent: criterion 1 was general vertex-cover **decision + witness**
  (`n m k`), while criterion 2 was **minimum-vertex-cover SIZE** on a bipartite graph with a
  two-wing `nA nB` schema and integer-only output — a different task, output, and schema.
- **B6** — criterion inputs were byte-identical to families 10 and 11 (resolved earlier by reseeding
  those partners; family 08 itself was left unchanged at that point).

Criterion 3 was already a proper **certificate** task (output k+1 pairwise-independent corridors — a
matching lower bound proving no size-k cover exists), so it was never gameable (G7 passed for it).

## What changed

The family is now unified on **vertex cover: decide whether k guards can watch every corridor, and
report them** — one schema (`n m k` + edges), one output (`YES` + guard vertices / `NO`) across
criteria 1 and 2. The A/B switch is exactly the graph class.

### Criterion 1 (NPC) — general graph
- Kept the bounded-search-tree (FPT, O(2^k·m)) decision + witness reference. n ≤ 54, k ≤ 18.

### Criterion 2 (P) — bipartite graph (the one switch)
- Rewritten from bipartite-min-cover-SIZE to the **same vertex-cover decision + witness** on the
  unified `n m k` schema. Reference: 2-colour to recover the two wings, Hopcroft-Karp matching,
  **Koenig** minimum vertex cover `(A\Z) ∪ (B∩Z)`, decide `|cover| ≤ k` and output the cover.
  ~0.41 s at n = 50000 vs the 2 s limit (gate 12). The graph-class word is kept out of the statement
  (leakage rule); the "two wings" wording conveys it and the solver recovers it by 2-colouring.

### Criterion 3 (INFEASIBLE) — unchanged
- Already an instance-specific certificate (k+1 independent corridors). Non-gameable; left as is.

## Correctness testing

C1 (general FPT) and C2 (bipartite Koenig) references were **verified against a brute-force minimum
vertex cover** on 250 random graphs each, across all k values — checking YES witnesses (a valid cover
of size ≤ k) and NO decisions (against the brute-force minimum). All passed.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.04 s ≤ 5 s, C2 0.41 s ≤ 2 s, C3 0.09 s ≤ 2 s.
- `release_check`: all four automated gates remain green (G1, G7, G9, G16).

## Honest limitation

Same gradeable-NPC ceiling as the other families: the FPT reference (a competent exact solver, fast
for k ≤ 18) solves every C1 case quickly. The tier separates the C(n,k) subset baseline from FPT
branching; it does not prove hardness against a competent solver. True SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_08.py --criterion 1 --k <k> --seed <s> --coverable <yes|no>   # general
python tools/gen_family_08.py --criterion 2 --n <n> --seed <s> --kind <yes|no>        # bipartite
python tools/gen_family_08.py --criterion 3 --n <n> --m <m> --k <k> --seed <s>        # certificate
```

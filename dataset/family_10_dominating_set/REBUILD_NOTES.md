# Family 10 (Dominating Set / Sensor Placement) — Rebuild Notes

Rebuilt following the family_04/08/09 template. Completes the graph-cluster (08 vertex cover, 09
independent set, 10 dominating set), each now a clean general-vs-tractable pair.

## What was wrong (audit findings for family 10)

- **B4** — criterion 1 was general dominating-set **decision + witness** (`n m k`), while criterion 2
  was minimum-dominating-set **SIZE** on a tree with a rooted parent-list schema (`n` then
  `child parent` links) and integer-only output — a different task, output, and schema.
- **B6** — criterion-1 inputs were byte-identical to family 08 (resolved earlier by reseeding
  family 10's NPC cases during the dedup pass).

Criterion 3 was already an instance-specific certificate (report the smallest link-free location — an
undominatable vertex under budget 0), so it was never gameable (G7 passed for it).

## What changed

The family is now unified on **dominating set: decide whether k sensors can cover every location, and
report them** — one schema (`n m k` + undirected edges), one output (`YES` + sensor vertices / `NO`)
across criteria 1 and 2. The A/B switch is exactly the graph class.

### Criterion 1 (NPC) — general graph
- Kept the closed-neighbourhood bitset branch-and-bound (decision + witness). n ≤ 48.

### Criterion 2 (P) — tree (the one switch)
- Rewritten from min-dominating-set SIZE (parent-list schema) to the **same dominating-set decision +
  witness** on the unified `n m k` edge-list schema. Reference: root the tree and run the standard
  **3-state tree DP** (in-set / dominated-by-child / undominated) for the minimum dominating set,
  reconstruct one witness top-down, decide `|set| ≤ k`. Linear; **~0.62 s at n = 200000** (gate 12).
  The graph-class word is kept out of the statement (leakage rule); "loop-free hierarchy with n−1
  links" conveys it.

### Criterion 3 (INFEASIBLE) — unchanged
- Already a certificate (smallest link-free location). Non-gameable; left as is.

## Correctness testing

The C2 3-state tree DP (with witness reconstruction — the most intricate DP in the rebuild) was
**verified against a brute-force minimum dominating set** on 400 random trees, across all k values —
checking YES witnesses (a valid dominating set of size ≤ k) and NO decisions. All passed.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.03 s ≤ 5 s, C2 0.62 s ≤ 2 s, C3 0.07 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation

Same gradeable-NPC ceiling: the branch-and-bound C1 reference solves every case quickly. The tier
separates a subset baseline from the pruned search; it does not prove hardness against a competent
solver. True SOTA-resistance needs P2–P3.

## Regeneration

```
python tools/gen_family_10.py --criterion 1 --k <k> --seed <s> --dominatable <yes|no>          # general
python tools/gen_family_10.py --criterion 2 --n <n> --seed <s> --kind <yes|no> --shape <...>   # tree
python tools/gen_family_10.py --criterion 3 --n <n> --m <m> --seed <s> --at high               # certificate
```

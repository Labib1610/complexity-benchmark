# Family 14 (Steiner Tree / Network Extension) — Rebuild Notes

Rebuilt per the audit's per-family guidance: "keep the terminal schema; use a tractable structural
promise such as tree topology, without changing the objective."

## What was wrong (audit findings for family 14)

- **B4** — criterion 1 was Steiner tree (`n m t` + required sites + weighted edges), but criterion 2
  had been switched to a minimum-spanning-tree over *all* vertices on a different `n m` schema (no
  required-sites line) — a schema change from the paired criterion.

Criterion 1 (Dreyfus-Wagner, min cost) runs in 0.17 s at t ≤ 10 — no timing problem. Criterion 3 was
already an instance-specific certificate (smallest required site with no incident cabling), with
varied outputs (3, 4, 20, 26, 30, 34, 40). Both left as is.

## What changed

Criterion 2 is unified onto the **same schema as criterion 1** (`n m t` + required sites + weighted
edges) with one structural promise: **the cabling graph is a tree**. The objective is unchanged
(minimum total cost to connect the required sites).

### Criterion 2 (P) — tree graph (the one switch)
- Rewritten from MST-over-all-vertices to **Steiner tree on a tree**: the minimum subtree connecting
  the required sites is unique — an edge belongs to it iff removing it leaves a required site on each
  side. Root the tree, count required sites per subtree, sum the weights of qualifying edges. O(n),
  **~0.47 s at n = 200000**. Same min-cost integer output as criterion 1 (judge stays exact).

## Correctness testing

The tree-Steiner reference was **verified against a brute-force per-edge cut check** on 500 random
weighted trees (all terminal counts). All matched.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 0.17 s ≤ 5 s, C2 0.47 s ≤ 2 s, C3 0.01 s ≤ 1 s.
- `release_check`: all four automated gates remain green.

## Honest limitation / note

Family 14's output is a single cost number (no witness tree), so it is judged by exact optimum and
does not support partial-credit approximation scoring without an output-contract change (a witness
tree). The C1 tier separates a weak baseline from the Dreyfus-Wagner O(3^t) DP; the gradeable size is
capped by that DP (t ≤ 10). True SOTA-resistance needs the sealed P2–P3 evaluation.

## Regeneration

```
python tools/gen_family_14.py --criterion 1 --n <n> --t <t> --seed <s>          # general Steiner
python tools/gen_family_14.py --criterion 2 --n <n> --t <t> --seed <s>          # tree graph
python tools/gen_family_14.py --criterion 3 --n <n> --m <m> --t <t> --seed <s> --at <pos>  # unconnectable
```

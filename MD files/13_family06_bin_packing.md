# 13 — Fill Family 06: Cargo Loading (Bin Packing)

> Follow `08_START_family_filling.md`. Target: `dataset/family_06_bin_packing/`.

## Domain framing

Load items of given weights into containers of fixed capacity. NPC variant: indivisible items, fixed number of bins. P variant: items are divisible (fractional). Infeasible: an item heavier than any container.

## Criterion 1 — NP-complete (Bin Packing decision)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given `n` indivisible item weights, bin capacity `C`, and a number of bins `k`, decide whether all items fit into `k` bins; output an assignment (item → bin) or `NO`.
- **Input:** `n k C` then `n` weights. `1 ≤ n ≤ 18`, weights ≤ C.
- **Output:** `YES` + `n` integers (bin index 1..k per item, lexicographically smallest valid assignment by item order), else `NO`. If lexicographic is heavy, `judge: custom` "any valid packing" with a validator checking each bin's load ≤ C and exactly k bins used at most. Pick one.
- **Reference:** backtracking assigning each item to the lowest feasible bin (with symmetry pruning: don't open a new empty bin index beyond the first empty one). Deterministic.

## Criterion 2 — P (fractional bin packing)

- **Class:** P. **Letter:** B.
- **Problem:** items are **divisible** (you may split any item across containers). Given total of item weights and capacity `C`, the minimum number of bins is `ceil(total / C)`; output that number and a greedy fill.
- **Input:** `n C` then `n` weights (can be split). `1 ≤ n ≤ 2e5`.
- **Output:** the minimum number of containers = `ceil(sum(weights)/C)`. (Optionally also a fill description, but keep output simple and unique → `exact`.)
- **Reference:** sum weights, integer ceil division. O(n). Never say "fractional relaxation"; just state items may be divided.

## Criterion 3 — Infeasible (oversized item)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** indivisible items and capacity `C`, but **at least one item's weight exceeds `C`**. That item fits in no container; loading is impossible. Report it.
- **Input:** `n C` then `n` weights; guaranteed some weight > C.
- **Output:** the smallest index of an item whose weight exceeds `C`.
- **Judge:** `exact`.
- **Reference:** scan for first weight > C, print its index.

## Test cases

- C1: items that fit in k bins (`YES`), items that don't (`NO`), n=1.
- C2: a few weight/capacity combos checking the ceil arithmetic, including exact multiples.
- C3: two instances with a known oversized item.

Generate `.out`, run `reference_check`, fix, report, wait for `14`.

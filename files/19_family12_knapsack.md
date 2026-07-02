# 19 — Fill Family 12: Investment Portfolios (Knapsack)

> Follow `08_START_family_filling.md`. Target: `dataset/family_12_knapsack/`.

## Domain framing

Choose investments to maximize total return without exceeding a budget. NPC: indivisible investments with large numbers. P: divisible (fractional) investments. Infeasible: zero budget with all positive costs.

## Criterion 1 — NP-complete (0-1 Knapsack, large values)

- **Class:** NPC. **Letter:** A.
- **Problem:** `n` indivisible investments each with cost and value, budget `B`. Maximize total value with total cost ≤ B. Output the max value and the chosen indices.
- **Input:** `n B` then `n` lines `cost value`. `1 ≤ n ≤ 40`, values/costs up to `1e9` (so value-DP and weight-DP are both too large; meet-in-the-middle over 2^(n/2) is intended).
- **Output:** the maximum achievable value, then the chosen indices (lexicographically smallest optimal set). If reconstruction tie-break is heavy, output just the max value (unique) and use `exact`; OR `judge: custom` validating cost ≤ B and value == optimal. Pick one.
- **Reference:** meet-in-the-middle: split items, enumerate half-subsets, sort one half by cost keeping a prefix-max of value, binary-search the complement. Deterministic.

## Criterion 2 — P (fractional knapsack)

- **Class:** P. **Letter:** B.
- **Problem:** investments are **divisible** — you may buy any fraction. Maximize value within budget `B`.
- **Input:** `n B` then `n` lines `cost value`. `1 ≤ n ≤ 2e5`.
- **Output:** the maximum value as a number. To keep `exact` clean, require output rounded to a fixed precision (e.g. 6 decimal places) and state that rounding in the problem; the reference produces the same rounding.
- **Reference:** greedy by value/cost ratio (sort desc, take fully until budget, then a fraction). O(n log n). State items are divisible; never say "greedy" or "fractional relaxation" as a hint about difficulty.

## Criterion 3 — Infeasible (zero budget, positive costs)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** every investment has a **strictly positive** cost, but the budget is **0**. No investment (not even a fraction, since any positive fraction costs > 0) can be made; the only achievable value is 0 with nothing bought — but the task asks to *select at least one* investment, which is impossible. Report impossibility.
  - Make the infeasibility crisp: state "you must select at least one investment" so that B=0 with positive costs is genuinely infeasible (not just "buy nothing").
- **Input:** `n B` (B=0) then `n` lines with positive costs.
- **Output:** a single line `NO`. `judge: exact`.
- **Reference:** if B=0 and a "must pick ≥1" constraint, print `NO`.

## Test cases

- C1: a small instance with a known optimum, an all-too-expensive instance (value 0 / `NO` per your convention), n=1.
- C2: divisible instances with known optimal values at the stated precision, a budget larger than total cost (buy everything).
- C3: two instances with B=0 and positive costs.

Generate `.out`, run `reference_check`, fix, report, wait for `20`.

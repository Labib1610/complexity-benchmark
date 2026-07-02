# 20 — Fill Family 13: Workload Partitioning (Partition Problem)

> Follow `08_START_family_filling.md`. Target: `dataset/family_13_partition/`.

## Domain framing

Split tasks between two identical machines so both finish at the same time (equal total duration). NPC: large durations. P: small integer durations. Infeasible: odd total (cannot be halved).

## Criterion 1 — NP-complete (Partition, large values)

- **Class:** NPC. **Letter:** A.
- **Problem:** `n` task durations; decide whether they can be split into two groups of equal sum; output one group's task indices or `NO`.
- **Input:** `n` then `n` durations. `1 ≤ n ≤ 40`, durations up to `1e9` (sum DP too large → meet-in-the-middle for subset summing to total/2).
- **Output:** `YES` + the indices of one group summing to half (lexicographically smallest such index set), else `NO`. If heavy, `judge: custom` validating the chosen subset sums to total/2. Pick one.
- **Reference:** if total is odd → `NO`; else meet-in-the-middle for a subset summing to total/2. Deterministic.

## Criterion 2 — P (small integer durations)

- **Class:** P. **Letter:** B.
- **Problem:** identical task, but durations are **small** (each ≤ 2, or ≤ some small constant) so the sum `S` is `O(n)` and the DP table `O(n·S)` is polynomial.
- **Input:** `n` then `n` small durations. `n ≤ 2000`, each duration ≤ 100, so `S ≤ 2e5`.
- **Output:** `YES` + one group's indices (lexicographically smallest) summing to S/2, else `NO`. Same convention as C1.
- **Reference:** if S odd → `NO`; else subset-sum DP to S/2 with predecessor reconstruction. O(n·S). Never say "pseudo-polynomial".

## Criterion 3 — Infeasible (odd total)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** the total of all durations is **odd**, so it cannot be divided into two equal integer halves — impossible by parity. Report impossibility.
- **Input:** `n` then `n` durations whose sum is guaranteed odd.
- **Output:** a single line `NO`. `judge: exact`.
- **Reference:** read durations, confirm/print `NO` (sum is odd).

## Test cases

- C1: an equally-splittable set (`YES`), a non-splittable even-sum set (`NO`), n=1 (`NO` unless the single duration is 0).
- C2: small-duration splittable and non-splittable even-sum cases.
- C3: two odd-sum instances.

Generate `.out`, run `reference_check`, fix, report, wait for `21`.

# 22 — Fill Family 15: Bioinformatics Alignment (Longest Common Subsequence)

> Follow `08_START_family_filling.md`. Target: `dataset/family_15_lcs/`.

## Domain framing

Find the longest sequence of symbols appearing (in order, not necessarily contiguous) in all given sequences. NPC: three or more sequences. P: exactly two sequences. Infeasible: sequences over disjoint alphabets (no common symbol at all).

## Criterion 1 — NP-complete (Multiple-sequence LCS, k ≥ 3)

- **Class:** NPC. **Letter:** A.
- **Problem:** `k` sequences; output the length of (and one instance of) their longest common subsequence.
- **Input:** `k` then `k` sequences (lowercase letters). Keep `k ≤ 5`, each length ≤ 20 (the k-dimensional DP is `O(L^k)`; bounded so it runs, but the exponential-in-k shape is the point).
- **Output:** the LCS length, then one longest common subsequence (lexicographically smallest among the longest). `exact` if you pin lexicographic; else `judge: custom` validating it is a common subsequence of max length.
- **Reference:** k-dimensional DP with reconstruction choosing lexicographically smallest. Deterministic. (For small bounds this is fine.)

## Criterion 2 — P (two sequences)

- **Class:** P. **Letter:** B.
- **Problem:** exactly **two** sequences; output the LCS length and one LCS.
- **Input:** two sequences, each length ≤ 2000.
- **Output:** the LCS length, then the lexicographically smallest LCS of that length. `judge: exact` (pin lexicographic in the reconstruction).
- **Reference:** standard 2D DP; reconstruct lexicographically smallest by preferring the smaller character when choices tie. O(L^2). Don't mention dimensionality as a difficulty hint.

## Criterion 3 — Infeasible (disjoint alphabets)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** the sequences use **mutually disjoint alphabets** (no symbol appears in more than one sequence). No symbol is common to all, so the only common subsequence is empty — there is no common subsequence of length ≥ 1. Report impossibility (length 0 with the "must be ≥ 1" framing → infeasible).
  - To make it a crisp infeasibility rather than "answer is 0", phrase the task as: "output a non-empty common subsequence, or report that none exists." Then disjoint alphabets → `NONE`.
- **Input:** `k` then `k` sequences with pairwise-disjoint character sets.
- **Output:** a single line `NONE`. `judge: exact`.
- **Reference:** intersect the alphabets; if empty intersection across all, print `NONE`.

## Test cases

- C1: three sequences with a known common subsequence, three with only single-char commonality, k with one length-1 sequence.
- C2: two sequences with a known LCS, two with LCS length 1, identical sequences (LCS = whole).
- C3: two instances with disjoint alphabets.

Generate `.out`, run `reference_check`, fix, report, wait for `23`.

# 14 — Fill Family 07: DNA/Log Assembly (Shortest Common Superstring)

> Follow `08_START_family_filling.md`. Target: `dataset/family_07_shortest_common_superstring/`.

## Domain framing

Reassemble fragments (DNA reads / log shards) into the shortest single string that contains every fragment as a contiguous substring. NPC: many fragments. P: exactly two fragments. Infeasible: a forbidden substring contradicts a required fragment.

## Criterion 1 — NP-complete (SCS, k ≥ 3 fragments)

- **Class:** NPC. **Letter:** A.
- **Problem:** Given `k` strings, output the length of (and one instance of) the shortest string containing all of them as substrings. First remove any fragment that is already a substring of another.
- **Input:** `k` then `k` fragment strings (lowercase letters). `1 ≤ k ≤ 12`, each length ≤ 20.
- **Output:** the shortest common superstring; if several share the minimum length, output the lexicographically smallest. (This makes `exact` valid. If too heavy, `judge: custom` validating that the output contains all fragments and matches the optimal length computed by the reference.) Pick one.
- **Reference:** compute pairwise overlaps; bitmask DP over orderings (TSP-style on the overlap graph) reconstructing the shortest, lexicographically smallest superstring. O(2^k · k^2). Deterministic.

## Criterion 2 — P (exactly two fragments)

- **Class:** P. **Letter:** B.
- **Problem:** exactly **two** strings; the shortest superstring is the one merging them on their maximum overlap (try both orders, take the shorter; tie → lexicographically smallest).
- **Input:** the two strings (each length ≤ 1e5).
- **Output:** the shortest common superstring of the two (lexicographically smallest on tie). `judge: exact`.
- **Reference:** compute max suffix-prefix overlap both directions (KMP/Z), merge, compare lengths, pick smaller / lexicographically smaller. O(n). Don't mention "overlap graph" or "TSP".

## Criterion 3 — Infeasible (forbidden-substring contradiction)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** fragments must all appear in the output, but there is a **forbidden substring `F`** that the output must NOT contain — and one of the required fragments itself **contains `F`**. Any superstring contains that fragment, hence contains `F`: impossible. Report which fragment forces the contradiction.
- **Input:** `k`, `k` fragments, then the forbidden string `F`; guaranteed some fragment contains `F`.
- **Output:** the smallest index of a fragment that contains `F` as a substring.
- **Judge:** `exact` (optionally `validator.py` confirming that fragment contains F).
- **Reference:** scan fragments, print smallest index containing F.

## Test cases

- C1: 3 fragments with overlaps (known SCS), fragments with no overlap (concatenation), k=1.
- C2: two overlapping strings, two with no overlap, identical strings.
- C3: two instances with a fragment containing the forbidden substring.

Generate `.out`, run `reference_check`, fix, report, wait for `15`.

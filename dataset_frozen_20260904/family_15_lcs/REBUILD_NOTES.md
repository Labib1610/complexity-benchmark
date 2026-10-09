# Family 15 (Longest Common Subsequence) — Rebuild Notes

Rebuilt following the family_04 template. LCS is an **optimization** family, so it also adds **B7**
approximation scoring, and it required a **B4** schema/canonicalization unification.

## What was wrong (audit findings for family 15)

- **B4** — criterion 2 used a *different input schema* (two bare lines, no `k` header) and demanded
  the **lexicographically smallest** LCS, while criterion 1 used a `k` header and accepted any
  longest motif. Two mismatches (schema + canonicalization) between the paired arms.
- **B5** — criterion 3 used mutually disjoint alphabets and required a constant `NONE`;
  `print("NONE")` passed every test.
- **B7 / gate 3** — this optimization family had **no `objective.py`**, so the time-budget study
  could not score partial credit.
- **B6** — inputs overlapped with family 07 and within the family.

## What changed

The family is unified on **shared motif = longest common subsequence** (report length + one longest
motif) with one schema (`k` header then k sequences) and one output contract (any longest motif).

### Criterion 1 (NPC) — k ≥ 3 sequences
- Kept the k-dimensional O(L^k) DP reference. Statement bound tightened to 3 ≤ k ≤ 5 (the genuine
  multi-sequence regime). Added `objective.py` (B7); reseeded per case (B6).

### Criterion 2 (P) — k = 2 sequences (the one switch)
- **Unified schema**: now begins with a `k` header (k = 2), exactly like criterion 1.
- **Unified output**: any longest motif is accepted; the lexicographically-smallest requirement is
  removed. Reference is the standard O(n·m) 2D DP with a simple optimal-path reconstruction —
  ~0.28 s at L = 2000 vs the 2 s limit (gate 12). Added `objective.py` (B7).

### Criterion 3 (INFEASIBLE) — certificate task (B5)
- Redesigned into an **instance-specific certificate**: since any shared motif must start with a
  letter common to all sequences (and in particular to sequence 1), the model prints `BLOCK` then,
  for each distinct letter of sequence 1, a pair `c j` naming a sequence j that lacks c. This proves
  no letter is shared, so no non-empty motif exists. **A constant program fails** — verified: `NONE`
  scores WRONG_ANSWER. The certificate is instance-specific (the letters and witnessing indices vary),
  which is what makes it non-gameable despite the single infeasibility mechanism.

## B7 approximation scoring (gate 3)

`objective.py` (C1 and C2) exposes `value()` returning the motif length **if it is a common
subsequence of every sequence**, else 0. Verified through the real `studies/time_budget/scoring.py`:
exact → ratio 1.0; a shorter valid motif (length 1 vs optimal 5) → ratio 0.2.

## Correctness testing

The C1 (k-dim DP) and C2 (2D DP) references were **verified against a brute-force LCS solver**
(exhaustive subsequence enumeration) on 300 random instances each — matching both the length and a
valid witness. All passed.

## Verification

- `reference_check` passes all 3 criteria (statement leakage clean).
- References within the declared limit: C1 2.25 s ≤ 5 s (k=5, L=16), C2 0.28 s ≤ 2 s, C3 0.02 s ≤ 2 s.
- Constant `NONE` fails C3.
- `release_check`: family 15 clean on G7 and G9 (global gameable arms 2→1, duplicate groups 20→17).

## Honest limitation

Gradeable-NPC ceiling: the reference is itself O(L^k), so a case must stay small enough for the
reference to finish under the limit. The audit notes the true hard regime is *variable k*, but a
gradeable case cannot use large k. The tier separates memo-less recursion from the L^k DP; it does
not prove hardness against a competent solver. True SOTA-resistance needs phases P2–P3.

## Regeneration

```
python tools/gen_family_15.py --criterion 1 --k <k> --L <L> --seed <s> --alphabet abc   # k>=3
python tools/gen_family_15.py --criterion 2 --L <L> --seed <s> --mode <identical|low|random>  # k=2
python tools/gen_family_15.py --criterion 3 --k <k> --L <L> --seed <s>                   # disjoint
```

# 40 — Scale Family 15: Bioinformatics Alignment (LCS)

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_15_lcs/`.
>
> **Context:** in the first Main Study run, `gemma3-27b` scored TLE on this family's
> criterion 1 and its solution **hung the evaluator for 20+ minutes**. So this family already
> has NPC bite — but confirm the timeout is now enforced (the runner was hardened after that
> incident). Verify no case can hang evaluation.

## Family 15 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | k-dimensional DP, **O(L^k)** | **naive: recursive LCS without memoization, O(k^L)** | **asymptotic gap ✅** |
| 2 | P | 2-D DP, O(L²) | naive: recursive without memo, O(2^L) | **huge gap ✅** |
| 3 | INFEASIBLE | alphabet intersection, O(total) | naive: attempts LCS search first | asymptotic gap ✅ |

**Note the reference itself is exponential in k** (L^k). Keep `k` small (≤5) and grow `L`
moderately — the reference's cost is L^k, the baseline's is exponential in L. Both grow with L,
so probe carefully: you need the region where the baseline TLEs but the reference is merely
slow (offline, unlimited — so "slow" is fine).

## Criterion 1 (NPC) — memoized DP vs naive recursion

1. `tools/naive_family_15_criterion_1.py` — realistic: recursive LCS over k sequences
   **without memoization** (branch on "skip in sequence i" per position). This is a genuinely
   common model mistake and is exponential.
   - A memoized k-D DP *is* the reference — do not use that as the baseline.
2. Probe `k ∈ [3, 4, 5]` with `L ∈ [12, 16, 20, 24]`. **Hard instances: sequences over a small
   alphabet (e.g. {a,b,c}) with many partial matches** — maximizes branching.
3. Statement says `k ≤ 5, L ≤ 20`. Raise `L` to the new max where the baseline TLEs; verify the
   reference's L^k stays generatable offline (5 seqs × L=24 → 24⁵ ≈ 8M — fine).

## Criterion 2 (P) — 2-D DP, punish naive recursion

Reference is O(L²) at L ≤ 2000 → 4M, fast. Baseline = recursive LCS without memoization → 2^L,
dead by L=30. This arm bites trivially. Scale `L ∈ [100, 500, 1000, 2000]`. Include identical
strings (LCS = whole) and disjoint-ish strings (LCS = 1).

Also consider a realistic-inefficiency case: an O(L²) DP with poor constants (Python nested
lists vs arrays) may strain at L=2000 — check whether the reference is comfortable.

## Criterion 3 (INFEASIBLE) — disjoint alphabets

Reference intersects alphabets, O(total). Baseline attempts LCS search first → TLEs. Scale k
and L toward bounds with guaranteed-disjoint alphabets. Answer stays `NONE`.

## Procedure

1. `tools/gen_family_15.py` — seeded: `gen_lcs_multi(k, L, seed, alphabet="abc")`,
   `gen_lcs_two(L, seed, similarity=...)`, `gen_disjoint_alphabets(k, L, seed)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm exponential blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_15_lcs` → clean.

## EXTRA CHECK (specific to this family)
Confirm that a runaway solution on the largest criterion-1 case is **killed cleanly by the
evaluator's timeout** and recorded as TLE — it must not hang. Test explicitly:
```bash
timeout 5 python tools/naive_family_15_criterion_1.py < <largest .in> ; echo "exit=$?"
```
and verify `evaluate.py`'s runner kills it at `time_limit_s`. Report the result.

## Report
Probe curve, threshold, ramp, proof exit codes, reference gen times, bound changes, clean check,
**plus the runaway-kill confirmation**.

Then **stop and wait** for `41_scale_family16_job_shop.md`.

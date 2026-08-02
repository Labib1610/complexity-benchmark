# 41 — Scale Family 16: Factory Scheduling (Job-Shop) + FINAL PHASE WRAP-UP

> Follow `25_START_test_case_scaling.md` (corrected). Target: `dataset/family_16_job_shop/`.
> **This is the last family.** After it, run the phase-wide checks at the bottom.

## Family 16 at a glance

| Criterion | Class | Reference | Realistic baseline | Gap |
|---|---|---|---|---|
| 1 | NPC | branch-and-bound over disjunctive orderings | B&B with weaker/no bounding, or full permutation search | **same shape** — hardness from instance structure |
| 2 | P | Johnson's rule, O(j log j) | **naive: try all j! orderings, or O(j²) insertion search** | **huge gap ✅** |
| 3 | INFEASIBLE | max(p1) vs T check, O(j) | naive: attempts scheduling first | asymptotic gap ✅ |

**Criterion 1 has the narrowest window in the set** (like Family 01) — the reference and a
competent baseline share the B&B shape. Hardness must come from instance structure.

## Criterion 1 (NPC) — instance structure carries it

1. `tools/naive_family_16_criterion_1.py` — realistic: B&B over machine orderings with a
   simple lower bound (e.g. max machine load). Competent but not expert — no sophisticated
   bounding, no dominance rules.
2. Probe `j ∈ [6, 8, 10]` with `m = 3` machines and total ops ≤ ~30. **Hard instances: jobs
   with similar processing times across machines** (many near-tie orderings defeat bounding),
   and tight makespan targets.
3. Statement says `j ≤ 6, ops ≤ 18`. Raise carefully — job-shop explodes fast; the reference
   must still finish offline (which can be minutes — that's fine).
4. **If the window proves too narrow** (baseline matches the reference at every size), report
   it honestly — same situation Family 01 faced. Options: a weaker baseline is NOT acceptable
   (strawman), so the answer may be that criterion 1 needs a stronger reference (e.g. CP/SAT
   based) before it can carry the NPC arm. **That's the user's call — do not rewrite
   `reference.py`.**

## Criterion 2 (P) — Johnson's rule, huge gap

Reference is O(j log j). Baseline = try all j! orderings (or an O(j²) insertion heuristic
search) → dies by j=12. Scale `j ∈ [1e3, 1e4, 1e5, 2e5]`. Include already-sorted, reverse, and
random cases. This arm bites easily and cleanly.

## Criterion 3 (INFEASIBLE) — deadline below max p1

Reference computes `max_j p1_j`, O(j). Baseline attempts scheduling first → TLEs. Scale j
toward the bound with `T < max p1` guaranteed. Answer stays `NO`.

## Procedure

1. `tools/gen_family_16.py` — seeded: `gen_jobshop(j, m, seed)` (similar processing times),
   `gen_flowshop(j, seed, order=...)`, `gen_infeasible_deadline(j, seed)`.
2. Write realistic baselines.
3. **Probe with the baseline**; confirm blow-up.
4. 5-case ramp straddling; keep anchors, append.
5. **Generate `.out` with reference, unlimited time.** Record elapsed.
6. **Mandatory proof:** baseline exit=124 on largest cases.
7. Update `statement.md` bounds.
8. Append `scaling:` provenance.
9. `reference_check dataset/family_16_job_shop` → clean.

---

# FINAL PHASE-WIDE CHECKS (after Family 16 passes)

1. **Validate everything:**
   ```bash
   for f in dataset/family_*; do python -m harness.reference_check "$f"; done
   ```
   All 16 clean. (Uses the generous `REFERENCE_CHECK_TIMEOUT_S`, not the model limit.)

2. **Scaling coverage table.** Print a 16×3 table showing, per criterion:
   `chosen_max_size`, `baseline_tle_confirmed` (✅/❌), and number of test cases.
   **Flag every criterion where `baseline_tle_confirmed` is ❌** — those are arms that do not
   bite and must be reported to the user (expected candidates: family 01 c1, family 16 c1,
   possibly family 05 c2 / family 08 c2 where Kuhn-vs-HK is narrow).

3. **Statement/bound audit.** Confirm every `statement.md` bound matches its criterion's actual
   maximum test size. No statement may understate or overstate. List every bound changed during
   this phase.

4. **Anchors intact.** Confirm the original small hand-verifiable cases (01–04) still exist in
   every criterion and still pass. These are the ground-truth anchors — they protect against a
   silently wrong reference.

5. **Runaway safety.** Confirm `evaluate.py` kills a runaway solution at `time_limit_s` and
   records TLE (the Family 15 incident). No case may hang evaluation.

6. **Report the headline:** how many of the 16 NPC criteria now have a confirmed baseline TLE.
   That number is the phase's success metric — it is how many families can actually detect
   complexity-blindness.

## Next step for the user (state this in your report)

Re-run the Main Study against the scaled dataset:
```bash
python -m harness.generate --config runs/<new-date>_scaled/run_config.yaml   # re-generate (models see new bounds)
python -m harness.evaluate --config runs/<new-date>_scaled/run_config.yaml
```
The expectation: **NPC pass@1 should now fall below P pass@1.** That gap is the finding the
whole benchmark was built to measure.

Report completion and stop.

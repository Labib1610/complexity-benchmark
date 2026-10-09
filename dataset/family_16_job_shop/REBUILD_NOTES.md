# Family 16 (Job-Shop / Flow-Shop Scheduling) — Rebuild Notes

Rebuilt following the family_04 template. This is the family the audit flagged as **weakest**
("the gap is unreliable … only one hunted seed separates solvers") and suggested rebuilding with a
CP-SAT reference **or removing**. This pass fixes the machine-checkable gates (B5) and documents the
remaining strategic decisions honestly.

## What was wrong (audit findings for family 16)

- **B5** — criterion 3 guaranteed `T < (some job's machine-1 time)` and required a constant `NO`;
  `print("NO")` passed every test.
- **B2 (known, documented)** — the criterion-1 NPC arm does **not reliably bite**: the reference
  (Giffler-Thompson B&B) and a competent weaker-bound baseline blow up at nearly the same size, and
  the baseline is sometimes *faster*. The meta already records `baseline_tle_confirmed: false`.
- **B4 (known)** — criterion 1 is job-shop (`j m` + jobs-with-operations) while criteria 2 and 3 are
  a two-machine *flow shop* (`j [T]` + `p1 p2`), a different problem and schema.

## What changed in this pass

### Criterion 3 (INFEASIBLE) — redesigned as a certificate task (B5) ✓ fixed
- From constant-`NO` into an infeasibility-certificate task with **two mechanisms** in the same
  two-machine schema:
  - `JOB i` — job i's sequential work `p1+p2 > T` (it alone cannot finish by the deadline);
  - `LOAD c` — machine c's total serial load exceeds T.
- Output is the certificate, checked by `validator.py`. **A constant program fails** — verified:
  constant `NO`, `JOB 1`, and `LOAD 1` all score WRONG_ANSWER. The identifying index is
  instance-specific, so no constant passes.

### Verification
- `reference_check` passes all 3 criteria.
- C3 reference solves within the declared limit (0.025 s ≤ 2 s).
- Constant / single-mechanism programs all fail C3.
- **release_check G7 (constant cannot pass INFEASIBLE) now PASSES for the whole benchmark** — family
  16 was the last gameable arm.
- Family 16 has no duplicate inputs (G9), so C1/C2 were left unchanged.

## Remaining strategic decisions (flagged for the user — the audit's "or remove the family")

These are **not** machine-gated and require a design decision:

1. **NPC arm does not reliably bite (B2).** Making criterion 1 a genuine hard tier needs a stronger
   reference/calibration (e.g. a CP-SAT / SAT-backed makespan solver) so that a competent exact
   baseline is actually challenged. This is a substantial change (external solver dependency) and a
   research decision — left to the user, exactly as the audit frames it.
2. **Schema unification (B4).** Criteria 2/3 (flow shop) differ in schema from criterion 1 (job
   shop). A clean fix is to express the polynomial arm as a two-machine case *in the job-shop
   schema* (Johnson's rule), or to re-scope the family entirely. Also a design decision.
3. **Approximation objective (B7).** Job-shop/flow-shop output is a single makespan number with no
   schedule witness, so partial-credit approximation scoring would require changing the output
   contract to include a schedule (start times) that an objective can validate. Deferred.

**Recommendation:** family 16 is the strongest candidate for either a CP-SAT-backed rebuild or
removal from the benchmark, per the audit. The B5 gate is now satisfied so it no longer blocks the
automated release check; items 1–3 above are strategic and should be decided before relying on this
family for research claims.

## Regeneration

```
python tools/gen_family_16.py --criterion 3 --j <j> --seed <s> --kind <job|load1|load2>
```

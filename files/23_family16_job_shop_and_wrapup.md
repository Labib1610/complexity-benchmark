# 23 — Fill Family 16: Factory Scheduling (Job-Shop) + Final Wrap-Up

> Follow `08_START_family_filling.md`. Target: `dataset/family_16_job_shop/`. This is the LAST family. After it, do the final dataset-wide checks at the bottom.

## Domain framing

Schedule jobs on machines to finish as early as possible (minimize makespan). NPC: 3+ machines, job-shop. P: 2-machine flow-shop (Johnson's rule). Infeasible: deadline shorter than the single fastest unavoidable operation.

## Criterion 1 — NP-complete (Job-Shop, m ≥ 3 machines)

- **Class:** NPC. **Letter:** A.
- **Problem:** `j` jobs, each a sequence of operations on specified machines with given durations; `m ≥ 3` machines; each machine runs one operation at a time; operations of a job run in order. Find the minimum makespan (the decision/optimization output is the minimal completion time).
- **Input:** `j m` then for each job: its operation count followed by `(machine, duration)` pairs in order. Keep instances **small** (`j ≤ 6`, total operations ≤ ~18) so an exact branch-and-bound / disjunctive-graph search terminates.
- **Output:** the minimum makespan (a number). Unique → `exact`. (A full schedule would need a tie-break; keep output = makespan.)
- **Reference:** branch-and-bound over operation orderings on each machine (disjunctive graph), pruning by current best. Deterministic. Keep bounds small enough to finish within the time limit.

## Criterion 2 — P (2-machine flow-shop, Johnson's rule)

- **Class:** P. **Letter:** B.
- **Problem:** exactly **two** machines, and **every** job goes through machine 1 then machine 2 (same order for all jobs). Each job has a duration on each machine. Find the minimum makespan.
- **Theorem:** Johnson's rule gives the optimal sequence: jobs with `p1 ≤ p2` first (sorted asc by p1), then the rest (sorted desc by p2); compute makespan by simulating.
- **Input:** `j` then `j` lines `p1 p2`. `j ≤ 2e5`.
- **Output:** the minimum makespan. Unique → `exact`.
- **Reference:** Johnson's rule ordering, then simulate the two-machine pipeline to get makespan. O(j log j). Don't name "Johnson" or "flow-shop" as difficulty hints.

## Criterion 3 — Infeasible (deadline below minimum possible)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** a two-machine flow-shop with a required deadline `T`, but `T` is **less than the largest single operation duration on machine 1** (or less than the minimum possible makespan lower bound `max(sum p1, sum p2, max over jobs of (p1+p2))`). Even the most optimistic schedule cannot meet `T` — impossible. Report impossibility.
  - Simplest crisp version: `T < max_j p1_j` (the longest machine-1 op alone exceeds the deadline). Guarantee that in the input.
- **Input:** `j T` then `j` lines `p1 p2`; guaranteed `T < max_j p1_j`.
- **Output:** a single line `NO`. `judge: exact`.
- **Reference:** compute `max_j p1_j`; if `T < that`, print `NO`.

## Test cases

- C1: a tiny job-shop with a known optimal makespan, another small one, a single-job case.
- C2: flow-shop instances with known Johnson makespans, including already-sorted and reverse cases.
- C3: two instances with `T` below the machine-1 max.

Generate `.out`, run `reference_check dataset/family_16_job_shop`, fix flags.

---

## FINAL DATASET-WIDE CHECKS (run after Family 16 passes)

1. **Validate every family at once.** Loop over all 16 families:
   `for f in dataset/family_*; do python -m harness.reference_check "$f"; done`
   Every family must report clean (no reference mismatch, no missing `.out`, no leakage term). Fix any straggler.

2. **Confirm completeness.** For all 48 criteria verify:
   - `statement.md` is real (no PLACEHOLDER comment remains),
   - `reference.py` does not raise `NotImplementedError`,
   - `tests/` has at least two `.in`/`.out` pairs,
   - `meta.yaml` `class` matches the family table.
   Print a 16×3 table of ✅/❌ so the user sees full coverage at a glance.

3. **Full dry-run end-to-end.** Run the dry-run path (reference-as-solution) of the generate+evaluate drivers across ALL families and confirm `summary.csv` shows the reference passing every problem. This proves the entire 48-problem benchmark is internally consistent before any real model is run.

4. **Report final status:** total problems filled (should be 48), any `judge: custom` problems and their validators, and the exact commands to launch the first real model run:
   ```
   scripts/new_run.sh main
   # edit runs/<date>_main/run_config.yaml: set models + study: main
   python -m harness.generate  --config runs/<date>_main/run_config.yaml
   python -m harness.evaluate  --config runs/<date>_main/run_config.yaml
   ```

## Done

The dataset is complete (16 families × 3 criteria = 48 problems), self-validated, and dry-run-verified. The benchmark is ready for real model generation and for the constraint studies in `studies/`. Report completion to the user.

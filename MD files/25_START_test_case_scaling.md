# 25 — START OF TEST-CASE SCALING: How These Files Work

> **You are Claude Code.** The benchmark is built and all 16 families are filled and validated. A first Main Study run has completed. This phase **scales up test-case input sizes** so that the complexity distinction actually bites.
>
> The files numbered `26`–`41` each scale **one family** (families 01–16). The user will drop them one at a time. Read this file, then wait for `26`.

## Why we are doing this

The first run produced this:

```
Model            P        NPC     INFEAS   Overall
gpt-oss-20b      93.75%   100.00%  100.00%  97.92%
```

`gpt-oss` scores **higher on NP-complete than on P**. That is backwards for a
difficulty story, and it reveals the problem: **our NPC inputs are so small
(n ≤ 18–20) that a naive brute-force solution finishes inside the time limit.**
NP-completeness never actually bites. The benchmark currently measures "can you
write correct code", not "can you recognize intractability".

**The goal of this phase:** make inputs large enough that a naive exponential
solution **times out**, while our own reference solution **still finishes**. Only
then can a P-vs-NPC gap appear, and only then is the gap attributable to
complexity rather than to coding skill.

This also answers the contamination objection: a memorized exponential algorithm
gives no uplift when the memorized algorithm is too slow for the input size.

## The core constraint (read this twice)

For every criterion we need:

```
naive brute force  →  TLE on the largest case
our reference      →  finishes comfortably on the largest case
```

That window exists only because our references use *smarter* exponential
algorithms (meet-in-the-middle 2^(n/2), bitmask DP 2^n·n, branch-and-bound with
pruning) while a naive model solution often does something like plain 3^n or n!
search. The gap between those growth rates is our working room.

**The window is different for every family.** Family 04 (subset sum,
meet-in-the-middle) has huge headroom. Family 01 (3-coloring, 3^n reference) has
very little. Family 16 (job-shop branch-and-bound) has almost none. This is why
each family is scaled individually, with the ceiling **measured empirically**, not
guessed.

## Per-class expectations

| Class | Reference cost | Scaling difficulty |
|-------|----------------|--------------------|
| **P** | polynomial | Easy — scale freely toward the stated bound (e.g. n=1e5) |
| **INFEASIBLE** | usually O(n) detection | Easy — scale freely |
| **NPC** | exponential | **Hard — this is the real work; find the ceiling** |

For P problems, the point of scaling is different but still important: a *correct
but inefficient* polynomial solution (e.g. O(n²) where O(n log n) is needed)
should TLE. That is what makes the P arm meaningful.

## The fixed procedure for every family

1. **Read** the family's three `meta.yaml` files (class, intended algorithm, time limit).
2. **Write a seeded generator** `tools/gen_family_XX.py` that emits valid inputs of a
   requested size for each criterion. Fixed seed ⇒ reproducible.
3. **Probe the reference ceiling** (NPC especially): generate inputs at increasing
   size, time `reference.py` on each, find the largest size where it finishes
   comfortably (target: **≤ 25% of the problem's `time_limit_s`**, so there is margin).
4. **Emit ~5 scaled test cases on a ramp**, not all at maximum. E.g. one medium,
   two large, two near the ceiling. A ramp tells us *where* a model breaks, not
   just that it broke.
5. **Keep the existing small cases.** They are our hand-verifiable ground-truth
   anchors. Never delete them. New cases are appended with the next numbers.
6. **Generate every `.out` by running `reference.py`** on the `.in`. Never hand-write.
7. **Prove the point (mandatory):** write a deliberately naive brute-force solution
   in `tools/naive_family_XX_criterion_n.py` and confirm it **TLEs on the largest
   case** while the reference passes. If naive brute force still passes, **the
   scaling failed for that family** — go bigger or report that the family has no
   usable window.
8. **Validate:** `python -m harness.reference_check dataset/family_XX_<slug>` until clean.
9. **Record** the chosen sizes and measured timings in `meta.yaml` under a new
   `scaling:` block (see below), and report to the user.

## The `scaling:` block to add to each meta.yaml

Append (do not overwrite existing fields):

```yaml
scaling:
  ceiling_probe:
    - {size: 18, reference_s: 0.03}
    - {size: 22, reference_s: 0.41}
    - {size: 26, reference_s: 5.2}
  chosen_max_size: 24
  ramp_sizes: [14, 18, 21, 23, 24]
  naive_tle_confirmed: true
  naive_time_at_max: ">120s (killed)"
  notes: "reference is 3^n backtracking with pruning; narrow window"
```

This is the provenance that lets a reviewer (and your collaborator) see the window
was measured, not guessed.

## Important reminders

- **Do not modify `statement.md` bounds** unless the file explicitly says to. If a
  statement says `n ≤ 20` and we now test at n=24, the statement is **wrong** and
  must be updated to match — flag this to the user rather than silently diverging.
  Statement bounds and actual test sizes MUST agree.
- **Do not touch `reference.py` logic.** We use it to produce outputs; we do not
  rewrite it. If a reference is too slow to reach a useful size, report that — it
  may need a better algorithm, which is a separate decision for the user.
- Keep generators deterministic (fixed seed) and committed, so any test case can be
  regenerated.
- Work **one family at a time**. Validate before moving on.

## What to do now

Acknowledge, confirm the dataset validates and Family 1 exists, then **stop and
wait** for `26_scale_family01_graph_coloring.md`.

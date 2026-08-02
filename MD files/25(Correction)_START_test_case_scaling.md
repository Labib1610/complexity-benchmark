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

## THE CORE RULE (read this twice — it governs everything)

**Ground-truth generation and the model's time limit are COMPLETELY SEPARATE.**

```
Generating .out with reference.py  →  UNLIMITED TIME. One-time offline cost.
                                      25 s, 5 min, an hour — all fine.

The time_limit_s in meta.yaml      →  applies ONLY to models at evaluation.
                                      This is what makes NP-completeness bite.
```

The reference does **not** need to be fast. It needs to be **correct**. We run it
once, offline, with no time pressure, and cache its answer in the `.out` file.
Forever after, checking a model's output is just a string comparison — instant.

**Therefore: do NOT choose input size based on how fast the reference runs.**
That was a mistake in an earlier version of this file. Choosing sizes where the
reference is comfortable guarantees the problem is EASY — because the reference
*is* a good solution, so if it finishes in 0.4 s, any model that writes a good
solution also finishes in 0.4 s and passes. The NPC arm cannot bite there.

## How to choose NPC input size (the corrected rule)

Target the size where **a solution a competent model would plausibly write
exceeds the model's time limit.**

```
realistic good solution (e.g. pruned backtracking)  →  TLE at the model's limit
reference (same or better algorithm, run offline)   →  finishes eventually, no limit
```

Concretely, for each NPC criterion:

1. Write `tools/naive_family_XX_criterion_1.py` = **what a good model would
   actually write** (pruned backtracking, standard DP, etc.). NOT a strawman with
   pruning deliberately removed — a realistic, competent solution.
2. Find the size where **that** solution exceeds `time_limit_s`. That is your
   target size. Push INTO the exponential wall, do not back away from it.
   - You will recognize the wall by the timing curve: 0.1 → 0.5 → 4 → 40 s.
     Linear-looking growth (0.09 → 0.19 → 0.32 → 0.42) means you are nowhere
     near it — keep going.
   - Hardness varies enormously by seed near a phase transition. Select
     adversarial seeds deliberately.
3. Generate the `.out` at that size with `reference.py`, taking **as long as it
   takes**. Run it with `nohup`/background if needed. This is a one-time cost.

**The old "reference ≤ 25% of the limit" rule is DELETED. Ignore it entirely.**

If generating a single `.out` becomes impractical (many hours), THEN — and only
then — report that the reference may need a stronger exact algorithm. Correctness
matters; speed does not.

## Per-class expectations

| Class | What must fail at the model's time limit | Sizing target |
|-------|------------------------------------------|---------------|
| **P** | a *correct but inefficient* poly solution (O(n²) where O(n log n) is needed) | scale toward the stated bound (e.g. n=2e5) |
| **INFEASIBLE** | a brute-force search that ignores the impossibility shortcut | scale toward the stated bound |
| **NPC** | **a realistic, competent exact solution** (pruned backtracking, standard DP) | **push INTO the exponential wall** |

The NPC row is the one that carries the hypothesis. Get it right.

## The fixed procedure for every family

1. **Read** the family's three `meta.yaml` files (class, intended algorithm, time limit).
2. **Write a seeded generator** `tools/gen_family_XX.py` that emits valid inputs of a
   requested size for each criterion. Fixed seed ⇒ reproducible.
3. **Write the realistic baseline** `tools/naive_family_XX_criterion_n.py` — what a
   competent model would plausibly write. For NPC this is a *pruned/standard* exact
   solution, NOT a deliberately handicapped strawman.
4. **Probe with the BASELINE, not the reference.** Time the baseline at increasing
   sizes. Find where it **exceeds `time_limit_s`**. That size is your target.
   Report the timing curve; confirm you can see exponential blow-up (0.1 → 0.5 → 4
   → 40 s), not linear growth.
5. **Emit ~5 scaled test cases on a ramp** straddling that threshold — e.g. two
   below where the baseline still passes, and three at/above where it fails. The
   ramp shows *where* each model breaks, which is far more informative than a
   single pass/fail.
6. **Keep the existing small cases.** They are our hand-verifiable ground-truth
   anchors. Never delete or renumber them. New cases append with the next numbers.
7. **Generate every `.out` by running `reference.py`** on the `.in`, **with no time
   limit**. Use `nohup`/background for long ones. Never hand-write an `.out`.
   Record how long each took (provenance), but do not let it constrain size choice.
8. **Prove the point (mandatory):** confirm the **realistic baseline TLEs** at the
   model's `time_limit_s` on the largest cases. If a competent solution still
   passes, the NPC arm is not biting — go bigger or report the family has no usable
   window.
9. **Validate:** `python -m harness.reference_check dataset/family_XX_<slug>` until clean.
   (Note: reference_check compares reference output to the cached `.out`; if a
   reference is slow, this check itself may take a while. That is expected and fine.)
10. **Record** sizes, baseline timings, and reference generation times in `meta.yaml`
    under a `scaling:` block, and report to the user.

## The `scaling:` block to add to each meta.yaml

Append (do not overwrite existing fields):

```yaml
scaling:
  # timings of the REALISTIC baseline (what a competent model would write).
  # This drives the size choice.
  baseline_probe:
    - {size: 30, baseline_s: 0.18}    # passes
    - {size: 34, baseline_s: 3.1}     # passes, straining
    - {size: 38, baseline_s: 47.0}    # TLE at limit -> in the wall
  model_time_limit_s: 2
  baseline_tle_from_size: 36
  chosen_max_size: 40
  ramp_sizes: [30, 34, 36, 38, 40]
  baseline_tle_confirmed: true
  # ground-truth generation cost (informational ONLY; must not constrain sizing)
  reference_gen_seconds_at_max: 620
  notes: "pushed into the exponential wall; adversarial seeds near m~2.35n"
```

This provenance lets a reviewer see the size was chosen by **where a competent
solution fails**, not by convenience. `reference_gen_seconds_at_max` is recorded for
transparency but is explicitly NOT a constraint — it is a one-time offline cost.

## Important reminders

- **Do not modify `statement.md` bounds** unless the file explicitly says to. If a
  statement says `n ≤ 20` and we now test at n=24, the statement is **wrong** and
  must be updated to match — flag this to the user rather than silently diverging.
  Statement bounds and actual test sizes MUST agree.
- **Do not touch `reference.py` logic.** We use it to produce outputs; we do not
  rewrite it. **A slow reference is NOT a problem** — ground-truth generation is
  unlimited and offline. Only report it if a single `.out` would take many hours,
  which would make the one-time cost impractical; that is the user's call, not
  yours.
- **Never let reference speed influence input size.** Size is chosen by where the
  realistic baseline TLEs at the model's limit. Nothing else.
- Keep generators deterministic (fixed seed) and committed, so any test case can be
  regenerated.
- Work **one family at a time**. Validate before moving on.

## What to do now

Acknowledge, confirm the dataset validates and Family 1 exists, then **stop and
wait** for `26_scale_family01_graph_coloring.md`.

# 26 (CORRECTED) — Re-scale Family 01: Graph Coloring — THE TEMPLATE

> **This supersedes the earlier version of file 26.** Family 01 was scaled once
> using a flawed rule ("reference must finish in ≤25% of the time limit"). That rule
> is **deleted**. It caused us to back away from the exponential wall and settle at
> n=30, where a competent solution passes in 0.18 s — i.e. the NPC arm does not bite.
>
> Read `25_START_test_case_scaling.md` (corrected) first. Then re-do criterion 1 of
> Family 01 with the rule below. **Criteria 2 and 3 are already correct — do not
> redo them.**

## What went wrong last time (so you don't repeat it)

The previous run reported:

| n | 24 | 26 | 28 | 30 | 32 |
|---|----|----|----|----|----|
| ref s | 0.092 | 0.193 | 0.319 | 0.422 | 0.522 |

That growth is **roughly linear** — proof we were nowhere near the exponential wall.
And the report noted the real signal, then walked away from it:

> *"Worst NO instances explode (n=34 seed 4 > 25 s), so I held the ceiling at 30 to
> keep the reference < 0.5 s."*

**That n=34 explosion IS the target.** The old rule pushed us away from the only
place hardness lives. We were optimizing for the reference's convenience, when the
reference's speed is irrelevant — it runs offline, once, with no limit.

## The corrected rule for criterion 1

```
Ground truth (.out):  reference.py, UNLIMITED time, offline, one-time.
                      25 s? 10 min? Fine. Run it in the background.

Size choice:          the size where a REALISTIC competent solution
                      exceeds the model's time_limit_s (2 s).
```

## Step 1 — Define the realistic baseline (this drives everything)

Create `tools/naive_family_01_criterion_1.py` = **pruned backtracking**: try colors
1,2,3 per vertex in index order, check conflicts against already-colored neighbors,
backtrack on failure. No DSATUR ordering, no bitsets, no clever heuristics — just
the straightforward correct solution **a good model would plausibly write**.

> This is NOT a strawman. The previously committed
> `naive_family_01_criterion_1_bruteforce.py` (unpruned full 3^n) is a strawman —
> no competent model writes that. **Delete it from consideration as the baseline.**
> The whole point is: if the *realistic* solution passes, NP-completeness is not
> biting.

## Step 2 — Probe with the BASELINE until it TLEs

Use adversarial seeds near the phase transition (m ≈ 2.35·n), and specifically hunt
**hard NO instances** — the previous run found these explode (n=34 seed 4 > 25 s).
Hardness varies enormously by seed; select for the hard ones deliberately.

```bash
for n in 30 32 34 36 38 40 42; do
  for seed in 1 2 3 4 5 6 7 8; do
    python tools/gen_family_01.py --criterion 1 --n $n --seed $seed --mode hard > /tmp/p.in
    /usr/bin/time -f "n=$n seed=$seed  %e s" \
      timeout 120 python tools/naive_family_01_criterion_1.py < /tmp/p.in > /dev/null
  done
done
```

Record the curve. **You are looking for exponential blow-up** — something like
0.2 → 1 → 6 → 45 s. When you see it, you have found the wall.

- `baseline_tle_from_size` = smallest n where the baseline reliably exceeds **2 s**.
- `chosen_max_size` = comfortably past that (baseline takes ~10 s+, decisively TLE).

Based on the earlier n=34/25 s datapoint, expect the threshold somewhere around
**n ≈ 32–36**. Verify empirically; do not assume.

## Step 3 — Emit a ramp that STRADDLES the threshold

Five cases, spanning pass→fail for the baseline. If the threshold is n=34:

`ramp_sizes: [28, 32, 34, 37, 40]` → baseline passes the first two, strains at the
third, TLEs on the last two.

This ramp is scientifically valuable: it shows **where** each model breaks, not just
that it broke. Mix YES and NO verdicts (hard NO instances are the expensive ones).

**Renumber note:** Family 01 criterion 1 currently has cases 01–09 (01–04 anchors,
05–09 from the flawed scaling). Keep 01–04 (hand-verifiable anchors). **Replace
05–09** with the new ramp — they were built to the wrong rule and are not worth
keeping.

## Step 4 — Generate `.out` with UNLIMITED time

```bash
D=dataset/family_01_graph_coloring/criterion_1_npc
# no timeout; run in background if slow; record elapsed for provenance
for i in 05 06 07 08 09; do
  /usr/bin/time -f "case $i: %e s" python $D/reference.py < $D/tests/$i.in > $D/tests/$i.out
done
```

If a case takes 10+ minutes, **that is fine** — let it run. Record the elapsed time
in the `scaling:` provenance block as `reference_gen_seconds_at_max`. It is
informational only.

> If a single case would take many hours, stop and report — that is the only
> situation where the reference's algorithm becomes the user's decision.

## Step 5 — MANDATORY proof

On the largest case, confirm:

```bash
D=dataset/family_01_graph_coloring/criterion_1_npc
# realistic baseline must TLE at the model's limit (2 s)
timeout 2 python tools/naive_family_01_criterion_1.py < $D/tests/09.in > /dev/null
echo "exit=$?"   # 124 = TLE = SUCCESS. This is the whole point.
```

**Success = the realistic, competent solution TIMES OUT.** If it passes, go bigger.

Also sanity-check that the `.out` is right: the reference (unlimited) produced it,
and `reference_check` will confirm consistency.

## Step 6 — Update the statement bound

Criterion 1's statement currently says `n ≤ 30` (changed from 20 last round). Update
it again to the new `chosen_max_size`. The bound must be truthful — models reason
about difficulty from it.

## Step 7 — Provenance

Append/replace the `scaling:` block in `criterion_1_npc/meta.yaml` using the
corrected schema from file 25 (`baseline_probe`, `baseline_tle_from_size`,
`chosen_max_size`, `ramp_sizes`, `baseline_tle_confirmed`,
`reference_gen_seconds_at_max`).

## Step 8 — Validate

```bash
python -m harness.reference_check dataset/family_01_graph_coloring
```
Must be clean. Note this check re-runs the reference, so it may now take a while on
the big cases — expected and fine.

## Step 9 — Report

1. The **baseline probe curve** — show the exponential blow-up.
2. `baseline_tle_from_size` and `chosen_max_size`.
3. The ramp, with which cases the baseline passes vs TLEs.
4. **Proof line:** realistic baseline exit=124 (TLE) on the largest case.
5. Reference generation time per case (informational).
6. Statement bound change.
7. `reference_check` clean.

Then **stop and wait**. The user will confirm this recipe works before the remaining
families are scaled.

---

## Why this family is the template

If we can make **pruned backtracking TLE** on 3-coloring, we have proven the recipe
works on the family with the *narrowest* window in the set (reference and baseline
share the same 3^n shape). Every other family has more room — Family 04 (subset sum)
pits meet-in-the-middle 2^(n/2) against a naive 2^n, a genuine asymptotic gap.

Get this one right and the remaining fifteen are mechanical.

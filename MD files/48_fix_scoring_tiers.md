# 48 — Fix scoring: retirement metric, scaled tests, failure types

> **Build/edit only. Run nothing.**

Three contained changes. The loop, gate, prompts, strategies, base versions, harness, and
student panel are all unchanged.

---

## Evidence motivating this

**The survival curve was an artifact.** In L008, depths 3, 5 and 6 record all four models
as `PASS` in `verdicts`, yet `passers` reports 2 — because retirement permanently removes
a model from the count. The curve can only decline by construction. Raw per-depth pass
counts for L008 are 4, 3, 3, 4, 3, 4, 4 — flat.

**The tests could not detect intractability.** Scoring used only tiny cases (n≈4). Direct
check on the scaled cases already produced in Phase 2:

| case | n | answer | gemini-3-flash-lite | gpt-oss-20b |
|---|---|---|---|---|
| 05 | 30 | YES | 0.014 s | 0.014 s |
| 06 | 32 | YES | 0.024 s | 0.015 s |
| 07 | 34 | NO | **TLE** | 0.41 s |
| 08 | 38 | NO | **TLE** | 1.75 s |
| 09 | 40 | NO | **TLE** | 0.66 s |

gemini survived all 14 lineages across 6 depths of statement hardening, and fails on a
scaled input immediately. The agentic phase was excluding the tests that discriminate.

---

## Change 1 — Retirement is steering-only

Retirement decides **whose traces the summarizer reads**. It must not affect the
measurement.

In `harden_loop.py`, record per depth:
- `raw_passers` / `raw_failers` — every student, regardless of retirement. **This is the
  scientific metric.**
- `active_passers` — non-retired only. Steering-pool size, reported separately.

`report_lineage.py` plots the survival curve from `raw_passers`. Keep the active count as
a secondary line, labelled as the steering pool.

---

## Change 2 — Three test tiers, scored separately

Do **not** merge the tiers into one pass/fail. They measure different things, and merging
them makes the result uninterpretable.

`seed.py` copies all three tiers from `dataset/`:

| tier | source | measures |
|---|---|---|
| `anchor` | seed cases `01`–`04` | basic correctness; hand-verifiable |
| `corner` | `gen_tests.py` output | coding correctness, edge cases |
| `scaled` | Phase-2 cases `05`–`09` | intractability |

`harden_loop.py` scores each solution against all three and records per tier:
`{passed, total, verdicts[]}`. Add to `verdict.json`:

```json
{
  "tier_results": {
    "anchor": {"passed": 4, "total": 4},
    "corner": {"passed": 10, "total": 12},
    "scaled": {"passed": 2, "total": 5, "first_tle": "07"}
  },
  "overall_all_tiers": "WRONG_ANSWER"
}
```

Config controls which tier drives retirement:

```yaml
feedback_loop:
  scoring_tier: all        # all | anchor+corner | scaled
```

Default `all`. `anchor+corner` reproduces the previous behaviour for comparison.

**Availability:** scaled cases exist only where Phase 2 ran (Family 01 all criteria;
Family 02 criteria 2 and 3). If a criterion has no scaled tier, record
`"scaled": null` and continue — do not fail.

---

## Change 3 — Failure types in the report

`verdict.json` already distinguishes TLE from WRONG_ANSWER; the report pools them. Split
it, because the distinction is the thesis:

- **TLE on the scaled tier** → the model wrote an intractable algorithm. On-thesis.
- **WRONG_ANSWER on anchor/corner** → a coding slip (the lexicographic tie-break, most
  likely). Off-thesis noise.

`report_lineage.py` adds:
- Per-depth breakdown: `PASS / WRONG_ANSWER / TLE / RUNTIME_ERROR`, split by tier.
- **Two survival curves per criterion:** one scored on `anchor+corner` (does statement
  hardening work?) and one on `scaled` (does instance hardness bite?). Plotting them
  together is the paper's central figure.
- Per student: `scaled_tier_pass_rate` and `first_tle_case`.

CSV gains: `tier`, `tier_passed`, `tier_total`, `verdict_type`, `first_tle_case`.

---

## What to expect

gemini will likely fail the scaled tier on every version, at every depth, regardless of
statement. **That is the result, not a bug** — it is instance hardness dominating framing.
The loop then effectively steers on gpt-oss alone. Report the panel collapse honestly
rather than treating it as failure.

Keeping the tiers separate is what makes this interpretable: the anchor+corner curve
isolates framing difficulty, the scaled curve isolates instance difficulty.

---

## Note: timing fragility

gpt-oss passes case 08 in 1.75 s against a 2 s limit. Machine load could flip that to TLE
and make results irreproducible. Add to `report_lineage.py` a warning for any scaled-tier
pass within 20% of the limit, listing the cases. Do not change limits or test cases —
just surface it.

---

## Re-run implications (for the user, not for you)

The 240 base versions are reused unchanged. The loop must re-run from d0, because with
scaled tests different students pass, so different traces reach the summarizer and the
lineages diverge from depth 0. Wall-clock rises: a TLE burns the full limit.

## Order of work

1. Change 1 (metric) — smallest, unblocks correct reading of existing data.
2. Change 2 (tiers) — `seed.py` then `harden_loop.py`.
3. Change 3 (report).
4. Re-run `report_lineage.py` on the **existing** criterion-1 lineages first. Change 1
   alone will show the true flat curve from data already on disk, with no API calls.

## Done

Apply the three changes, run nothing, report what changed.

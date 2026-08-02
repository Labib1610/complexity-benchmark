# 49 — Fix the report, then re-run with tiers

> **Steps 1 and 3 are for Claude Code (edit only, run nothing). Steps 2 and 4 are for the
> user to run.**

---

# STEP 1 — Claude Code: fix two bugs in `report_lineage.py`

## Bug 1 — the `raw` curve is not raw

The report prints `raw d0:2.9 d1:2.6 d2:2.3 d3:2.1 d4:1.9 d5:1.7 d6:1.6`. That is
byte-identical to the pre-fix curve, so `raw` is still reading the `passers` field.
`passers` excludes retired students by construction, which is the artifact we are
removing.

Recounting directly from `verdicts` across the same 14 lineages gives:

```
d0:2.9  d1:3.3  d2:3.1  d3:3.4  d4:3.1  d5:3.1  d6:3.4
```

Flat, slightly rising. That is the correct series.

**Fix:** for every depth, compute

```python
raw_passers = [s for s, v in (depth.get("verdicts") or {}).items() if v == "PASS"]
```

Never derive `raw` from `passers`. Old lineage files have no `raw_passers` field, so the
report must recount from `verdicts` when the field is absent, and use it when present.

Also fix the `steer` line: it currently prints `d0:4.0 d1:2.9 d2:2.6 …`, which is the old
series shifted by one — it is reporting pool size, not active passers. `steer` must be
`len(depth["passers"])`, i.e. non-retired students that passed.

Skip depths with an empty `verdicts` dict (the final depth of each lineage has none).

## Bug 2 — the CSV dropped from 392 rows to 0

Rows lacking tier data are being skipped. Lineages produced before tiers existed have no
tier data and must still be written, with `tier`, `tier_passed`, `tier_total`, and
`first_tle_case` left null/empty. Emit one row per (criterion, lineage, depth, student) as
before; tier columns are optional, not required.

## Also confirm from file 48

State plainly in your report whether each is already applied, and apply it if not:
- `harden_loop.py` writes `raw_passers` and `active_passers` per depth.
- `seed.py` copies all three tiers (`anchor` = 01–04, `corner`, `scaled` = 05–09).
- `harden_loop.py` scores each solution per tier and writes `tier_results` in
  `verdict.json`.
- `report_lineage.py` prints the verdict-type breakdown (PASS / WRONG_ANSWER / TLE /
  RUNTIME_ERROR) per tier, and warns on any scaled-tier pass within 20% of the limit.
- `run_config.yaml` has `feedback_loop.scoring_tier: all`.

Run nothing. Report what you changed.

---

# STEP 2 — User: verify the fix (no API calls)

```bash
python tools/report_lineage.py --family 01
```

**Expected:**

```
raw    d0:2.9  d1:3.3  d2:3.1  d3:3.4  d4:3.1  d5:3.1  d6:3.4
```

and the CSV back to **392 rows**.

`a+c` and `scaled` will still say "no data — tier absent". That is correct: these
lineages predate tiers. Tiers populate only on a re-run.

If `raw` still reads 2.9→1.6, Bug 1 is not fixed. Stop and report.

---

# STEP 3 — Claude Code: confirm tier scoring is wired

Only after Step 2 passes. Verify on Family 01 that `seed.py` will pick up cases 05–09 as
the `scaled` tier from `dataset/family_01_graph_coloring/*/tests/`, and that
`scoring_tier: all` makes a problem fail if any tier fails.

Handle a missing scaled tier gracefully: `"scaled": null`, no crash. Families other than
01 have no scaled cases yet.

Run nothing.

---

# STEP 4 — User: re-run criterion 1 with tiers

```bash
python tools/harden_loop.py --family 01 --criterion 1 --reset
python tools/report_lineage.py --family 01
```

Cost is comparable to the last run plus extra wall-clock, since a TLE burns the full
limit instead of finishing fast.

**What to look for:**
- `a+c` curve — should stay flat, confirming statement hardening does nothing.
- `scaled` curve — should sit far lower, and gemini-3-flash-lite should fail it at every
  depth.
- Verdict breakdown — TLE concentrated in the scaled tier, WRONG_ANSWER in anchor/corner.

The two curves side by side are the paper's central figure.

---

## Summary of changes

| Change | Where | Effect |
|---|---|---|
| `raw` recounts from `verdicts` | `report_lineage.py` | curve becomes flat, artifact removed |
| `steer` = `len(passers)` | `report_lineage.py` | correct steering-pool line |
| CSV writes tierless rows | `report_lineage.py` | 392 rows restored |
| `raw_passers` / `active_passers` recorded | `harden_loop.py` | future runs need no recounting |
| three tiers copied and scored | `seed.py`, `harden_loop.py` | scaled cases finally used |
| verdict-type split per tier | `report_lineage.py` | separates intractability from coding slips |

Unchanged: loop structure, validity gate, all prompts, the strategy library, the 240 base
versions, the harness, the student panel and student prompt.

# 51 — Frontier Evaluation of Final Statements (with timing, TLE ignored)

> **Build the tool, then run it.** Purpose: independently assess whether the hardened
> statements are genuinely good and genuinely hard, using two strong models that were
> not students.

---

## Why

The 4-student panel tells us the problems are hard *for that panel*. It does not tell us
whether the statements are **well-formed** or whether the difficulty **transfers to
frontier models**. This evaluation answers both.

Key change in method: **TLE is not a verdict here.** We run each solution to completion
(generous ceiling) and record wall-clock time per test case. Difficulty then becomes a
*continuous* measure — a frontier model finishing a case in 0.01 s means the case is
easy; taking 45 s means it is genuinely hard. Binary pass/fail throws that away.

---

## Model selection — read carefully

Two evaluators, both strong, both outside the student panel:

| slot | model | check before use |
|---|---|---|
| A | GPT-5.6 Sol | never used in any role — clean |
| B | a strong Gemini | **must NOT be `gemini-3.1-pro`** |

**Contamination warning.** `gemini-3.1-pro` is the **teacher** — it wrote every one of
these statements. Asking it to solve its own output is not an independent check. Use a
different Gemini (e.g. `gemini-3.6-pro`) and confirm it is not currently the H5 solver,
a student, or the held-out model. Record the exact model strings used.

Verify both strings resolve before running.

---

## What to evaluate

**Both the seed and the final statement of every lineage**, so hardening's effect on
frontier models is measurable rather than assumed:

- `d000/statement.md` — the base version (baseline)
- `d<final_depth>/statement.md` — the hardened endpoint

Across 42 lineages that is **84 statements × 2 models = 168 generation calls**.

Without the d000 baseline we cannot distinguish "hard because we hardened it" from
"hard all along" — so do not skip it.

---

## Tool: `tools/frontier_eval.py`

```
python tools/frontier_eval.py --family 01 [--models A B] [--depths seed,final] [--reset]
```

### Behaviour

1. For each lineage, read `lineage.json` to find `final_depth`. Collect the `d000` and
   `d<final_depth>` statements.
2. For each (statement, evaluator model): send the **same fixed student prompt** from
   `prompts/student_system.md` — do not write a new prompt, comparability depends on it.
3. Extract code exactly as the student path does (`strip_thinking` then `extract_code`).
4. Execute against all three tiers: `anchor`, `corner`, `scaled`.
5. **Timing, not TLE:**
   - Use a hard ceiling of **300 s per case** purely to prevent runaways.
   - Record `elapsed_s` for every case.
   - Verdicts are `PASS`, `WRONG_ANSWER`, `RUNTIME_ERROR`, or `EXCEEDED_CEILING`.
     **Do not emit TLE and do not apply the problem's `time_limit_s`.**
   - A case that is correct but slow is a `PASS` with a large `elapsed_s`. That is the
     point of this run.
6. Also record generation time (`gen_elapsed_s`) and token counts if the API returns them.

### Output layout

```
frontier_eval/family_01/criterion_1_npc/L008/
├── seed/<model_id>/{solution.py, raw.txt, result.json}
└── final/<model_id>/{solution.py, raw.txt, result.json}
```

`result.json`:

```json
{
  "lineage": "L008",
  "which": "final",
  "depth": 4,
  "model": "gpt-5.6-sol",
  "gen_elapsed_s": 22.4,
  "tiers": {
    "anchor": {"passed": 4, "total": 4,
               "cases": [{"name":"01","verdict":"PASS","elapsed_s":0.012}]},
    "corner": {"passed": 12, "total": 12, "cases": [...]},
    "scaled": {"passed": 5, "total": 7,
               "cases": [{"name":"09","verdict":"PASS","elapsed_s":47.3}]}
  },
  "solved_all": false,
  "max_elapsed_s": 47.3,
  "total_elapsed_s": 61.8
}
```

Atomic writes, checkpointed — skip any (statement, model) that already has `result.json`
unless `--reset`.

---

## Tool: `tools/report_frontier.py`

```
python tools/report_frontier.py --family 01
```

Writes `reports/frontier_eval.csv` (one row per lineage × which × model × tier × case)
and prints:

**1. Correctness — did the frontier model solve it, ignoring time?**

| criterion | model | seed solved | final solved | delta |
|---|---|---|---|---|

Report per tier as well as overall.

**2. Runtime — how hard are the cases?** This is the headline for this run.

| criterion | model | which | median case time | p90 | max | slowest case |
|---|---|---|---|---|---|---|

Also report `max_elapsed_s` distribution: how many statements have a case exceeding
1 s / 10 s / 60 s. A case that takes a frontier model 60 s is objectively hard.

**3. Reference comparison.** For the same cases, report the reference solution's runtime
alongside. Ratio `frontier_time / reference_time` is a clean difficulty signal — near 1
means the model matched the intended algorithm; 100× means it wrote something far worse.

**4. Seed vs final.** Per criterion: did solve-rate drop, and did runtime rise, from d000
to the final depth? This is the direct measure of whether hardening affected frontier
models at all.

**5. Cross-check against the student panel.** Per criterion, frontier solve-rate versus
the 4-student solve-rate on the same statements. Large gap ⇒ our panel is weak. Small gap
⇒ the difficulty is real and transfers.

---

## Cost

168 generation calls plus local execution. Estimate **$15–25**, dominated by GPT-5.6 Sol
at $5/$30 per M tokens. Execution time may be substantial since we no longer cut off slow
solutions — budget a few hours if several cases run near the 300 s ceiling.

---

## Run order

```bash
python tools/frontier_eval.py --family 01 --only-lineage L001    # smoke test, 1 lineage
cat frontier_eval/family_01/criterion_1_npc/L001/final/*/result.json

python tools/frontier_eval.py --family 01                        # full run
python tools/report_frontier.py --family 01
```

Smoke-test one lineage first and confirm `elapsed_s` is populated per case and no TLE
verdicts appear.

---

## Guardrails

- Do not modify `../dataset/`, `seeds/`, `versions/`, or `lineages/`.
- Do not reuse the teacher model as an evaluator.
- Use the existing student prompt unchanged.
- Record exact model strings and run dates in `reports/frontier_eval_meta.json`.

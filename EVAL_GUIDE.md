# Evaluation Guide

Scores the model panel against **every** statement in `final_dataset/` (all
`versions/` + all `lineages/` depths), under **4 time constraints** (1s, 2s, 5s,
10s), and writes results to a **separate** directory: `../evaluation/`.

## Fast by default: "derive" mode

Generating + grading a separate solution for each of the 4 limits is ~4× the work,
and the worst-case tests (designed to beat 300 s solvers) TLE identically at 1/2/5/10 s —
so grading them at 10 s to learn what 1 s already says is pure waste.

**Default `EVAL_MODE=derive`:** generate **one** solution per (statement, model), run it
**once** at the largest limit while recording each test's elapsed time, then **derive**
the 1/2/5/10 s results (a case passes at limit L iff it is correct *and* finished within
L s). Identical pass/fail numbers for the hard tiers, ~4× fewer API calls (~$11 vs ~$44),
and ~2× less grading. Set `EVAL_MODE=per_limit` to restore the original (one generation
per limit, the model told that exact limit).

Rough grading wall on this 12-core box (derive, max limit 10 s): **~64 h total**, of which
**family_01 ≈ 45 h** (its 130 large worst-case tests). The other 11 families together ≈ 19 h.
So the practical plan is: run the 11 smaller families first (done in ~a day), and run
family_01 on its own in the background.

## One command

```bash
cd /home/labib/Desktop/labib_codes/research_codes/np_completeness/complexity-benchmark
python evaluate.py
```

That runs the whole thing (all 12 families, NPC statements, all 4 limits) and
prints the report tables at the end. **Interrupt any time (Ctrl-C) and re-run the
exact same command** — it resumes where it stopped (one checkpoint JSON per
statement×model×limit; done tasks are skipped).

Run it from your own terminal so it survives; for a long unattended run:
```bash
nohup python evaluate.py > ../evaluation/run.log 2>&1 &
tail -f ../evaluation/run.log
```

## Common variations (env vars)

```bash
FAM=17 python evaluate.py            # a single family
FAM=17,20 python evaluate.py         # a few families
EVAL_CRIT=1,2 python evaluate.py     # also score the P statements (default: NPC only)
LIMITS=2,10 python evaluate.py       # a subset of time limits
EVAL_MAX_STMTS=2 FAM=17 python evaluate.py   # quick smoke test (2 statements only)
EVAL_WORKERS=8 python evaluate.py    # more concurrency
```

## What each model sees

For an NPC statement under an `X`-second constraint, the statement's
`Time limit:` line is set to `X s` and a strict scoring note is appended: *the
program must terminate within X seconds per test case or that case scores 0.* No
new statement files are created — the edit is applied on the fly per constraint.
(P statements, if enabled, are passed through unchanged — the constraint edit is
"only for NP", per spec.) Each solution is then run against **all** curated test
cases for that family under a hard wall-clock limit equal to `X`.

## Failure handling (never freezes a bad result)

The run never stops on an API failure. It distinguishes two cases:
- **API error / empty (no-code) reply** — the task is **NOT** checkpointed. It is
  tracked in a `*.fail.json` sidecar and **retried on the next run**. So a rate
  limit, timeout, or network blip is *corrected*, never frozen as a 0. Only after
  `EVAL_MAX_GEN_RETRIES` (default 4) reruns still failing is it finally stored as
  a real 0 so the campaign can terminate.
- **Real wrong answer / TLE / runtime error** — this is a legitimate result, so it
  **is** checkpointed and never re-spent.

Net effect: re-running the same command retries **only** the genuinely-failed
generations; every good result and every real wrong/TLE answer is kept. The end
of each run prints `... N generation failures (NOT stored -- re-run to retry them)`.

To see what's still pending:
```bash
find ../evaluation/grades -name '*.fail.json' | wc -l          # how many left to retry
find ../evaluation/grades -name '*.fail.json'                   # which ones
```

## The report

`evaluate.py` calls `eval_report.py` at the end; you can also run it standalone
anytime (even mid-run) to summarize whatever grades exist so far:

```bash
python eval_report.py
```

Per family (and an OVERALL across families), for each criterion it prints:
- **(A) PASS %** — total test cases passed / total tried, one column per time limit.
- **(B) AVG cases** — average number of test cases a model passes per statement,
  one column per time limit.

Written to `../evaluation/reports/summary.md` and `summary.json`.

## The models (`agentic/config/eval_models.yaml`)

Gemma 3 (4B/12B/27B), Qwen 3.8 (flash/27B/2.4T-A95B), DeepSeek V4 Pro, Kimi K3,
Mistral Medium 3.5, Llama 4 Scout — all via **OpenRouter**; **Gemini 3.8 Flash**
via the **Google API**. Ollama is supported too (add an entry with
`backend: ollama`). To add/remove a model, edit that file (`enabled: true/false`).

If a model errors with a mandatory-reasoning 400 (like kimi/gpt-oss do), add
`reasoning: {max_tokens: 4000, exclude: true}` to its entry. Failed generations
are recorded (`gen_error`) and score 0 — re-running retries only unfinished tasks.

## Output layout (`../evaluation/`)

```
evaluation/
├── solutions/family_NN/<crit>/<stmt>/<model>/<limit>s/solution.py   # cached generations
├── grades/family_NN/<crit>/<stmt>/<model>/<limit>s.json             # checkpoint + per-case results
└── reports/summary.md, summary.json
```
`<stmt>` is `ver_vNNN` (a version) or `lin_LNNN_dNNN` (a lineage depth).

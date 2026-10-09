#!/usr/bin/env python3
"""
Evaluate the model panel on the P (polynomial) statements.

Difference from evaluate.py (which does NPC with a 1/2/5/10 s time-constraint sweep):
  * P statements are evaluated ONCE each -- no added time-constraint sweep.
  * The wall-clock limit is exactly the limit ALREADY WRITTEN in the statement
    ("Time limit: X s"), i.e. "the statement's time constraint only". The statement
    text is passed to the model UNCHANGED (the strict NP note is NP-only).
  * One pass% per model per family (students + frontier), reported the usual way.

Reuses all the trusted machinery from evaluate.py (panel, generation + caching,
grading, validator/exact-match judge, failure handling). Writes to a SEPARATE
place so it never collides with the NPC run:
    evaluation/grades_p/family_NN/<stmt>/<model>/result.json
    evaluation/solutions_p/family_NN/<stmt>/<model>/solution.py

Checkpointed + resumable + crash-proof, exactly like the NPC harness.

HOW TO RUN
    cd complexity-benchmark
    python evaluate_p.py                 # all families, P statements
    FAM=17 python evaluate_p.py          # one family
    EVAL_MODELS=gemma-3-4b python evaluate_p.py   # one model (e.g. local Ollama)
  Interrupt (Ctrl-C) and re-run the same command to continue. Runs eval_report_p.py
  at the end.
"""
import os, re, sys, json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import evaluate as E   # reuse PANEL, generate, grade, make_judge, load_tests, collect_statements, OUT, log

CRIT = "2"
CRIT_DIR = "criterion_2_p"
DEFAULT_LIMIT = 5.0    # fallback if a statement has no parseable "Time limit:" line


def stated_limit(statement):
    m = re.search(r"(?im)^Time limit:\s*([0-9]+(?:\.[0-9]+)?)\s*s", statement)
    return float(m.group(1)) if m else DEFAULT_LIMIT


def families():
    want = os.environ.get("FAM", "").strip()
    wants = {w.strip().zfill(2) for w in want.split(",") if w.strip()} if want else None
    out = []
    for d in sorted(E.DATASET.glob("family_*")):
        num = d.name.split("_")[1]
        if wants is None or num in wants:
            out.append((num, d))
    return out


def task_p(fam, fam_dir, stmt_id, stmt_path, model, tests, judge):
    mid = model["id"]
    gpath = E.OUT / "grades_p" / f"family_{fam}" / stmt_id / mid / "result.json"
    if gpath.exists():
        return ("skip", None)
    fail_path = gpath.with_name("result.fail.json")
    sol_path = E.OUT / "solutions_p" / f"family_{fam}" / stmt_id / mid / "solution.py"
    statement = stmt_path.read_text()           # UNCHANGED: P uses its own stated limit, no NP note
    limit = stated_limit(statement)

    code, gen_err = E.generate(model, statement, sol_path)

    if not code.strip():
        n = 0
        if fail_path.exists():
            try: n = json.loads(fail_path.read_text()).get("attempts", 0)
            except Exception: n = 0
        n += 1
        if n < E.MAX_GEN_RETRIES:
            fail_path.parent.mkdir(parents=True, exist_ok=True)
            fail_path.write_text(json.dumps({"attempts": n, "last_error": gen_err,
                                             "model": mid, "stmt": stmt_id}))
            return ("fail", f"{mid:<20} {stmt_id:<22} GEN-FAIL ({gen_err}) "
                            f"-> will retry (attempt {n}/{E.MAX_GEN_RETRIES})")
        p, t, tle, per = 0, len(tests), 0, [{"name": nm, "pass": False, "why": "gen_failed"} for nm, _, _ in tests]
        gen_note = f"gen_failed_after_{E.MAX_GEN_RETRIES}_retries"
    else:
        p, t, tle, per = E.grade(sol_path, tests, limit, judge)
        gen_note = None

    gpath.parent.mkdir(parents=True, exist_ok=True)
    gpath.write_text(json.dumps({
        "family": fam, "crit": CRIT, "stmt": stmt_id, "model": mid, "limit": limit,
        "passed": p, "total": t, "tle": tle, "gen_error": gen_err, "gen_note": gen_note,
        "cases": per,
    }, indent=2))
    if fail_path.exists():
        fail_path.unlink()
    return ("done", f"{mid:<20} {stmt_id:<22} @{limit:g}s  {p}/{t}" + (f"  (tle {tle})" if tle else ""))


def main():
    E.OUT.mkdir(parents=True, exist_ok=True)
    fams = families()
    E.log(f"EVAL (P) PANEL: {len(E.PANEL)} models | crit {CRIT_DIR} (stated time limit only) | "
          f"families {[f for f,_ in fams]} | workers {E.WORKERS}")
    E.log(f"output dir: {E.OUT}/grades_p\n")
    total_done = total_skip = total_fail = 0
    skipped_fams = []
    for fam, fam_dir in fams:
        try:
            stmts = E.collect_statements(fam_dir, CRIT_DIR)
            tests = E.load_tests(fam_dir, CRIT_DIR)
            if not stmts or not tests:
                E.log(f"[family_{fam}/{CRIT_DIR}] no statements or tests -- skip"); continue
            judge, jmode = E.make_judge(fam_dir, CRIT_DIR)
        except Exception as e:
            E.log(f"[family_{fam}/{CRIT_DIR}] SETUP ERROR ({type(e).__name__}: {e}) -- skipping")
            skipped_fams.append(f"{fam}: {type(e).__name__}"); continue
        jobs = [(fam, fam_dir, sid, sp, m, tests, judge) for (sid, sp) in stmts for m in E.PANEL]
        E.log(f"[family_{fam}/{CRIT_DIR}] {len(stmts)} statements x {len(E.PANEL)} models "
              f"x {len(tests)} tests = {len(jobs)} tasks (judge={jmode})")
        with ThreadPoolExecutor(max_workers=E.WORKERS) as ex:
            futs = [ex.submit(task_p, *j) for j in jobs]
            for fut in as_completed(futs):
                try:
                    status, msg = fut.result()
                except Exception as e:
                    total_fail += 1; E.log(f"  TASK ERROR ({type(e).__name__}: {e})"); continue
                if status == "done":
                    total_done += 1
                    if msg: E.log("  " + msg)
                elif status == "fail":
                    total_fail += 1
                    if msg: E.log("  " + msg)
                else:
                    total_skip += 1
        E.log(f"[family_{fam}/{CRIT_DIR}] complete\n")
    E.log(f"\nDONE (P). graded {total_done} new, skipped {total_skip} done, "
          f"{total_fail} generation failures (NOT stored -- re-run to retry).")
    if skipped_fams:
        E.log("  SKIPPED families (setup error): " + "; ".join(skipped_fams))
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "eval_report_p.py")])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Evaluate the model panel against the final_dataset statements.

WHAT IT DOES
  For every NPC statement in final_dataset (all `versions/` + all `lineages/`
  depths), for every model in agentic/config/eval_models.yaml, for every time
  constraint (1s, 2s, 5s, 10s):
    1. tell the model the time limit (the statement's "Time limit:" line is set
       to the constraint and a scoring note is appended -- ONLY for NPC),
    2. ask it for a Python 3 solution,
    3. run that solution against ALL curated test cases for the family under a
       STRICT wall-clock limit equal to the constraint (a test that does not
       finish in time scores 0),
    4. grade each output with the family's validator and record pass/total.

  Everything is written under a SEPARATE directory (evaluation/, a sibling of
  complexity-benchmark), so the dataset is untouched.

CHECKPOINTING
  One JSON per (family, criterion, statement, model, limit) under evaluation/grades/.
  If that JSON exists, the task is skipped -- so an interrupted run resumes exactly
  where it stopped. Generated solutions are cached under evaluation/solutions/ too,
  so re-grading never re-calls the model.

HOW TO RUN
    cd complexity-benchmark
    python evaluate.py                 # all 12 families, NPC, all 4 limits
    FAM=17 python evaluate.py          # just family 17
    FAM=17,20 python evaluate.py       # a couple of families
    EVAL_CRIT=1,2 python evaluate.py   # also evaluate the P statements
  Interrupt any time (Ctrl-C) and re-run the SAME command to continue.

  Knobs (env): FAM, EVAL_CRIT (default "1"=NPC), LIMITS (default "1,2,5,10"),
  EVAL_WORKERS, EVAL_SCOPE (all|versions|lineages), EVAL_MAX_STMTS (cap per
  family/crit for a quick smoke test). Runs eval_report.py at the end.
"""
import os, sys, re, json, subprocess, importlib.util, threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "agentic" / "tools"))
import backends as B                        # chat(), extract_code(), strip_thinking()
import yaml

DATASET = ROOT / "final_dataset"
OUT     = ROOT.parent / "evaluation"        # a DIFFERENT directory (sibling of complexity-benchmark)
CRIT_DIR = {"1": "criterion_1_npc", "2": "criterion_2_p"}

# ---- config ----------------------------------------------------------------
CFG   = yaml.safe_load((ROOT / "agentic/config/eval_models.yaml").read_text())
PANEL = [m for m in CFG["eval_panel"] if m.get("enabled", True)]
# Optional model filter: EVAL_MODELS=gemma-3-4b,llama-4-scout runs only those ids.
_only = {x.strip() for x in os.environ.get("EVAL_MODELS", "").split(",") if x.strip()}
if _only:
    PANEL = [m for m in PANEL if m["id"] in _only]
LIMITS = [int(x) for x in os.environ.get("LIMITS", ",".join(map(str, CFG.get("time_limits", [1,2,5,10])))).split(",")]
CRITS  = [c.strip() for c in os.environ.get("EVAL_CRIT", "1").split(",") if c.strip()]
WORKERS = int(os.environ.get("EVAL_WORKERS", CFG.get("execution", {}).get("workers", 6)))
GEN_TIMEOUT = int(CFG.get("execution", {}).get("gen_timeout_s", 600))
RETRIES = int(CFG.get("execution", {}).get("retries", 2))
SCOPE = os.environ.get("EVAL_SCOPE", "all")           # all | versions | lineages
MAX_STMTS = int(os.environ.get("EVAL_MAX_STMTS", "0"))  # 0 = no cap
# How many times (across re-runs) a task may FAIL GENERATION (API error / empty output)
# before we give up and store it as a real 0 result so the run can finish. Transient
# failures recover well within this; only a deterministically-broken generation hits it.
MAX_GEN_RETRIES = int(os.environ.get("EVAL_MAX_GEN_RETRIES", "4"))
# MODE:
#   derive    (default, FAST) -- generate ONE solution per (statement, model), run it ONCE
#             against all tests at the largest limit while recording each test's elapsed
#             time, then DERIVE the result at every limit (a case passes at limit L iff it
#             is correct AND finished within L seconds). ~4x fewer generations and far less
#             grading wall, identical pass/fail numbers for the designed-hard tiers.
#   per_limit (ORIGINAL, SLOW) -- generate a separate solution per limit (model told that
#             exact limit) and grade each at its own limit. Most faithful to "told the time"
#             but 4x the cost/time.
MODE = os.environ.get("EVAL_MODE", "derive")
MAX_LIMIT = max(LIMITS)

SYS_PROMPT = (ROOT / "agentic/prompts/student_system.md").read_text()
USR_TMPL   = (ROOT / "agentic/prompts/student_user_template.md").read_text()

_print_lock = threading.Lock()
def log(msg):
    with _print_lock:
        print(msg, flush=True)


def families():
    want = os.environ.get("FAM", "").strip()
    wants = {w.strip().zfill(2) for w in want.split(",") if w.strip()} if want else None
    out = []
    for d in sorted(DATASET.glob("family_*")):
        num = d.name.split("_")[1]
        if wants is None or num in wants:
            out.append((num, d))
    return out


def collect_statements(fam_dir, crit_dir):
    """All statements to evaluate: version statements + lineage statements at
    every depth. Returns [(stmt_id, path)]."""
    items = []
    if SCOPE in ("all", "versions"):
        vroot = fam_dir / "versions" / crit_dir
        for vd in sorted(vroot.glob("v*")) if vroot.exists() else []:
            sp = vd / "statement.md"
            if sp.exists():
                items.append((f"ver_{vd.name}", sp))
    if SCOPE in ("all", "lineages"):
        lroot = fam_dir / "lineages" / crit_dir
        for L in sorted(lroot.glob("L*")) if lroot.exists() else []:
            for dd in sorted(L.glob("d*")):
                sp = dd / "statement.md"
                if sp.exists():
                    items.append((f"lin_{L.name}_{dd.name}", sp))
    if MAX_STMTS:
        items = items[:MAX_STMTS]
    return items


def _norm(s):
    """Normalize output for exact-match judging: strip trailing spaces per line and
    drop leading/trailing blank lines."""
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").split("\n")).strip()


def make_judge(fam_dir, crit_dir):
    """Return (judge, mode). judge(input_text, model_out, expected_out) -> bool.

    - If the family ships a validator.py (witness/constraint-checked families like
      graph-coloring and the obscure families), use it: validate(input, output).
    - Otherwise (optimization families graded 'judge: exact', e.g. steiner/job-shop),
      fall back to EXACT MATCH against the test's .out reference answer.
    """
    vp = fam_dir / "seed" / crit_dir / "validator.py"
    if vp.exists():
        spec = importlib.util.spec_from_file_location(f"val_{fam_dir.name}_{crit_dir}", vp)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        validate = m.validate
        return (lambda inp, out, exp: bool(validate(inp, out)[0]), "validator")
    return (lambda inp, out, exp: exp is not None and _norm(out) == _norm(exp), "exact_match")


def load_tests(fam_dir, crit_dir):
    """Return [(name, input_text, expected_out_or_None)]."""
    tdir = fam_dir / "tests" / crit_dir
    if not tdir.exists():
        return []
    out = []
    for f in sorted(tdir.glob("*.in")):
        of = f.with_suffix(".out")
        out.append((f.stem, f.read_text(), of.read_text() if of.exists() else None))
    return out


def _set_time_limit_line(s, limit):
    out = re.sub(r"(?im)^Time limit:.*$",
                 f"Time limit: {limit} s   Memory limit: 256 MB", s, count=1)
    if out == s and not re.search(r"(?im)^Time limit:", out):
        out = re.sub(r"(?m)^(# .*)$", rf"\1\n\nTime limit: {limit} s   Memory limit: 256 MB",
                     out, count=1)
    return out


def with_time_limit(statement, limit, is_npc):
    """per_limit mode: set one stated limit and append a strict single-limit note.
    Only NPC gets the note (per spec 'only for NP'); P is passed through unchanged."""
    if not is_npc:
        return statement
    s = _set_time_limit_line(statement, limit)
    note = (f"\n\n## Time constraint (strict)\n"
            f"Your program is executed under a hard wall-clock limit of **{limit} second(s) "
            f"per test case**. If it does not terminate within {limit} second(s) on a test "
            f"case, that test case scores **0**, no matter how correct the logic is. Choose an "
            f"algorithm that reliably finishes within {limit} second(s) on every input allowed "
            f"by the constraints.\n")
    return s + note


def with_time_limits_multi(statement, limits, is_npc):
    """derive mode: the model writes ONE solution that will be judged under several
    wall-clock limits; faster is strictly better. Only NPC gets the note."""
    if not is_npc:
        return statement
    s = _set_time_limit_line(statement, max(limits))
    lim_txt = ", ".join(f"{l} s" for l in sorted(limits))
    note = (f"\n\n## Time constraint (strict)\n"
            f"Your program will be run under several hard per-test wall-clock limits: "
            f"**{lim_txt}**. On a given test case you earn credit at a limit only if your "
            f"program terminates within that many seconds AND is correct; otherwise it scores "
            f"**0** at that limit. A faster correct program is strictly better because it earns "
            f"credit at the tighter limits too. Write the single fastest correct algorithm you "
            f"can for the constraints given.\n")
    return s + note


def generate(model, statement, sol_path):
    """Return (code, error) for this statement+limit.

    Reuses a cached NON-EMPTY solution if present (never re-spends on a good
    generation). On an API failure or an empty/no-code reply, returns ("", error)
    and writes NOTHING to disk -- so the task is NOT checkpointed and will be
    retried on the next run. Only a successful, non-empty generation is cached.
    """
    if sol_path.exists() and sol_path.read_text().strip():
        return sol_path.read_text(), None
    user = USR_TMPL.replace("{STATEMENT}", statement)
    r = B.chat(model, SYS_PROMPT, user, timeout=GEN_TIMEOUT, retries=RETRIES)
    err = r.get("error")
    code = B.extract_code(B.strip_thinking(r.get("text", "")))
    if code.strip() and not err:
        sol_path.parent.mkdir(parents=True, exist_ok=True)
        sol_path.write_text(code)
        return code, None
    return "", (err or "empty_output")


def grade(sol_path, tests, limit, judge):
    """Run the solution against every test under a strict wall-clock `limit`."""
    passed = tle = 0
    per = []
    code = sol_path.read_text()
    if not code.strip():
        return 0, len(tests), 0, [{"name": n, "pass": False, "why": "empty"} for n, _, _ in tests]
    for name, inp, exp in tests:
        why = ""
        try:
            r = subprocess.run([sys.executable, str(sol_path)], input=inp,
                               capture_output=True, text=True, timeout=limit)
            if r.returncode != 0:
                ok, why = False, "runtime_error"
            else:
                try:
                    ok = bool(judge(inp, r.stdout, exp))
                    why = "" if ok else "wrong_answer"
                except Exception as e:
                    ok, why = False, f"judge_error:{type(e).__name__}"
        except subprocess.TimeoutExpired:
            ok, why = False, "tle"; tle += 1
        passed += ok
        per.append({"name": name, "pass": bool(ok), "why": why})
    return passed, len(tests), tle, per


def grade_timed(sol_path, tests, max_limit, judge):
    """Run each test ONCE at `max_limit`, recording elapsed time + correctness, so the
    result at ANY limit <= max_limit can be derived without re-running. Returns a list of
    {name, correct, elapsed, timed_out}."""
    import time as _t
    out = []
    for name, inp, exp in tests:
        correct = False; timed_out = False; elapsed = max_limit
        t0 = _t.perf_counter()
        try:
            r = subprocess.run([sys.executable, str(sol_path)], input=inp,
                               capture_output=True, text=True, timeout=max_limit)
            elapsed = _t.perf_counter() - t0
            if r.returncode == 0:
                try:
                    correct = bool(judge(inp, r.stdout, exp))
                except Exception:
                    correct = False
        except subprocess.TimeoutExpired:
            timed_out = True; elapsed = max_limit
        out.append({"name": name, "correct": correct, "elapsed": round(elapsed, 4),
                    "timed_out": timed_out})
    return out


def derive_at(cases, limit):
    """From grade_timed() records, compute (passed, total, tle, per) at a given limit:
    a case passes iff it is correct AND finished within `limit` seconds."""
    passed = tle = 0; per = []
    for c in cases:
        over = c["timed_out"] or c["elapsed"] > limit
        ok = c["correct"] and not over
        why = "" if ok else ("tle" if over else "wrong_answer")
        if over and not c["correct"]:
            why = "tle"          # ran out of time (would also be wrong, but time is the cause)
        if over: tle += 1
        passed += ok
        per.append({"name": c["name"], "pass": bool(ok), "why": why,
                    "elapsed": c["elapsed"]})
    return passed, len(cases), tle, per


def task(fam, fam_dir, crit, crit_dir, stmt_id, stmt_path, model, limit, tests, judge):
    mid = model["id"]
    grade_path = OUT / "grades" / f"family_{fam}" / crit_dir / stmt_id / mid / f"{limit}s.json"
    if grade_path.exists():
        return ("skip", None)
    fail_path = grade_path.with_name(f"{limit}s.fail.json")   # transient-failure tracker
    sol_path = OUT / "solutions" / f"family_{fam}" / crit_dir / stmt_id / mid / f"{limit}s" / "solution.py"
    statement = with_time_limit(stmt_path.read_text(), limit, crit == "1")

    code, gen_err = generate(model, statement, sol_path)

    # --- generation FAILED (API error or empty/no-code reply) -----------------
    # Do NOT write the grade checkpoint, so this exact task is retried next run.
    # Track attempts across runs; only after MAX_GEN_RETRIES do we give up and
    # store a real 0 result, so the campaign can still terminate.
    if not code.strip():
        n = 0
        if fail_path.exists():
            try: n = json.loads(fail_path.read_text()).get("attempts", 0)
            except Exception: n = 0
        n += 1
        if n < MAX_GEN_RETRIES:
            fail_path.parent.mkdir(parents=True, exist_ok=True)
            fail_path.write_text(json.dumps({"attempts": n, "last_error": gen_err,
                                             "model": mid, "stmt": stmt_id, "limit": limit}))
            return ("fail", f"{mid:<20} {stmt_id:<22} {limit}s  GEN-FAIL ({gen_err}) "
                            f"-> will retry (attempt {n}/{MAX_GEN_RETRIES})")
        # exhausted retries -> store as a genuine 0 so the run finishes
        p, t, tle, per = 0, len(tests), 0, [{"name": nm, "pass": False, "why": "gen_failed"} for nm, _, _ in tests]
        gen_note = f"gen_failed_after_{MAX_GEN_RETRIES}_retries"
    else:
        # --- generation OK: grade it. A wrong/TLE/crash 0 here is a REAL result,
        #     so it IS checkpointed and never re-spent. ---------------------------
        p, t, tle, per = grade(sol_path, tests, limit, judge)
        gen_note = None

    grade_path.parent.mkdir(parents=True, exist_ok=True)
    grade_path.write_text(json.dumps({
        "family": fam, "crit": crit, "stmt": stmt_id, "model": mid, "limit": limit,
        "passed": p, "total": t, "tle": tle, "gen_error": gen_err, "gen_note": gen_note,
        "cases": per,
    }, indent=2))
    if fail_path.exists():
        fail_path.unlink()   # clear the tracker once the task is genuinely recorded
    return ("done", f"{mid:<20} {stmt_id:<22} {limit}s  {p}/{t}" + (f"  (tle {tle})" if tle else ""))


def task_derive(fam, fam_dir, crit, crit_dir, stmt_id, stmt_path, model, tests, judge):
    """derive mode: ONE generation + ONE timed grading at MAX_LIMIT, write one grade
    JSON per limit (derived). The task is checkpointed per (statement, model) -- skipped
    only when ALL requested limits already have a grade file."""
    mid = model["id"]
    gdir = OUT / "grades" / f"family_{fam}" / crit_dir / stmt_id / mid
    if all((gdir / f"{lim}s.json").exists() for lim in LIMITS):
        return ("skip", None)
    fail_path = gdir / "derive.fail.json"
    sol_path = OUT / "solutions" / f"family_{fam}" / crit_dir / stmt_id / mid / "solution.py"
    statement = with_time_limits_multi(stmt_path.read_text(), LIMITS, crit == "1")

    code, gen_err = generate(model, statement, sol_path)

    if not code.strip():
        n = 0
        if fail_path.exists():
            try: n = json.loads(fail_path.read_text()).get("attempts", 0)
            except Exception: n = 0
        n += 1
        if n < MAX_GEN_RETRIES:
            fail_path.parent.mkdir(parents=True, exist_ok=True)
            fail_path.write_text(json.dumps({"attempts": n, "last_error": gen_err,
                                             "model": mid, "stmt": stmt_id}))
            return ("fail", f"{mid:<20} {stmt_id:<22} GEN-FAIL ({gen_err}) "
                            f"-> will retry (attempt {n}/{MAX_GEN_RETRIES})")
        cases = None; gen_note = f"gen_failed_after_{MAX_GEN_RETRIES}_retries"
    else:
        cases = grade_timed(sol_path, tests, MAX_LIMIT, judge)
        gen_note = None

    gdir.mkdir(parents=True, exist_ok=True)
    summ = []
    for lim in LIMITS:
        if cases is None:
            p, t, tle, per = 0, len(tests), 0, [{"name": nm, "pass": False, "why": "gen_failed"} for nm, _, _ in tests]
        else:
            p, t, tle, per = derive_at(cases, lim)
        (gdir / f"{lim}s.json").write_text(json.dumps({
            "family": fam, "crit": crit, "stmt": stmt_id, "model": mid, "limit": lim,
            "passed": p, "total": t, "tle": tle, "gen_error": gen_err, "gen_note": gen_note,
            "mode": "derive", "cases": per,
        }, indent=2))
        summ.append(f"{lim}s:{p}/{t}")
    if fail_path.exists():
        fail_path.unlink()
    return ("done", f"{mid:<20} {stmt_id:<22} " + "  ".join(summ))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fams = families()
    log(f"EVAL PANEL: {len(PANEL)} models | mode {MODE} | limits {LIMITS}s | crit {CRITS} | "
        f"families {[f for f,_ in fams]} | workers {WORKERS}")
    log(f"output dir: {OUT}\n")
    total_done = total_skip = total_fail = 0
    skipped_fams = []
    for fam, fam_dir in fams:
        for crit in CRITS:
            crit_dir = CRIT_DIR[crit]
            # Guard the WHOLE per-family setup: a bad/missing file for one family must
            # never crash the campaign -- log it, skip that family, keep going.
            try:
                stmts = collect_statements(fam_dir, crit_dir)
                tests = load_tests(fam_dir, crit_dir)
                if not stmts or not tests:
                    log(f"[family_{fam}/{crit_dir}] no statements or tests -- skip"); continue
                judge, jmode = make_judge(fam_dir, crit_dir)
            except Exception as e:
                msg = f"[family_{fam}/{crit_dir}] SETUP ERROR ({type(e).__name__}: {e}) -- skipping this family"
                log(msg); skipped_fams.append(f"{fam}/{crit_dir}: {type(e).__name__}"); continue
            if MODE == "derive":
                fn = task_derive
                jobs = [(fam, fam_dir, crit, crit_dir, sid, sp, m, tests, judge)
                        for (sid, sp) in stmts for m in PANEL]
                log(f"[family_{fam}/{crit_dir}] {len(stmts)} statements x {len(PANEL)} models "
                    f"x {len(tests)} tests = {len(jobs)} tasks (derive @ {MAX_LIMIT}s, {len(LIMITS)} "
                    f"limits derived, judge={jmode})")
            else:
                fn = task
                jobs = [(fam, fam_dir, crit, crit_dir, sid, sp, m, lim, tests, judge)
                        for (sid, sp) in stmts for m in PANEL for lim in LIMITS]
                log(f"[family_{fam}/{crit_dir}] {len(stmts)} statements x {len(PANEL)} models "
                    f"x {len(LIMITS)} limits x {len(tests)} tests = {len(jobs)} tasks "
                    f"(per_limit, judge={jmode})")
            with ThreadPoolExecutor(max_workers=WORKERS) as ex:
                futs = [ex.submit(fn, *j) for j in jobs]
                for fut in as_completed(futs):
                    try:
                        status, msg = fut.result()
                    except Exception as e:          # a single task should never kill the run
                        total_fail += 1
                        log(f"  TASK ERROR ({type(e).__name__}: {e})"); continue
                    if status == "done":
                        total_done += 1
                        if msg: log("  " + msg)
                    elif status == "fail":
                        total_fail += 1
                        if msg: log("  " + msg)
                    else:
                        total_skip += 1
            log(f"[family_{fam}/{crit_dir}] complete\n")
    log(f"\nDONE. graded {total_done} new tasks, skipped {total_skip} already-done, "
        f"{total_fail} generation failures (NOT stored -- re-run to retry them).")
    if total_fail:
        log("  ^ these were API errors / empty replies; the SAME command will retry only "
            "those. Good results and real wrong/TLE answers are kept and won't be re-spent.")
    if skipped_fams:
        log("  SKIPPED families (setup error): " + "; ".join(skipped_fams))
    # produce the report tables
    subprocess.run([sys.executable, str(ROOT / "eval_report.py")])


if __name__ == "__main__":
    main()

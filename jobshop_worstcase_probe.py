#!/usr/bin/env python3
"""Worst-case (witness-graded) probe for family 16 — job-shop, mirroring the family-01 coloring probe.
For each model: read the feasibility+witness statement, ask it to solve, then grade on two tiers:
  - SEED tier  : small instances (does the model solve the base witness task at all?)
  - WORST tier : large, densely-packed instances (scaled hardness).
Prints pass% per tier per model. Run from your terminal (API calls, ~6 generations):

    cd complexity-benchmark
    nohup python jobshop_worstcase_probe.py > jobshop_worstcase.log 2>&1 &
    tail -f jobshop_worstcase.log
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "agentic/tools"))
sys.path.insert(0, str(ROOT / "tools"))
import backends as B
import worstcase_jobshop as JS

STATEMENT = """# Problem — Fit the Schedule

Time limit: 2 s   Memory limit: 256 MB

## Description
A factory has **m** machines and must process **j** jobs. Each job is a fixed sequence of operations;
each operation runs on a specific machine for a given number of time units. Rules:
- a job's operations must run in their listed order (an operation starts only after the previous
  operation of the same job finishes);
- each machine runs only one operation at a time;
- once started, an operation runs to completion.

You are also given a deadline **T**. Produce a schedule (a start time for every operation) whose last
operation finishes at time at most **T**, or report that it is impossible.

## Input
The first line contains three integers j, m and T. Each of the next j lines describes one job: an
integer o (number of operations) followed by o pairs `machine duration` (1-indexed machine), in order.

## Output
If no valid schedule with makespan <= T exists, print a single line `NO`.
Otherwise print `YES`, then j lines; line i contains the start times of job i's operations, in order.
"""

# tiers (all YES by construction; the planted schedule proves makespan <= T)
SEED = [JS.plant(nj, m, ops, s)[0] for (nj, m, ops, s) in
        [(4, 3, 3, 11), (6, 3, 4, 12), (8, 4, 4, 13), (10, 4, 5, 14),
         (12, 4, 5, 15), (15, 5, 6, 16), (18, 5, 6, 17), (20, 5, 7, 18)]]
WORST = [JS.plant(nj, m, ops, s)[0] for (nj, m, ops, s) in
         [(40, 5, 10, 21), (60, 5, 12, 22), (80, 6, 12, 23), (100, 6, 14, 24),
          (120, 6, 15, 25), (150, 8, 15, 26), (200, 8, 18, 27), (250, 10, 20, 28)]]
LIM = 2.0


def grade_tier(sol_path, instances):
    npass = 0
    for inp in instances:
        try:
            out = subprocess.run([sys.executable, str(sol_path)], input=inp,
                                 capture_output=True, text=True, timeout=LIM).stdout
            ok, _ = JS.grade(inp, out)
            npass += bool(ok)
        except subprocess.TimeoutExpired:
            pass
    return npass, len(instances)


def main():
    models = B.load_models()
    panel = [s for s in models["students"] if s.get("enabled", True)] + \
            models.get("frontier_evaluators", [])
    sys_t = (B.PROMPTS_DIR / "student_system.md").read_text()
    usr_t = (B.PROMPTS_DIR / "student_user_template.md").read_text()
    outdir = ROOT / "agentic/attempts/family_16/worstcase_probe"
    print(f"JOB-SHOP WORST-CASE PROBE | {len(panel)} models | "
          f"seed={len(SEED)} worst={len(WORST)} | limit {LIM}s\n", flush=True)
    print(f"{'model':<26}{'SEED tier':>12}{'WORST tier':>12}", flush=True)
    print("-" * 50, flush=True)
    for mdl in panel:
        d = outdir / mdl["id"]; d.mkdir(parents=True, exist_ok=True)
        sol = d / "solution.py"
        if not sol.exists():
            resp = B.chat(mdl, sys_t, usr_t.replace("{STATEMENT}", STATEMENT),
                          timeout=600, retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(resp["text"])))
        sp, st = grade_tier(sol, SEED)
        wp, wt = grade_tier(sol, WORST)
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>12}"
              f"{f'{100*wp//wt}% ({wp}/{wt})':>12}", flush=True)
    print("\nSEED low  => job-shop witness task is hard even small.  "
          "WORST low => scaled hardness holds.\nBoth ~100% => bound T is too loose (greedy matches "
          "it); tighten T to make it a real worst-case tier.", flush=True)


if __name__ == "__main__":
    main()

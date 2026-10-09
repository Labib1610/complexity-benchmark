#!/usr/bin/env python3
"""Probe an UNCOMMON NP-complete family (Graph Bandwidth) to see whether it carries a real
failure rate that common families (colouring) do not. For each model it:
  1. reads the seed statement, asks the model to write a solver (API),
  2. grades that solver on two tiers:
       - SEED tier  : small witness-graded instances (does the model even solve the base problem?)
       - WORST tier : planted near-threshold instances at scale (n=200..800),
  3. prints pass% per tier per model.

Run from your terminal (makes API calls, ~6 generations):
    cd complexity-benchmark
    nohup python uncommon_probe.py > uncommon_probe.log 2>&1 &
    tail -f uncommon_probe.log
"""
import subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "agentic/tools"))
sys.path.insert(0, str(ROOT / "tools"))
import backends as B
import bandwidth as BW

STATEMENT = (ROOT / "dataset/family_17_graph_bandwidth/criterion_1_npc/statement.md").read_text()

# ---- build the two tiers of instances (witness-graded, all YES by construction) ----
SEED = [BW.plant(n, b, 3.0, s) for (n, b, s) in
        [(8, 2, 11), (10, 3, 12), (12, 3, 13), (15, 3, 14), (20, 4, 15),
         (30, 4, 16), (40, 5, 17), (50, 5, 18)]]
WORST = [BW.plant(n, b, 4.0, s) for (n, b, s) in
         [(200, 6, 21), (200, 6, 22), (400, 8, 23), (400, 8, 24),
          (600, 10, 25), (600, 10, 26), (800, 12, 27), (800, 12, 28)]]
LIM = 2.0


def grade_tier(sol_path, instances):
    npass = 0
    for inp in instances:
        try:
            out = subprocess.run([sys.executable, str(sol_path)], input=inp,
                                 capture_output=True, text=True, timeout=LIM).stdout
            ok, _ = BW.grade(inp, out)
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
    outdir = ROOT / "agentic/attempts/family_17/criterion_1_npc/v000"
    print(f"UNCOMMON PROBE — Graph Bandwidth | {len(panel)} models | "
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
    print("\nSEED tier low  => uncommon problem trips models on the BASE problem (what we want).\n"
          "WORST tier low => scaled/near-threshold hardness (the SOTA-resistant tier).", flush=True)


if __name__ == "__main__":
    main()

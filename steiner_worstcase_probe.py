#!/usr/bin/env python3
"""Worst-case probe for family 14 — Steiner tree (witness decision: find a tree <= B, verify it).
SEED tier = small t (easy). WORST tier = the scaled dataset instances (100<t<200 and t>200):
exact 2^t solvers TLE; MST/heuristic solvers may pass (scale-documentation tier)."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "agentic/tools")); sys.path.insert(0, str(ROOT / "tools"))
import backends as B
import worstcase_steiner as ST

STATEMENT = """# Problem — Connect the Required Sites Within Budget

Time limit: 2 s   Memory limit: 256 MB

## Description
There are n sites. m cabling options can each join two sites at a cost. Among the sites, t are REQUIRED
and must all end up connected (directly or via other sites). You are given a budget B. Choose a set of
cabling options forming a subtree that connects all required sites with total cost at most B, or report
that it is impossible.

## Input
Line 1: four integers n, m, t, B.
Line 2: t integers — the required-site ids.
Next m lines: three integers u v w — a cabling option joining u and v at cost w.

## Output
If impossible, print a single line `NO`.
Otherwise print `YES`, then the chosen options, one `u v` per line (a subtree connecting all required
sites with total cost <= B).
"""

SEED  = [ST.plant(t, 0.5, 2.0, s) for (t, s) in [(6,11),(8,12),(10,13),(12,14),(15,15),(18,16),(20,17),(22,18)]]
WORST = [ST.plant(t, 0.5, 2.0, s) for (t, s) in [(120,1),(150,2),(180,3),(160,5),(220,6),(260,7),(300,8),(280,10)]]
LIM = 2.0

def grade_tier(sol, insts):
    ok=0
    for inp in insts:
        try:
            out=subprocess.run([sys.executable,str(sol)],input=inp,capture_output=True,text=True,timeout=LIM).stdout
            ok+=bool(ST.grade(inp,out)[0])
        except subprocess.TimeoutExpired: pass
    return ok,len(insts)

def main():
    models=B.load_models()
    panel=[s for s in models["students"] if s.get("enabled",True)]+models.get("frontier_evaluators",[])
    sys_t=(B.PROMPTS_DIR/"student_system.md").read_text(); usr_t=(B.PROMPTS_DIR/"student_user_template.md").read_text()
    outdir=ROOT/"agentic/attempts/family_14/worstcase_probe"
    print(f"STEINER WORST-CASE PROBE | {len(panel)} models | seed={len(SEED)} worst={len(WORST)} | {LIM}s\n",flush=True)
    print(f"{'model':<26}{'SEED tier':>12}{'WORST tier':>12}",flush=True); print("-"*50,flush=True)
    for mdl in panel:
        d=outdir/mdl["id"]; d.mkdir(parents=True,exist_ok=True); sol=d/"solution.py"
        if not sol.exists():
            r=B.chat(mdl,sys_t,usr_t.replace("{STATEMENT}",STATEMENT),timeout=600,retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(r["text"])))
        sp,st=grade_tier(sol,SEED); wp,wt=grade_tier(sol,WORST)
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>12}{f'{100*wp//wt}% ({wp}/{wt})':>12}",flush=True)
    print("\nWORST: exact 2^t solvers TLE; MST/heuristic may pass (scale tier).",flush=True)

if __name__=="__main__": main()

#!/usr/bin/env python3
"""Worst-case (TLE) probe for family 09 — independent set. SEED tier = small (easy); WORST tier =
degree-equalized planted IS at n>=150, k~15-25 (finding the IS forces search -> TLE). Witness-graded."""
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"agentic/tools")); sys.path.insert(0,str(ROOT/"tools"))
import backends as B
import worstcase_is as IS
STATEMENT=(ROOT/"dataset/family_09_clique_independent_set/criterion_1_npc/statement.md").read_text()
SEED =[IS.plant(n,k,0.5,s) for (n,k,s) in [(30,5,11),(40,6,12),(50,6,13),(60,7,14),(70,8,15),(80,8,16),(60,6,17),(50,5,18)]]
WORST=[IS.plant(n,k,0.5,s) for (n,k,s) in [(300,30,21),(300,50,22),(400,40,23),(400,60,24),(500,40,25),(500,60,26),(700,50,27),(800,50,28)]]
LIM=2.0
def grade_tier(sol,insts):
    ok=0
    for inp in insts:
        try:
            out=subprocess.run([sys.executable,str(sol)],input=inp,capture_output=True,text=True,timeout=LIM).stdout
            ok+=bool(IS.grade(inp,out)[0])
        except subprocess.TimeoutExpired: pass
    return ok,len(insts)
def main():
    models=B.load_models()
    panel=[s for s in models["students"] if s.get("enabled",True)]+models.get("frontier_evaluators",[])
    sys_t=(B.PROMPTS_DIR/"student_system.md").read_text(); usr_t=(B.PROMPTS_DIR/"student_user_template.md").read_text()
    outdir=ROOT/"agentic/attempts/family_09/worstcase_probe"
    print(f"IS WORST-CASE PROBE | {len(panel)} models | seed={len(SEED)} worst={len(WORST)} | {LIM}s\n",flush=True)
    print(f"{'model':<26}{'SEED tier':>12}{'WORST tier':>12}",flush=True); print("-"*50,flush=True)
    for mdl in panel:
        d=outdir/mdl["id"]; d.mkdir(parents=True,exist_ok=True); sol=d/"solution.py"
        if not sol.exists():
            r=B.chat(mdl,sys_t,usr_t.replace("{STATEMENT}",STATEMENT),timeout=600,retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(r["text"])))
        sp,st=grade_tier(sol,SEED); wp,wt=grade_tier(sol,WORST)
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>12}{f'{100*wp//wt}% ({wp}/{wt})':>12}",flush=True)
    print("\nWORST low => planted-IS near-threshold forces search -> TLE (SOTA-resistant).",flush=True)
if __name__=="__main__": main()

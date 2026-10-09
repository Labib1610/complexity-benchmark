#!/usr/bin/env python3
"""Worst-case (TLE) probe for family 17 — exact cover (X3C). SEED tier = small (easy); WORST tier =
near-threshold planted X3C at q>=80, high ratio (many decoy triples) -> finding the cover forces search
-> TLE. Witness-graded (verify the chosen triples partition the universe)."""
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"agentic/tools")); sys.path.insert(0,str(ROOT/"tools"))
import backends as B
import family17_exactcover as X
STATEMENT=(ROOT/"dataset/family_17_exact_cover/criterion_1_npc/statement.md").read_text()
SEED =[X.x3c_plant(q,3.0,s,True) for (q,s) in [(8,11),(10,12),(12,13),(15,14),(18,15),(20,16),(22,17),(16,18)]]
WORST=[X.x3c_plant(q,r,s,True) for (q,r,s) in [(80,8,21),(80,10,22),(100,8,23),(100,12,24),(120,10,25),(150,8,26),(150,12,27),(200,10,28)]]
LIM=2.0
def grade_tier(sol,insts):
    ok=0
    for inp in insts:
        try:
            out=subprocess.run([sys.executable,str(sol)],input=inp,capture_output=True,text=True,timeout=LIM).stdout
            ok+=bool(X.x3c_validate(inp,out)[0])
        except subprocess.TimeoutExpired: pass
    return ok,len(insts)
def main():
    models=B.load_models()
    panel=[s for s in models["students"] if s.get("enabled",True)]+models.get("frontier_evaluators",[])
    sys_t=(B.PROMPTS_DIR/"student_system.md").read_text(); usr_t=(B.PROMPTS_DIR/"student_user_template.md").read_text()
    outdir=ROOT/"agentic/attempts/family_17/worstcase_probe"
    print(f"X3C WORST-CASE PROBE | {len(panel)} models | seed={len(SEED)} worst={len(WORST)} | {LIM}s\n",flush=True)
    print(f"{'model':<26}{'SEED tier':>12}{'WORST tier':>12}",flush=True); print("-"*50,flush=True)
    for mdl in panel:
        d=outdir/mdl["id"]; d.mkdir(parents=True,exist_ok=True); sol=d/"solution.py"
        if not sol.exists():
            r=B.chat(mdl,sys_t,usr_t.replace("{STATEMENT}",STATEMENT),timeout=600,retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(r["text"])))
        sp,st=grade_tier(sol,SEED); wp,wt=grade_tier(sol,WORST)
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>12}{f'{100*wp//wt}% ({wp}/{wt})':>12}",flush=True)
    print("\nWORST low => near-threshold X3C forces search -> TLE (SOTA-resistant). If strong models still\n"
          "pass, raise q/ratio (re-tune against the real solvers, as we did for 3DM and IS).",flush=True)
if __name__=="__main__": main()

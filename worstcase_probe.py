#!/usr/bin/env python3
"""Parameterized worst-case (TLE / scale) probe. Usage:  FAM=NN python worstcase_probe.py
Generates one solution per model from the family's NPC statement (cached), grades on a SEED tier
(small, easy) and a WORST tier (hard/large), prints the table, and saves per-model WORST% to
agentic/reports/worstcase_family_NN.json for family_report.py. Change only FAM."""
import os, sys, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"agentic/tools")); sys.path.insert(0,str(ROOT/"tools"))
import backends as B
FAM=os.environ.get("FAM","17")
LIM=2.0

# per-family adapters: module, statement slug, and generators (return input-text) + grade(text,out)->bool
def _adapters(fam):
    if fam=="17":
        import family17_exactcover as X
        seed=[X.x3c_plant(q,3.0,s,True) for q,s in [(8,11),(10,12),(12,13),(15,14),(18,15),(20,16),(22,17),(16,18)]]
        worst=[X.x3c_plant(q,r,s,True) for q,r,s in [(100,8,21),(100,12,22),(120,10,23),(150,8,24),(150,12,25),(180,10,26),(200,8,27),(200,12,28)]]
        return "family_17_exact_cover", seed, worst, lambda t,o: X.x3c_validate(t,o)[0]
    if fam=="18":
        import family18_linarr as L
        seed=[L.plant(n,"general",s) for n,s in [(10,11),(20,12),(30,13),(50,14),(80,15),(120,16),(60,17),(40,18)]]
        worst=[L.plant(n,"general",s) for n,s in [(3000,21),(5000,22),(8000,23),(11000,24),(14000,25),(17000,26),(20000,27),(15000,28)]]
        return "family_18_linear_arrangement", seed, worst, lambda t,o: L.validate(t,o)[0]
    if fam=="19":
        import family19_multicommodity as F
        seed=[F.plant(n,3,s)[0] for n,s in [(10,11),(16,12),(20,13),(24,14),(30,15),(40,16),(18,17),(12,18)]]
        worst=[F.plant(n,3,s)[0] for n,s in [(200,21),(400,22),(600,23),(800,24),(1000,25),(1400,26),(1800,27),(2200,28)]]
        return "family_19_multicommodity_flow", seed, worst, lambda t,o: F.validate(t,o,single=False)[0]
    if fam=="20":
        import family20_edgecolour as E
        def cg(n,s): return E.cubic_plant(n if n%2==0 else n+1,s)[0]
        seed=[cg(n,s) for n,s in [(10,11),(16,12),(20,13),(28,14),(36,15),(44,16),(24,17),(14,18)]]
        worst=[cg(n,s) for n,s in [(200,21),(300,22),(400,23),(500,24),(600,25),(700,26),(800,27),(1000,28)]]
        return "family_20_edge_colouring", seed, worst, lambda t,o: E.edge3col_validate(t,o)[0]
    if fam=="21":
        import family21_multiwaycut as C
        seed=[C.plant(n,3,s,two=False) for n,s in [(10,11),(20,12),(30,13),(40,14),(60,15),(80,16),(50,17),(25,18)]]
        worst=[C.plant(n,3,s,two=False) for n,s in [(2000,21),(2500,22),(3000,23),(3500,24),(4000,25),(4500,26),(5000,27),(6000,28)]]
        return "family_21_multiway_cut", seed, worst, lambda t,o: C.validate(t,o,two=False)[0]
    if fam=="22":
        import family22_precedence as P
        seed=[P.npc_plant(n,3,s) for n,s in [(10,11),(20,12),(30,13),(50,14),(80,15),(120,16),(60,17),(40,18)]]
        worst=[P.npc_plant(n,3,s) for n,s in [(5000,21),(8000,22),(11000,23),(15000,24),(18000,25),(21000,26),(25000,27),(30000,28)]]
        return "family_22_precedence_scheduling", seed, worst, lambda t,o: P.npc_validate(t,o)[0]
    if fam in ("01","02","03","04","08","10","11","13"):
        import originals_worst as O
        cfg={
          "01":("family_01_graph_coloring", O.grade_color,
                [O.plant_color(n,s)[0] for n,s in [(10,11),(16,12),(22,13),(28,14),(30,15),(24,16),(18,17),(12,18)]],
                [O.plant_color(n,s)[0] for n,s in [(60,21),(80,22),(100,23),(120,24),(140,25),(100,26),(120,27),(140,28)]]),
          "02":("family_02_sat", O.grade_sat,
                [O.plant_sat(n,4.0,s)[0] for n,s in [(10,11),(14,12),(18,13),(22,14),(25,15),(20,16),(16,17),(12,18)]],
                [O.plant_sat(n,4.3,s)[0] for n,s in [(200,21),(250,22),(300,23),(350,24),(400,25),(300,26),(350,27),(400,28)]]),
          "03":("family_03_hamiltonian_path", O.grade_ham,
                [O.plant_ham(n,1.0,s)[0] for n,s in [(8,11),(12,12),(16,13),(20,14),(22,15),(18,16),(14,17),(10,18)]],
                [O.plant_ham(n,1.2,s)[0] for n,s in [(60,21),(80,22),(100,23),(120,24),(150,25),(100,26),(120,27),(150,28)]]),
          "04":("family_04_subset_sum", O.grade_subset,
                [O.plant_subset(n,s)[0] for n,s in [(10,11),(14,12),(18,13),(22,14),(24,15),(20,16),(16,17),(12,18)]],
                [O.plant_subset(n,s)[0] for n,s in [(48,21),(52,22),(56,23),(60,24),(64,25),(56,26),(60,27),(64,28)]]),
          "08":("family_08_vertex_cover", O.grade_vc,
                [O.plant_vc(n,s)[0] for n,s in [(10,11),(16,12),(22,13),(28,14),(30,15),(24,16),(18,17),(12,18)]],
                [O.plant_vc(n,s)[0] for n,s in [(60,21),(80,22),(100,23),(120,24),(140,25),(100,26),(120,27),(140,28)]]),
          "10":("family_10_dominating_set", O.grade_dom,
                [O.plant_dom(n,s)[0] for n,s in [(10,11),(16,12),(22,13),(28,14),(30,15),(24,16),(18,17),(12,18)]],
                [O.plant_dom(n,s)[0] for n,s in [(60,21),(80,22),(100,23),(120,24),(140,25),(100,26),(120,27),(140,28)]]),
          "11":("family_11_set_cover", O.grade_setcover,
                [O.plant_setcover(u,k,s)[0] for u,k,s in [(8,3,11),(12,4,12),(16,5,13),(20,6,14),(22,7,15),(18,6,16),(14,5,17),(10,4,18)]],
                [O.plant_setcover(u,k,s)[0] for u,k,s in [(28,9,21),(30,10,22),(32,10,23),(34,11,24),(36,12,25),(30,10,26),(34,11,27),(36,12,28)]]),
          "13":("family_13_partition", O.grade_partition,
                [O.plant_partition(n,s)[0] for n,s in [(10,11),(14,12),(18,13),(22,14),(24,15),(20,16),(16,17),(12,18)]],
                [O.plant_partition(n,s)[0] for n,s in [(48,21),(52,22),(56,23),(60,24),(64,25),(56,26),(60,27),(64,28)]]),
        }[fam]
        slug,grade,seed,worst=cfg
        return slug, seed, worst, grade
    return None  # optimization families (06,07,12,15) -> scale-only, probe skips gracefully

def grade_tier(sol, insts, grade):
    ok=0
    for inp in insts:
        try:
            out=subprocess.run([sys.executable,str(sol)],input=inp,capture_output=True,text=True,timeout=LIM).stdout
            ok+=bool(grade(inp,out))
        except subprocess.TimeoutExpired: pass
    return ok,len(insts)

def main():
    ad = _adapters(FAM)
    if ad is None:
        print(f"[worstcase_probe] no worst-case adapter for family {FAM} yet — skipping (hardening + "
              f"frontier + report still run). Add an adapter in _adapters() when ready.", flush=True)
        return
    slug, seed, worst, grade = ad
    statement=(ROOT/"dataset"/slug/"criterion_1_npc"/"statement.md").read_text()
    models=B.load_models()
    panel=[s for s in models["students"] if s.get("enabled",True)]+models.get("frontier_evaluators",[])
    sys_t=(B.PROMPTS_DIR/"student_system.md").read_text(); usr_t=(B.PROMPTS_DIR/"student_user_template.md").read_text()
    outdir=ROOT/"agentic/attempts"/f"family_{FAM}"/"worstcase_probe"
    print(f"WORST-CASE PROBE family {FAM} ({slug}) | {len(panel)} models | seed={len(seed)} worst={len(worst)} | {LIM}s\n",flush=True)
    print(f"{'model':<26}{'SEED':>10}{'WORST':>10}",flush=True); print("-"*46,flush=True)
    results={}
    for mdl in panel:
        d=outdir/mdl["id"]; d.mkdir(parents=True,exist_ok=True); sol=d/"solution.py"
        if not sol.exists():
            r=B.chat(mdl,sys_t,usr_t.replace("{STATEMENT}",statement),timeout=600,retries=2)
            sol.write_text(B.extract_code(B.strip_thinking(r["text"])))
        sp,st=grade_tier(sol,seed,grade); wp,wt=grade_tier(sol,worst,grade)
        results[mdl["id"]]={"seed_pass":sp,"seed_total":st,"worst_pass":wp,"worst_total":wt,"worst_pct":100*wp//wt}
        print(f"{mdl['id']:<26}{f'{100*sp//st}% ({sp}/{st})':>10}{f'{100*wp//wt}% ({wp}/{wt})':>10}",flush=True)
    rep=ROOT/"agentic/reports"; rep.mkdir(exist_ok=True)
    (rep/f"worstcase_family_{FAM}.json").write_text(json.dumps(results,indent=2))
    strong=[results[m]["worst_pct"] for m in ["gpt-oss-120b","gpt-5.6-sol","gemini-3.7-flash-frontier"] if m in results]
    if strong and max(strong)>50:
        print("\nNOTE: strong models still pass the WORST tier -> raise the sizes in _adapters (re-tune, like 3DM/IS).",flush=True)
    print(f"\nsaved -> agentic/reports/worstcase_family_{FAM}.json",flush=True)
if __name__=="__main__": main()

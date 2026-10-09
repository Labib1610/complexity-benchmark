#!/usr/bin/env python3
"""Build final_dataset/ : the 12 completed families, each organized for evaluation.
Per family: seed/ (statement+reference+validator+meta), tests/ (curated), versions/ (accepted+flagged
+ attempts), lineages/ (hardening). Obscure families (17-22) keep ALL tests; originals keep only the
discriminating (high-failure) tests, dropping trivially-passed small cases."""
import json, shutil
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "final_dataset"
CRITS = ["criterion_1_npc", "criterion_2_p"]
DONE = {  # family number -> (slug, keep_all_tests?)
  "01":("family_01_graph_coloring",False), "02":("family_02_sat",False),
  "05":("family_05_three_dim_matching",False), "09":("family_09_clique_independent_set",False),
  "14":("family_14_steiner_tree",False), "16":("family_16_job_shop",False),
  "17":("family_17_exact_cover",True), "18":("family_18_linear_arrangement",True),
  "19":("family_19_multicommodity_flow",True), "20":("family_20_edge_colouring",True),
  "21":("family_21_multiway_cut",True), "22":("family_22_precedence_scheduling",True),
}
ACCEPTED = {"ACCEPT","PASS","FLAG"}

def case_fail_rates(num, crit):
    """pass/total per test-case NAME across all attempts + lineage runs."""
    stat = defaultdict(lambda: [0,0])  # name -> [pass,total]
    for base in [ROOT/"agentic/attempts"/f"family_{num}"/crit, ROOT/"agentic/lineages"/f"family_{num}"/crit]:
        if not base.exists(): continue
        for vj in base.glob("**/verdict.json"):
            try: d=json.loads(vj.read_text())
            except: continue
            for c in d.get("cases",[]):
                s=stat[c["name"]]; s[1]+=1; s[0]+= (c["verdict"]=="PASS")
    return {n:(1-p/t if t else 0.0, t) for n,(p,t) in stat.items()}

def curate_tests(num, slug, keep_all, crit, dst):
    dst.mkdir(parents=True, exist_ok=True)
    seed_tests = ROOT/"agentic/seeds"/slug/crit/"tests"          # 30 for obscure; 4 for originals
    corner_tests = ROOT/"agentic/tests"/f"family_{num}"/crit      # u* corner cases (originals)
    worst = ROOT/"dataset"/slug/crit/"worstcase"                  # worst-case tier files if any
    kept=[]
    if keep_all:
        for f in sorted(seed_tests.glob("*.in")):
            shutil.copy(f, dst/f.name); 
            if f.with_suffix(".out").exists(): shutil.copy(f.with_suffix(".out"), dst/(f.stem+".out"))
            kept.append(f.name)
    else:
        fr = case_fail_rates(num, crit)   # name -> (fail_rate,total)
        # keep seed cases only if they are NOT trivially passed (drop simple small anchors)
        for f in sorted(seed_tests.glob("*.in")):
            if fr.get(f.stem,(0,0))[0] > 0.0:      # at least one model failed it
                shutil.copy(f, dst/("seed_"+f.name))
                if f.with_suffix(".out").exists(): shutil.copy(f.with_suffix(".out"), dst/("seed_"+f.stem+".out"))
                kept.append("seed_"+f.stem)
        # keep ALL corner cases — these are the adversarial, high-failure discriminators by design
        if corner_tests.exists():
            for f in sorted(corner_tests.glob("*.in")):
                dn=f"corner_{f.stem}"
                shutil.copy(f, dst/(dn+".in"))
                if f.with_suffix(".out").exists(): shutil.copy(f.with_suffix(".out"), dst/(dn+".out"))
                kept.append(dn)
    # always include the worst-case tier files (the hard/scaled discriminators)
    if worst.exists():
        for f in sorted(worst.glob("*.in")):
            shutil.copy(f, dst/("worst_"+f.name))
            if f.with_suffix(".out").exists(): shutil.copy(f.with_suffix(".out"), dst/("worst_"+f.stem+".out"))
            kept.append("worst_"+f.stem)
    return len(kept)

def copy_seed(slug, crit, dst):
    dst.mkdir(parents=True, exist_ok=True)
    for fn in ["statement.md","reference.py","validator.py","meta.yaml"]:
        src=ROOT/"dataset"/slug/crit/fn
        if src.exists(): shutil.copy(src, dst/fn)

def copy_versions_and_attempts(num, crit, vdst, adst):
    vbase=ROOT/"agentic/versions"/f"family_{num}"/crit
    abase=ROOT/"agentic/attempts"/f"family_{num}"/crit
    if not vbase.exists(): return 0,0
    nv=na=0
    for vd in sorted(vbase.glob("v*")):
        gj=vd/"gate.json"
        res=json.loads(gj.read_text()).get("result") if gj.exists() else None
        if res not in ACCEPTED: continue
        vt=vdst/vd.name; vt.mkdir(parents=True, exist_ok=True)
        for fn in ["statement.md","edit.json","gate.json"]:
            if (vd/fn).exists(): shutil.copy(vd/fn, vt/fn)
        nv+=1
        # attempts for this version
        ad=abase/vd.name
        if ad.exists():
            for mdl in sorted(ad.glob("*")):
                if not mdl.is_dir(): continue
                mt=adst/vd.name/mdl.name; mt.mkdir(parents=True, exist_ok=True)
                for fn in ["solution.py","verdict.json"]:
                    if (mdl/fn).exists(): shutil.copy(mdl/fn, mt/fn); 
                na+=1
    return nv,na

def copy_lineages(num, crit, ldst):
    lbase=ROOT/"agentic/lineages"/f"family_{num}"/crit
    if not lbase.exists(): return 0
    ldst.mkdir(parents=True, exist_ok=True)
    n=0
    for L in sorted(lbase.glob("L*")):
        shutil.copytree(L, ldst/L.name, dirs_exist_ok=True); n+=1
    for meta in ["plan.json","criterion_memory.json"]:
        if (lbase/meta).exists(): shutil.copy(lbase/meta, ldst/meta)
    return n

if OUT.exists(): shutil.rmtree(OUT)
summary=[]
for num,(slug,keep_all) in DONE.items():
    fam_dir = OUT/slug
    row={"family":slug,"keep_all_tests":keep_all}
    for crit in CRITS:
        copy_seed(slug, crit, fam_dir/"seed"/crit)
        row[crit+"_tests"]=curate_tests(num, slug, keep_all, crit, fam_dir/"tests"/crit)
        nv,na=copy_versions_and_attempts(num, crit, fam_dir/"versions"/crit, fam_dir/"attempts"/crit)
        row[crit+"_versions"]=nv; row[crit+"_attempts"]=na
        row[crit+"_lineages"]=copy_lineages(num, crit, fam_dir/"lineages"/crit)
    summary.append(row)
    print(f"packed {slug}: "+", ".join(f"{c[10:]} tests={row[c+'_tests']} ver={row[c+'_versions']} lin={row[c+'_lineages']}" for c in CRITS))
(OUT/"_manifest.json").write_text(json.dumps(summary,indent=2))
print(f"\nfinal_dataset/ built with {len(summary)} families -> {OUT}")

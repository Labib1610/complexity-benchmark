#!/usr/bin/env python3
"""BASE-DATA QUALITY CHECK: run the student panel on the *seed* (v000) of every family and
report the seed failure rate per family / criterion. This is the "full pass" to see whether the
seed problems are actually hard enough (supervisor: seeds should already have some failure rate).

- No hardening, no variants: only the untouched seed statement + its seed/adversarial tests.
- Resumable: skips any (family, criterion, model) whose verdict.json already exists.
Run from your own terminal so it survives:

    cd complexity-benchmark
    nohup python seed_quality_check.py > seed_quality.log 2>&1 &
    tail -f seed_quality.log
"""
import sys, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "agentic/tools"))
import backends as B
import run_students as RS

models = B.load_models()
run_cfg = B.load_run_config()
exec_cfg = models.get("execution", {})
students = [s for s in models["students"] if s.get("enabled", True)]
sys_t = RS._load_prompt("student_system.md", RS._FALLBACK_STUDENT_SYSTEM)
usr_t = RS._load_prompt("student_user_template.md", RS._FALLBACK_STUDENT_USER)

# build seed-only tasks for every family
all_tasks = []
for fam in B.list_families("all"):
    slug = B.family_slug(fam)
    seedmap = RS.seed_criteria_map(fam, slug)
    for cd, sc in seedmap.items():
        all_tasks.append((fam, cd, sc, sc.statement_path.read_text()))

jobs = [(t, s) for s in students for t in all_tasks]
print(f"[seed-check] {len(all_tasks)} seed problems x {len(students)} students = {len(jobs)} generations",
      flush=True)

def work(job):
    (fam, cd, sc, stmt), student = job
    RS._family = fam
    return RS.attempt((cd, sc, "v000", stmt, None), student, sys_t, usr_t, run_cfg, exec_cfg)

with ThreadPoolExecutor(max_workers=6) as ex:
    for i, r in enumerate(ex.map(work, jobs), 1):
        if i % 10 == 0:
            print(f"  ...{i}/{len(jobs)}", flush=True)

# ---- report ----
print("\n===== SEED (base-data) failure rate per family =====", flush=True)
for fam in B.list_families("all"):
    slug = B.family_slug(fam)
    seedmap = RS.seed_criteria_map(fam, slug)
    print(f"\nfamily_{fam} ({slug})")
    for cd in sorted(seedmap):
        row = []
        for s in students:
            vj = ROOT / "agentic/attempts" / f"family_{fam}" / cd / "v000" / s["id"] / "verdict.json"
            if not vj.exists():
                row.append(f"{s['id']}:?"); continue
            d = json.loads(vj.read_text()); cs = d.get("cases", [])
            p = sum(1 for x in cs if x["verdict"] == "PASS")
            row.append(f"{s['id']}:{p}/{len(cs)}")
        print(f"  {cd:<24} " + "  ".join(row))
print("\n[seed-check] done.", flush=True)

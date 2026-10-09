#!/usr/bin/env python3
"""Evaluate the frontier models on ALL hardened statement variants of family 01,
using the exact same run_students machinery (generate -> judge -> verdict.json) so the
numbers are directly comparable to the students' hardened-variant aggregate.

Resumable: skips any (variant, model) that already has a verdict.json.
Run from your own terminal so it survives:

    cd complexity-benchmark
    nohup python run_frontier_variants.py > frontier_variants.log 2>&1 &
    tail -f frontier_variants.log
"""
import os, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))                     # harness.*
sys.path.insert(0, str(ROOT / "agentic/tools"))
import backends as B
import run_students as RS

FAM = os.environ.get("FAM", "01")                 # which family (FAM=16 python run_frontier_variants.py)
RS._family = FAM
RS._reset = False
models = B.load_models()
run_cfg = B.load_run_config()
exec_cfg = models.get("execution", {})
fronts = models.get("frontier_evaluators", [])
sys_t = RS._load_prompt("student_system.md", RS._FALLBACK_STUDENT_SYSTEM)
usr_t = RS._load_prompt("student_user_template.md", RS._FALLBACK_STUDENT_USER)

slug = B.family_slug(FAM)
seedmap = RS.seed_criteria_map(FAM, slug)
tasks = list(RS.build_tasks(FAM, None, slug, seedmap))   # all criteria, all variants
jobs = [(t, f) for f in fronts for t in tasks]
print(f"frontier variant-eval: {len(tasks)} tasks x {len(fronts)} models = {len(jobs)} generations",
      flush=True)

done = [0]
def work(job):
    t, f = job
    r = RS.attempt(t, f, sys_t, usr_t, run_cfg, exec_cfg)
    done[0] += 1
    if done[0] % 10 == 0:
        print(f"  ...{done[0]}/{len(jobs)}", flush=True)
    return r

with ThreadPoolExecutor(max_workers=6) as ex:
    for _ in ex.map(work, jobs):
        pass
print("GENDONE", flush=True)

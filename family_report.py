#!/usr/bin/env python3
"""Parameterized final report. Usage:  FAM=NN python family_report.py
Prints the standard table for a family: per model, NPC test / P test / NPC worst / NPC overall (equal
weight), plus averages, for all 6 models (4 students + 2 frontier). Reads hardening verdicts and the
worst-case json written by worstcase_probe.py."""
import os, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FAM=os.environ.get("FAM","17")
students=["gpt-oss-120b","qwen3-coder","deepseek-v4-flash","glm-5"]
front=["gpt-5.6-sol","gemini-3.7-flash-frontier"]
ATT=ROOT/"agentic/attempts"/f"family_{FAM}"; LIN=ROOT/"agentic/lineages"/f"family_{FAM}"

def hard(m,c):
    p=t=0
    for r in [ATT/c,LIN/c]:
        if not r.exists(): continue
        for vj in r.glob(f"**/{m}/verdict.json"):
            try: d=json.loads(vj.read_text())
            except: continue
            for x in d.get("cases",[]): t+=1; p+=x["verdict"]=="PASS"
    return (100*p//t) if t else None

wc={}
wf=ROOT/"agentic/reports"/f"worstcase_family_{FAM}.json"
if wf.exists(): wc=json.loads(wf.read_text())

print(f"\n===== FAMILY {FAM} — full report (test -> worst -> overall) =====")
print(f"{'model':<26}{'NPC test':>9}{'P test':>8}{'NPC worst':>11}{'NPC overall':>13}")
print("-"*67)
agg={"npc":[],"p":[],"worst":[],"ov":[]}
for m in students+front:
    n=hard(m,"criterion_1_npc"); pp=hard(m,"criterion_2_p")
    w=wc.get(m,{}).get("worst_pct")
    ov=None
    if n is not None and w is not None: ov=(n+w)//2
    if n is not None: agg["npc"].append(n)
    if pp is not None: agg["p"].append(pp)
    if w is not None: agg["worst"].append(w)
    if ov is not None: agg["ov"].append(ov)
    f=lambda v,suf="%": (str(v)+suf) if v is not None else "-"
    print(f"{m:<26}{f(n):>9}{f(pp):>8}{f(w):>11}{f(ov):>13}")
print("-"*67)
avg=lambda a: f"{sum(a)/len(a):.1f}%" if a else "-"
print(f"{'AVERAGE (all present)':<26}{avg(agg['npc']):>9}{avg(agg['p']):>8}{avg(agg['worst']):>11}{avg(agg['ov']):>13}")
print("\nNotes: NPC overall = (NPC test + NPC worst)/2 (equal weight). '-' = not yet computed")
print("       (run hardening + frontier + worstcase_probe.py first). P worst-case is a scale tier")
print("       (polynomial) so it is not folded into 'overall'.")

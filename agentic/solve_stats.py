#!/usr/bin/env python3
"""
solve_stats.py -- how many students solve each instance?

Answers: "how many instances can ALL models solve, in how many cases n-1, and so on"
Run from agentic/ :   python solve_stats.py --family 01
"""
import json, glob, argparse, collections, os

ap = argparse.ArgumentParser()
ap.add_argument("--family", default="01")
a = ap.parse_args()

root = f"lineages/family_{a.family}"
crits = sorted({os.path.basename(os.path.dirname(os.path.dirname(p)))
                for p in glob.glob(f"{root}/*/L*/lineage.json")})

ALL = collections.defaultdict(lambda: collections.Counter())
D0 = collections.defaultdict(lambda: collections.Counter())
FINAL = collections.defaultdict(lambda: collections.Counter())
STUD = collections.defaultdict(lambda: collections.Counter())
VERD = collections.defaultdict(lambda: collections.Counter())
TIER = collections.defaultdict(lambda: collections.Counter())
OUT = collections.defaultdict(lambda: collections.Counter())
DEPTHS = collections.defaultdict(list)

for crit in crits:
    for f in sorted(glob.glob(f"{root}/{crit}/L*/lineage.json")):
        d = json.load(open(f))
        OUT[crit][d.get("outcome", "?")] += 1
        DEPTHS[crit].append(d.get("final_depth", 0))
        pds = [p for p in d.get("per_depth", []) if p.get("verdicts")]
        for i, p in enumerate(pds):
            v = p["verdicts"]
            n_tot = len(v)
            n_pass = sum(1 for x in v.values() if x == "PASS")
            key = f"{n_pass}/{n_tot}"
            ALL[crit][key] += 1
            if p.get("depth") == 0:
                D0[crit][key] += 1
            if i == len(pds) - 1:
                FINAL[crit][key] += 1
            for s, verd in v.items():
                VERD[s][verd] += 1
                STUD[crit][s] += (1 if verd == "PASS" else 0)
                STUD[crit][s + "__n"] += 1
            for s, tv in (p.get("tier_verdicts") or {}).items():
                for tier in ("anchor", "corner", "scaled"):
                    t = (tv or {}).get(tier)
                    if not t:
                        continue
                    TIER[tier][t.get("verdict_type", "?")] += 1

def show(title, table):
    print(f"\n== {title} ==")
    for crit in crits:
        c = table[crit]
        tot = sum(c.values())
        if not tot:
            continue
        parts = "  ".join(f"{k}:{v}({100*v/tot:.0f}%)"
                          for k, v in sorted(c.items(), reverse=True))
        print(f"  {crit:<24} n={tot:<4} {parts}")

print(f"########## family {a.family} -- solve-rate distribution ##########")
show("ALL depths: how many students passed", ALL)
show("DEPTH 0 only (the seed/base version)", D0)
show("FINAL depth of each lineage", FINAL)

print("\n== Per-student pass rate ==")
for crit in crits:
    print(f"  [{crit}]")
    for s in sorted(k for k in STUD[crit] if not k.endswith("__n")):
        n = STUD[crit][s + "__n"]
        print(f"    {s:<22} {STUD[crit][s]}/{n} ({100*STUD[crit][s]/max(n,1):.0f}%)")

print("\n== Verdict types per student (all criteria) ==")
for s in sorted(VERD):
    tot = sum(VERD[s].values())
    print(f"  {s:<22} " + "  ".join(f"{k}:{v}({100*v/tot:.0f}%)"
                                     for k, v in VERD[s].most_common()))

print("\n== Verdict types per tier (all students) ==")
for tier in ("anchor", "corner", "scaled"):
    c = TIER[tier]; tot = sum(c.values())
    if tot:
        print(f"  {tier:<8} " + "  ".join(f"{k}:{v}({100*v/tot:.0f}%)"
                                          for k, v in c.most_common()))

print("\n== Lineage outcomes ==")
for crit in crits:
    ds = DEPTHS[crit]
    avg = sum(ds)/len(ds) if ds else 0
    print(f"  {crit:<24} {dict(OUT[crit])}  avg_final_depth={avg:.1f}")

print("\n== Contamination check: empty solution.py ==")
tot_e = 0
per = collections.Counter()
for p in glob.glob(f"{root}/*/L*/d*/attempts/*/solution.py"):
    if os.path.getsize(p) == 0:
        per[os.path.basename(os.path.dirname(p))] += 1
        tot_e += 1
print(f"  total empty: {tot_e}")
for s, n in per.most_common():
    print(f"    {s:<22} {n}")

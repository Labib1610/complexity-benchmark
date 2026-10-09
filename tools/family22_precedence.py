#!/usr/bin/env python3
"""Family 22 — PRECEDENCE SCHEDULING (unit-time jobs).  NPC = >=2 machines, makespan <= T
(P2|prec|Cmax is NP-complete); P = single machine (any valid order = topological sort). Both
witness-graded. Obscure: OR/scheduling-specific, outside general CS curricula.

NPC I/O: line1 "n M T m"; next m lines "a b" (job a must finish before b starts). Output: "YES" then
         n integers slot[1..n] (time slot 1..T of each job); or "NO".
P   I/O: line1 "n m"; next m lines "a b". Output: "YES" then a permutation of 1..n = a processing order
         respecting all precedences (single machine); or "NO" (cycle).
"""
import argparse, random, sys
from collections import deque, defaultdict

def _dag(n, m, seed):
    rng=random.Random(seed*2_600_003+n); edges=set()
    while len(edges)<m:
        a=rng.randint(1,n-1); b=rng.randint(a+1,n)   # a<b keeps it acyclic
        edges.add((a,b))
    return sorted(edges)

def _list_schedule(n, M, edges):
    """O(n+m) list scheduling on M machines (unit jobs): topo order, assign each job the earliest
    non-full slot >= 1+max(pred slot). Returns slot[1..n] and makespan."""
    from collections import deque, defaultdict
    succ=defaultdict(list); indeg=[0]*(n+1)
    for a,b in edges: succ[a].append(b); indeg[b]+=1
    earliest=[1]*(n+1); slot=[0]*(n+1); count=defaultdict(int)
    q=deque(sorted(j for j in range(1,n+1) if indeg[j]==0))
    while q:
        u=q.popleft(); s=earliest[u]
        while count[s]>=M: s+=1
        count[s]+=1; slot[u]=s
        for b in succ[u]:
            if s+1>earliest[b]: earliest[b]=s+1
            indeg[b]-=1
            if indeg[b]==0: q.append(b)
    return slot, (max(slot[1:]) if n else 0)

# ---------- NPC: M machines, unit jobs, makespan <= T (list scheduling plants T) ----------
def npc_plant(n, M, seed):
    edges=_dag(n, min(int(1.5*n), n*(n-1)//2), seed)
    slot,T=_list_schedule(n, M, edges)
    lines=[f"{n} {M} {T} {len(edges)}"]+[f"{a} {b}" for a,b in edges]
    return "\n".join(lines)+"\n"

def _npc_parse(text):
    d=text.split(); n=int(d[0]); M=int(d[1]); T=int(d[2]); m=int(d[3])
    edges=[(int(d[4+2*i]),int(d[5+2*i])) for i in range(m)]
    return n,M,T,m,edges

def npc_reference(text):
    n,M,T,m,edges=_npc_parse(text)
    slot,ms=_list_schedule(n, M, edges)
    if ms>T: return "NO\n"
    return "YES\n"+" ".join(str(slot[i]) for i in range(1,n+1))+"\n"

def npc_validate(input_text, output_text):
    n,M,T,m,edges=_npc_parse(input_text); toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO": return False,"claimed NO but a schedule <= T was planted"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: slot=[0]+[int(x) for x in nums]
    except ValueError: return False,"non-integer"
    if len(slot)!=n+1: return False,f"expected {n} slots"
    if any(s<1 or s>T for s in slot[1:]): return False,f"slots must be in 1..T={T}"
    for a,b in edges:
        if slot[b]<=slot[a]: return False,f"precedence {a}->{b} violated"
    cnt=defaultdict(int)
    for s in slot[1:]:
        cnt[s]+=1
        if cnt[s]>M: return False,f"slot {s} has >{M} jobs"
    return True,f"valid schedule, makespan {max(slot[1:])} <= T={T}"

# ---------- P: single machine, any valid order (topological sort) ----------
def p_plant(n, seed):
    edges=_dag(n, min(int(1.2*n), n*(n-1)//2), seed)
    return "\n".join([f"{n} {len(edges)}"]+[f"{a} {b}" for a,b in edges])+"\n"

def p_reference(text):
    d=text.split(); n=int(d[0]); m=int(d[1])
    succ=defaultdict(list); indeg=[0]*(n+1)
    for i in range(m):
        a=int(d[2+2*i]); b=int(d[3+2*i]); succ[a].append(b); indeg[b]+=1
    q=deque(sorted(j for j in range(1,n+1) if indeg[j]==0)); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for b in sorted(succ[u]):
            indeg[b]-=1
            if indeg[b]==0: q.append(b)
    if len(order)!=n: return "NO\n"
    return "YES\n"+" ".join(map(str,order))+"\n"

def p_validate(input_text, output_text):
    d=input_text.split(); n=int(d[0]); m=int(d[1])
    edges=[(int(d[2+2*i]),int(d[3+2*i])) for i in range(m)]
    toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO": return False,"claimed NO but the DAG has a valid order"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: order=[int(x) for x in nums]
    except ValueError: return False,"non-integer"
    if sorted(order)!=list(range(1,n+1)): return False,"not a permutation of 1..n"
    posn={j:i for i,j in enumerate(order)}
    for a,b in edges:
        if posn[a]>=posn[b]: return False,f"precedence {a}->{b} violated"
    return True,"valid processing order"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--crit",choices=["npc","p"],default="npc")
    ap.add_argument("--gen",action="store_true"); ap.add_argument("--ref",metavar="F"); ap.add_argument("--grade",metavar="F")
    ap.add_argument("--n",type=int,default=100); ap.add_argument("--M",type=int,default=3); ap.add_argument("--seed",type=int,default=1)
    a=ap.parse_args()
    if a.crit=="npc":
        if a.gen: sys.stdout.write(npc_plant(a.n,a.M,a.seed))
        elif a.ref: sys.stdout.write(npc_reference(open(a.ref).read()))
        elif a.grade: ok,msg=npc_validate(open(a.grade).read(),sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg)
    else:
        if a.gen: sys.stdout.write(p_plant(a.n,a.seed))
        elif a.ref: sys.stdout.write(p_reference(open(a.ref).read()))
        elif a.grade: ok,msg=p_validate(open(a.grade).read(),sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg)
if __name__=="__main__": main()

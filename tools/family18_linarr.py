#!/usr/bin/env python3
"""Family 18 — MINIMUM LINEAR ARRANGEMENT.  NPC = general graphs (NP-hard); P = trees (poly, Chung).
Decision+witness reframe: given a graph and budget B, output a linear arrangement (a permutation giving
each vertex a distinct position 1..n) whose total edge stretch sum|pos(u)-pos(v)| is <= B, or NO.
Witness-graded (verify the permutation and the sum). B is set to a BFS-order arrangement's cost, so a
solution provably exists; the reference reproduces that arrangement. Obscure: VLSI/graph-layout niche.

I/O: line1 "n m B"; next m lines "u v" (edges, 1..n). Output: "YES" then n integers pos[1..n]
     (a permutation of 1..n), or "NO".
"""
import argparse, random, sys
from collections import deque

def _bfs_arrangement(n, adj):
    pos = [0]*(n+1); seen=[False]*(n+1); nxt=1
    for s in range(1, n+1):
        if seen[s]: continue
        seen[s]=True; q=deque([s])
        while q:
            u=q.popleft(); pos[u]=nxt; nxt+=1
            for v in sorted(adj[u]):
                if not seen[v]: seen[v]=True; q.append(v)
    return pos

def _cost(edges, pos): return sum(abs(pos[u]-pos[v]) for u,v in edges)

def plant(n, kind, seed):
    rng=random.Random(seed*1_800_019+n); adj=[set() for _ in range(n+1)]; edges=[]
    def add(u,v):
        if u!=v and v not in adj[u]: adj[u].add(v); adj[v].add(u); edges.append((u,v))
    if kind=="tree":
        for v in range(2, n+1): add(v, rng.randint(1, v-1))
    else:  # general: a random tree for connectivity + extra random edges
        for v in range(2, n+1): add(v, rng.randint(1, v-1))
        extra=int(1.5*n)
        for _ in range(extra): add(rng.randint(1,n), rng.randint(1,n))
    pos=_bfs_arrangement(n, adj); B=_cost(edges, pos)
    lines=[f"{n} {len(edges)} {B}"]+[f"{u} {v}" for u,v in edges]
    return "\n".join(lines)+"\n"

def _parse(text):
    d=text.split(); n=int(d[0]); m=int(d[1]); B=int(d[2])
    edges=[(int(d[3+2*i]),int(d[4+2*i])) for i in range(m)]
    return n,m,B,edges

def reference(text):
    n,m,B,edges=_parse(text); adj=[set() for _ in range(n+1)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    pos=_bfs_arrangement(n,adj)
    if _cost(edges,pos)<=B: return "YES\n"+" ".join(str(pos[i]) for i in range(1,n+1))+"\n"
    return "NO\n"

def validate(input_text, output_text):
    n,m,B,edges=_parse(input_text); toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO": return False,"claimed NO but an arrangement <= B was planted"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: pos=[0]+[int(x) for x in nums]
    except ValueError: return False,"non-integer"
    if len(pos)!=n+1: return False,f"expected {n} positions"
    if sorted(pos[1:])!=list(range(1,n+1)): return False,"positions must be a permutation of 1..n"
    c=_cost(edges,pos)
    return (c<=B),(f"stretch {c} <= B={B}" if c<=B else f"stretch {c} > B={B}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--gen",action="store_true"); ap.add_argument("--ref",metavar="F"); ap.add_argument("--grade",metavar="F")
    ap.add_argument("--n",type=int,default=100); ap.add_argument("--kind",default="general"); ap.add_argument("--seed",type=int,default=1)
    a=ap.parse_args()
    if a.gen: sys.stdout.write(plant(a.n,a.kind,a.seed))
    elif a.ref: sys.stdout.write(reference(open(a.ref).read()))
    elif a.grade:
        ok,msg=validate(open(a.grade).read(),sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg)
    else: ap.error("use --gen/--ref/--grade")
if __name__=="__main__": main()

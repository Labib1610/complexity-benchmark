#!/usr/bin/env python3
"""Family 19 — MULTICOMMODITY FLOW.  NPC = >=2 commodities, INTEGER flow (feasibility is NP-complete,
Even-Itai-Shamir); P = single commodity (max-flow, poly). Both witness-graded: verify per-commodity
conservation + demand + shared-edge capacity + integrality. Obscure: deep network-flow theory.

I/O: line1 "n m k"; next k lines "s_i t_i d_i" (demand of commodity i); next m lines "u v cap"
     (directed edge u->v, capacity). Output: "YES" then k lines, each m integers = flow of commodity i
     on edge j (input order); or "NO".
"""
import argparse, random, sys
from collections import defaultdict, deque

def plant(n, k, seed):
    """Route each commodity along a random simple path carrying its demand; capacity = planted usage
    (+ slack). The planted per-edge/per-commodity flow is a feasible integer solution (the witness)."""
    rng=random.Random(seed*1_900_007+n+k)
    edge_index={}; edges=[]; usage=defaultdict(lambda: defaultdict(int))  # (u,v)->{commodity:flow}
    commodities=[]; witness=[]  # witness[i] aligned to edges after all added
    paths=[]
    for i in range(k):
        s=rng.randint(1,n); 
        t=rng.randint(1,n)
        while t==s: t=rng.randint(1,n)
        # random simple path s -> ... -> t
        length=rng.randint(1,4); mids=rng.sample([x for x in range(1,n+1) if x not in (s,t)], min(length, max(0,n-2)))
        path=[s]+mids+[t]; d=rng.randint(1,6)
        commodities.append((s,t,d)); paths.append((path,d))
        for a,b in zip(path,path[1:]):
            if (a,b) not in edge_index:
                edge_index[(a,b)]=len(edges); edges.append([a,b,0])
            usage[(a,b)][i]+=d
    # capacities = total planted usage (+ small slack), and a few extra unused edges as decoys
    for (a,b),perc in usage.items():
        edges[edge_index[(a,b)]][2]=sum(perc.values())+rng.randint(0,2)
    for _ in range(int(0.5*n)):
        a=rng.randint(1,n); b=rng.randint(1,n)
        if a!=b and (a,b) not in edge_index:
            edge_index[(a,b)]=len(edges); edges.append([a,b,rng.randint(1,4)])
    m=len(edges)
    # witness: flow[i][j]
    flow=[[0]*m for _ in range(k)]
    for i,(path,d) in enumerate(paths):
        for a,b in zip(path,path[1:]): flow[i][edge_index[(a,b)]]=d
    text="\n".join([f"{n} {m} {k}"]+[f"{s} {t} {d}" for s,t,d in commodities]+[f"{u} {v} {c}" for u,v,c in edges])+"\n"
    wit="YES\n"+"\n".join(" ".join(map(str,flow[i])) for i in range(k))+"\n"
    return text, wit

def _parse(text):
    d=text.split(); idx=0; n=int(d[0]); m=int(d[1]); k=int(d[2]); idx=3
    comm=[]
    for _ in range(k): comm.append((int(d[idx]),int(d[idx+1]),int(d[idx+2]))); idx+=3
    edges=[]
    for _ in range(m): edges.append((int(d[idx]),int(d[idx+1]),int(d[idx+2]))); idx+=3
    return n,m,k,comm,edges

def validate(input_text, output_text, single=False):
    n,m,k,comm,edges=_parse(input_text)
    toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO": return False,"claimed NO but a feasible flow was planted"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: vals=[int(x) for x in nums]
    except ValueError: return False,"non-integer flow"
    if len(vals)!=k*m: return False,f"expected {k}*{m}={k*m} flow values, got {len(vals)}"
    flow=[vals[i*m:(i+1)*m] for i in range(k)]
    # capacity (shared across commodities)
    for j,(u,v,c) in enumerate(edges):
        tot=sum(flow[i][j] for i in range(k))
        if any(flow[i][j]<0 for i in range(k)): return False,"negative flow"
        if tot>c: return False,f"edge {u}->{v} capacity {c} exceeded ({tot})"
    # conservation + demand per commodity
    for i,(s,t,dem) in enumerate(comm):
        net=defaultdict(int)
        for j,(u,v,c) in enumerate(edges):
            f=flow[i][j]; net[u]+=f; net[v]-=f
        for node in range(1,n+1):
            want = dem if node==s else (-dem if node==t else 0)
            if net[node]!=want: return False,f"commodity {i}: conservation fails at node {node}"
    return True,f"feasible {k}-commodity integer flow"

# ---- single-commodity reference (P): Dinic max-flow, route the demand ----
def single_reference(text):
    n,m,k,comm,edges=_parse(text)
    s,t,dem=comm[0]
    from collections import deque
    S0=n+1; N=n+1
    g=[[] for _ in range(N+1)]
    def add(u,v,c):
        g[u].append([v,c,len(g[v])]); g[v].append([u,0,len(g[u])-1])
    eref=[]
    for (u,v,c) in edges:
        eref.append((u,len(g[u]))); add(u,v,c)
    add(S0, s, dem)      # limiter: at most dem units can enter s -> flow value is exactly min(maxflow,dem)
    s=S0
    def bfs():
        lvl=[-1]*(N+1); lvl[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for e in g[u]:
                if e[1]>0 and lvl[e[0]]<0: lvl[e[0]]=lvl[u]+1; q.append(e[0])
        return lvl
    def dfs(u,f,lvl,it):
        if u==t: return f
        while it[u]<len(g[u]):
            e=g[u][it[u]]
            if e[1]>0 and lvl[e[0]]==lvl[u]+1:
                d=dfs(e[0],min(f,e[1]),lvl,it)
                if d>0: e[1]-=d; g[e[0]][e[2]][1]+=d; return d
            it[u]+=1
        return 0
    flow=0
    while True:
        lvl=bfs()
        if lvl[t]<0: break
        it=[0]*(N+1)
        while True:
            f=dfs(s,float("inf"),lvl,it)
            if f==0: break
            flow+=f
    if flow<dem: return "NO\n"
    # recover per-edge flow (cap - residual on forward), cap the total at dem by using residual value
    out=[]
    for (u,slot) in eref:
        fwd=g[u][slot]; used=0
        out.append(used)  # placeholder; recompute below
    # recompute forward usage = original cap - current residual
    res=[]
    for j,(u,v,c) in enumerate(edges):
        u0,slot=eref[j]; used=c-g[u0][slot][1]; res.append(max(0,used))
    return "YES\n"+" ".join(map(str,res))+"\n"

def multi_reference(text):
    """Greedy per-commodity routing (successive augmenting paths on shared residual). Feasible for the
    planted instances at small/medium sizes; grading is witness-based so exactness at scale is not required."""
    from collections import deque
    n,m,k,comm,edges=_parse(text)
    resid=[c for (_,_,c) in edges]
    adj=[[] for _ in range(n+1)]
    for j,(u,v,c) in enumerate(edges): adj[u].append(j)
    flow=[[0]*m for _ in range(k)]
    for i,(s,t,dem) in enumerate(comm):
        need=dem
        while need>0:
            prevj=[-1]*(n+1); prev=[-1]*(n+1); q=deque([s]); prev[s]=s
            while q:
                u=q.popleft()
                for j in adj[u]:
                    v=edges[j][1]
                    if prev[v]==-1 and resid[j]>0:
                        prev[v]=u; prevj[v]=j; q.append(v)
            if prev[t]==-1: return "NO\n"
            # bottleneck along path
            b=need; x=t
            while x!=s: b=min(b,resid[prevj[x]]); x=prev[x]
            x=t
            while x!=s: j=prevj[x]; resid[j]-=b; flow[i][j]+=b; x=prev[x]
            need-=b
    return "YES\n"+"\n".join(" ".join(map(str,flow[i])) for i in range(k))+"\n"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--crit",choices=["npc","p"],default="npc")
    ap.add_argument("--gen",action="store_true"); ap.add_argument("--ref",metavar="F"); ap.add_argument("--grade",metavar="F")
    ap.add_argument("--n",type=int,default=40); ap.add_argument("--k",type=int,default=2); ap.add_argument("--seed",type=int,default=1)
    a=ap.parse_args(); single=(a.crit=="p")
    if a.gen:
        text,wit=plant(a.n, 1 if single else a.k, a.seed); sys.stdout.write(text)
    elif a.ref:
        if single: sys.stdout.write(single_reference(open(a.ref).read()))
        else: sys.stdout.write(multi_reference(open(a.ref).read()))
    elif a.grade:
        ok,msg=validate(open(a.grade).read(), sys.stdin.read(), single=single); print("PASS" if ok else "FAIL","--",msg)
if __name__=="__main__": main()

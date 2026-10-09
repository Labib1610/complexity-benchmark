#!/usr/bin/env python3
"""Family 21 — MULTIWAY / MULTITERMINAL CUT.  NPC = >=3 terminals (min edges to separate all
terminals; NP-complete for k>=3); P = 2 terminals = s-t min-cut (max-flow / min-cut, poly). Both
decision+witness: output a set of edges whose removal separates the required terminals, total weight
<= B. Witness-graded (union-find after removing the cut). Obscure: specialized cut-algorithms lit.

NPC I/O: line1 "n m k B"; line2 k terminal ids; next m lines "u v w". Output: "YES" then a line with
         the number c of cut edges, then c lines "u v" (edges to remove), or "NO".
P   I/O: line1 "n m s t B"; next m lines "u v w". Output: same cut format separating s and t.
"""
import argparse, random, sys
from collections import defaultdict, deque

# ---------------- Dinic max-flow / min-cut (for the P side reference) ----------------
class Dinic:
    def __init__(self, n):
        self.n=n; self.g=[[] for _ in range(n+1)]
    def add(self,u,v,c):
        self.g[u].append([v,c,len(self.g[v])]); self.g[v].append([u,0,len(self.g[u])-1])
    def bfs(self,s,t):
        self.lvl=[-1]*(self.n+1); self.lvl[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for e in self.g[u]:
                if e[1]>0 and self.lvl[e[0]]<0: self.lvl[e[0]]=self.lvl[u]+1; q.append(e[0])
        return self.lvl[t]>=0
    def dfs(self,u,t,f):
        if u==t: return f
        while self.it[u]<len(self.g[u]):
            e=self.g[u][self.it[u]]
            if e[1]>0 and self.lvl[e[0]]==self.lvl[u]+1:
                d=self.dfs(e[0],t,min(f,e[1]))
                if d>0: e[1]-=d; self.g[e[0]][e[2]][1]+=d; return d
            self.it[u]+=1
        return 0
    def maxflow(self,s,t):
        flow=0
        while self.bfs(s,t):
            self.it=[0]*(self.n+1); 
            while True:
                f=self.dfs(s,t,float("inf"))
                if f==0: break
                flow+=f
        return flow
    def min_cut_side(self,s):
        return set(u for u in range(1,self.n+1) if self.lvl[u]>=0)

def _st_mincut(n, edges, s, t):
    d=Dinic(n)
    for u,v,w in edges: d.add(u,v,w); d.add(v,u,w)   # undirected
    val=d.maxflow(s,t); d.bfs(s,t); S=d.min_cut_side(s)
    cut=[(u,v) for (u,v,w) in edges if (u in S)!=(v in S)]
    return val, cut

def _iso_cut(n, terms, edges):
    """Isolation heuristic cut (same as reference): union of per-terminal min-cuts vs the others."""
    cost={(min(u,v),max(u,v)):w for u,v,w in edges}; cutset=set()
    for i,ti in enumerate(terms):
        d=Dinic(n+1); SUPER=n+1
        for u,v,w in edges: d.add(u,v,w); d.add(v,u,w)
        for j,tj in enumerate(terms):
            if j!=i: d.add(tj,SUPER,10**9); d.add(SUPER,tj,10**9)
        d.maxflow(ti,SUPER); d.bfs(ti,SUPER); S=d.min_cut_side(ti)
        for (u,v,w) in edges:
            if (u in S)!=(v in S): cutset.add((min(u,v),max(u,v)))
    return sum(cost[e] for e in cutset)

# ---------------- plant a multiway-cut instance (regions) ----------------
def plant(n, k, seed, two=False):
    """Partition vertices into k regions (region i contains terminal i). Intra-region edges cheap and
    plentiful; inter-region edges are the cut (set B = their total weight = a feasible multiway cut)."""
    if two: k=2
    rng=random.Random(seed*2_100_017+n)
    region=[0]+[rng.randrange(k) for _ in range(n)]
    terms=[]
    for i in range(k):
        members=[v for v in range(1,n+1) if region[v]==i]
        if not members:  # ensure each region non-empty
            v=rng.randint(1,n); region[v]=i; members=[v]
        terms.append(members[0])
    edges=[]
    # intra-region: many cheap edges (keep each region connected)
    for i in range(k):
        mem=[v for v in range(1,n+1) if region[v]==i]
        for j in range(1,len(mem)): edges.append((mem[j], mem[rng.randint(0,j-1)], rng.randint(1,3)))
    # inter-region edges (these form the planted cut)
    inter=int(0.6*n)
    cutw=0
    for _ in range(inter):
        u=rng.randint(1,n); v=rng.randint(1,n)
        if region[u]!=region[v] and u!=v:
            w=rng.randint(1,5); edges.append((u,v,w)); cutw+=w
    B=max(cutw, _iso_cut(n, terms, edges))   # guarantee the reference isolation cut is <= B
    if two:
        lines=[f"{n} {len(edges)} {terms[0]} {terms[1]} {B}"]+[f"{u} {v} {w}" for u,v,w in edges]
    else:
        lines=[f"{n} {len(edges)} {k} {B}", " ".join(map(str,terms))]+[f"{u} {v} {w}" for u,v,w in edges]
    return "\n".join(lines)+"\n"

def _parse(text, two=False):
    d=text.split(); idx=0; n=int(d[0]); m=int(d[1]); idx=2
    if two:
        s=int(d[2]); t=int(d[3]); B=int(d[4]); idx=5; terms=[s,t]
    else:
        k=int(d[2]); B=int(d[3]); idx=4; terms=[int(d[idx+i]) for i in range(k)]; idx+=k
    edges=[]; cost={}
    for i in range(m):
        u=int(d[idx]); v=int(d[idx+1]); w=int(d[idx+2]); idx+=3; edges.append((u,v,w)); cost[(min(u,v),max(u,v))]=w
    return n,m,terms,B,edges,cost

def reference(text, two=False):
    n,m,terms,B,edges,cost=_parse(text,two)
    if two:
        val,cut=_st_mincut(n,edges,terms[0],terms[1])
        if val<=B: return "YES\n%d\n%s"%(len(cut),"\n".join(f"{u} {v}" for u,v in cut))+"\n"
        return "NO\n"
    # NPC: the planted inter-region edges are a feasible multiway cut of weight B -> just output them
    # (find inter-region edges by max-flow isolating each terminal is heavier; the planted B cut works)
    # Recover a feasible cut: isolate each terminal via s-t cuts against a super-sink of the others,
    # union the cut edges (classic isolation heuristic; <= optimal*2, and <= B here by construction).
    cutset=set()
    for i,ti in enumerate(terms):
        d=Dinic(n+1); SUPER=n+1
        for u,v,w in edges: d.add(u,v,w); d.add(v,u,w)
        for j,tj in enumerate(terms):
            if j!=i: d.add(tj, SUPER, 10**9); d.add(SUPER, tj, 10**9)
        d.maxflow(ti, SUPER); d.bfs(ti, SUPER); S=d.min_cut_side(ti)
        for (u,v,w) in edges:
            if (u in S)!=(v in S): cutset.add((min(u,v),max(u,v)))
    total=sum(cost[e] for e in cutset)
    if total<=B:
        return "YES\n%d\n%s"%(len(cutset),"\n".join(f"{u} {v}" for u,v in sorted(cutset)))+"\n"
    return "NO\n"

def validate(text, output_text, two=False):
    n,m,terms,B,edges,cost=_parse(text,two)
    toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO": return False,"claimed NO but a cut <= B was planted"
    try:
        c=int(toks[1]); nums=toks[2:2+2*c]
        pairs=[(int(nums[2*i]),int(nums[2*i+1])) for i in range(c)]
    except (ValueError,IndexError): return False,"bad cut format"
    cutset=set(); total=0
    for u,v in pairs:
        e=(min(u,v),max(u,v))
        if e not in cost: return False,f"edge {e} not in graph"
        if e not in cutset: cutset.add(e); total+=cost[e]
    if total>B: return False,f"cut weight {total} > B={B}"
    # union-find over non-cut edges; every pair of terminals must be disconnected
    par=list(range(n+1))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for (u,v,w) in edges:
        if (min(u,v),max(u,v)) not in cutset: par[f(u)]=f(v)
    roots={t:f(t) for t in terms}
    if len(set(roots.values()))!=len(terms): return False,"some terminals still connected"
    return True,f"valid multiway cut, weight {total} <= {B}"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--crit",choices=["npc","p"],default="npc")
    ap.add_argument("--gen",action="store_true"); ap.add_argument("--ref",metavar="F"); ap.add_argument("--grade",metavar="F")
    ap.add_argument("--n",type=int,default=100); ap.add_argument("--k",type=int,default=3); ap.add_argument("--seed",type=int,default=1)
    a=ap.parse_args(); two=(a.crit=="p")
    if a.gen: sys.stdout.write(plant(a.n,a.k,a.seed,two=two))
    elif a.ref: sys.stdout.write(reference(open(a.ref).read(),two=two))
    elif a.grade: ok,msg=validate(open(a.grade).read(),sys.stdin.read(),two=two); print("PASS" if ok else "FAIL","--",msg)
if __name__=="__main__": main()

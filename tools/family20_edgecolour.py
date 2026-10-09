#!/usr/bin/env python3
"""Family 20 — EDGE COLOURING.  NPC = 3-edge-colouring of cubic graphs (Holyer: class-1 vs class-2 is
NP-complete); P = bipartite edge colouring in Delta colours (Konig's theorem, always feasible).
Both witness-graded: verify adjacent edges (sharing a vertex) get different colours.

3EC (NPC) I/O: line1 "n m"; next m lines "u v" (cubic, 1..n). Output: "YES" then m integers in {1,2,3}
              (colour of edge i in input order), or "NO".
BEC (P)   I/O: line1 "nL nR m"; next m lines "u v" (u in 1..nL side, v in 1..nR side). Output: "YES"
              then m integers (colours 1..Delta), or "NO" (never, bipartite is always Delta-colourable).
"""
import argparse, random, sys
sys.setrecursionlimit(1 << 20)

# ---------------- 3-edge-colouring cubic graphs (NPC) ----------------
def cubic_plant(n, seed):
    """3-regular graph that is 3-edge-colourable by construction = union of 3 edge-disjoint perfect
    matchings (n even). The colouring (which matching) is hidden in the edge list."""
    assert n % 2 == 0
    rng = random.Random(seed * 1_700_021 + n)
    used = set(); matchings = []
    def rand_pm(avoid):
        for _ in range(200):
            verts = list(range(1, n + 1)); rng.shuffle(verts)
            pm = []; ok = True
            for i in range(0, n, 2):
                a, b = verts[i], verts[i+1]; e = (min(a,b), max(a,b))
                if e in avoid or a == b: ok = False; break
                pm.append(e)
            if ok and len(set(pm)) == n // 2:
                return pm
        return None
    for _ in range(3):
        pm = rand_pm(used)
        if pm is None: return None
        for e in pm: used.add(e)
        matchings.append(pm)
    tagged = [(e, ci+1) for ci, pm in enumerate(matchings) for e in pm]
    rng.shuffle(tagged)
    edges = [e for e, _ in tagged]; colours = [c for _, c in tagged]
    lines = [f"{n} {len(edges)}"] + [f"{u} {v}" for u, v in edges]
    return "\n".join(lines) + "\n", colours

def _parse(text):
    d = text.split(); n = int(d[0]); m = int(d[1])
    edges = [(int(d[2+2*i]), int(d[3+2*i])) for i in range(m)]
    return n, m, edges

def edge3col_solve(text, deadline=None):
    import time
    n, m, edges = _parse(text)
    inc = [[] for _ in range(n+1)]           # vertex -> list of edge indices
    for i,(u,v) in enumerate(edges): inc[u].append(i); inc[v].append(i)
    col = [0]*m; t0 = time.monotonic()
    # order edges by a DFS-ish adjacency to propagate constraints
    order = sorted(range(m), key=lambda i: -(len(inc[edges[i][0]])+len(inc[edges[i][1]])))
    def used_at(v, exclude):
        s=0
        for j in inc[v]:
            if j!=exclude and col[j]: s |= (1<<col[j])
        return s
    def rec(k):
        if deadline and time.monotonic()-t0>deadline: raise TimeoutError
        if k==m: return True
        i=order[k]; u,v=edges[i]
        forb = used_at(u,i)|used_at(v,i)
        for c in (1,2,3):
            if not (forb>>c)&1:
                col[i]=c
                if rec(k+1): return True
                col[i]=0
        return False
    ok=rec(0)
    return (col if ok else None)

def edge3col_reference(text):
    sol=edge3col_solve(text, deadline=None)
    if sol is None: return "NO\n"
    return "YES\n"+" ".join(map(str,sol))+"\n"

def edge3col_validate(input_text, output_text):
    n,m,edges=_parse(input_text)
    toks=output_text.split()
    if not toks: return False,"empty"
    if toks[0].upper()=="NO":
        try:
            return (edge3col_solve(input_text,deadline=2) is None),"claimed NO"
        except TimeoutError:
            return False,"claimed NO but instance is planted 3-edge-colourable"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: col=[int(x) for x in nums]
    except ValueError: return False,"non-integer"
    if len(col)!=m: return False,f"expected {m} colours, got {len(col)}"
    if any(c<1 or c>3 for c in col): return False,"colours must be in 1..3"
    inc=[[] for _ in range(n+1)]
    for i,(u,v) in enumerate(edges): inc[u].append(i); inc[v].append(i)
    for v in range(1,n+1):
        seen=set()
        for j in inc[v]:
            if col[j] in seen: return False,f"vertex {v} has two edges of colour {col[j]}"
            seen.add(col[j])
    return True,"proper 3-edge-colouring"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--gen",action="store_true"); ap.add_argument("--ref",metavar="F"); ap.add_argument("--grade",metavar="F")
    ap.add_argument("--n",type=int,default=50); ap.add_argument("--seed",type=int,default=1)
    a=ap.parse_args()
    if a.gen: sys.stdout.write((cubic_plant(a.n,a.seed) or ("",None))[0])
    elif a.ref: sys.stdout.write(edge3col_reference(open(a.ref).read()))
    elif a.grade:
        ok,msg=edge3col_validate(open(a.grade).read(),sys.stdin.read()); print("PASS" if ok else "FAIL","--",msg)
    else: ap.error("use --gen/--ref/--grade")
if __name__=="__main__": main()

# ---------------- Bipartite edge colouring in Delta colours (P; Konig) ----------------
def bip_plant(nL, nR, maxdeg, seed):
    """Sample edges directly (O(m)) so it scales to large nL,nR without enumerating all pairs."""
    rng = random.Random(seed * 2_400_017 + nL + nR)
    edges = set(); degL = [0]*(nL+1); degR = [0]*(nR+1)
    target = maxdeg * min(nL, nR); attempts = 0
    while len(edges) < target and attempts < 40*target + 2000:
        attempts += 1
        u = rng.randint(1, nL); v = rng.randint(1, nR)
        if degL[u] < maxdeg and degR[v] < maxdeg and (u, v) not in edges:
            edges.add((u, v)); degL[u]+=1; degR[v]+=1
    el = list(edges); rng.shuffle(el)
    return "\n".join([f"{nL} {nR} {len(el)}"] + [f"{u} {v}" for u, v in el]) + "\n"

def _bip_parse(text):
    d = text.split(); nL=int(d[0]); nR=int(d[1]); m=int(d[2])
    edges=[(int(d[3+2*i]), int(d[4+2*i])) for i in range(m)]
    return nL, nR, m, edges

def bec_reference(text):
    """Konig Delta-edge-colouring of a bipartite graph: decompose the Delta-regular multigraph
    completion into Delta perfect matchings (iterative Kuhn with augmenting-path flips)."""
    from collections import deque
    nL, nR, m, edges = _bip_parse(text)
    degL=[0]*(nL+1); degR=[0]*(nR+1)
    for u,v in edges: degL[u]+=1; degR[v]+=1
    D=max([1]+degL[1:]+degR[1:]); N=max(nL,nR)
    adj=[[] for _ in range(N+1)]; slots=[]; dl=[0]*(N+1); dr=[0]*(N+1)
    for i,(u,v) in enumerate(edges):
        sid=len(slots); slots.append((u,v,i)); adj[u].append(sid); dl[u]+=1; dr[v]+=1
    ldef=[u for u in range(1,N+1) for _ in range(D-dl[u])]
    rdef=[v for v in range(1,N+1) for _ in range(D-dr[v])]
    for u,v in zip(ldef,rdef):
        sid=len(slots); slots.append((u,v,-1)); adj[u].append(sid)
    ecol=[0]*m; alive=[True]*len(slots)
    for colour in range(1, D+1):
        matchR=[0]*(N+1)      # right -> left
        matchL=[0]*(N+1)      # left  -> right
        slotOf=[0]*(N+1)      # right -> sid
        for s in range(1, N+1):
            parent={}         # right v -> (left u, sid)
            seenL={s}; dq=deque([s]); aug_end=None
            while dq and aug_end is None:
                u=dq.popleft()
                for sid in adj[u]:
                    if not alive[sid]: continue
                    v=slots[sid][1]
                    if v in parent: continue
                    parent[v]=(u,sid)
                    if matchR[v]==0:
                        aug_end=v; break
                    w=matchR[v]
                    if w not in seenL:
                        seenL.add(w); dq.append(w)
            if aug_end is not None:
                v=aug_end
                while v!=0:
                    u,sid=parent[v]
                    prev=matchL[u]
                    matchR[v]=u; matchL[u]=v; slotOf[v]=sid
                    v=prev
        for v in range(1, N+1):
            if matchR[v]:
                sid=slotOf[v]; alive[sid]=False
                ri=slots[sid][2]
                if ri>=0: ecol[ri]=colour
    return "YES\n"+" ".join(map(str,ecol))+"\n"

def bec_validate(input_text, output_text):
    nL,nR,m,edges=_bip_parse(input_text)
    degL=[0]*(nL+1); degR=[0]*(nR+1)
    for u,v in edges: degL[u]+=1; degR[v]+=1
    D=max([1]+degL[1:]+degR[1:])
    toks=output_text.split()
    if not toks: return False,"empty"
    nums=toks[1:] if toks[0].upper()=="YES" else toks
    try: col=[int(x) for x in nums]
    except ValueError: return False,"non-integer"
    if len(col)!=m: return False,f"expected {m} colours"
    if any(c<1 or c>D for c in col): return False,f"colours must be in 1..Delta={D}"
    seenL=[set() for _ in range(nL+1)]; seenR=[set() for _ in range(nR+1)]
    for i,(u,v) in enumerate(edges):
        if col[i] in seenL[u] or col[i] in seenR[v]: return False,f"conflict at edge {i}"
        seenL[u].add(col[i]); seenR[v].add(col[i])
    return True,f"proper edge colouring with Delta={D} colours"

#!/usr/bin/env python3
"""Witness-only worst-case generators + graders for the witness-clean original families
(02 SAT, 03 Hamiltonian, 04 subset-sum, 08 vertex-cover, 10 dominating-set, 11 set-cover, 13 partition).
Each plant_* returns (input_text, witness_output) with a planted YES; each grade_* verifies a certificate
in near-linear time (NO recompute) -> gradeable at large sizes where the model's search TLEs. Formats
match the families' existing validators exactly (so model outputs are graded consistently)."""
import random

# ---------------- 02 SAT (3-SAT), input "n m" + m "a b c" (signed lits); out YES + n {0,1} ----------------
def plant_sat(n, ratio, seed):
    rng=random.Random(seed*101+n); A=[rng.randint(0,1) for _ in range(n+1)]
    m=int(ratio*n); cls=[]
    def lit_true(l): return (A[abs(l)]==1) if l>0 else (A[abs(l)]==0)
    for _ in range(m):
        vs=rng.sample(range(1,n+1),3); lits=[v if rng.random()<0.5 else -v for v in vs]
        if not any(lit_true(l) for l in lits):
            i=rng.randint(0,2); lits[i]=abs(lits[i]) if A[abs(lits[i])]==1 else -abs(lits[i])
        cls.append(lits)
    txt="\n".join([f"{n} {m}"]+[f"{a} {b} {c}" for a,b,c in cls])+"\n"
    wit="YES\n"+" ".join(str(A[i]) for i in range(1,n+1))+"\n"
    return txt,wit
def grade_sat(text,out):
    d=text.split(); n=int(d[0]); m=int(d[1]); cls=[(int(d[2+3*i]),int(d[3+3*i]),int(d[4+3*i])) for i in range(m)]
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    v=t[1:]
    if len(v)!=n: return False
    try: a=[0]+[int(x) for x in v]
    except ValueError: return False
    if any(x not in (0,1) for x in a[1:]): return False
    for cl in cls:
        if not any((l>0 and a[l]==1) or (l<0 and a[-l]==0) for l in cl): return False
    return True

# ---------------- 03 Hamiltonian path, input "n m" + edges; out YES + permutation ----------------
def plant_ham(n, extra_mult, seed):
    rng=random.Random(seed*211+n); perm=list(range(1,n+1)); rng.shuffle(perm)
    edges=set((min(perm[i],perm[i+1]),max(perm[i],perm[i+1])) for i in range(n-1))
    tgt=len(edges)+int(extra_mult*n); guard=0
    while len(edges)<tgt and guard<80*tgt+2000:
        guard+=1; u=rng.randint(1,n); v=rng.randint(1,n)
        if u!=v: edges.add((min(u,v),max(u,v)))
    el=list(edges); rng.shuffle(el)
    txt="\n".join([f"{n} {len(el)}"]+[f"{u} {v}" for u,v in el])+"\n"
    wit="YES\n"+" ".join(map(str,perm))+"\n"
    return txt,wit
def grade_ham(text,out):
    d=text.split(); n=int(d[0]); m=int(d[1]); E=set((min(int(d[2+2*i]),int(d[3+2*i])),max(int(d[2+2*i]),int(d[3+2*i]))) for i in range(m))
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: seq=[int(x) for x in t[1:]]
    except ValueError: return False
    if len(seq)!=n or sorted(seq)!=list(range(1,n+1)): return False
    return all((min(a,b),max(a,b)) in E for a,b in zip(seq,seq[1:]))

# ---------------- 04 subset-sum, input "n" + costs + "T"; out YES + indices ----------------
def plant_subset(n, seed):
    rng=random.Random(seed*307+n); costs=[rng.randint(10**6,10**9) for _ in range(n)]
    pick=sorted(rng.sample(range(n), max(1,n//2))); T=sum(costs[i] for i in pick)
    txt="\n".join([str(n)]+[" ".join(map(str,costs))]+[str(T)])+"\n"
    wit="YES\n"+" ".join(str(i+1) for i in pick)+"\n"
    return txt,wit
def grade_subset(text,out):
    d=text.split(); n=int(d[0]); costs=[int(d[1+i]) for i in range(n)]; T=int(d[1+n])
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: idx=[int(x) for x in t[1:]]
    except ValueError: return False
    if len(set(idx))!=len(idx) or any(i<1 or i>n for i in idx): return False
    return sum(costs[i-1] for i in idx)==T

# ---------------- 08 vertex cover, input "n m k" + edges; out YES + verts ----------------
def plant_vc(n, seed):
    rng=random.Random(seed*401+n); cover=set(rng.sample(range(1,n+1), n//2)); k=len(cover)
    edges=set(); tgt=int(2.0*n); guard=0
    cl=list(cover); other=[x for x in range(1,n+1) if x not in cover]
    while len(edges)<tgt and guard<80*tgt+2000:
        guard+=1; u=rng.choice(cl); v=rng.randint(1,n)
        if u!=v: edges.add((min(u,v),max(u,v)))          # every edge touches the cover
    el=list(edges); rng.shuffle(el)
    txt="\n".join([f"{n} {len(el)} {k}"]+[f"{u} {v}" for u,v in el])+"\n"
    wit="YES\n"+" ".join(map(str,sorted(cover)))+"\n"
    return txt,wit
def grade_vc(text,out):
    d=text.split(); n=int(d[0]); m=int(d[1]); k=int(d[2]); edges=[(int(d[3+2*i]),int(d[4+2*i])) for i in range(m)]
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: verts=set(int(x) for x in t[1:])
    except ValueError: return False
    if any(w<1 or w>n for w in verts) or len(verts)>k: return False
    return all(u in verts or v in verts for u,v in edges)

# ---------------- 10 dominating set, input "n m k" + edges; out YES + verts ----------------
def plant_dom(n, seed):
    rng=random.Random(seed*503+n); D=set(rng.sample(range(1,n+1), max(1,n//4))); k=len(D)
    nb=[set() for _ in range(n+1)]; edges=set(); dl=list(D)
    for v in range(1,n+1):                                 # ensure every vertex is dominated by D
        if v in D: continue
        u=rng.choice(dl); edges.add((min(u,v),max(u,v))); nb[u].add(v); nb[v].add(u)
    tgt=len(edges)+int(1.0*n); guard=0
    while len(edges)<tgt and guard<80*tgt+2000:
        guard+=1; u=rng.randint(1,n); v=rng.randint(1,n)
        if u!=v: edges.add((min(u,v),max(u,v)))
    el=list(edges); rng.shuffle(el)
    txt="\n".join([f"{n} {len(el)} {k}"]+[f"{u} {v}" for u,v in el])+"\n"
    wit="YES\n"+" ".join(map(str,sorted(D)))+"\n"
    return txt,wit
def grade_dom(text,out):
    d=text.split(); n=int(d[0]); m=int(d[1]); k=int(d[2])
    nb=[1<<v for v in range(n)]
    for i in range(m):
        u=int(d[3+2*i])-1; v=int(d[4+2*i])-1; nb[u]|=1<<v; nb[v]|=1<<u
    full=(1<<n)-1; t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: chosen=set(int(x) for x in t[1:])
    except ValueError: return False
    if any(w<1 or w>n for w in chosen) or len(chosen)>k: return False
    cov=0
    for w in chosen: cov|=nb[w-1]
    return cov==full

# ---------------- 11 set cover, input "u s k" + s sets "cnt e..."; out YES + picks ----------------
def plant_setcover(u, k, seed):
    rng=random.Random(seed*601+u)
    elems=list(range(1,u+1)); rng.shuffle(elems)
    base=[elems[i::k] for i in range(k)]                   # k disjoint sets covering the universe
    sets=[list(b) for b in base if b]
    while len(sets)<int(3.0*k):                            # decoy sets (random small)
        sets.append(rng.sample(range(1,u+1), rng.randint(1,3)))
    rng.shuffle(sets)
    lines=[f"{u} {len(sets)} {k}"]+[f"{len(s)} "+" ".join(map(str,s)) for s in sets]
    # witness = indices of the base sets after shuffle
    baseset=[frozenset(b) for b in base if b]; picks=[i+1 for i,s in enumerate(sets) if frozenset(s) in baseset]
    txt="\n".join(lines)+"\n"; wit="YES\n"+" ".join(map(str,picks[:k]))+"\n"
    return txt,wit
def grade_setcover(text,out):
    d=text.split(); idx=0; u=int(d[0]); s=int(d[1]); k=int(d[2]); idx=3
    masks=[]
    for _ in range(s):
        cnt=int(d[idx]); idx+=1; mk=0
        for _ in range(cnt): mk|=1<<(int(d[idx])-1); idx+=1
        masks.append(mk)
    full=(1<<u)-1; t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: picks=set(int(x) for x in t[1:])
    except ValueError: return False
    if any(p<1 or p>s for p in picks) or len(picks)>k: return False
    cov=0
    for p in picks: cov|=masks[p-1]
    return cov==full

# ---------------- 13 partition, input "n" + durations; out YES + picks (machine-1 indices) ----------------
def plant_partition(n, seed):
    rng=random.Random(seed*701+n); vals=[rng.randint(10**6,10**9) for _ in range(n)]
    pick=sorted(rng.sample(range(n), n//2)); s1=sum(vals[i] for i in pick); s2=sum(vals)-s1
    diff=s2-s1
    # make totals equal: bump one non-picked item by (diff) if diff>0 (kept positive), else a picked item
    if diff>0: vals[[i for i in range(n) if i not in pick][0]] += 0  # keep values as-is; instead adjust target below
    # simplest exact: append nothing; ensure equal by construction -> set one item so sums match
    # rebuild: choose vals freely, then set the LAST picked item to balance
    vals=[rng.randint(10**6,10**9) for _ in range(n)]
    pick=sorted(rng.sample(range(n), n//2))
    rest=[i for i in range(n) if i not in pick]
    sp=sum(vals[i] for i in pick[:-1]); sr=sum(vals[i] for i in rest)
    vals[pick[-1]] = sr - sp
    if vals[pick[-1]] <= 0: vals[pick[-1]] = 1; # fallback (rare); recompute rest to match
    # ensure equality exactly: set one rest item to absorb any residual
    s1=sum(vals[i] for i in pick); s2=sum(vals[i] for i in rest)
    if s1!=s2: vals[rest[-1]] += (s1 - s2)
    if vals[rest[-1]]<=0: vals[rest[-1]] += (1-vals[rest[-1]]); vals[pick[-1]] += (1-vals[rest[-1]])
    txt="\n".join([str(n)]+[" ".join(map(str,vals))])+"\n"
    wit="YES\n"+" ".join(str(i+1) for i in pick)+"\n"
    return txt,wit
def grade_partition(text,out):
    d=text.split(); n=int(d[0]); vals=[int(d[1+i]) for i in range(n)]; total=sum(vals)
    if total%2: return False
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: picks=set(int(x) for x in t[1:])
    except ValueError: return False
    if any(p<1 or p>n for p in picks): return False
    return sum(vals[p-1] for p in picks)==total//2


# ---------------- 01 graph coloring, input "n m k" + edges; out YES + colors ----------------
def plant_color(n, seed):
    rng=random.Random(seed*101+n); k=3  # Defaulting to 3-coloring which is NPC
    colors=[rng.randint(1,k) for _ in range(n)]
    edges=set(); tgt=int(2.5*n); guard=0
    while len(edges)<tgt and guard<80*tgt+2000:
        guard+=1; u=rng.randint(1,n); v=rng.randint(1,n)
        if u!=v and colors[u-1]!=colors[v-1]: edges.add((min(u,v),max(u,v)))
    el=list(edges); rng.shuffle(el)
    txt="\n".join([f"{n} {len(el)} {k}"]+[f"{u} {v}" for u,v in el])+"\n"
    wit="YES\n"+" ".join(map(str,colors))+"\n"
    return txt,wit

def grade_color(text,out):
    d=text.split(); n=int(d[0]); m=int(d[1]); k=int(d[2]); edges=[(int(d[3+2*i]),int(d[4+2*i])) for i in range(m)]
    t=out.split()
    if not t or t[0].upper()!="YES": return False
    try: colors=[int(x) for x in t[1:]]
    except ValueError: return False
    if len(colors)!=n or any(c<1 or c>k for c in colors): return False
    return all(colors[u-1]!=colors[v-1] for u,v in edges)
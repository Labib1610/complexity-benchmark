import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0]); t = int(data[1])
    n = 3*q
    idx = 2
    triples = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a,b,c))
    
    # Build adjacency: for each pair (u,v), list of triples containing both
    # We'll use a dict keyed by (min(u,v), max(u,v))
    pair_triples = {}
    for i,(a,b,c) in enumerate(triples):
        for u,v in ((a,b),(a,c),(b,c)):
            key = (u,v) if u<v else (v,u)
            pair_triples.setdefault(key, []).append(i)
    
    # We'll do a backtracking search with the following structure:
    # - Maintain a list of unassigned operators in sorted order.
    # - Always pick the smallest unassigned operator u.
    # - For each triple containing u, if the other two are unassigned, try it.
    # - Use bitset for assigned operators for speed.
    
    # Precompute for each operator, the list of triples containing it
    op_triples = [[] for _ in range(n+1)]
    for i,(a,b,c) in enumerate(triples):
        op_triples[a].append(i)
        op_triples[b].append(i)
        op_triples[c].append(i)
    
    assigned = [False]*(n+1)  # 1-indexed
    chosen = []
    
    # Convert op_triples to tuples for faster iteration
    op_triples = [tuple(lst) for lst in op_triples]
    
    def backtrack():
        # Find smallest unassigned
        u = -1
        for i in range(1, n+1):
            if not assigned[i]:
                u = i
                break
        if u == -1:
            return True
        
        # Try each triple containing u
        for ti in op_triples[u]:
            a,b,c = triples[ti]
            # Check if all three are unassigned
            if assigned[a] or assigned[b] or assigned[c]:
                continue
            # Assign
            assigned[a] = assigned[b] = assigned[c] = True
            chosen.append(ti)
            if backtrack():
                return True
            chosen.pop()
            assigned[a] = assigned[b] = assigned[c] = False
        
        return False
    
    if backtrack():
        print("YES")
        out = []
        for ti in chosen:
            a,b,c = triples[ti]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out)+"\n")
    else:
        print("NO")

solve()
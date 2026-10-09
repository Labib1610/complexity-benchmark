import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    triples = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a, b, c))
    
    if n % 3 != 0:
        print("NO")
        return
    
    # Build adjacency: for each vertex, list of (triple_id, other two vertices)
    adj = [[] for _ in range(n+1)]
    for i, (a, b, c) in enumerate(triples):
        adj[a].append((i, b, c))
        adj[b].append((i, a, c))
        adj[c].append((i, a, b))
    
    # For each vertex, sort triples by degree sum (heuristic)
    deg = [0]*(n+1)
    for a, b, c in triples:
        deg[a] += 1
        deg[b] += 1
        deg[c] += 1
    
    for v in range(1, n+1):
        adj[v].sort(key=lambda x: deg[triples[x[0]][0]] + deg[triples[x[0]][1]] + deg[triples[x[0]][2]])
    
    used_triple = [False] * t
    covered = [False] * (n+1)
    chosen = []
    
    import sys
    sys.setrecursionlimit(10000)
    
    def backtrack():
        # Find first uncovered vertex
        v = 1
        while v <= n and covered[v]:
            v += 1
        if v > n:
            return True
        
        for (tid, x, y) in adj[v]:
            if not used_triple[tid] and not covered[x] and not covered[y]:
                used_triple[tid] = True
                covered[v] = True
                covered[x] = True
                covered[y] = True
                chosen.append(tid)
                if backtrack():
                    return True
                chosen.pop()
                used_triple[tid] = False
                covered[v] = False
                covered[x] = False
                covered[y] = False
        return False
    
    if backtrack():
        print("YES")
        for tid in chosen:
            a, b, c = triples[tid]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()
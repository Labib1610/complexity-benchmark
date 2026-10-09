import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    
    # Greedy approach: repeatedly pick the vertex with minimum degree in the remaining graph
    remaining = set(range(1, n + 1))
    result = []
    
    while len(result) < k and remaining:
        # Find vertex with minimum conflicts in remaining set
        best = -1
        best_conflicts = n + 1
        
        for v in remaining:
            conflicts = 0
            for u in remaining:
                if adj[v] & (1 << (u - 1)):
                    conflicts += 1
            if conflicts < best_conflicts:
                best_conflicts = conflicts
                best = v
        
        if best == -1:
            break
        
        result.append(best)
        remaining.remove(best)
        
        # Remove all neighbors of best from remaining
        to_remove = []
        for u in remaining:
            if adj[best] & (1 << (u - 1)):
                to_remove.append(u)
        for u in to_remove:
            remaining.remove(u)
    
    if len(result) >= k:
        print("YES")
        print(' '.join(map(str, result[:k])))
    else:
        print("NO")

solve()
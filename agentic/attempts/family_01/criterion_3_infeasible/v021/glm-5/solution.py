import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges lexicographically to find lexicographically smallest triangle first
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w where w > v (to maintain u < v < w)
        # We need w such that w in adj[u] and w in adj[v] and w > v
        # Iterate through the smaller adjacency set for efficiency
        if len(adj[u]) > len(adj[v]):
            smaller, larger = adj[v], adj[u]
        else:
            smaller, larger = adj[u], adj[v]
        
        for w in smaller:
            if w > v and w in larger:
                print(u, v, w)
                return
    
    # Should not reach here as problem guarantees a solution exists
    # But if we do, we need to check all possibilities more carefully
    # This handles cases where edges weren't sorted optimally
    for u in range(1, n - 1):
        for v in adj[u]:
            if v <= u:
                continue
            for w in adj[v]:
                if w <= v:
                    continue
                if w in adj[u]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    solve()
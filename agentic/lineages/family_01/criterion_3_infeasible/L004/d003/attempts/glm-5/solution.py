import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
        edges.append((min(u, v), max(u, v)))
    
    edges.sort()
    
    for a, b in edges:
        if len(adj[a]) <= len(adj[b]):
            smaller, other = adj[a], adj[b]
        else:
            smaller, other = adj[b], adj[a]
        
        min_c = n + 1
        for c in smaller:
            if c > b and c in other:
                min_c = min(min_c, c)
        
        if min_c <= n:
            print(a, b, min_c)
            return

solve()
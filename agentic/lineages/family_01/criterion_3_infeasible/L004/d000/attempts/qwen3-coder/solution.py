import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store edges and build adjacency list
    edges = set()
    adj = defaultdict(set)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for node in range(1, n+1):
        adj[node] = sorted(list(adj[node]))
    
    # Look for triangle: for each edge (u,v), check common neighbors
    for u in range(1, n+1):
        for v in adj[u]:
            if v <= u:
                continue
            # Check if there's a common neighbor w where u < v < w
            for w in adj[u]:
                if w <= v:
                    continue
                if w in adj[v]:
                    # Found triangle (u, v, w)
                    print(u, v, w)
                    return

find_triangle()
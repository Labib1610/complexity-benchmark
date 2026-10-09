import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store adjacency information
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices by ID
    vertices = sorted(adj.keys())
    
    # For each edge, check if there's a common neighbor
    # We want the lexicographically smallest triangle
    for u in vertices:
        for v in sorted(adj[u]):
            if v <= u:
                continue
            # Check for common neighbors greater than v to ensure lexicographic order
            for w in sorted(adj[u]):
                if w <= v:
                    continue
                if w in adj[v]:
                    print(u, v, w)
                    return

find_triangle()
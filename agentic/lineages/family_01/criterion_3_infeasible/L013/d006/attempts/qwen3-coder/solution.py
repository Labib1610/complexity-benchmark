import sys
from collections import defaultdict

def find_unresolvable_core():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices for lexicographic ordering
    vertices = list(range(1, n + 1))
    
    # Check all combinations of 3 vertices in lexicographic order
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = vertices[i], vertices[j], vertices[k]
                # Check if they form a triangle (each pair is connected)
                if b in adj[a] and c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

find_unresolvable_core()
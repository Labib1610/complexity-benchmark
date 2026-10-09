import sys
from collections import defaultdict

def find_impossible_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge, check if it can form a triangle with any common neighbor
    for u, v in edges:
        if u >= v:
            continue
            
        # Find common neighbors
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

find_impossible_triangle()
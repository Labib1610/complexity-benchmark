import sys
from collections import defaultdict

def find_triangle():
    n, m = map(int, sys.stdin.readline().split())
    
    # Store edges in adjacency list and edge set for O(1) lookup
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
    
    # For each edge, check if it forms a triangle with any common neighbor
    for u, v in edges:
        # Find common neighbors of u and v
        if len(adj[u]) > len(adj[v]):
            u, v = v, u
            
        for w in adj[u]:
            if w in adj[v] and u != w and v != w:
                # Found a triangle: u, v, w
                result = sorted([u, v, w])
                print(result[0], result[1], result[2])
                return

find_triangle()
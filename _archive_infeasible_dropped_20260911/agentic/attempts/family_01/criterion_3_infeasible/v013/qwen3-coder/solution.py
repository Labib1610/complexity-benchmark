import sys
from collections import defaultdict

def find_triangle():
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
    
    # For each edge, check if there's a common neighbor
    found = False
    result = None
    
    # Sort edges to ensure we find lexicographically smallest triangle first
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors of u and v
        for w in adj[u]:
            if w in adj[v]:
                # Found a triangle: u, v, w
                triangle = sorted([u, v, w])
                if not found or triangle < result:
                    result = triangle
                    found = True
                elif found and triangle > result:
                    continue
                break
        if found and u > result[0]:  # Early termination optimization
            break
                
    if result:
        print(result[0], result[1], result[2])

find_triangle()
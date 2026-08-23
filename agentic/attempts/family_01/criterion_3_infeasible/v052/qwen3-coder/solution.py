import sys
from collections import defaultdict

def find_minimal_trio():
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
    
    # For each edge (u,v), check if there exists a node w such that 
    # w is connected to both u and v - forming a triangle
    min_trio = None
    
    # Try all nodes as the first element of the trio
    for a in range(1, n+1):
        if a not in adj:
            continue
        # Get neighbors of a
        neighbors_a = list(adj[a])
        neighbors_a.sort()
        # For each pair of neighbors of a, check if they are connected
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            for j in range(i+1, len(neighbors_a)):
                c = neighbors_a[j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    # Found a trio (a,b,c)
                    return f"{a} {b} {c}"
    
    return ""

print(find_minimal_trio())
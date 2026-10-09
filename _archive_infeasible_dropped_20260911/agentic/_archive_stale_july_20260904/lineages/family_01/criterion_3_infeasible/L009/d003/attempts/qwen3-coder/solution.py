import sys
from collections import defaultdict

def find_minimal_certificate():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Convert to sorted lists for consistent iteration
    vertices = sorted(adj.keys())
    
    # Check all triangles - three nodes that are all connected to each other
    # This is equivalent to finding a triangle in the graph
    # A triangle is a minimal certificate because it's impossible to 2-color
    
    # For each edge, check if there's a common neighbor
    min_cert = None
    
    # Sort edges for consistent processing
    edges = [(min(u,v), max(u,v)) for u, v in edges]
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors of u and v
        common_neighbors = adj[u] & adj[v]
        
        for w in sorted(common_neighbors):
            # We have a triangle u-v-w
            # Make sure u < v < w for canonical form
            a, b, c = sorted([u, v, w])
            
            if min_cert is None or (a, b, c) < min_cert:
                min_cert = (a, b, c)
    
    # Output the result
    print(min_cert[0], min_cert[1], min_cert[2])

find_minimal_certificate()
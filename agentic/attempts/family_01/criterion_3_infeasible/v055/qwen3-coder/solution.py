import sys
from collections import defaultdict

def find_critical_cluster():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort vertices for deterministic processing
    vertices = sorted(adj.keys())
    
    # For each edge, check if it's part of a triangle
    best_cluster = None
    
    # Try all edges as potential edges in a triangle
    for u, v in edges:
        if u > v:
            continue  # Process each edge only once
            
        # Find common neighbors of u and v
        common_neighbors = adj[u] & adj[v]
        
        # For each common neighbor, we have a triangle
        for w in common_neighbors:
            # Create the cluster and sort it
            cluster = sorted([u, v, w])
            
            # Check if this is better than our current best
            if best_cluster is None or cluster < best_cluster:
                best_cluster = cluster
    
    # Output the result
    print(best_cluster[0], best_cluster[1], best_cluster[2])

find_critical_cluster()
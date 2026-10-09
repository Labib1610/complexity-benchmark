import sys
from collections import defaultdict

def find_minimal_irreconcilable_group():
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list using sets for O(1) lookup
    conflicts = defaultdict(set)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        conflicts[u].add(v)
        conflicts[v].add(u)
        edges.append((min(u, v), max(u, v)))
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge, check if there exists a third node that conflicts with both
    for u, v in edges:
        # Find common neighbors of u and v
        common_neighbors = conflicts[u] & conflicts[v]
        
        if common_neighbors:
            # Find the smallest neighbor
            w = min(common_neighbors)
            # Output in sorted order
            result = sorted([u, v, w])
            print(result[0], result[1], result[2])
            return

find_minimal_irreconcilable_group()
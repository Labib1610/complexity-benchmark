import sys
from collections import defaultdict

def find_deadlock():
    n, m = map(int, input().split())
    
    # Store edges and build adjacency list
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges for consistent processing
    edges.sort()
    
    # For each edge, look for a third node that connects to both endpoints
    for u, v in edges:
        # Find common neighbors of u and v
        common_neighbors = adj[u] & adj[v]
        
        # For each common neighbor, we have a triangle (deadlock)
        for w in sorted(common_neighbors):
            if w > v:  # Ensure we get lexicographically smallest
                return u, v, w
    
    return None

# Find and output the deadlock
result = find_deadlock()
print(result[0], result[1], result[2])
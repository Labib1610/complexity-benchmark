import sys
from collections import defaultdict

def find_triangle(n, edges):
    # Build adjacency list with sets for O(1) lookup
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Also build adjacency list as lists for ordered iteration
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # For each node, sort its adjacency list
    for u in adj_list:
        adj_list[u].sort()
    
    # Iterate through all edges to find a triangle
    # We want the lexicographically smallest triangle
    best = None
    
    # Try all edges as potential edge (u,v) in triangle
    # Check if there exists a w such that (u,w) and (v,w) exist
    for u in range(1, n+1):
        if u not in adj_list:
            continue
        for v in adj_list[u]:
            if v <= u:
                continue  # Ensure u < v
            # Look for common neighbor w of u and v
            # To get lexicographically smallest, we check neighbors in order
            for w in adj_list[u]:
                if w <= v:
                    continue  # We want u < v < w
                if w in adj[v]:
                    return (u, v, w)
    
    return None

# Read input
line = sys.stdin.readline().split()
n, m = int(line[0]), int(line[1])
edges = []
for _ in range(m):
    line = sys.stdin.readline().split()
    u, v = int(line[0]), int(line[1])
    edges.append((u, v))

# Find and print the triangle
result = find_triangle(n, edges)
print(result[0], result[1], result[2])
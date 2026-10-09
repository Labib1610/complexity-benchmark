import sys
from collections import defaultdict

def find_triangle(edges, n):
    # Create adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for u in range(1, n + 1):
        adj[u] = sorted(list(adj[u]))
    
    # Look for triangles - for each edge (u,v), check for common neighbors
    min_triangle = None
    
    for u in range(1, n + 1):
        if u not in adj:
            continue
        neighbors_u = adj[u]
        # For each pair of neighbors of u, check if they're connected
        for i in range(len(neighbors_u)):
            v = neighbors_u[i]
            if v <= u:  # Ensure we don't double-check or get out-of-order triplets
                continue
            for j in range(i + 1, len(neighbors_u)):
                w = neighbors_u[j]
                if w <= u or w <= v:  # Maintain order
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    triangle = tuple(sorted([u, v, w]))
                    if min_triangle is None or triangle < min_triangle:
                        min_triangle = triangle
    
    return min_triangle

# Read input
line = sys.stdin.readline().split()
n, m = int(line[0]), int(line[1])
edges = []
for _ in range(m):
    line = sys.stdin.readline().split()
    u, v = int(line[0]), int(line[1])
    edges.append((u, v))

# Find and print the lexicographically smallest triangle
result = find_triangle(edges, n)
if result:
    print(result[0], result[1], result[2])
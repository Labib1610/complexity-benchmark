import sys
from collections import defaultdict

def find_lexicographically_smallest_triangle(n, m, edges):
    # Create adjacency list using sets for O(1) lookup
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Also create a sorted list of neighbors for each node
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists
    for u in adj_list:
        adj_list[u].sort()
    
    # For each node, check its neighbors
    # We want to find a triangle (u, v, w) where u < v < w
    for u in range(1, n + 1):
        if u not in adj_list:
            continue
        # For each pair of neighbors (v, w) of u where u < v < w
        neighbors = adj_list[u]
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v <= u:
                continue
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                if w <= v:
                    continue
                # Check if v and w are connected
                if w in adj[v]:
                    return [u, v, w]
    
    return None

# Read input
line = sys.stdin.readline().split()
n, m = int(line[0]), int(line[1])
edges = []
for _ in range(m):
    line = sys.stdin.readline().split()
    u, v = int(line[0]), int(line[1])
    edges.append((u, v))

# Find the triangle
result = find_lexicographically_smallest_triangle(n, m, edges)
print(result[0], result[1], result[2])
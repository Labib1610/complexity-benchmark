import sys
from collections import defaultdict

def find_triangle(edges, n):
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, create a sorted list of neighbors for consistent iteration
    neighbors = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # Map each node to a set of its neighbors for O(1) lookup
    neighbor_set = [set(adj[i]) for i in range(n + 1)]
    
    # Iterate through all combinations of nodes i < j < k
    for i in range(1, n + 1):
        for j_index in range(len(neighbors[i])):
            j = neighbors[i][j_index]
            if j <= i:
                continue
            # Check neighbors of j that are > j
            for k_index in range(j_index + 1, len(neighbors[i])):
                k = neighbors[i][k_index]
                if k <= j:
                    continue
                # Check if j and k are connected
                if k in neighbor_set[j]:
                    return (i, j, k)
    return None

# Read input
input_lines = []
for line in sys.stdin:
    input_lines.append(line.strip())

n, m = map(int, input_lines[0].split())
edges = []
for i in range(1, m + 1):
    u, v = map(int, input_lines[i].split())
    edges.append((u, v))

# Find triangle
result = find_triangle(edges, n)
print(result[0], result[1], result[2])
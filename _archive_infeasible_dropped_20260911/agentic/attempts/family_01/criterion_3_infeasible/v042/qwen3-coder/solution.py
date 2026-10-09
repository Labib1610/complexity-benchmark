import sys
from collections import defaultdict

def find_triangle(edges, n):
    # Create adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, check its neighbors
    # For every pair of neighbors of a node, check if they are connected
    for a in range(1, n + 1):
        neighbors = sorted(list(adj[a]))
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b <= a:
                continue
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if c <= a or c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    return (a, b, c)
    return None

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find triangle
result = find_triangle(edges, n)
print(result[0], result[1], result[2])
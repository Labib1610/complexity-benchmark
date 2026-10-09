import sys
from collections import defaultdict

def find_triangle(edges, n):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for u in range(1, n + 1):
        adj[u] = sorted(list(adj[u]))
    
    # For each edge, check if there's a common neighbor forming a triangle
    for a in range(1, n + 1):
        for i, b in enumerate(adj[a]):
            if b <= a:
                continue
            # Check neighbors of b to see if any form a triangle with a
            for c in adj[b]:
                if c <= b:
                    continue
                if c in adj[a]:
                    return (a, b, c)
    return None

# Read input
line = sys.stdin.readline().split()
n, m = int(line[0]), int(line[1])
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find and print the triangle
result = find_triangle(edges, n)
print(result[0], result[1], result[2])
import sys
from collections import defaultdict

def find_smallest_clique(n, edges):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for consistent iteration
    for u in range(1, n + 1):
        adj[u] = sorted(list(adj[u]))
    
    # For each node, check its neighbors
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # For each pair of neighbors of 'a'
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    return [a, b, c]
    
    return None

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find and print the result
result = find_smallest_clique(n, edges)
print(' '.join(map(str, result)))
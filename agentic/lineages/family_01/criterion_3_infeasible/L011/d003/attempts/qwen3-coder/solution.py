import sys
from itertools import combinations

def find_bottleneck(n, m, edges):
    # Create adjacency list representation
    adj = [set() for _ in range(n + 1)]
    edge_set = set()
    
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        edge_set.add((min(u, v), max(u, v)))
    
    # Check all combinations of 3 nodes
    for combo in combinations(range(1, n + 1), 3):
        a, b, c = sorted(combo)
        
        # Check if all three pairs are connected (form a triangle)
        if (a, b) in edge_set and (a, c) in edge_set and (b, c) in edge_set:
            return a, b, c
    
    return None

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find and output the bottleneck
result = find_bottleneck(n, m, edges)
print(result[0], result[1], result[2])
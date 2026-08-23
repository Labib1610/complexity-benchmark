import sys
from collections import defaultdict

def find_deadlock_triad(n, edges):
    # Build adjacency list and set for O(1) lookup
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for deterministic iteration
    nodes = sorted(adj.keys())
    
    # Iterate through all combinations of 3 nodes
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            for k in range(j+1, len(nodes)):
                a, b, c = nodes[i], nodes[j], nodes[k]
                # Check if they form a triangle (deadlock triad)
                if b in adj[a] and c in adj[a] and c in adj[b]:
                    return a, b, c
    
    return None

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find and print the lexicographically smallest deadlock triad
triad = find_deadlock_triad(n, edges)
print(triad[0], triad[1], triad[2])
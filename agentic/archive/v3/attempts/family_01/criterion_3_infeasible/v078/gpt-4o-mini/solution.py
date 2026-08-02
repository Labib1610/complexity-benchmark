def find_hazard_set(n, m, edges):
    from collections import defaultdict
    
    # Create an adjacency set for fast lookup
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through each pair (a, b) and check for a third element c
    for a in range(1, n + 1):
        for b in adj[a]:
            if b > a:  # Ensure a < b
                for c in adj[a].intersection(adj[b]):
                    if c > b:  # Ensure b < c
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_hazard_set(n, m, edges)
print(result[0], result[1], result[2])
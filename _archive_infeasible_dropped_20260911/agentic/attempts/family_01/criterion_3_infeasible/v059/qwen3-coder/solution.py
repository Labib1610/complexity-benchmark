import sys
from collections import defaultdict

def find_first_triangle(edges, n):
    # Create adjacency list and set for O(1) lookup
    adj = defaultdict(set)
    adj_list = defaultdict(list)
    
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Sort adjacency lists for consistent iteration
    for u in adj_list:
        adj_list[u].sort()
    
    # Iterate through all possible triplets (a, b, c) in increasing order
    for a in range(1, n + 1):
        if a not in adj_list:
            continue
        for i in range(len(adj_list[a])):
            b = adj_list[a][i]
            if b <= a:
                continue
            for j in range(i + 1, len(adj_list[a])):
                c = adj_list[a][j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in adj[b]:
                    return (a, b, c)
    
    return None

# Read input
line = sys.stdin.readline().split()
n, m = int(line[0]), int(line[1])
edges = []

for _ in range(m):
    line = sys.stdin.readline().split()
    u, v = int(line[0]), int(line[1])
    edges.append((u, v))

# Find the first triangle
result = find_first_triangle(edges, n)
print(result[0], result[1], result[2])
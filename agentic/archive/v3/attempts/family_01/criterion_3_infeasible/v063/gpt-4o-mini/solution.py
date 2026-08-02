import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Create an adjacency set for each node
adj = defaultdict(set)
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)

# To find the smallest triplet (a, b, c)
result = None

# Go through each edge and check for a triplet
for u, v in edges:
    # Check common neighbors of u and v
    common_neighbors = adj[u].intersection(adj[v])
    for w in common_neighbors:
        triplet = sorted([u, v, w])
        if result is None or triplet < result:
            result = triplet

print(*result)
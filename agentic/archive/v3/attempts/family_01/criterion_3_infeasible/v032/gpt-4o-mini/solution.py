import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = defaultdict(set)

for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    edges[u].add(v)
    edges[v].add(u)

# We need to find a triplet (a, b, c) such that a < b < c and all pairs are connected
result = None

for a in range(1, n + 1):
    for b in edges[a]:
        if b > a:  # Ensure a < b
            for c in edges[b]:
                if c > b and c in edges[a]:  # Ensure b < c and a, b, c are all connected
                    result = (a, b, c) if result is None else min(result, (a, b, c))

print(*result)
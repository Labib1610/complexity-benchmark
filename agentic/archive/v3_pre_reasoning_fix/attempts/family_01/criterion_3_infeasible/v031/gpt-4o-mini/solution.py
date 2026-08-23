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

# Find the lexicographically smallest triangle
for a in range(1, n + 1):
    for b in edges[a]:
        if b > a:  # Ensure b > a for lexicographical order
            for c in edges[b]:
                if c > b and c in edges[a]:  # Ensure c > b and a, b, c form a triangle
                    print(a, b, c)
                    exit()
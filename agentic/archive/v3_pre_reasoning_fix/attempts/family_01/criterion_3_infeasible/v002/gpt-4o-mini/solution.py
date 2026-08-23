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

for a in range(1, n + 1):
    for b in edges[a]:
        if b > a:  # Ensure that b is greater than a to maintain order
            for c in edges[b]:
                if c > b and c in edges[a]:  # c must be greater than b and also connected to a
                    print(a, b, c)
                    exit()
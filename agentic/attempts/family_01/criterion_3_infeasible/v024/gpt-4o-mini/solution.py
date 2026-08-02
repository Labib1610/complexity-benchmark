import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

graph = defaultdict(set)

for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)

for a in range(1, n + 1):
    for b in graph[a]:
        if b > a:
            for c in graph[b]:
                if c > b and c in graph[a]:
                    print(a, b, c)
                    sys.exit()
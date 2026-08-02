from sys import stdin

n, m = map(int, stdin.readline().split())
graph = {}
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    graph[u].add(v)
    graph[v].add(u)

# Try to find the smallest triplet (a, b, c) such that a < b < c and they are all connected
for a in range(1, n + 1):
    if a not in graph:
        continue
    for b in sorted(graph[a]):
        if b <= a:
            continue
        for c in sorted(graph[a]):
            if c <= b or c not in graph[b]:
                continue
            print(a, b, c)
            exit()
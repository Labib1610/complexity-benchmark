import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
mandatory = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

degree = [0] * (n + 1)
for i in range(1, n + 1):
    degree[i] = len(adj[i])

# Remove non-mandatory leaves
q = deque()
for i in range(1, n + 1):
    if degree[i] == 1 and i not in mandatory:
        q.append(i)

removed = [False] * (n + 1)
while q:
    u = q.popleft()
    removed[u] = True
    for v, w in adj[u]:
        if not removed[v]:
            degree[v] -= 1
            if degree[v] == 1 and v not in mandatory:
                q.append(v)

# Sum weights of edges between remaining nodes
total_cost = 0
for u in range(1, n + 1):
    if not removed[u]:
        for v, w in adj[u]:
            if v > u and not removed[v]:
                total_cost += w

print(total_cost)
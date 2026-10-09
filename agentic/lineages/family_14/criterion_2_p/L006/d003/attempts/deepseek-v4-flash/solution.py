import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
priority = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

if t <= 1:
    print(0)
    sys.exit()

degree = [0] * (n + 1)
for i in range(1, n + 1):
    degree[i] = len(adj[i])

visited = [False] * (n + 1)
q = deque()
for i in range(1, n + 1):
    if degree[i] == 1 and i not in priority:
        q.append(i)
        visited[i] = True

total_cost = 0
while q:
    u = q.popleft()
    for v, w in adj[u]:
        if not visited[v]:
            if v not in priority:
                degree[v] -= 1
                if degree[v] == 1:
                    visited[v] = True
                    q.append(v)
            else:
                total_cost += w

print(total_cost)
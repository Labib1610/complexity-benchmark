import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
critical = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# If only one critical node, no edges needed
if t == 1:
    print(0)
    sys.exit()

degree = [len(adj[i]) for i in range(n + 1)]
visited = [False] * (n + 1)
q = deque()

# Start with non-critical leaves
for i in range(1, n + 1):
    if i not in critical and degree[i] == 1:
        q.append(i)
        visited[i] = True

total_cost = 0

while q:
    u = q.popleft()
    for v, w in adj[u]:
        if visited[v]:
            continue
        if v not in critical:
            degree[v] -= 1
            if degree[v] == 1:
                visited[v] = True
                q.append(v)
        else:
            total_cost += w

print(total_cost)
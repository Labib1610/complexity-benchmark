import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
spores = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# If only one spore, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Degree count and active flag
degree = [0] * (n + 1)
active = [False] * (n + 1)
for i in range(1, n + 1):
    degree[i] = len(adj[i])
    active[i] = True

# Queue of leaves that are not spores
q = deque()
for i in range(1, n + 1):
    if degree[i] == 1 and i not in spores:
        q.append(i)

# Remove non-spore leaves iteratively
while q:
    u = q.popleft()
    if not active[u]:
        continue
    active[u] = False
    for v, w in adj[u]:
        if active[v]:
            degree[v] -= 1
            if degree[v] == 1 and v not in spores:
                q.append(v)

# Sum weights of edges where both endpoints are active
total = 0
for u in range(1, n + 1):
    if active[u]:
        for v, w in adj[u]:
            if u < v and active[v]:
                total += w

print(total)
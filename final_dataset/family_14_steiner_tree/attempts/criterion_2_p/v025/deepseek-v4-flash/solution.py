import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
core = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
total_weight = 0
deg = [0] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    total_weight += w
    deg[u] += 1
    deg[v] += 1

if t == 1:
    print(0)
    sys.exit()

removed = 0
in_queue = [False] * (n + 1)
q = deque()

for i in range(1, n + 1):
    if deg[i] == 1 and i not in core:
        q.append(i)
        in_queue[i] = True

while q:
    u = q.popleft()
    for v, w in adj[u]:
        if not in_queue[v]:
            removed += w
            deg[v] -= 1
            if deg[v] == 1 and v not in core:
                q.append(v)
                in_queue[v] = True

print(total_weight - removed)
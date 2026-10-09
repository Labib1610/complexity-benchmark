import sys
from collections import deque

input = sys.stdin.readline

R, S, P = map(int, input().split())
mandated = set(map(int, input().split()))

adj = [[] for _ in range(R + 1)]
degree = [0] * (R + 1)

for _ in range(S):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    degree[u] += 1
    degree[v] += 1

# Remove leaves that are not mandated
removed = [False] * (R + 1)
q = deque()

for i in range(1, R + 1):
    if degree[i] == 1 and i not in mandated:
        q.append(i)

while q:
    u = q.popleft()
    if removed[u]:
        continue
    removed[u] = True
    for v, w in adj[u]:
        if not removed[v]:
            degree[v] -= 1
            if degree[v] == 1 and v not in mandated:
                q.append(v)

# Sum weights of edges where both endpoints are not removed
total = 0
for u in range(1, R + 1):
    if removed[u]:
        continue
    for v, w in adj[u]:
        if u < v and not removed[v]:
            total += w

print(total)
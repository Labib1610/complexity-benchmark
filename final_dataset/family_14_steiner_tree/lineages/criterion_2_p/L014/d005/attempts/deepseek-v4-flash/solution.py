import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
keys = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# If only one key, answer is 0
if t == 1:
    print(0)
    sys.exit()

degree = [len(adj[i]) for i in range(n + 1)]
visited = [False] * (n + 1)
q = deque()

# Start with leaves that are not key nodes
for i in range(1, n + 1):
    if degree[i] == 1 and i not in keys:
        q.append(i)
        visited[i] = True

# Prune non-key leaves
while q:
    u = q.popleft()
    for v, w in adj[u]:
        if not visited[v]:
            degree[v] -= 1
            if degree[v] == 1 and v not in keys:
                visited[v] = True
                q.append(v)

# Sum weights of edges that remain in the pruned tree
total = 0
for u in range(1, n + 1):
    if not visited[u]:
        for v, w in adj[u]:
            if not visited[v] and u < v:
                total += w

print(total)
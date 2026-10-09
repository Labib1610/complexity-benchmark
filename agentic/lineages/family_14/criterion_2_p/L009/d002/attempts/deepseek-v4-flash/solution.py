import sys
from collections import deque

input = sys.stdin.readline

N, E, F = map(int, input().split())
critical = set(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# If only one critical panel, no thread needed
if F == 1:
    print(0)
    sys.exit()

degree = [len(adj[i]) for i in range(N + 1)]
visited = [False] * (N + 1)
q = deque()

# Start with non-critical leaves
for i in range(1, N + 1):
    if i not in critical and degree[i] == 1:
        q.append(i)
        visited[i] = True

while q:
    u = q.popleft()
    for v, w in adj[u]:
        if not visited[v]:
            degree[v] -= 1
            if v not in critical and degree[v] == 1:
                visited[v] = True
                q.append(v)

# Now sum weights of edges where both endpoints are not removed
total = 0
for u in range(1, N + 1):
    if not visited[u]:
        for v, w in adj[u]:
            if u < v and not visited[v]:
                total += w

print(total)
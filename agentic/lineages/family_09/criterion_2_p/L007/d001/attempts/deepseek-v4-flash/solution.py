import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
groups = [[], []]

# BFS to color bipartite graph
from collections import deque
for i in range(n):
    if color[i] == -1:
        color[i] = 0
        groups[0].append(i + 1)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    groups[color[v]].append(v + 1)
                    q.append(v)

# Pick from the larger group
if len(groups[0]) >= k:
    chosen = groups[0][:k]
else:
    chosen = groups[1][:k]

if len(chosen) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, chosen)))
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    edges.append((u, v))

color = [-1] * n

for i in range(n):
    if color[i] == -1:
        color[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    sys.exit()

print("YES")
print(" ".join(str(color[i]) for i in range(n)))
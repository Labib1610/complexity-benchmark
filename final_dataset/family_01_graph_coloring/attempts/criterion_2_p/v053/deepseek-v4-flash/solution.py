import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
res = [1] * n

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    res[start] = 1
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                res[v] = color[v] + 1
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

print("YES")
print(" ".join(map(str, res)))
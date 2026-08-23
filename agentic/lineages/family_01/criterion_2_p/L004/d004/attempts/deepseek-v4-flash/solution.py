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
color[0] = 1  # start with 1 for lexicographically smallest

for start in range(n):
    if color[start] == -1:
        color[start] = 1
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 3 - color[u]  # 1 -> 2, 2 -> 1
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

print("YES")
print(" ".join(str(c) for c in color))
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

def bfs(start):
    q = deque([start])
    color[start] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 3 - color[u]  # 1 -> 2, 2 -> 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

possible = True
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            possible = False
            break

if not possible:
    print("NO")
else:
    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))
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

color = [0] * n  # 0 = uncolored, 1 or 2

def bfs(start):
    q = deque([start])
    color[start] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]  # alternate 1 <-> 2
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == 0:
        if not bfs(i):
            print("NO")
            sys.exit()

print("YES")
print(" ".join(str(c) for c in color))
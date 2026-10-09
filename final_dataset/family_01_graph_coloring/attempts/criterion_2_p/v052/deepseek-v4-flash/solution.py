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

def bfs(start, first_color):
    q = deque([start])
    color[start] = first_color
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# Try coloring node 0 as 1 first
ok = True
for i in range(n):
    if color[i] == -1:
        if not bfs(i, 1):
            ok = False
            break

if not ok:
    # Try coloring node 0 as 2 instead
    color = [-1] * n
    ok = True
    for i in range(n):
        if color[i] == -1:
            if not bfs(i, 0):
                ok = False
                break

if not ok:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c + 1) for c in color))
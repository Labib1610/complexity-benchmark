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
possible = True

for start in range(n):
    if color[start] != 0:
        continue
    # try assigning color 1 to start
    color[start] = 1
    q = deque([start])
    ok = True
    comp_nodes = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                comp_nodes.append(v)
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if ok:
        continue
    # conflict with starting color 1, reset component and try starting color 2
    for node in comp_nodes:
        color[node] = 0
    color[start] = 2
    q = deque([start])
    ok = True
    comp_nodes = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                comp_nodes.append(v)
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        possible = False
        break

if not possible:
    print("NO")
else:
    print("YES")
    print(' '.join(str(c) for c in color))
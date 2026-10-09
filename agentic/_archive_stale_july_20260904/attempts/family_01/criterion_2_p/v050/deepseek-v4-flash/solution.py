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
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    # try to color start with 1
    color[start] = 0  # 0 means code 1, 1 means code 2
    q = deque([start])
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        # try starting with 2
        color[start] = 1
        q = deque([start])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
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
    print(" ".join(str(c + 1) for c in color))
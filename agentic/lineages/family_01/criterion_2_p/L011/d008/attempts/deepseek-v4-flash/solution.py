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

for i in range(n):
    if color[i] == -1:
        # try starting with 1
        color[i] = 1
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # try starting with 2
            color[i] = 2
            q = deque([i])
            ok = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                possible = False
                break
        # If starting with 1 works, keep it; else we already switched to 2

if not possible:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c) for c in color))
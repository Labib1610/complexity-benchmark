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
color[0] = 1  # assign 1 to first node

q = deque([0])
ok = True

while q and ok:
    u = q.popleft()
    for v in adj[u]:
        if color[v] == -1:
            color[v] = 3 - color[u]  # alternate 1 <-> 2
            q.append(v)
        elif color[v] == color[u]:
            ok = False
            break

# In case graph is disconnected, color remaining components
for i in range(n):
    if color[i] == -1:
        color[i] = 1
        q = deque([i])
        while q and ok:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break

if not ok:
    print("NO")
else:
    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))
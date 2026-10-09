import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n
color[0] = 1
q = deque([0])
possible = True

while q and possible:
    u = q.popleft()
    for v in adj[u]:
        if color[v] == -1:
            color[v] = 3 - color[u]
            q.append(v)
        elif color[v] == color[u]:
            possible = False
            break

if not possible:
    print("NO")
else:
    # Check for disconnected components
    for i in range(n):
        if color[i] == -1:
            color[i] = 1
            q = deque([i])
            while q and possible:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
            if not possible:
                break

    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
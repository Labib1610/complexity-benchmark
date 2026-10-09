import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

color = [-1] * n
possible = True

for i in range(n):
    if color[i] == -1:
        color[i] = 1
        q = deque([i])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if color[nei] == -1:
                    color[nei] = 3 - color[node]
                    q.append(nei)
                elif color[nei] == color[node]:
                    possible = False
                    break
            if not possible:
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c) for c in color))
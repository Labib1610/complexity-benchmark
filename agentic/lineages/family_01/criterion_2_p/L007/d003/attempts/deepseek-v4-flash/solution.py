from collections import deque
import sys

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

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

print("YES")
print(" ".join(str(c + 1) for c in color))
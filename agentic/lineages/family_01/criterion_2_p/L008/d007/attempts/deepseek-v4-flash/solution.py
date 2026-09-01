from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

color = [-1] * n
possible = True

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.append(neighbor)
                elif color[neighbor] == color[node]:
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
    print(" ".join(str(c + 1) for c in color))
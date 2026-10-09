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
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    possible = False
                    break
            if not possible:
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # To get lexicographically smallest, we try to set 1 for each node if possible
    # We can do a BFS/DFS that assigns 1 to unvisited nodes when possible
    res = [1] * n
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        res[v] = 3 - res[u]  # 1 -> 2, 2 -> 1
                        q.append(v)
    print("YES")
    print(" ".join(map(str, res)))
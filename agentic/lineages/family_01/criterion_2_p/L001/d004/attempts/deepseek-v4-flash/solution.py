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
    # Now we have a valid bipartite coloring.
    # To get lexicographically smallest, we want color 0 -> coordinate 1, color 1 -> coordinate 2.
    # But we can flip colors per component to favor smaller indices.
    # We'll do BFS/DFS again, but for each component, decide starting color based on smallest index.
    visited = [False] * n
    res = [0] * n
    for i in range(n):
        if not visited[i]:
            # BFS to collect component
            comp = []
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            # Decide starting color: smallest index in comp should be 0 (coordinate 1)
            start_color = 0
            # We'll assign colors relative to start node
            # color[i] already has a bipartite coloring; we can flip if needed
            # If color[comp[0]] != start_color, flip all in comp
            if color[comp[0]] != start_color:
                for u in comp:
                    color[u] ^= 1
            for u in comp:
                res[u] = color[u] + 1  # 0->1, 1->2

    print("YES")
    print(" ".join(map(str, res)))
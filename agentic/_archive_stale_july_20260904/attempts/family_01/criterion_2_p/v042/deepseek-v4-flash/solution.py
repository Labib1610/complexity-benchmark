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
    # color 0 -> hall 1, color 1 -> hall 2
    # But we want lexicographically smallest: prefer 1 at earlier indices
    # We can flip colors in each connected component if it makes earlier nodes 1
    visited = [False] * n
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
            # Check if flipping helps lexicographically
            # Count how many in comp have color 0 vs 1
            # If flipping makes earlier index smaller, flip
            flip = False
            for u in comp:
                if color[u] == 1:
                    # if first differing position would be smaller with flip
                    if not flip:
                        # compare: current color[u]=1 means hall2, flip would make hall1
                        # We want smallest lexicographic, so if first node in comp is 1, flip
                        if u == min(comp):
                            flip = True
                    break
                elif color[u] == 0:
                    break
            # Actually simpler: if the smallest index in comp has color 1, flip
            if color[min(comp)] == 1:
                flip = True
            if flip:
                for u in comp:
                    color[u] ^= 1

    res = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, res)))
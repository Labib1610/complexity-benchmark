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
res = [0] * n

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    comp = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
                comp.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()
    # Assign lexicographically smallest: try to put 1 on smallest index in this component
    # color 0 -> value 1, color 1 -> value 2
    # But we can flip colors if it makes the smallest index get 1
    if color[min(comp)] == 1:
        for node in comp:
            color[node] ^= 1
    for node in comp:
        res[node] = 1 if color[node] == 0 else 2

print("YES")
print(" ".join(map(str, res)))
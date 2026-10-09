import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)
side1 = []
side2 = []

for i in range(1, n + 1):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        side1.append(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    if color[v] == 0:
                        side1.append(v)
                    else:
                        side2.append(v)
                    q.append(v)

if len(side1) >= k:
    print("YES")
    print(" ".join(map(str, side1[:k])))
elif len(side2) >= k:
    print("YES")
    print(" ".join(map(str, side2[:k])))
else:
    print("NO")
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
ok = True

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
                    ok = False
                    break
            if not ok:
                break
    if not ok:
        break

if not ok:
    print("NO")
else:
    # color 0 -> p=1, color 1 -> p=2
    # But we want lexicographically smallest: try to assign 1 to node 0 if possible
    # If node 0 is color 1, we can flip all colors
    if color[0] == 1:
        for i in range(n):
            color[i] ^= 1
    res = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, res)))
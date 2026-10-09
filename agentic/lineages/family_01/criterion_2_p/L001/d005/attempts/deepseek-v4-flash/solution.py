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

mode = [-1] * n
possible = True

for i in range(n):
    if mode[i] == -1:
        mode[i] = 1  # start as transmitter
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if mode[v] == -1:
                    mode[v] = 3 - mode[u]  # opposite mode
                    q.append(v)
                elif mode[v] == mode[u]:
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
    print(" ".join(str(mode[i]) for i in range(n)))
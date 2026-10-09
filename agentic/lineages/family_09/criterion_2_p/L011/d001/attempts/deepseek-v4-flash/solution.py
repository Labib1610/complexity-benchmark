import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n
side = [[], []]

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        side[0].append(i)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    side[color[v]].append(v)
                    q.append(v)

# Choose from the larger side
if len(side[0]) >= k:
    chosen = side[0][:k]
else:
    chosen = side[1][:k]

if len(chosen) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(str(x+1) for x in chosen))
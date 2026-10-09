import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n

for i in range(n):
    if color[i] == -1:
        color[i] = 1  # start with tier 1
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]  # 1 -> 2, 2 -> 1
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    sys.exit()

print("YES")
print(" ".join(str(color[i]) for i in range(n)))
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
groups = [[], []]

for i in range(1, n + 1):
    if color[i] == -1:
        color[i] = 0
        groups[0].append(i)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    groups[color[v]].append(v)
                    q.append(v)

# The larger color class is an independent set
if len(groups[0]) >= k:
    ans = groups[0][:k]
elif len(groups[1]) >= k:
    ans = groups[1][:k]
else:
    print("NO")
    sys.exit()

print("YES")
print(" ".join(map(str, ans)))
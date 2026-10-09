import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
groups = [[], []]

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        groups[0].append(i + 1)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    groups[color[v]].append(v + 1)
                    q.append(v)

if len(groups[0]) >= k:
    ans = groups[0][:k]
elif len(groups[1]) >= k:
    ans = groups[1][:k]
else:
    print("NO")
    sys.exit()

print("YES")
print(" ".join(map(str, ans)))
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

tier = [-1] * n

for i in range(n):
    if tier[i] == -1:
        tier[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if tier[v] == -1:
                    tier[v] = 3 - tier[u]  # 1 -> 2, 2 -> 1
                    q.append(v)
                elif tier[v] == tier[u]:
                    print("NO")
                    sys.exit()

print("YES")
print(" ".join(map(str, tier)))
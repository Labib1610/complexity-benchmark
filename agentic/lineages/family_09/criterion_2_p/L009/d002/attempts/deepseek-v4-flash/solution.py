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
components = []  # each: (list of color0, list of color1)

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        c0, c1 = [], []
        while q:
            u = q.popleft()
            if color[u] == 0:
                c0.append(u)
            else:
                c1.append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
        components.append((c0, c1))

# Maximum independent set size
max_size = sum(max(len(c0), len(c1)) for c0, c1 in components)
if k > max_size:
    print("NO")
    sys.exit()

# Build the independent set
chosen = []
for c0, c1 in components:
    if len(c0) >= len(c1):
        chosen.extend(c0)
    else:
        chosen.extend(c1)

# If we have more than k, trim
if len(chosen) > k:
    chosen = chosen[:k]

print("YES")
print(" ".join(str(x + 1) for x in chosen))
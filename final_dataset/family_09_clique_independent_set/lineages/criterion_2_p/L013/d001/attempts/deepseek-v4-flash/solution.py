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
components = []  # list of (size0, size1, vertices0, vertices1)

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        cnt = [0, 0]
        verts = [[], []]
        while q:
            u = q.popleft()
            cnt[color[u]] += 1
            verts[color[u]].append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    # Not bipartite — but problem guarantees bipartite
                    pass
        components.append((cnt[0], cnt[1], verts[0], verts[1]))

# DP to see if we can reach exactly k
dp = [False] * (n + 1)
dp[0] = True
choice = [-1] * (n + 1)  # store which component and side chosen

for idx, (a, b, va, vb) in enumerate(components):
    new_dp = dp[:]
    for s in range(n, -1, -1):
        if dp[s]:
            if s + a <= n and not new_dp[s + a]:
                new_dp[s + a] = True
                choice[s + a] = (idx, 0)
            if s + b <= n and not new_dp[s + b]:
                new_dp[s + b] = True
                choice[s + b] = (idx, 1)
    dp = new_dp

if not dp[k]:
    print("NO")
else:
    print("YES")
    selected = []
    s = k
    while s > 0:
        idx, side = choice[s]
        a, b, va, vb = components[idx]
        if side == 0:
            selected.extend(va)
            s -= a
        else:
            selected.extend(vb)
            s -= b
    print(" ".join(str(x + 1) for x in selected))
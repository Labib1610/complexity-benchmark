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
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    comp = []
    while q:
        u = q.popleft()
        comp.append(u)
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                possible = False
                break
        if not possible:
            break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # For each component, decide orientation
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        # collect component
        comp = []
        q = deque([start])
        visited[start] = True
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        # count cost if we keep color as is
        # color 0 -> mode 1, color 1 -> mode 2
        # cost = sum((s_i - 1) * 2^(n-i-1))
        # We compare flipping
        cost_no_flip = 0
        cost_flip = 0
        for i in comp:
            if color[i] == 0:
                cost_no_flip += 1 * (1 << (n - i - 1))
                cost_flip += 0
            else:
                cost_no_flip += 0
                cost_flip += 1 * (1 << (n - i - 1))
        if cost_flip < cost_no_flip:
            for i in comp:
                color[i] ^= 1

    ans = [1 if color[i] == 0 else 2 for i in range(n)]
    print("YES")
    print(" ".join(map(str, ans)))
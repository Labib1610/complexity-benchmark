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
res = [0] * n

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to color component
    color[start] = 0
    q = deque([start])
    comp = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
                comp.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()
    # Now decide orientation for lexicographically smallest
    # Try color 0 for start vs color 1 for start
    # Build two candidate assignments
    cand1 = [0] * n
    cand2 = [0] * n
    for u in comp:
        cand1[u] = color[u] + 1
        cand2[u] = (color[u] ^ 1) + 1
    # Choose lexicographically smaller for this component
    # Compare only within component indices
    comp_sorted = sorted(comp)
    for u in comp_sorted:
        if cand1[u] < cand2[u]:
            for v in comp:
                res[v] = cand1[v]
            break
        elif cand2[u] < cand1[u]:
            for v in comp:
                res[v] = cand2[v]
            break
    else:
        # equal, pick either
        for v in comp:
            res[v] = cand1[v]

print("YES")
print(" ".join(map(str, res)))
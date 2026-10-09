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
result = [1] * n
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to get component
    comp = []
    q = deque([start])
    color[start] = 0
    comp.append(start)
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                comp.append(v)
                q.append(v)
            elif color[v] == color[u]:
                ok = False
    if not ok:
        possible = False
        break

    # Try both colorings for this component
    # coloring A: keep as is (color 0 -> shift 1, color 1 -> shift 2)
    # coloring B: swap (color 0 -> shift 2, color 1 -> shift 1)
    # We need lexicographically smallest overall, so for each component choose the better
    # But since components are independent, we can choose per component.
    # However, to be lexicographically smallest globally, we must consider the smallest index in the component.
    # We'll compare the two options for this component.
    
    # Build both options
    optA = [0] * n
    optB = [0] * n
    for u in comp:
        optA[u] = 1 if color[u] == 0 else 2
        optB[u] = 2 if color[u] == 0 else 1
    
    # Compare lexicographically for this component only
    # Find first index in comp where they differ
    comp_sorted = sorted(comp)
    useA = True
    for u in comp_sorted:
        if optA[u] != optB[u]:
            useA = optA[u] < optB[u]
            break
    
    for u in comp:
        result[u] = optA[u] if useA else optB[u]

if not possible:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result)))
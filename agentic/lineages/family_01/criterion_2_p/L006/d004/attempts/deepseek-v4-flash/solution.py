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
        print("NO")
        sys.exit()
    
    # Try both assignments for this component
    # assignment A: color 0 -> code 1, color 1 -> code 2
    # assignment B: color 0 -> code 2, color 1 -> code 1
    # We choose the one that gives smaller integer when considering smallest index in comp
    min_idx = min(comp)
    # For assignment A, code at min_idx is 1 if color[min_idx]==0 else 2
    codeA_min = 1 if color[min_idx] == 0 else 2
    codeB_min = 2 if color[min_idx] == 0 else 1
    if codeA_min < codeB_min:
        for u in comp:
            res[u] = 1 if color[u] == 0 else 2
    else:
        for u in comp:
            res[u] = 2 if color[u] == 0 else 1

print("YES")
print(" ".join(map(str, res)))
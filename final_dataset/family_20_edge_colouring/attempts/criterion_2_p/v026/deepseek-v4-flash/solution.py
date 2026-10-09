import sys
from collections import defaultdict

input = sys.stdin.readline

N_emp, N_ven, M = map(int, input().split())
edges = []
deg_emp = [0] * (N_emp + 1)
deg_ven = [0] * (N_ven + 1)

for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg_emp[u] += 1
    deg_ven[v] += 1

F = max(max(deg_emp), max(deg_ven))

# color[u][v] = color assigned to edge (u, v)
color_emp = [{} for _ in range(N_emp + 1)]
color_ven = [{} for _ in range(N_ven + 1)]

# For each edge, find a free color
ans = [0] * M
for idx, (u, v) in enumerate(edges):
    # Find smallest color not used by u or v
    used = set()
    if u in color_emp:
        used.update(color_emp[u].values())
    if v in color_ven:
        used.update(color_ven[v].values())
    c = 1
    while c in used:
        c += 1
    ans[idx] = c
    color_emp[u][v] = c
    color_ven[v][u] = c

print("YES")
print(" ".join(map(str, ans)))
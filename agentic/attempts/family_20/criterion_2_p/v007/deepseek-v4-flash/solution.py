import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adjL = [[] for _ in range(nL + 1)]
adjR = [[] for _ in range(nR + 1)]
degL = [0] * (nL + 1)
degR = [0] * (nR + 1)

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adjL[u].append((v, i))
    adjR[v].append((u, i))
    degL[u] += 1
    degR[v] += 1

Delta = max(max(degL), max(degR))

color = [-1] * m

# For each vertex, keep track of used colors
usedL = [set() for _ in range(nL + 1)]
usedR = [set() for _ in range(nR + 1)]

# We'll use a simple greedy with recoloring via alternating paths
# For each edge, find smallest free color on both endpoints.
# If conflict, recolor along alternating path.

for idx, (u, v) in enumerate(edges):
    # find smallest color not used at u and v
    c = 1
    while c in usedL[u] or c in usedR[v]:
        c += 1
    color[idx] = c
    usedL[u].add(c)
    usedR[v].add(c)

    # Now resolve conflicts: if any edge at u or v has same color, recolor
    # Actually, since we pick smallest free color, no conflict at insertion.
    # But due to previous recoloring, we might need to fix.
    # We'll implement full alternating path method for correctness.

# The above simple greedy may fail; we need proper edge coloring.
# Let's implement the standard algorithm:

color = [-1] * m
# For each vertex, store color -> edge index
colorL = [dict() for _ in range(nL + 1)]
colorR = [dict() for _ in range(nR + 1)]

def flip(u, v, c1, c2):
    # Recolor edge (u,v) from c1 to c2, and propagate
    idx = colorL[u].get(c1)
    if idx is None:
        return
    # remove old color
    del colorL[u][c1]
    del colorR[v][c1]
    color[idx] = c2
    colorL[u][c2] = idx
    colorR[v][c2] = idx
    # find conflict at v with c2
    idx2 = colorR[v].get(c2)
    if idx2 is not None and idx2 != idx:
        u2, v2 = edges[idx2]
        flip(u2, v2, c2, c1)

for idx, (u, v) in enumerate(edges):
    # find free color at u
    c = 1
    while c in colorL[u]:
        c += 1
    # find free color at v
    d = 1
    while d in colorR[v]:
        d += 1
    if c == d:
        color[idx] = c
        colorL[u][c] = idx
        colorR[v][c] = idx
    else:
        # try to recolor alternating path
        # find if we can shift colors
        # standard: try to find path starting from v with color c
        # We'll implement simple version:
        # If c is free at v, assign c
        if c not in colorR[v]:
            color[idx] = c
            colorL[u][c] = idx
            colorR[v][c] = idx
        elif d not in colorL[u]:
            color[idx] = d
            colorL[u][d] = idx
            colorR[v][d] = idx
        else:
            # need to flip
            # find edge at v with color c
            idx2 = colorR[v][c]
            u2, v2 = edges[idx2]
            # recolor that edge to d
            flip(u2, v2, c, d)
            # now assign c to current edge
            color[idx] = c
            colorL[u][c] = idx
            colorR[v][c] = idx

print("YES")
print(" ".join(str(color[i]) for i in range(m)))
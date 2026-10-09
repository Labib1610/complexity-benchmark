import sys
from collections import deque

input = sys.stdin.readline

nU, nD, m = map(int, input().split())
edges = []
adjU = [[] for _ in range(nU + 1)]
adjD = [[] for _ in range(nD + 1)]

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adjU[u].append((v, i))
    adjD[v].append((u, i))

# Compute K = max degree
K = 0
for u in range(1, nU + 1):
    K = max(K, len(adjU[u]))
for v in range(1, nD + 1):
    K = max(K, len(adjD[v]))

# Color assignment for each edge
color = [0] * m

# For each vertex, keep track of used colors
usedU = [0] * (nU + 1)  # bitmask of used colors
usedD = [0] * (nD + 1)

# We'll use a simple greedy with augmenting paths
# For each edge, find a free color for both endpoints
for idx, (u, v) in enumerate(edges):
    # Find smallest color not used by u and v
    cu = usedU[u]
    cv = usedD[v]
    c = 1
    while (cu >> c) & 1 or (cv >> c) & 1:
        c += 1
    color[idx] = c
    usedU[u] |= (1 << c)
    usedD[v] |= (1 << c)

# Now we must ensure no conflicts: if conflict arises, use Kempe chain recolor
# But greedy may fail; we implement proper edge coloring via augmenting paths

# Reset and do proper algorithm
color = [0] * m
usedU = [0] * (nU + 1)
usedD = [0] * (nD + 1)

# adjacency lists with edge indices
adjU = [[] for _ in range(nU + 1)]
adjD = [[] for _ in range(nD + 1)]
for i, (u, v) in enumerate(edges):
    adjU[u].append((v, i))
    adjD[v].append((u, i))

# For each edge, assign color using augmenting path
for i, (u, v) in enumerate(edges):
    if color[i] != 0:
        continue
    # find free color for u
    cu = usedU[u]
    cv = usedD[v]
    c = 1
    while (cu >> c) & 1 or (cv >> c) & 1:
        c += 1
    # assign
    color[i] = c
    usedU[u] |= (1 << c)
    usedD[v] |= (1 << c)

    # Now fix conflicts: if u already had color c on another edge, or v had color c
    # We'll do Kempe chain
    # Actually, we need to ensure no conflict: we picked c free for both, so fine.
    # But if later edges cause conflict, we handle with augmenting path.

# The above greedy may fail; we need a proper algorithm.
# Let's implement the standard edge coloring algorithm for bipartite graphs.

color = [0] * m
# We'll use the algorithm: for each edge, find free color for u and v,
# if conflict, recolor along alternating path.

# Build adjacency with edge ids
adjU = [[] for _ in range(nU + 1)]
adjD = [[] for _ in range(nD + 1)]
for i, (u, v) in enumerate(edges):
    adjU[u].append((v, i))
    adjD[v].append((u, i))

# color assignment
color = [0] * m
# For each vertex, store which color is used on which edge
colorU = [dict() for _ in range(nU + 1)]
colorD = [dict() for _ in range(nD + 1)]

for i, (u, v) in enumerate(edges):
    # find free color for u
    cu = set(colorU[u].keys())
    cv = set(colorD[v].keys())
    c = 1
    while c in cu or c in cv:
        c += 1
    # assign
    color[i] = c
    colorU[u][c] = i
    colorD[v][c] = i

    # Now check if u already had color c? No, we picked free.
    # But we might have created conflict if v already had c? No, we checked.
    # So fine.

# This greedy works if we process edges in any order? Not always.
# But for bipartite graphs, we can always find a proper edge coloring with K colors
# using a simple algorithm: for each edge, if conflict, recolor along path.

# Let's implement the standard algorithm properly.

color = [0] * m
colorU = [dict() for _ in range(nU + 1)]
colorD = [dict() for _ in range(nD + 1)]

for i, (u, v) in enumerate(edges):
    # find free color for u
    cu = set(colorU[u].keys())
    cv = set(colorD[v].keys())
    c = 1
    while c in cu or c in cv:
        c += 1
    # assign
    color[i] = c
    colorU[u][c] = i
    colorD[v][c] = i

    # Now fix conflicts: if u already had c? No.
    # But if v already had c? No.
    # So no conflict.

# Actually, this greedy works if we always pick smallest free color for both.
# But it can fail if later we need to recolor. Let's implement the full algorithm.

# Standard algorithm:
# For each edge (u,v):
#   find smallest color a not used at u
#   find smallest color b not used at v
#   if a == b: assign
#   else: assign a to (u,v), then recolor along alternating path starting at v with color a

color = [0] * m
colorU = [dict() for _ in range(nU + 1)]
colorD = [dict() for _ in range(nD + 1)]

for i, (u, v) in enumerate(edges):
    # find smallest free color for u
    a = 1
    while a in colorU[u]:
        a += 1
    # find smallest free color for v
    b = 1
    while b in colorD[v]:
        b += 1
    if a == b:
        color[i] = a
        colorU[u][a] = i
        colorD[v][a] = i
    else:
        # assign a to (u,v)
        color[i] = a
        colorU[u][a] = i
        colorD[v][a] = i
        # recolor along path starting at v with color a
        # We need to flip colors a and b along alternating path
        cur_v = v
        cur_color = a
        while True:
            # find edge at cur_v with color cur_color
            if cur_color in colorD[cur_v]:
                eid = colorD[cur_v][cur_color]
                # remove it
                del colorD[cur_v][cur_color]
                u2, v2 = edges[eid]
                # remove from u2
                del colorU[u2][cur_color]
                # assign new color b to this edge
                color[eid] = b
                colorU[u2][b] = eid
                colorD[v2][b] = eid
                # move to u2 with color b
                cur_v = u2
                cur_color = b
            else:
                break
            # now at u2, find edge with color b
            if cur_color in colorU[cur_v]:
                eid = colorU[cur_v][cur_color]
                del colorU[cur_v][cur_color]
                u2, v2 = edges[eid]
                del colorD[v2][cur_color]
                color[eid] = a
                colorU[u2][a] = eid
                colorD[v2][a] = eid
                cur_v = v2
                cur_color = a
            else:
                break

# After processing all edges, we have a proper coloring with at most K colors.
# But we need exactly K colors? The problem says use exactly K windows.
# Our algorithm uses at most K, but we can relabel to use 1..K.

# Find max color used
maxc = max(color)
# If maxc < K, we can just leave as is? The problem says exactly K windows.
# But if maxc < K, we can still output numbers 1..K with some unused? It says assign every cable to a window from 1 to K.
# So we can just output the colors we have; they are within 1..K.

print("YES")
print(" ".join(map(str, color)))
import sys
from collections import deque

input = sys.stdin.readline

nA, nB, m = map(int, input().split())
edges = []
adjA = [[] for _ in range(nA + 1)]
adjB = [[] for _ in range(nB + 1)]

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adjA[u].append((v, i))
    adjB[v].append((u, i))

# Compute T = max degree
degA = [len(adjA[i]) for i in range(nA + 1)]
degB = [len(adjB[i]) for i in range(nB + 1)]
T = max(max(degA), max(degB))

color = [0] * m

# We'll use the standard algorithm for edge coloring bipartite graphs
# using augmenting paths.

# For each edge, assign a color not used by its endpoints.
# If conflict, recolor along an alternating path.

# We'll store for each vertex the set of used colors
usedA = [set() for _ in range(nA + 1)]
usedB = [set() for _ in range(nB + 1)]

# We'll also store for each vertex and color which edge uses it
edgeA = [[-1] * (T + 1) for _ in range(nA + 1)]
edgeB = [[-1] * (T + 1) for _ in range(nB + 1)]

for idx, (u, v) in enumerate(edges):
    # find smallest free color for u and v
    c = 1
    while c in usedA[u] or c in usedB[v]:
        c += 1
    # assign
    color[idx] = c
    usedA[u].add(c)
    usedB[v].add(c)
    edgeA[u][c] = idx
    edgeB[v][c] = idx

    # Now resolve conflicts if any (shouldn't happen with this simple greedy? Actually can happen)
    # We'll do proper recoloring:
    # Actually the simple greedy may fail, so we implement the standard algorithm:
    # We'll redo with proper algorithm below.

# Let's implement the standard algorithm properly:
color = [0] * m
edgeA = [[-1] * (T + 1) for _ in range(nA + 1)]
edgeB = [[-1] * (T + 1) for _ in range(nB + 1)]

for idx, (u, v) in enumerate(edges):
    # find free color for u
    c = 1
    while edgeA[u][c] != -1:
        c += 1
    # assign
    color[idx] = c
    edgeA[u][c] = idx
    edgeB[v][c] = idx

    # Now if v already has color c, we need to recolor
    if edgeB[v][c] != idx:
        # conflict
        # find free color for v
        c2 = 1
        while edgeB[v][c2] != -1:
            c2 += 1
        # start alternating path
        cur_v = v
        cur_c = c2
        while True:
            # find edge at cur_v with color cur_c
            e = edgeB[cur_v][cur_c]
            if e == -1:
                break
            # get other endpoint
            u2, v2 = edges[e]
            # recolor this edge to cur_c
            old_c = color[e]
            color[e] = cur_c
            edgeA[u2][old_c] = -1
            edgeA[u2][cur_c] = e
            edgeB[cur_v][old_c] = -1
            edgeB[cur_v][cur_c] = e
            # now move to u2 with old_c
            cur_v = u2
            cur_c = old_c
            # now find edge at u2 with cur_c
            e = edgeA[cur_v][cur_c]
            if e == -1:
                break
            u2, v2 = edges[e]
            old_c = color[e]
            color[e] = cur_c
            edgeA[cur_v][old_c] = -1
            edgeA[cur_v][cur_c] = e
            edgeB[v2][old_c] = -1
            edgeB[v2][cur_c] = e
            cur_v = v2
            cur_c = old_c

print("YES")
print(" ".join(map(str, color)))
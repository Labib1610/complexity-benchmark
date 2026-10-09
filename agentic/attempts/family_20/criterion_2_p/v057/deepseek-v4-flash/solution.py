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

# Find D = max degree
degA = [len(adjA[i]) for i in range(nA + 1)]
degB = [len(adjB[i]) for i in range(nB + 1)]
D = max(max(degA), max(degB))

color = [0] * m  # 1-based colors

# colorA[u][c] = edge index or -1
colorA = [[-1] * (D + 1) for _ in range(nA + 1)]
colorB = [[-1] * (D + 1) for _ in range(nB + 1)]

for idx, (u, v) in enumerate(edges):
    # find free color for u
    cu = 1
    while colorA[u][cu] != -1:
        cu += 1
    cv = 1
    while colorB[v][cv] != -1:
        cv += 1

    # If same color free for both, assign
    if cu == cv:
        color[idx] = cu
        colorA[u][cu] = idx
        colorB[v][cu] = idx
        continue

    # Otherwise, recolor along alternating path
    # Start with color cu on u side, cv on v side
    current_u = u
    current_v = v
    c1 = cu
    c2 = cv

    # We'll flip colors along path
    path_edges = []
    visited_u = [False] * (nA + 1)
    visited_v = [False] * (nB + 1)

    # Build path: start from u with color c1
    # We'll alternate: from u side, find edge with color c1; from v side, find edge with color c2
    u_side = True
    cur_u = u
    cur_v = v
    while True:
        if u_side:
            # find edge from cur_u with color c1
            e = colorA[cur_u][c1]
            if e == -1:
                break
            path_edges.append(e)
            # move to v side
            cur_v = edges[e][1]
            u_side = False
        else:
            # find edge from cur_v with color c2
            e = colorB[cur_v][c2]
            if e == -1:
                break
            path_edges.append(e)
            cur_u = edges[e][0]
            u_side = True

    # Flip colors along path
    for e in path_edges:
        old = color[e]
        new = c1 if old == c2 else c2
        uu, vv = edges[e]
        colorA[uu][old] = -1
        colorB[vv][old] = -1
        color[e] = new
        colorA[uu][new] = e
        colorB[vv][new] = e

    # Now assign the new edge
    color[idx] = c1
    colorA[u][c1] = idx
    colorB[v][c1] = idx

print("YES")
print(" ".join(map(str, color)))
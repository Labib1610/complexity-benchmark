import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adjL = [[] for _ in range(nL + 1)]
adjR = [[] for _ in range(nR + 1)]

for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adjL[u].append((v, i))
    adjR[v].append((u, i))

# Find Δ
degL = [len(adjL[i]) for i in range(nL + 1)]
degR = [len(adjR[i]) for i in range(nR + 1)]
Delta = max(max(degL), max(degR))

color = [0] * m  # color of each edge (1..Delta)

# colorL[u][c] = edge index incident to u with color c, or -1
colorL = [[-1] * (Delta + 1) for _ in range(nL + 1)]
colorR = [[-1] * (Delta + 1) for _ in range(nR + 1)]

# Greedy edge coloring with alternating paths
for idx, (u, v) in enumerate(edges):
    # find smallest free color at u and v
    cu = 1
    while colorL[u][cu] != -1:
        cu += 1
    cv = 1
    while colorR[v][cv] != -1:
        cv += 1

    if cu == cv:
        c = cu
        color[idx] = c
        colorL[u][c] = idx
        colorR[v][c] = idx
    else:
        # Need to recolor along alternating path
        # Start from v with color cu
        c = cu
        current_vertex = v
        current_side = 'R'
        path_edges = []
        while True:
            if current_side == 'R':
                # find edge at current_vertex with color c
                e = colorR[current_vertex][c]
                if e == -1:
                    break
                path_edges.append(e)
                # move to left side
                current_vertex = edges[e][0]
                current_side = 'L'
            else:
                e = colorL[current_vertex][c]
                if e == -1:
                    break
                path_edges.append(e)
                current_vertex = edges[e][1]
                current_side = 'R'
            # switch color
            c = cu if c == cv else cv

        # Recolor path
        c = cu
        for e in path_edges:
            uu, vv = edges[e]
            # remove old color
            old = color[e]
            colorL[uu][old] = -1
            colorR[vv][old] = -1
            # assign new color
            color[e] = c
            colorL[uu][c] = e
            colorR[vv][c] = e
            c = cu if c == cv else cv

        # Now assign the new edge
        color[idx] = cu
        colorL[u][cu] = idx
        colorR[v][cu] = idx

print("YES")
print(" ".join(map(str, color)))
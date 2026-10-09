import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adjL = [[] for _ in range(nL)]
adjR = [[] for _ in range(nR)]
degL = [0] * nL
degR = [0] * nR

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adjL[u].append((v, i))
    adjR[v].append((u, i))
    degL[u] += 1
    degR[v] += 1

D = max(max(degL, default=0), max(degR, default=0))
color = [0] * m

# We'll use the standard algorithm:
# For each edge, find free colors on both sides, if conflict, recolor along alternating path.

def find_free_color(adj_list, node, color, used):
    used_colors = set()
    for _, idx in adj_list[node]:
        if color[idx] != 0:
            used_colors.add(color[idx])
    for c in range(1, D + 1):
        if c not in used_colors:
            return c
    return 0

for u, v in edges:
    # find free color for u
    cu = find_free_color(adjL, u, color, None)
    cv = find_free_color(adjR, v, color, None)
    if cu == 0 or cv == 0:
        # Should not happen if D is correct
        continue
    if cu == cv:
        # find edge index
        for idx in range(m):
            if edges[idx] == (u, v):
                color[idx] = cu
                break
    else:
        # Need to recolor along alternating path
        # We'll find the edge index
        edge_idx = None
        for idx in range(m):
            if edges[idx] == (u, v):
                edge_idx = idx
                break
        # Try to assign cu to (u,v)
        # Check conflict on v side
        conflict = None
        for _, idx in adjR[v]:
            if color[idx] == cu:
                conflict = idx
                break
        if conflict is None:
            color[edge_idx] = cu
        else:
            # Recolor along path
            # Standard approach: swap colors along alternating path
            # We'll implement iterative path recoloring
            current_edge = edge_idx
            current_color = cu
            current_side = 'L'  # start from left
            while True:
                # assign current_color to current_edge
                color[current_edge] = current_color
                uu, vv = edges[current_edge]
                if current_side == 'L':
                    # check conflict on right side
                    conflict = None
                    for _, idx in adjR[vv]:
                        if color[idx] == current_color and idx != current_edge:
                            conflict = idx
                            break
                    if conflict is None:
                        break
                    else:
                        # find the other color for conflict edge
                        other_color = None
                        for c in range(1, D + 1):
                            if c != current_color:
                                # check if free on left side of conflict edge
                                u2, v2 = edges[conflict]
                                used = set()
                                for _, idx in adjL[u2]:
                                    if color[idx] != 0:
                                        used.add(color[idx])
                                if c not in used:
                                    other_color = c
                                    break
                        current_edge = conflict
                        current_color = other_color
                        current_side = 'R'
                else:
                    # current_side == 'R'
                    uu, vv = edges[current_edge]
                    conflict = None
                    for _, idx in adjL[uu]:
                        if color[idx] == current_color and idx != current_edge:
                            conflict = idx
                            break
                    if conflict is None:
                        break
                    else:
                        other_color = None
                        for c in range(1, D + 1):
                            if c != current_color:
                                u2, v2 = edges[conflict]
                                used = set()
                                for _, idx in adjR[v2]:
                                    if color[idx] != 0:
                                        used.add(color[idx])
                                if c not in used:
                                    other_color = c
                                    break
                        current_edge = conflict
                        current_color = other_color
                        current_side = 'L'

print("YES")
print(" ".join(str(c) for c in color))
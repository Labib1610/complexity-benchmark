import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
degL = [0] * (nL + 1)
degR = [0] * (nR + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    degL[u] += 1
    degR[v] += 1

Delta = max(max(degL), max(degR), 1)

# color[u][v] = color of edge (u,v), 0 means uncolored
colorL = [{} for _ in range(nL + 1)]
colorR = [{} for _ in range(nR + 1)]

# For each vertex, keep a set of used colors
usedL = [set() for _ in range(nL + 1)]
usedR = [set() for _ in range(nR + 1)]

# We'll store the color for each edge index
edge_color = [0] * m

# Helper to find a free color for a vertex
def find_free(used_set):
    c = 1
    while c in used_set:
        c += 1
    return c

# Process edges
for idx, (u, v) in enumerate(edges):
    # Find a color not used by u and not used by v
    cu = find_free(usedL[u])
    cv = find_free(usedR[v])
    if cu != cv:
        # Assign cu to edge, but need to check if v uses cu
        if cu not in usedR[v]:
            # assign cu
            colorL[u][v] = cu
            colorR[v][u] = cu
            usedL[u].add(cu)
            usedR[v].add(cu)
            edge_color[idx] = cu
        else:
            # cu is used by v, so we need to swap along alternating path
            # Find the edge (u2, v) with color cu
            u2 = None
            for uu, cc in colorR[v].items():
                if cc == cu:
                    u2 = uu
                    break
            # Now we have edge (u2, v) colored cu
            # We'll try to recolor (u2, v) with cv
            # But cv might be used by u2, so we continue
            # Standard Kempe chain: swap colors cu and cv along path starting from (u,v)
            # We'll implement iterative path recoloring
            # Path: start at (u,v) with color cu, but v already has cu from (u2,v)
            # So we do: color (u,v) with cv, then recolor (u2,v) with cu, but u2 might have cu? Actually u2 has cu, so we need to recolor (u2, something) etc.
            # Simpler: use BFS/DFS to find alternating path
            # We'll implement a standard function
            # For simplicity, we can do a recursive swap
            def swap_colors(u, v, c1, c2):
                # Edge (u,v) is to be colored c1, but c1 is used by v from another edge
                # Find that other edge
                u2 = None
                for uu, cc in colorR[v].items():
                    if cc == c1:
                        u2 = uu
                        break
                # Recolor (u,v) to c2
                # Remove old color from u and v
                old = colorL[u].get(v)
                if old:
                    usedL[u].discard(old)
                    usedR[v].discard(old)
                colorL[u][v] = c2
                colorR[v][u] = c2
                usedL[u].add(c2)
                usedR[v].add(c2)
                # Now (u2,v) has c1, but u2 might have c2? If not, we can recolor it to c1
                if c2 not in usedL[u2]:
                    # recolor (u2,v) to c1
                    old2 = colorL[u2].get(v)
                    if old2:
                        usedL[u2].discard(old2)
                        usedR[v].discard(old2)
                    colorL[u2][v] = c1
                    colorR[v][u2] = c1
                    usedL[u2].add(c1)
                    usedR[v].add(c1)
                else:
                    # c2 is used by u2, so we need to continue the chain
                    # Find edge (u2, v2) with color c2
                    v2 = None
                    for vv, cc in colorL[u2].items():
                        if cc == c2:
                            v2 = vv
                            break
                    # Recolor (u2,v) to c1, then swap on (u2,v2)
                    old2 = colorL[u2].get(v)
                    if old2:
                        usedL[u2].discard(old2)
                        usedR[v].discard(old2)
                    colorL[u2][v] = c1
                    colorR[v][u2] = c1
                    usedL[u2].add(c1)
                    usedR[v].add(c1)
                    # Now recurse on (u2, v2) with colors c2 and c1 swapped
                    swap_colors(u2, v2, c2, c1)

            swap_colors(u, v, cu, cv)
            edge_color[idx] = cv  # after swap, (u,v) got cv
    else:
        # cu == cv, assign directly
        colorL[u][v] = cu
        colorR[v][u] = cu
        usedL[u].add(cu)
        usedR[v].add(cu)
        edge_color[idx] = cu

print("YES")
print(" ".join(map(str, edge_color)))
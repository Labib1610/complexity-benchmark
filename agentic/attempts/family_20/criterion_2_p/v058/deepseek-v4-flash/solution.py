import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adjL = [[] for _ in range(nL)]
adjR = [[] for _ in range(nR)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adjL[u].append((v, i))
    adjR[v].append((u, i))

# Determine peak load = max degree
deg = [0] * (nL + nR)
for u, v in edges:
    deg[u] += 1
    deg[nL + v] += 1
peak = max(deg) if deg else 0

# Edge coloring using augmenting path algorithm
color = [0] * m
# colorL[u][c] = edge index incident to left u with color c
# colorR[v][c] = edge index incident to right v with color c
colorL = [dict() for _ in range(nL)]
colorR = [dict() for _ in range(nR)]

def get_free_colorL(u):
    c = 1
    while c in colorL[u]:
        c += 1
    return c

def get_free_colorR(v):
    c = 1
    while c in colorR[v]:
        c += 1
    return c

def flip(u, c1, c2):
    # flip colors c1 and c2 along path starting from left u
    v = -1
    while True:
        # find edge from u with color c1
        if v is None:
            break
        if u is not None:
            e = colorL[u].get(c1)
            if e is None:
                break
            v = edges[e][1]
            # recolor
            colorL[u].pop(c1)
            colorR[v].pop(c2)
            color[e] = c2
            colorL[u][c2] = e
            colorR[v][c2] = e
            u = None
            # swap colors
            c1, c2 = c2, c1
        else:
            e = colorR[v].get(c1)
            if e is None:
                break
            u = edges[e][0]
            colorL[u].pop(c2)
            colorR[v].pop(c1)
            color[e] = c2
            colorL[u][c2] = e
            colorR[v][c2] = e
            v = None
            c1, c2 = c2, c1

for idx, (u, v) in enumerate(edges):
    c1 = get_free_colorL(u)
    c2 = get_free_colorR(v)
    if c1 == c2:
        color[idx] = c1
        colorL[u][c1] = idx
        colorR[v][c1] = idx
    else:
        # try augmenting path
        # find path starting from v with color c1
        # We'll do iterative walk
        # First, check if we can find a path from v using color c1
        path_edges = []
        cur_v = v
        cur_color = c1
        seen = set()
        while True:
            e = colorR[cur_v].get(cur_color)
            if e is None:
                break
            path_edges.append((e, cur_color))
            u2 = edges[e][0]
            # now on left u2, switch to color c2
            e2 = colorL[u2].get(c2)
            if e2 is None:
                break
            path_edges.append((e2, c2))
            cur_v = edges[e2][1]
            cur_color = c1
            if len(path_edges) > m + m:
                break

        # If we found path (ended at a free color), do flip
        # Simpler: standard procedure
        # We'll implement recursive/iterative standard augmenting
        # Use stack to remember path
        stack = [(u, c1, None)]  # (current left node, color to find, previous edge)
        found = False
        visited = set()
        while stack:
            cur_u, col, prev_e = stack.pop()
            if cur_u in visited:
                continue
            visited.add(cur_u)
            e = colorL[cur_u].get(col)
            if e is None:
                # free at left: flip along prev path
                # backtrack
                path = []
                c = col
                node = cur_u
                while True:
                    # find edge from node with color c
                    e = colorL[node].get(c) if node is not None else None
                    if e is None:
                        break
                    path.append((e, c))
                    v2 = edges[e][1]
                    # switch to other color
                    c = c2 if c == c1 else c1
                    e2 = colorR[v2].get(c)
                    if e2 is None:
                        break
                    path.append((e2, c))
                    node = edges[e2][0]
                    c = c1 if c == c2 else c2
                # flip
                for eidx, oldc in path:
                    uu, vv = edges[eidx]
                    newc = c2 if oldc == c1 else c1
                    colorL[uu].pop(oldc)
                    colorR[vv].pop(oldc)
                    color[eidx] = newc
                    colorL[uu][newc] = eidx
                    colorR[vv][newc] = eidx
                # now assign new edge
                color[idx] = c1
                colorL[u][c1] = idx
                colorR[v][c1] = idx
                found = True
                break
            else:
                # go to right node with other color
                v2 = edges[e][1]
                # from v2, try color c2
                stack.append((None, c2, e))  # placeholder
        if not found:
            # fallback simple assign (shouldn't happen)
            color[idx] = c1
            colorL[u][c1] = idx
            colorR[v][c1] = idx

# Output
print("YES")
print(" ".join(str(c) for c in color))
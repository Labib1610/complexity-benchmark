import sys
sys.setrecursionlimit(1 << 25)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it)); nR = int(next(it)); m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    Delta = max(degL + degR) if m else 0

    # adjacency lists storing (neighbor, edge_id)
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for idx, (u, v) in enumerate(edges):
        adjL[u].append((v, idx))
        adjR[v].append((u, idx))

    # color of each edge, 0 means uncolored
    col = [0] * m

    # for each vertex, map color -> edge id (only for colored edges)
    usedL = [{} for _ in range(nL)]
    usedR = [{} for _ in range(nR)]

    # helper to find a free color at a vertex
    def free_color(used, deg):
        # used is dict of used colors
        # deg is degree of vertex
        # we know Delta >= deg, so there is at least one free color
        # try sequentially from 1..Delta
        for c in range(1, Delta + 1):
            if c not in used:
                return c
        return 1  # never reached

    from collections import deque

    for eid, (u, v) in enumerate(edges):
        if col[eid]:
            continue
        # try to assign a free color directly
        cu = set(usedL[u].keys())
        cv = set(usedR[v].keys())
        for c in range(1, Delta + 1):
            if c not in cu and c not in cv:
                col[eid] = c
                usedL[u][c] = eid
                usedR[v][c] = eid
                break
        if col[eid]:
            continue

        # need to recolor via alternating path
        # pick any color a not used at u, any color b not used at v
        a = free_color(usedL[u], degL[u])
        b = free_color(usedR[v], degR[v])

        # BFS to find alternating path from u using colors a/b
        # vertices are represented as (side, vertex)
        # side 0 = left, 1 = right
        prev = {}  # (side, vertex) -> (prev_side, prev_vertex, edge_id, color_used)
        q = deque()
        q.append( (0, u) )
        prev[(0, u)] = None
        target = None

        while q and target is None:
            side, x = q.popleft()
            if side == 0:  # left vertex, we can follow edge of color a
                if a in usedL[x]:
                    eid2 = usedL[x][a]
                    y = edges[eid2][1]
                    if (1, y) not in prev:
                        prev[(1, y)] = (0, x, eid2, a)
                        q.append( (1, y) )
                # also can follow edge of color b from right side later
            else:  # right vertex, we can follow edge of color b
                if b in usedR[x]:
                    eid2 = usedR[x][b]
                    y = edges[eid2][0]
                    if (0, y) not in prev:
                        prev[(0, y)] = (1, x, eid2, b)
                        q.append( (0, y) )
                # also can follow edge of color a from left side later

        # In bipartite case, such alternating path always exists and ends at a vertex where the needed color is free.
        # Reconstruct and flip colors along the path
        # Start from v with color b free, we will toggle colors a<->b along the path
        cur_side, cur_vert = 1, v
        while True:
            p = prev.get((cur_side, cur_vert))
            if p is None:
                break
            prev_side, prev_vert, peid, pcol = p
            # flip color of edge peid
            newcol = a if pcol == b else b
            col[peid] = newcol
            # update used maps
            if prev_side == 0:
                usedL[prev_vert][newcol] = peid
                del usedL[prev_vert][pcol]
                usedR[edges[peid][1]][newcol] = peid
                del usedR[edges[peid][1]][pcol]
            else:
                usedR[prev_vert][newcol] = peid
                del usedR[prev_vert][pcol]
                usedL[edges[peid][0]][newcol] = peid
                del usedL[edges[peid][0]][pcol]
            cur_side, cur_vert = prev_side, prev_vert

        # finally assign color a to original edge
        col[eid] = a
        usedL[u][a] = eid
        usedR[v][a] = eid

    print("YES")
    print(' '.join(map(str, col)))

if __name__ == "__main__":
    main()
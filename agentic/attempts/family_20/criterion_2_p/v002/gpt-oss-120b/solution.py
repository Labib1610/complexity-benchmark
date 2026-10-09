import sys
from collections import deque, defaultdict

def solve() -> None:
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    Δ = max(max(degL) if nL else 0, max(degR) if nR else 0)

    # adjacency lists of colored edges
    # for each vertex store dict color -> neighbor vertex (edge index)
    colL = [dict() for _ in range(nL)]
    colR = [dict() for _ in range(nR)]

    ans = [0] * m

    # helper to find augmenting path and recolor
    def bfs(u_start, color_needed):
        """Find alternating path that frees color_needed on left vertex u_start.
        Returns dict of (vertex, side) -> (prev_vertex, prev_side, used_color) for reconstruction.
        """
        # side 0 = left, 1 = right
        q = deque()
        visited = {}
        q.append((u_start, 0))
        visited[(u_start, 0)] = None  # start has no predecessor

        while q:
            v, side = q.popleft()
            if side == 0:  # left vertex
                # try to move via the edge that currently uses color_needed on this left vertex
                if color_needed in colL[v]:
                    nb, _ = colL[v][color_needed]
                    nxt = (nb, 1)
                    if nxt not in visited:
                        visited[nxt] = (v, side, color_needed)
                        q.append(nxt)
                else:
                    # free color found on left side -> we can stop
                    return visited, (v, side)
            else:  # right vertex
                # we are at a right vertex that currently has some color c from previous step
                # we need to explore the other color on this right vertex that is free
                # The incoming edge gave us a color c (stored in visited)
                prev = visited[(v, side)]
                incoming_color = prev[2] if prev else None
                # try all colors on this right vertex except incoming_color
                for c, (nb, _) in colR[v].items():
                    if c == incoming_color:
                        continue
                    nxt = (nb, 0)
                    if nxt not in visited:
                        visited[nxt] = (v, side, c)
                        q.append(nxt)
                # also, if there is a free color on this right vertex, we can finish
                if incoming_color is not None and incoming_color not in colR[v]:
                    return visited, (v, side)
        return visited, None

    for idx, (u, v) in enumerate(edges):
        # try smallest free color
        usedL = colL[u]
        usedR = colR[v]
        c = 1
        while c in usedL or c in usedR:
            c += 1
        if c not in usedL and c not in usedR:
            # assign directly
            usedL[c] = (v, idx)
            usedR[c] = (u, idx)
            ans[idx] = c
            continue

        # need recoloring: we will free a color on left u
        # pick a color a that is free on left u (maybe >Δ but we know such exists <=Δ)
        a = 1
        while a in usedL:
            a += 1
        # now we need to make color a free on right v as well
        # perform BFS alternating path starting from left u trying to free color a
        visited, end = bfs(u, a)
        if end is None:
            # should not happen in bipartite graphs
            print("NO")
            return
        # reconstruct path and flip colors
        cur = end
        while visited[cur] is not None:
            pv, pside, col = visited[cur]
            # edge (pv, pside) uses color col and goes to cur
            if pside == 0:
                # left pv --col--> right cur[0]
                nb = cur[0]
                # swap colors: edge gets new color (col of next step)
                # actually we just flip along the path, effectively moving color a towards u
                # implement by reassigning the edge to the other color
                # remove old assignment
                del colL[pv][col]
                del colR[nb][col]
                # assign new color
                newcol = a if cur == (u,0) else col
                colL[pv][newcol] = (nb, None)
                colR[nb][newcol] = (pv, None)
            else:
                # right pv --col--> left cur[0]
                nb = cur[0]
                del colR[pv][col]
                del colL[nb][col]
                newcol = a if cur == (u,0) else col
                colR[pv][newcol] = (nb, None)
                colL[nb][newcol] = (pv, None)
            cur = (pv, pside)

        # finally assign edge (u,v) color a
        colL[u][a] = (v, idx)
        colR[v][a] = (u, idx)
        ans[idx] = a

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))

    edges = []
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    degL = [0] * nL
    degR = [0] * nR

    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adjL[u].append(idx)
        adjR[v].append(idx)
        degL[u] += 1
        degR[v] += 1

    Δ = max(max(degL) if degL else 0, max(degR) if degR else 0)

    # colour of each edge, 0 = not coloured yet
    col = [0] * m

    # colour -> edge index for each vertex
    usedL = [dict() for _ in range(nL)]
    usedR = [dict() for _ in range(nR)]

    # helper: smallest colour not in the dict
    def free_colour(used):
        c = 1
        while c in used:
            c += 1
        return c

    # recolouring routine, guarantees colour c becomes free at v
    def recolour(u, v, c):
        # c is used at v, free at u
        d = free_colour(usedL[u])
        # start from the edge of colour c at v
        start_edge = usedR[v][c]

        # BFS/DFS alternating between colours c and d
        stack = [(v, start_edge, c)]   # (vertex, incoming edge, colour of that edge)
        parent = {}                    # vertex -> (prev_vertex, edge, colour)

        while stack:
            cur, inc_edge, cur_col = stack.pop()
            # we arrived at cur via an edge of colour cur_col
            # we want to leave cur via the other colour
            next_col = d if cur_col == c else c
            # check if next_col is free at cur
            used = usedL[cur] if cur < nL else usedR[cur - nL]
            if next_col not in used:
                # found free colour, flip along the path
                # first flip the incoming edge
                edge_to_flip = inc_edge
                while True:
                    # swap colours on edge_to_flip
                    u1, v1 = edges[edge_to_flip]
                    old = col[edge_to_flip]
                    new = d if old == c else c
                    col[edge_to_flip] = new
                    # update dictionaries
                    if old != 0:
                        if edge_to_flip in usedL[u1]:
                            del usedL[u1][old]
                        if edge_to_flip in usedR[v1]:
                            del usedR[v1][old]
                    usedL[u1][new] = edge_to_flip
                    usedR[v1][new] = edge_to_flip

                    if edge_to_flip == start_edge:
                        break
                    # move to previous vertex
                    prev, prev_edge, prev_col = parent[(u1 if cur == v1 else v1)]
                    edge_to_flip = prev_edge
                    cur = prev
                return
            # otherwise follow the edge that currently has next_col
            next_edge = used[next_col]
            u2, v2 = edges[next_edge]
            nxt_vertex = v2 if cur == u2 else u2
            if nxt_vertex not in parent:
                parent[nxt_vertex] = (cur, next_edge, next_col)
                stack.append((nxt_vertex, next_edge, next_col))

    # main processing
    for idx, (u, v) in enumerate(edges):
        if col[idx]:
            continue
        c = free_colour(usedL[u])
        if c not in usedR[v]:
            col[idx] = c
            usedL[u][c] = idx
            usedR[v][c] = idx
        else:
            recolour(u, v, c)
            # now c is free at both ends
            col[idx] = c
            usedL[u][c] = idx
            usedR[v][c] = idx

    out = ['YES', '\n', ' '.join(str(x) for x in col)]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()
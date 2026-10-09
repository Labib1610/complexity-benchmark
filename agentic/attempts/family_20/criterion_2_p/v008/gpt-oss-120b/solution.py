import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    Delta = max(max(degL) if degL else 0, max(degR) if degR else 0)

    # colour of each edge, 0 = uncoloured
    col = [0] * m

    # for each vertex: colour -> edge id
    usedL = [dict() for _ in range(nL)]
    usedR = [dict() for _ in range(nR)]

    # helper to find a missing colour at a vertex
    def missing_colour(used, degree):
        # degree <= Delta, so at most Delta checks
        for c in range(1, Delta + 1):
            if c not in used:
                return c
        return 1  # never reached

    from collections import deque

    for eid, (u, v) in enumerate(edges):
        # try greedy colour
        found = None
        for c in range(1, Delta + 1):
            if c not in usedL[u] and c not in usedR[v]:
                found = c
                break
        if found is not None:
            col[eid] = found
            usedL[u][found] = eid
            usedR[v][found] = eid
            continue

        # need augmenting path
        c1 = missing_colour(usedL[u], degL[u])
        c2 = missing_colour(usedR[v], degR[v])

        # BFS on alternating c1/c2 edges
        # parent maps (vertex, side) -> (prev_vertex, prev_side, edge_id)
        parent = dict()
        q = deque()
        # start from left vertex u with colour c1
        q.append( (u, 0, c1) )
        parent[(u,0)] = None

        end = None  # (vertex, side) where c2 is missing
        while q:
            vert, side, col_cur = q.popleft()
            if side == 0:          # left side
                # edge of colour col_cur incident to this left vertex
                if col_cur in usedL[vert]:
                    e2 = usedL[vert][col_cur]
                    _, vr = edges[e2]
                    nxt = (vr, 1, col_cur)   # go to right vertex
                    if (vr,1) not in parent:
                        parent[(vr,1)] = (vert,0,e2)
                        q.append(nxt)
                else:
                    # colour missing here -> we have reached a free vertex
                    if col_cur == c2:
                        end = (vert,0)
                        break
            else:                 # right side
                if col_cur in usedR[vert]:
                    e2 = usedR[vert][col_cur]
                    vl, _ = edges[e2]
                    nxt = (vl, 0, col_cur)
                    if (vl,0) not in parent:
                        parent[(vl,0)] = (vert,1,e2)
                        q.append(nxt)
                else:
                    if col_cur == c2:
                        end = (vert,1)
                        break

        # reconstruct path and flip colours
        # we know end vertex has colour c2 missing, start is (u,0)
        cur = end
        while cur != (u,0):
            prev = parent[cur]
            pv, ps, e_id = prev
            # flip colour of edge e_id
            old = col[e_id]
            new = c1 if old == c2 else c2
            col[e_id] = new
            # update dictionaries
            lu, rv = edges[e_id]
            if old == c1:
                del usedL[lu][c1]
                del usedR[rv][c1]
                usedL[lu][c2] = e_id
                usedR[rv][c2] = e_id
            else:
                del usedL[lu][c2]
                del usedR[rv][c2]
                usedL[lu][c1] = e_id
                usedR[rv][c1] = e_id
            cur = (pv, ps)

        # now colour the original edge with c1
        col[eid] = c1
        usedL[u][c1] = eid
        usedR[v][c1] = eid

    # all edges coloured
    out = ['YES', '\n', ' '.join(map(str, col))]
    sys.stdout.write(''.join(out))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nO = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # degree calculation
    degA = [0] * nA
    degO = [0] * nO
    for u, v in edges:
        degA[u] += 1
        degO[v] += 1
    K = max(max(degA) if nA else 0, max(degO) if nO else 0)

    # adjacency: for each vertex store edge ids
    adjA = [[] for _ in range(nA)]
    adjO = [[] for _ in range(nO)]
    for idx, (u, v) in enumerate(edges):
        adjA[u].append(idx)
        adjO[v].append(idx)

    # color of each edge, 0 means uncolored, else 1..K
    col = [0] * m

    # for each vertex, which edge uses a given color (0 if none)
    # we store as dicts because degree may be far less than K
    usedA = [dict() for _ in range(nA)]
    usedO = [dict() for _ in range(nO)]

    # helper to find a free color at a vertex
    def free_color(vertex_used, deg):
        # vertex_used is dict color->edge
        # degree <= K, so there is at least one free color in 1..K
        # we can keep a pointer per vertex to speed up
        # but simple linear scan is acceptable because total scans O(mK) worst,
        # we improve by storing next candidate
        # We'll use while loop with a stored pointer
        ptr = free_color.ptr[vertex_used]
        while ptr in vertex_used:
            ptr += 1
        free_color.ptr[vertex_used] = ptr
        return ptr

    free_color.ptr = {}
    for d in usedA:
        free_color.ptr[d] = 1
    for d in usedO:
        free_color.ptr[d] = 1

    # BFS for alternating path
    from collections import deque

    for eid, (u, v) in enumerate(edges):
        if col[eid]:
            continue
        # try direct free color
        cu = free_color(usedA[u], degA[u])
        if cu not in usedO[v]:
            # assign directly
            col[eid] = cu
            usedA[u][cu] = eid
            usedO[v][cu] = eid
            continue
        cv = free_color(usedO[v], degO[v])
        if cv not in usedA[u]:
            col[eid] = cv
            usedA[u][cv] = eid
            usedO[v][cv] = eid
            continue

        # need to find alternating path between colors cu and cv
        # BFS on vertices, storing predecessor info
        # state: (side, vertex, color) where side 0=Alpha,1=Omega
        q = deque()
        prev = {}  # key -> (prev_key, edge_id)
        start_key = ('A', u, cu)  # we want to free cu at u
        q.append(start_key)
        prev[start_key] = None
        target_key = None

        while q and target_key is None:
            side, vert, colc = q.popleft()
            if side == 'A':
                # from Alpha vertex, we can go via edge that has color colc (if exists)
                if colc in usedA[vert]:
                    e = usedA[vert][colc]
                    _, v2 = edges[e]
                    # move to Omega vertex via same edge, now looking for color cv
                    nxt = ('O', v2, cv)
                    if nxt not in prev:
                        prev[nxt] = ( (side, vert, colc), e )
                        # check if cv free at this Omega vertex
                        if cv not in usedO[v2]:
                            target_key = nxt
                            break
                        q.append(nxt)
            else:  # Omega side
                if colc in usedO[vert]:
                    e = usedO[vert][colc]
                    u2, _ = edges[e]
                    nxt = ('A', u2, cu)
                    if nxt not in prev:
                        prev[nxt] = ( (side, vert, colc), e )
                        if cu not in usedA[u2]:
                            target_key = nxt
                            break
                        q.append(nxt)

        # reconstruct and flip colors along the path
        # target vertex now has free needed color
        cur = target_key
        while prev[cur] is not None:
            (pside, pvert, pcol), e = prev[cur]
            # flip edge e from pcol to the other color
            if pside == 'A':
                # edge e currently has color pcol at Alpha side, we will change it to cv if pcol==cu else to cu
                newc = cv if pcol == cu else cu
            else:
                newc = cv if pcol == cu else cu
            # update structures
            oldc = col[e]
            col[e] = newc
            # remove old mapping
            if pside == 'A':
                usedA[pvert].pop(oldc, None)
                usedO[edges[e][1]].pop(oldc, None)
                usedA[pvert][newc] = e
                usedO[edges[e][1]][newc] = e
            else:
                usedO[pvert].pop(oldc, None)
                usedA[edges[e][0]].pop(oldc, None)
                usedO[pvert][newc] = e
                usedA[edges[e][0]][newc] = e
            cur = (pside, pvert, pcol)

        # finally assign the original edge
        col[eid] = cu
        usedA[u][cu] = eid
        usedO[v][cu] = eid

    # output
    out = ['YES', ' '.join(str(c) for c in col)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
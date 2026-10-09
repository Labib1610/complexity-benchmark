import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    NS = int(next(it))
    NG = int(next(it))
    M = int(next(it))

    edges = []
    adjU = [[] for _ in range(NS)]
    adjV = [[] for _ in range(NG)]
    degU = [0] * NS
    degV = [0] * NG

    for idx in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adjU[u].append((idx, v))
        adjV[v].append((idx, u))
        degU[u] += 1
        degV[v] += 1

    D = 0
    for d in degU:
        if d > D:
            D = d
    for d in degV:
        if d > D:
            D = d

    # colour of each edge, 0 = not coloured yet
    col = [0] * M

    # used colours per vertex, stored as set for sparsity
    usedU = [set() for _ in range(NS)]
    usedV = [set() for _ in range(NG)]

    # helper: first free colour for a vertex
    def first_free(used_set):
        # colours are 1..D, used_set size is small, linear scan is fine
        for c in range(1, D + 1):
            if c not in used_set:
                return c
        return D + 1  # never happens

    for eid in range(M):
        if col[eid]:
            continue
        u, v = edges[eid]

        # try direct colour
        cu = first_free(usedU[u])
        cv = first_free(usedV[v])
        if cu == cv:
            c = cu
            col[eid] = c
            usedU[u].add(c)
            usedV[v].add(c)
            continue

        # need to swap colours cu (free at u) and cv (free at v)
        c1, c2 = cu, cv
        # BFS on vertices, alternating colours c1 and c2
        # start from the vertex that already has c1 free (u)
        start = u
        target = v
        start_colour = c1
        target_colour = c2

        # predecessor info: for each visited vertex store (prev_vertex, edge_id, colour_used_to_enter)
        prev = dict()
        q = deque()
        q.append(start)
        prev[start] = (-1, -1, -1)   # root marker

        found = False
        while q and not found:
            x = q.popleft()
            # which colour are we looking for from this vertex?
            # it alternates: if we arrived via colour c1 we now look for c2, etc.
            # we can deduce from the colour stored in prev[x]
            if x == start:
                need = start_colour
            else:
                need = c1 if prev[x][2] == c2 else c2

            # iterate over incident edges of colour 'need'
            if x < NS:          # satellite side
                for eid2, nb in adjU[x]:
                    if col[eid2] != need:
                        continue
                    if nb in prev:
                        continue
                    prev[nb] = (x, eid2, need)
                    if nb == target:
                        found = True
                        break
                    q.append(nb)
            else:               # ground side, index shifted by NS
                gx = x - NS
                for eid2, nb in adjV[gx]:
                    if col[eid2] != need:
                        continue
                    if nb in prev:
                        continue
                    prev[nb] = (x, eid2, need)
                    if nb == target:
                        found = True
                        break
                    q.append(nb)

        # reconstruct path and flip colours
        cur = target
        while cur != start:
            p, e_id, used_col = prev[cur]
            # flip colour of edge e_id
            new_col = c1 if col[e_id] == c2 else c2
            # update structures
            old = col[e_id]
            col[e_id] = new_col
            uu, vv = edges[e_id]
            usedU[uu].remove(old)
            usedU[uu].add(new_col)
            usedV[vv].remove(old)
            usedV[vv].add(new_col)

            cur = p

        # now colour the original edge with c1 (which is free at both ends)
        col[eid] = c1
        usedU[u].add(c1)
        usedV[v].add(c1)

    # output
    out = ['YES\n', ' '.join(str(c) for c in col)]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
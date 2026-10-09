import sys
from collections import deque, defaultdict

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
    Delta = max(max(degL) if nL else 0, max(degR) if nR else 0)

    # colour of each edge, 0 = uncoloured
    col = [0] * m

    # for each vertex: colour -> edge index
    usedL = [dict() for _ in range(nL)]
    usedR = [dict() for _ in range(nR)]

    # auxiliary structures for BFS
    # we store for each visited vertex the predecessor (vertex, edge, colour)
    # left vertices are numbered 0..nL-1, right vertices are offset by nL
    total_vertices = nL + nR
    pred = [-1] * total_vertices
    pred_edge = [-1] * total_vertices
    pred_col = [0] * total_vertices

    for idx, (u, v) in enumerate(edges):
        if col[idx]:   # already coloured (should not happen)
            continue

        # try to find a free colour directly
        free = None
        for c in range(1, Delta + 1):
            if c not in usedL[u] and c not in usedR[v]:
                free = c
                break
        if free is not None:
            col[idx] = free
            usedL[u][free] = idx
            usedR[v][free] = idx
            continue

        # need augmentation
        # pick any colour missing at u and any colour missing at v
        for c1 in range(1, Delta + 1):
            if c1 not in usedL[u]:
                break
        for c2 in range(1, Delta + 1):
            if c2 not in usedR[v]:
                break

        # BFS on alternating graph of colours c1 and c2
        for i in range(total_vertices):
            pred[i] = -1
        q = deque()
        start = u                     # left side vertex
        q.append(start)
        pred[start] = start           # mark visited

        end_vertex = -1
        while q and end_vertex == -1:
            x = q.popleft()
            if x < nL:                # left vertex
                cur_used = usedL[x]
                other_used = usedR
                offset = nL
                # follow edge of colour c2 (if exists)
                if c2 in cur_used:
                    e_id = cur_used[c2]
                    _, vv = edges[e_id]
                    y = vv + offset
                    if pred[y] == -1:
                        pred[y] = x
                        pred_edge[y] = e_id
                        pred_col[y] = c2
                        q.append(y)
                # follow edge of colour c1 (if exists) – this is the opposite direction
                if c1 in cur_used:
                    e_id = cur_used[c1]
                    _, vv = edges[e_id]
                    y = vv + offset
                    if pred[y] == -1:
                        pred[y] = x
                        pred_edge[y] = e_id
                        pred_col[y] = c1
                        q.append(y)
            else:                     # right vertex
                y = x - nL
                cur_used = usedR[y]
                # follow colour c1
                if c1 in cur_used:
                    e_id = cur_used[c1]
                    uu, _ = edges[e_id]
                    z = uu
                    if pred[z] == -1:
                        pred[z] = x
                        pred_edge[z] = e_id
                        pred_col[z] = c1
                        q.append(z)
                # follow colour c2
                if c2 in cur_used:
                    e_id = cur_used[c2]
                    uu, _ = edges[e_id]
                    z = uu
                    if pred[z] == -1:
                        pred[z] = x
                        pred_edge[z] = e_id
                        pred_col[z] = c2
                        q.append(z)
                # check if c1 is free here -> we have reached a free vertex
                if c1 not in cur_used:
                    end_vertex = x

        # reconstruct path and flip colours
        vtx = end_vertex
        while vtx != start:
            e_id = pred_edge[vtx]
            cur_c = pred_col[vtx]
            # swap colour on this edge
            u0, v0 = edges[e_id]
            # current colour of edge e_id is cur_c
            new_c = c1 if cur_c == c2 else c2
            # update structures
            # remove old
            del usedL[u0][cur_c]
            del usedR[v0][cur_c]
            # add new
            usedL[u0][new_c] = e_id
            usedR[v0][new_c] = e_id
            col[e_id] = new_c
            vtx = pred[vtx]

        # now colour c1 is free at u, assign it to the original edge
        col[idx] = c1
        usedL[u][c1] = idx
        usedR[v][c1] = idx

    # output
    out = ['YES\n', ' '.join(str(c) for c in col)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))

    edges = []
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1

    Δ = max(max(degA), max(degB))

    # colour dictionaries
    colA = [dict() for _ in range(nA + 1)]   # colour -> (v, edge_id)
    colB = [dict() for _ in range(nB + 1)]

    edge_colour = [0] * m

    # helper to find a missing colour at a vertex
    def missing_colour(col_dict):
        # try 1..Δ, stop at first absent
        for c in range(1, Δ + 1):
            if c not in col_dict:
                return c
        return None  # never happens

    for idx, (u, v) in enumerate(edges):
        cu = colA[u]
        cv = colB[v]

        # try direct colour
        found = None
        for c in range(1, Δ + 1):
            if c not in cu and c not in cv:
                found = c
                break
        if found is not None:
            edge_colour[idx] = found
            cu[found] = (v, idx)
            cv[found] = (u, idx)
            continue

        # need recolouring
        a = missing_colour(cu)
        b = missing_colour(cv)

        # BFS on alternating graph of colours a,b
        # state: (vertex, side, next_colour)
        # side = 0 for left (A), 1 for right (B)
        start = (u, 0, a)
        q = deque([start])
        prev = {start: None}   # maps state -> (prev_state, edge_id)

        end_state = None
        while q:
            x, side, need = q.popleft()
            # check if colour need is free at this vertex
            if side == 0:
                col_dict = colA[x]
            else:
                col_dict = colB[x]
            if need not in col_dict:
                end_state = (x, side, need)
                break
            # colour present, follow the edge
            nb, eid = col_dict[need]
            other_need = b if need == a else a
            nxt = (nb, 1 - side, other_need)
            if nxt not in prev:
                prev[nxt] = ((x, side, need), eid)
                q.append(nxt)

        # reconstruct path and flip colours
        cur = end_state
        while prev[cur] is not None:
            (px, pside, pneed), eid = prev[cur]
            # edge eid currently has colour pneed, we change it to the other colour
            new_colour = b if pneed == a else a
            # update dictionaries
            uu, vv = edges[eid]
            # remove old entry
            if pneed in colA[uu]:
                del colA[uu][pneed]
            if pneed in colB[vv]:
                del colB[vv][pneed]
            # add new entry
            colA[uu][new_colour] = (vv, eid)
            colB[vv][new_colour] = (uu, eid)
            edge_colour[eid] = new_colour
            cur = (px, pside, pneed)

        # now colour the original edge with a
        edge_colour[idx] = a
        colA[u][a] = (v, idx)
        colB[v][a] = (u, idx)

    # output
    out = ['YES\n', ' '.join(str(c) for c in edge_colour)]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
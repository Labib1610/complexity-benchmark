import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degA = [0] * nA
    degB = [0] * nB
    for u, v in edges:
        degA[u] += 1
        degB[v] += 1
    D = max(max(degA) if degA else 0, max(degB) if degB else 0)

    # adjacency: for each vertex store list of (neighbor, edge_idx)
    adjA = [[] for _ in range(nA)]
    adjB = [[] for _ in range(nB)]
    for idx, (u, v) in enumerate(edges):
        adjA[u].append((v, idx))
        adjB[v].append((u, idx))

    # color of each edge (0 = uncolored)
    col = [0] * m

    # for each vertex, map color -> edge idx (at most one per color)
    usedA = [{} for _ in range(nA)]
    usedB = [{} for _ in range(nB)]

    # helper to find smallest free color at a vertex
    def free_color(used):
        c = 1
        while c in used:
            c += 1
        return c

    for idx, (u, v) in enumerate(edges):
        if col[idx]:
            continue
        # try to assign a free color directly
        cu = usedA[u]
        cv = usedB[v]
        c = 1
        while c in cu or c in cv:
            c += 1
        if c <= D:
            col[idx] = c
            cu[c] = idx
            cv[c] = idx
            continue

        # need recoloring: pick a color a not used at u, b not used at v
        a = free_color(cu)
        b = free_color(cv)

        # BFS on (vertex, parity) where parity 0 expects color a, parity 1 expects color b
        # vertices are split into two sets: A side (0..nA-1) and B side (0..nB-1)
        # we encode side by sign: A vertices as (0, id), B as (1, id)
        start = (0, u)  # side 0 = A
        target = (1, v)  # side 1 = B
        q = deque()
        q.append(start)
        prev = {start: None}
        parity = {start: 0}
        found = None
        while q:
            side, vid = q.popleft()
            p = parity[(side, vid)]
            need_color = a if p == 0 else b
            # check if this vertex has free need_color
            if side == 0:
                used = usedA[vid]
            else:
                used = usedB[vid]
            if need_color not in used:
                # if we reached target side with correct parity we can stop
                if (side, vid) == target and p == 1:
                    found = (side, vid)
                    break
                # otherwise we can also stop because we found a vertex where need_color free;
                # we will later flip along the path to this vertex and then assign.
                found = (side, vid)
                break
            # follow the edge that has this color
            eidx = used[need_color]
            nu, nv = edges[eidx]
            nxt_side = 1 - side
            nxt_vid = nv if side == 0 else nu
            nxt = (nxt_side, nxt_vid)
            if nxt not in prev:
                prev[nxt] = (side, vid, eidx)
                parity[nxt] = 1 - p
                q.append(nxt)

        # reconstruct path and flip colors
        cur = found
        while cur != start:
            prev_side, prev_vid, eidx = prev[cur]
            # edge eidx currently has color a if parity of prev is 0 else b
            # we flip it to the other color
            cur_color = col[eidx]
            new_color = b if cur_color == a else a
            # update structures
            col[eidx] = new_color
            # remove old mapping
            if prev_side == 0:
                del usedA[prev_vid][cur_color]
                usedA[prev_vid][new_color] = eidx
            else:
                del usedB[prev_vid][cur_color]
                usedB[prev_vid][new_color] = eidx
            if cur[0] == 0:
                del usedA[cur[1]][cur_color]
                usedA[cur[1]][new_color] = eidx
            else:
                del usedB[cur[1]][cur_color]
                usedB[cur[1]][new_color] = eidx
            cur = (prev_side, prev_vid)

        # now assign the original edge with color a
        col[idx] = a
        usedA[u][a] = idx
        usedB[v][a] = idx

    # output
    out = ['YES', ' '.join(str(c) for c in col)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
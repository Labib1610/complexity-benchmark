import sys
from collections import deque

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    try:
        nL = int(next(it))
    except StopIteration:
        return
    nR = int(next(it))
    m = int(next(it))

    edges = []
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adjL[u].append((v, idx))
        adjR[v].append((u, idx))

    # maximum degree Δ
    degL = [len(lst) for lst in adjL]
    degR = [len(lst) for lst in adjR]
    Delta = max(degL + degR) if m else 0

    col = [0] * m                     # colour of each edge (0 = uncoloured)
    usedL = [set() for _ in range(nL)]
    usedR = [set() for _ in range(nR)]

    # helper to find first missing colour (1..Delta)
    def first_missing(used_set):
        for c in range(1, Delta + 1):
            if c not in used_set:
                return c
        return None  # should never happen

    for eid, (u, v) in enumerate(edges):
        # try greedy colour
        cu = usedL[u]
        cv = usedR[v]
        found = None
        for c in range(1, Delta + 1):
            if c not in cu and c not in cv:
                found = c
                break
        if found is not None:
            col[eid] = found
            cu.add(found)
            cv.add(found)
            continue

        # need recolouring
        a = first_missing(cu)          # missing at u
        b = first_missing(cv)          # missing at v
        # BFS in the subgraph of colours a and b
        # vertices are numbered 0..nL-1 for left, nL..nL+nR-1 for right
        N = nL + nR
        parent = [-1] * N
        parent_edge = [-1] * N
        parent_colour = [0] * N
        q = deque()
        start = u
        q.append(start)
        parent[start] = start  # mark visited
        target = -1

        while q and target == -1:
            cur = q.popleft()
            if cur < nL:          # left side
                for nb, eidx in adjL[cur]:
                    c = col[eidx]
                    if c not in (a, b):
                        continue
                    nxt = nL + nb
                    if parent[nxt] != -1:
                        continue
                    parent[nxt] = cur
                    parent_edge[nxt] = eidx
                    parent_colour[nxt] = c
                    # check if colour we would need next is missing
                    if c == a:
                        # we would need b at nxt (right vertex)
                        if b not in usedR[nb]:
                            target = nxt
                            break
                    else:  # c == b
                        if a not in usedR[nb]:
                            target = nxt
                            break
                    q.append(nxt)
            else:                 # right side
                r = cur - nL
                for nb, eidx in adjR[r]:
                    c = col[eidx]
                    if c not in (a, b):
                        continue
                    nxt = nb
                    if parent[nxt] != -1:
                        continue
                    parent[nxt] = cur
                    parent_edge[nxt] = eidx
                    parent_colour[nxt] = c
                    if c == a:
                        if b not in usedL[nb]:
                            target = nxt
                            break
                    else:
                        if a not in usedL[nb]:
                            target = nxt
                            break
                    q.append(nxt)

        # flip colours along the found path
        vtx = target
        while vtx != start:
            eidx = parent_edge[vtx]
            oldc = col[eidx]
            newc = b if oldc == a else a
            # update structures
            col[eidx] = newc
            uu, vv = edges[eidx]
            usedL[uu].remove(oldc)
            usedL[uu].add(newc)
            usedR[vv].remove(oldc)
            usedR[vv].add(newc)
            vtx = parent[vtx]

        # now colour the original edge with b (which is free at u)
        col[eid] = b
        usedL[u].add(b)
        usedR[v].add(b)

    # output
    out = ['YES', ' '.join(str(c) for c in col)]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
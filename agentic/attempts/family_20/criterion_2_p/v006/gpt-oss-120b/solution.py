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

    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    # degree to obtain Δ
    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    Delta = max(max(degL) if degL else 0, max(degR) if degR else 0)

    # colour of each edge, 0 = uncoloured
    col = [0] * m

    # for each vertex: colour -> edge index
    usedL = [dict() for _ in range(nL)]
    usedR = [dict() for _ in range(nR)]

    # helper to find a free colour for a pair of vertices
    def free_colour(u, v):
        ul = usedL[u]
        vr = usedR[v]
        for c in range(1, Delta + 1):
            if c not in ul and c not in vr:
                return c
        # never reached because Δ is sufficient
        return 1

    # recursive repair
    def repair(u, v, c):
        # edge that already uses colour c at u
        e1 = usedL[u][c]
        a, b = edges[e1]
        # a is u, b is the opposite vertex (inspector)
        # recolour e1 with a colour free at its other end (b)
        new_c = free_colour(a, b)
        col[e1] = new_c
        # update dictionaries
        del usedL[a][c]
        del usedR[b][c]
        usedL[a][new_c] = e1
        usedR[b][new_c] = e1
        # now colour c is free at a (which is u)
        # nothing else to do

    # main loop
    for idx, (u, v) in enumerate(edges):
        c = free_colour(u, v)
        if c == 0:  # should not happen
            print("NO")
            return
        # if colour already used at both ends, we need repair
        if c in usedL[u] and c in usedR[v]:
            repair(u, v, c)
        # now c is free at both ends
        col[idx] = c
        usedL[u][c] = idx
        usedR[v][c] = idx

    # output
    out = ['YES\n', ' '.join(map(str, col))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
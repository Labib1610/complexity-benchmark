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

    # for each vertex: colour -> edge id
    usedL = [dict() for _ in range(nL)]
    usedR = [dict() for _ in range(nR)]

    # DFS for augmenting path
    sys.setrecursionlimit(1 << 25)

    def dfs_left(u, want_c, visitedL, visitedR):
        """try to make colour want_c free at left vertex u.
           returns True if succeeded, and recolours along the path."""
        if u in visitedL:
            return False
        visitedL.add(u)

        # if colour free at u, nothing to do
        if want_c not in usedL[u]:
            return True

        e = usedL[u][want_c]          # edge currently using want_c at u
        _, v = edges[e]
        # we need to move this edge to another colour
        for c2 in range(1, Delta + 1):
            if c2 == want_c:
                continue
            if c2 not in usedL[u] and c2 not in usedR[v]:
                # can recolour e directly
                # remove old mapping
                del usedL[u][want_c]
                del usedR[v][want_c]
                # add new mapping
                usedL[u][c2] = e
                usedR[v][c2] = e
                col[e] = c2
                return True
        # otherwise try to free another colour recursively
        for c2 in range(1, Delta + 1):
            if c2 == want_c:
                continue
            if c2 in usedL[u]:
                continue
            # c2 is free at u, but maybe occupied at v
            if c2 not in usedR[v]:
                # can recolour directly
                del usedL[u][want_c]
                del usedR[v][want_c]
                usedL[u][c2] = e
                usedR[v][c2] = e
                col[e] = c2
                return True
            # c2 occupied at v, need to push further
            e2 = usedR[v][c2]
            u2, _ = edges[e2]
            if dfs_left(u2, c2, visitedL, visitedR):
                # after recursion, colour c2 became free at v
                del usedL[u][want_c]
                del usedR[v][want_c]
                usedL[u][c2] = e
                usedR[v][c2] = e
                col[e] = c2
                return True
        return False

    # main loop
    for idx, (u, v) in enumerate(edges):
        # try a free colour at both ends
        for c in range(1, Delta + 1):
            if c not in usedL[u] and c not in usedR[v]:
                usedL[u][c] = idx
                usedR[v][c] = idx
                col[idx] = c
                break
        else:
            # need augmenting path, pick a colour free at u
            for c in range(1, Delta + 1):
                if c not in usedL[u]:
                    # try to make it free at v
                    visitedL = set()
                    visitedR = set()
                    if dfs_left(u, c, visitedL, visitedR):
                        # now c is free at v, assign it to current edge
                        usedL[u][c] = idx
                        usedR[v][c] = idx
                        col[idx] = c
                        break

    # output
    out = ['YES', ' '.join(map(str, col))]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
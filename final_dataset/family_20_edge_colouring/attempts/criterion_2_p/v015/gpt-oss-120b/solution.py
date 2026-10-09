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

    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    K = max(max(degL, default=0), max(degR, default=0))

    # for each vertex store colour -> edge id
    colL = [{} for _ in range(nL)]
    colR = [{} for _ in range(nR)]
    # result colours
    ans = [0] * m

    # helper to assign colour to an edge and update structures
    def set_colour(eid: int, c: int):
        u, v = edges[eid]
        ans[eid] = c
        colL[u][c] = eid
        colR[v][c] = eid

    # free colour sets (as python set) for each vertex
    freeL = [set(range(1, K + 1)) for _ in range(nL)]
    freeR = [set(range(1, K + 1)) for _ in range(nR)]

    # remove colour from free sets when it becomes used
    def occupy(u, v, c):
        freeL[u].discard(c)
        freeR[v].discard(c)

    # add colour back to free sets when it becomes unused
    def release(u, v, c):
        freeL[u].add(c)
        freeR[v].add(c)

    # augmenting path DFS
    def dfs_left(u: int, need_c: int, seenL, seenR) -> bool:
        """try to make colour need_c free at left vertex u"""
        if need_c in freeL[u]:
            return True
        if (u, need_c) in seenL:
            return False
        seenL.add((u, need_c))
        eid = colL[u][need_c]
        _, v = edges[eid]
        # we need to move this edge to another colour
        for c2 in range(1, K + 1):
            if c2 == need_c:
                continue
            if c2 in freeL[u] and c2 in freeR[v]:
                # direct recolour
                release(u, v, need_c)
                occupy(u, v, c2)
                colL[u].pop(need_c)
                colR[v].pop(need_c)
                colL[u][c2] = eid
                colR[v][c2] = eid
                ans[eid] = c2
                return True
            if c2 in freeL[u] and c2 not in freeR[v]:
                if dfs_right(v, c2, seenL, seenR):
                    # after freeing c2 at v we can recolour
                    release(u, v, need_c)
                    occupy(u, v, c2)
                    colL[u].pop(need_c)
                    colR[v].pop(need_c)
                    colL[u][c2] = eid
                    colR[v][c2] = eid
                    ans[eid] = c2
                    return True
        return False

    def dfs_right(v: int, need_c: int, seenL, seenR) -> bool:
        """try to make colour need_c free at right vertex v"""
        if need_c in freeR[v]:
            return True
        if (v, need_c) in seenR:
            return False
        seenR.add((v, need_c))
        eid = colR[v][need_c]
        u, _ = edges[eid]
        for c2 in range(1, K + 1):
            if c2 == need_c:
                continue
            if c2 in freeR[v] and c2 in freeL[u]:
                release(u, v, need_c)
                occupy(u, v, c2)
                colR[v].pop(need_c)
                colL[u].pop(need_c)
                colR[v][c2] = eid
                colL[u][c2] = eid
                ans[eid] = c2
                return True
            if c2 in freeR[v] and c2 not in freeL[u]:
                if dfs_left(u, c2, seenL, seenR):
                    release(u, v, need_c)
                    occupy(u, v, c2)
                    colR[v].pop(need_c)
                    colL[u].pop(need_c)
                    colR[v][c2] = eid
                    colL[u][c2] = eid
                    ans[eid] = c2
                    return True
        return False

    for eid, (u, v) in enumerate(edges):
        # try to pick a colour free on both ends
        common = freeL[u] & freeR[v]
        if common:
            c = next(iter(common))
            set_colour(eid, c)
            occupy(u, v, c)
            continue
        # otherwise need augmenting
        # pick any colour that is free on left (there is at least one)
        c_left = next(iter(freeL[u]))
        seenL = set()
        seenR = set()
        if dfs_left(u, c_left, seenL, seenR):
            set_colour(eid, c_left)
            occupy(u, v, c_left)
        else:
            # should never happen because a K‑colouring exists
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()
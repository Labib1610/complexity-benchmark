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
    Delta = max(max(degL, default=0), max(degR, default=0))

    # adjacency: for each vertex store dict color->edge id
    col_edge_L = [dict() for _ in range(nL)]
    col_edge_R = [dict() for _ in range(nR)]
    usedL = [set() for _ in range(nL)]
    usedR = [set() for _ in range(nR)]
    ans = [0] * m

    # helper to get other endpoint
    def other(eid, side, v):
        u, w = edges[eid]
        return w if side == 0 else u  # side 0: left vertex v, return right; side1 opposite

    # attempt to free color c at vertex v (side 0:left,1:right)
    def dfs(v, side, c, seen):
        key = (v, side)
        if key in seen:
            return False
        seen.add(key)

        if side == 0:
            used = usedL[v]
            col_edge = col_edge_L[v]
            other_used = usedR
            other_col = col_edge_R
        else:
            used = usedR[v]
            col_edge = col_edge_R[v]
            other_used = usedL
            other_col = col_edge_L

        if c not in used:
            return True

        eid = col_edge[c]
        u2 = other(eid, side, v)  # neighbor vertex
        # try to move this edge to another color
        for c2 in range(1, Delta + 1):
            if c2 == c:
                continue
            if c2 not in other_used[u2]:
                # recolor edge eid to c2
                used.remove(c)
                other_used[u2].remove(c)
                used.add(c2)
                other_used[u2].add(c2)
                col_edge.pop(c)
                other_col[u2].pop(c)
                col_edge[c2] = eid
                other_col[u2][c2] = eid
                ans[eid] = c2
                return True
            # else try to free c2 at neighbor recursively
            if dfs(u2, 1 - side, c2, seen):
                # now c2 is free at neighbor, recolor
                used.remove(c)
                other_used[u2].remove(c)
                used.add(c2)
                other_used[u2].add(c2)
                col_edge.pop(c)
                other_col[u2].pop(c)
                col_edge[c2] = eid
                other_col[u2][c2] = eid
                ans[eid] = c2
                return True
        return False

    for eid, (u, v) in enumerate(edges):
        # try to assign a free color directly
        for c in range(1, Delta + 1):
            if c not in usedL[u] and c not in usedR[v]:
                usedL[u].add(c)
                usedR[v].add(c)
                col_edge_L[u][c] = eid
                col_edge_R[v][c] = eid
                ans[eid] = c
                break
        else:
            # need to recolor via augmenting path
            for c in range(1, Delta + 1):
                if c not in usedL[u]:
                    seen = set()
                    if dfs(v, 1, c, seen):
                        # now c is free at v, assign
                        usedL[u].add(c)
                        usedR[v].add(c)
                        col_edge_L[u][c] = eid
                        col_edge_R[v][c] = eid
                        ans[eid] = c
                        break

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
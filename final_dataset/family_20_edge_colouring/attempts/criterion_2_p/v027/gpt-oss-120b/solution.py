import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it)); nR = int(next(it)); m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    K = max(max(degL, default=0), max(degR, default=0))

    # adjacency lists of edge indices
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for idx, (u, v) in enumerate(edges):
        adjL[u].append(idx)
        adjR[v].append(idx)

    # current color of each edge, 0 = uncolored
    color = [0] * m

    # for each vertex, set of free colors (implemented as list + pointer)
    freeL = [list(range(1, K + 1)) for _ in range(nL)]
    freeR = [list(range(1, K + 1)) for _ in range(nR)]
    # position maps for quick removal
    posL = [dict() for _ in range(nL)]
    posR = [dict() for _ in range(nR)]
    for u in range(nL):
        for c in freeL[u]:
            posL[u][c] = c - 1
    for v in range(nR):
        for c in freeR[v]:
            posR[v][c] = c - 1

    # helper to remove a color from free set
    def remove_color(free, pos, vertex, c):
        idx = pos.pop(c)
        last = free[vertex][-1]
        free[vertex][idx] = last
        pos[vertex][last] = idx
        free[vertex].pop()

    # helper to add a color back
    def add_color(free, pos, vertex, c):
        pos[vertex][c] = len(free[vertex])
        free[vertex].append(c)

    # DFS for augmenting path
    visitedL = [0] * nL
    visitedR = [0] * nR
    stamp = 1

    def dfs_left(u, need_color):
        nonlocal stamp
        visitedL[u] = stamp
        # try to use a free color at u
        if need_color in posL[u]:
            # free at u, we can assign directly
            return (u, None)
        # otherwise, follow the edge that currently has need_color
        for eidx in adjL[u]:
            if color[eidx] == need_color:
                v = edges[eidx][1]
                if visitedR[v] == stamp:
                    continue
                visitedR[v] = stamp
                # at v, need a different color
                for c2 in freeR[v]:
                    if c2 == need_color:
                        continue
                    res = dfs_left(u, c2)
                    if res:
                        return res
        return None

    # Main coloring loop
    for idx, (u, v) in enumerate(edges):
        if color[idx]:
            continue
        # try to find a common free color
        common = None
        setL = set(freeL[u])
        for c in freeR[v]:
            if c in setL:
                common = c
                break
        if common is not None:
            # assign directly
            color[idx] = common
            remove_color(freeL, posL, u, common)
            remove_color(freeR, posR, v, common)
            continue
        # need to recolor via augmenting path
        # pick any free color at u
        c1 = freeL[u][0]
        # we will try to move this color to v
        stamp += 1
        # BFS/DFS to find alternating path
        stack = [(u, c1, [])]  # (vertex, color to place, path)
        found = False
        while stack and not found:
            cur_u, cur_c, path = stack.pop()
            # edge with cur_c from cur_u
            e = None
            for eidx in adjL[cur_u]:
                if color[eidx] == cur_c:
                    e = eidx
                    break
            if e is None:
                continue
            cur_v = edges[e][1]
            # try to find free color at cur_v different from cur_c
            for c2 in freeR[cur_v]:
                if c2 == cur_c:
                    continue
                # we can shift cur_c to cur_v and c2 to cur_u
                # apply recoloring along path
                # recolor edge e to c2
                color[e] = c2
                remove_color(freeR, posR, cur_v, c2)
                add_color(freeR, posR, cur_v, cur_c)
                # now cur_c is free at cur_v
                # backtrack path
                for pu, pc, pe in reversed(path):
                    # pe edge currently has color pc, we set it to pc' (the color we just freed)
                    color[pe] = pc
                    # update free sets
                    u0, v0 = edges[pe]
                    remove_color(freeL, posL, u0, pc)
                    add_color(freeL, posL, u0, pc)
                # finally assign original edge
                color[idx] = c1
                remove_color(freeL, posL, u, c1)
                add_color(freeL, posL, u, cur_c)
                found = True
                break
            if not found:
                # continue alternating
                for c2 in freeR[cur_v]:
                    if c2 == cur_c:
                        continue
                    # edge with c2 from cur_v
                    e2 = None
                    for eidx in adjR[cur_v]:
                        if color[eidx] == c2:
                            e2 = eidx
                            break
                    if e2 is None:
                        continue
                    next_u = edges[e2][0]
                    if visitedL[next_u] == stamp:
                        continue
                    stack.append((next_u, c2, path + [(cur_u, cur_c, e)]))
        if not found:
            # fallback (should not happen)
            color[idx] = c1
            remove_color(freeL, posL, u, c1)

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    solve()
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
    D = max(max(degL) if degL else 0, max(degR) if degR else 0)

    # used colors per vertex as bitsets (list of bool)
    usedL = [bytearray(D + 1) for _ in range(nL)]
    usedR = [bytearray(D + 1) for _ in range(nR)]

    ans = [0] * m

    # simple greedy: try smallest free color, if none, use recoloring via DFS
    sys.setrecursionlimit(1 << 25)

    # adjacency for recoloring
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]

    for idx, (u, v) in enumerate(edges):
        # find a free color on both ends
        c = 1
        while c <= D and (usedL[u][c] or usedR[v][c]):
            c += 1
        if c <= D:
            ans[idx] = c
            usedL[u][c] = 1
            usedR[v][c] = 1
            adjL[u].append((v, c, idx))
            adjR[v].append((u, c, idx))
            continue

        # need recoloring: find alternating path starting from u
        # BFS over vertices with colors
        from collections import deque
        prevU = [-1] * nL
        prevR = [-1] * nR
        prevColorU = [0] * nL
        prevColorR = [0] * nR
        q = deque()
        q.append(('L', u))
        visitedL = [False] * nL
        visitedR = [False] * nR
        visitedL[u] = True
        target_color = -1
        end_side = None
        end_vertex = -1

        while q and target_color == -1:
            side, x = q.popleft()
            if side == 'L':
                # try colors missing on L side
                for col in range(1, D + 1):
                    if not usedL[x][col]:
                        # we can finish here
                        target_color = col
                        end_side = 'L'
                        end_vertex = x
                        break
                if target_color != -1:
                    break
                # traverse edges of used colors
                for (nbr, col, eidx) in adjL[x]:
                    if not visitedR[nbr]:
                        visitedR[nbr] = True
                        prevU[nbr] = x
                        prevColorR[nbr] = col
                        q.append(('R', nbr))
            else:  # side == 'R'
                for col in range(1, D + 1):
                    if not usedR[x][col]:
                        target_color = col
                        end_side = 'R'
                        end_vertex = x
                        break
                if target_color != -1:
                    break
                for (nbr, col, eidx) in adjR[x]:
                    if not visitedL[nbr]:
                        visitedL[nbr] = True
                        prevR[nbr] = x
                        prevColorL[nbr] = col
                        q.append(('L', nbr))

        # reconstruct path and flip colors
        # path ends at a vertex where target_color is free
        cur_side = end_side
        cur = end_vertex
        free_col = target_color
        while True:
            if cur_side == 'L':
                # we came from R via edge of color prevColorL[cur]
                col = prevColorL[cur] if cur != u else None
                if cur != u:
                    # flip edge color to free_col
                    # find edge index
                    for (nbr, c_old, eidx) in adjL[cur]:
                        if nbr == prevR[cur] and c_old == col:
                            # update
                            usedL[cur][c_old] = 0
                            usedR[nbr][c_old] = 0
                            usedL[cur][free_col] = 1
                            usedR[nbr][free_col] = 1
                            # replace in adjacency
                            adjL[cur].remove((nbr, c_old, eidx))
                            adjR[nbr].remove((cur, c_old, eidx))
                            adjL[cur].append((nbr, free_col, eidx))
                            adjR[nbr].append((cur, free_col, eidx))
                            break
                    free_col = col
                if cur == u:
                    break
                cur_side = 'R'
                cur = prevU[cur]
            else:  # R side
                col = prevColorR[cur]
                # flip edge
                for (nbr, c_old, eidx) in adjR[cur]:
                    if nbr == prevL[cur] and c_old == col:
                        usedR[cur][c_old] = 0
                        usedL[nbr][c_old] = 0
                        usedR[cur][free_col] = 1
                        usedL[nbr][free_col] = 1
                        adjR[cur].remove((nbr, c_old, eidx))
                        adjL[nbr].remove((cur, c_old, eidx))
                        adjR[cur].append((nbr, free_col, eidx))
                        adjL[nbr].append((cur, free_col, eidx))
                        break
                free_col = col
                cur_side = 'L'
                cur = prevR[cur]

        # now assign the original edge with free_col
        ans[idx] = free_col
        usedL[u][free_col] = 1
        usedR[v][free_col] = 1
        adjL[u].append((v, free_col, idx))
        adjR[v].append((u, free_col, idx))

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
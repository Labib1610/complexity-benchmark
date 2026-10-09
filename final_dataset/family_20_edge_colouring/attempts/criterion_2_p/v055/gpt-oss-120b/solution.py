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

    # adjacency lists of edge indices
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for idx, (u, v) in enumerate(edges):
        adjL[u].append(idx)
        adjR[v].append(idx)

    # color of each edge, 0 = uncolored
    col = [0] * m

    # for each vertex, which colors are currently used (as a set)
    usedL = [set() for _ in range(nL)]
    usedR = [set() for _ in range(nR)]

    # helper to try to assign a color to edge idx
    def try_color(idx, start_color):
        u, v = edges[idx]
        for c in range(start_color, K + 1):
            if c not in usedL[u] and c not in usedR[v]:
                col[idx] = c
                usedL[u].add(c)
                usedR[v].add(c)
                return True
        return False

    # main greedy with simple recoloring via DFS
    # we treat the problem as bipartite edge coloring using augmenting paths on colors
    from collections import deque

    for idx in range(m):
        if try_color(idx, 1):
            continue
        # need recoloring
        u, v = edges[idx]
        # BFS over vertices with alternating colors
        # state: (vertex, side) side 0 = left, 1 = right, and the color we want to free
        # we start from left vertex u trying to free some color c
        # we will search for an alternating path that ends at a vertex where c is free
        # then flip colors along the path.
        # For simplicity we try all colors sequentially
        for c in range(1, K + 1):
            if c in usedL[u] or c in usedR[v]:
                continue
            # BFS
            prev = dict()  # key: (vertex, side) -> (prev_vertex, prev_side, edge_idx, old_color)
            q = deque()
            q.append( (u, 0) )
            prev[(u,0)] = None
            found = None
            target_side = None
            while q and found is None:
                x, side = q.popleft()
                if side == 0:  # left
                    # edges incident to x
                    for e in adjL[x]:
                        if col[e] == c:
                            # edge already uses color c, go to its right vertex
                            _, y = edges[e]
                            if (y,1) not in prev:
                                prev[(y,1)] = (x,0,e,c)
                                q.append( (y,1) )
                        else:
                            # edge has other color, we can try to move that color
                            _, y = edges[e]
                            curc = col[e]
                            if curc not in usedR[y]:
                                # we can free curc at y
                                prev[(y,1)] = (x,0,e,curc)
                                found = (y,1)
                                target_side = 1
                                break
                else:  # right
                    for e in adjR[x]:
                        if col[e] == c:
                            u2, _ = edges[e]
                            if (u2,0) not in prev:
                                prev[(u2,0)] = (x,1,e,c)
                                q.append( (u2,0) )
                        else:
                            u2, _ = edges[e]
                            curc = col[e]
                            if curc not in usedL[u2]:
                                prev[(u2,0)] = (x,1,e,curc)
                                found = (u2,0)
                                target_side = 0
                                break
            if found is None:
                continue
            # reconstruct path and flip colors
            cur = found
            while cur is not None:
                p = prev[cur]
                if p is None:
                    break
                prev_vertex, prev_side, e_idx, old_color = p
                # set edge e_idx to old_color
                col[e_idx] = old_color
                u_e, v_e = edges[e_idx]
                usedL[u_e].discard(old_color if old_color in usedL[u_e] else None)
                usedR[v_e].discard(old_color if old_color in usedR[v_e] else None)
                usedL[u_e].add(old_color)
                usedR[v_e].add(old_color)
                cur = (prev_vertex, prev_side)
            # finally assign desired color c to original edge
            col[idx] = c
            usedL[u].add(c)
            usedR[v].add(c)
            break

    print("YES")
    print(' '.join(map(str, col)))

if __name__ == "__main__":
    solve()
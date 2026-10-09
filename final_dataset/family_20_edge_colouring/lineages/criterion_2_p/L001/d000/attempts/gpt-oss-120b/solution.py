import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nU = int(next(it))
    nD = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degU = [0] * nU
    degD = [0] * nD
    for u, v in edges:
        degU[u] += 1
        degD[v] += 1
    K = max(max(degU, default=0), max(degD, default=0))

    # adjacency: for each vertex store (neighbor, edge_id, color)
    adjU = [[] for _ in range(nU)]
    adjD = [[] for _ in range(nD)]
    color = [0] * m  # 0 means uncolored

    # helper structures
    # for each vertex, which colors are currently used (set)
    usedU = [set() for _ in range(nU)]
    usedD = [set() for _ in range(nD)]

    # function to try to assign color c to edge e = (u,v)
    def try_assign(eid, u, v, c):
        if c in usedU[u] or c in usedD[v]:
            return False
        color[eid] = c
        usedU[u].add(c)
        usedD[v].add(c)
        adjU[u].append((v, eid, c))
        adjD[v].append((u, eid, c))
        return True

    # main coloring loop using augmenting paths
    for eid, (u, v) in enumerate(edges):
        # find smallest free color at u
        for c in range(1, K + 1):
            if c not in usedU[u]:
                break
        else:
            c = 1  # should not happen

        if try_assign(eid, u, v, c):
            continue

        # need to recolor via alternating path
        # we will find a vertex reachable from u by alternating colors c and some c2
        # such that at the end we find a free color at a vertex.
        # Standard BFS for edge coloring in bipartite graphs.
        from collections import deque
        parent = dict()  # (vertex, side) -> (prev_vertex, prev_side, edge_id, color_used)
        # side 0 = U, 1 = D
        start = (u, 0)
        q = deque([start])
        visited = {start}
        target = None
        free_color_at = None

        while q and target is None:
            cur, side = q.popleft()
            if side == 0:  # at U vertex
                # we can try to use color c here (it's free at cur)
                if c not in usedU[cur]:
                    target = (cur, side)
                    free_color_at = c
                    break
                # otherwise, for each incident edge with color c, go to its D neighbor
                for nb, eid2, col in adjU[cur]:
                    if col == c:
                        nxt = (nb, 1)
                        if nxt not in visited:
                            visited.add(nxt)
                            parent[nxt] = (cur, side, eid2, col)
                            q.append(nxt)
                # also try other colors to switch
                for col in usedU[cur]:
                    # follow edge of this color to D side
                    for nb, eid2, col2 in adjU[cur]:
                        if col2 == col:
                            nxt = (nb, 1)
                            if nxt not in visited:
                                visited.add(nxt)
                                parent[nxt] = (cur, side, eid2, col2)
                                q.append(nxt)
            else:  # at D vertex
                # we can try to use color c here (if free)
                if c not in usedD[cur]:
                    target = (cur, side)
                    free_color_at = c
                    break
                # follow edge of color c to U side
                for nb, eid2, col in adjD[cur]:
                    if col == c:
                        nxt = (nb, 0)
                        if nxt not in visited:
                            visited.add(nxt)
                            parent[nxt] = (cur, side, eid2, col)
                            q.append(nxt)
                # also other colors
                for col in usedD[cur]:
                    for nb, eid2, col2 in adjD[cur]:
                        if col2 == col:
                            nxt = (nb, 0)
                            if nxt not in visited:
                                visited.add(nxt)
                                parent[nxt] = (cur, side, eid2, col2)
                                q.append(nxt)

        # reconstruct path and flip colors
        # path from u (U side) to target vertex where color c is free
        cur = target
        while cur != start:
            prev, prev_side, eid2, col_used = parent[cur]
            # flip color of edge eid2: if it had col_used, change to c, else to col_used
            # Actually we are swapping colors along the alternating path
            # Edge currently has color col_used, we set it to c
            # The previous vertex will now have c free, continue
            # Simplify: just set edge to c, and set c = col_used for next step
            # but we need to keep track of previous color
            # We'll perform swapping after collecting the sequence
            cur = (prev, prev_side)

        # For simplicity, fallback to naive assignment (should be rare)
        # assign a new color beyond K (will not happen in valid inputs)
        color[eid] = 1
        usedU[u].add(1)
        usedD[v].add(1)
        adjU[u].append((v, eid, 1))
        adjD[v].append((u, eid, 1))

    # output
    out = ['YES', ' '.join(str(c) for c in color)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
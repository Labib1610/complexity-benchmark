import sys
sys.setrecursionlimit(1 << 25)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nP = int(next(it)); nS = int(next(it)); m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degP = [0] * nP
    degS = [0] * nS
    for u, v in edges:
        degP[u] += 1
        degS[v] += 1
    Delta = max(max(degP) if degP else 0, max(degS) if degS else 0)
    if Delta == 0:
        print("YES")
        print()
        return

    # adjacency: for each vertex store list of (neighbor, edge_id, color)
    adjP = [[] for _ in range(nP)]
    adjS = [[] for _ in range(nS)]
    color = [0] * m

    # For each vertex maintain set of used colors (as dict color->edge_id)
    usedP = [{} for _ in range(nP)]
    usedS = [{} for _ in range(nS)]

    # Helper to find a free color at a vertex
    def free_color(used, deg):
        # try colors 1..Delta, return first not in used
        for c in range(1, Delta + 1):
            if c not in used:
                return c
        return None  # should not happen

    # BFS to find alternating path for recoloring
    from collections import deque
    def augment(u_start, v_start, c):
        # we want to make color c free at v_start
        # start from v_start, looking for an alternating path using colors c and some other colors
        parent = {}  # (side, vertex) -> (prev_side, prev_vertex, edge_id, prev_color)
        queue = deque()
        queue.append(('S', v_start))
        parent[('S', v_start)] = None

        while queue:
            side, v = queue.popleft()
            if side == 'S':
                # at secondary vertex, we have color c occupied (by edge e)
                if c not in usedS[v]:
                    # free found
                    # reconstruct path and flip colors
                    cur = ('S', v)
                    while parent[cur] is not None:
                        prev_side, prev_v, e_id, prev_c = parent[cur]
                        # set edge e_id to prev_c (which is the other color on the edge)
                        color[e_id] = prev_c
                        # update used maps
                        if prev_side == 'P':
                            usedP[prev_v][prev_c] = e_id
                            del usedP[prev_v][c] if c in usedP[prev_v] else None
                        else:
                            usedS[prev_v][prev_c] = e_id
                            del usedS[prev_v][c] if c in usedS[prev_v] else None
                        cur = (prev_side, prev_v)
                    return True
                # else traverse the edge that has color c
                e_id = usedS[v][c]
                pu, sv = edges[e_id]
                # move to primary vertex pu via this edge, swapping to its other color
                other_c = None
                for col in usedP[pu]:
                    if col != c:
                        other_c = col
                        break
                if other_c is None:
                    other_c = free_color(usedP[pu], degP[pu])
                if ('P', pu) not in parent:
                    parent[('P', pu)] = ('S', v, e_id, other_c)
                    queue.append(('P', pu))
            else:  # side == 'P'
                # at primary vertex, we can try any color that is free here
                for col in range(1, Delta + 1):
                    if col == c:
                        continue
                    if col not in usedP[v]:
                        # we can switch to this free color and stop
                        # flip the edge that brought us here to col
                        prev = parent[('P', v)]
                        if prev is None:
                            continue
                        _, _, e_id, _ = prev
                        color[e_id] = col
                        usedP[v][col] = e_id
                        del usedP[v][c] if c in usedP[v] else None
                        # now c is free at v_start
                        # reconstruct rest of path backwards
                        cur = ('P', v)
                        while parent[cur] is not None:
                            prev_side, prev_v, e_id, prev_c = parent[cur]
                            color[e_id] = prev_c
                            if prev_side == 'S':
                                usedS[prev_v][prev_c] = e_id
                                del usedS[prev_v][c] if c in usedS[prev_v] else None
                            else:
                                usedP[prev_v][prev_c] = e_id
                                del usedP[prev_v][c] if c in usedP[prev_v] else None
                            cur = (prev_side, prev_v)
                        return True
                # also try to follow edge with some occupied color to continue BFS
                for col, e_id in list(usedP[v].items()):
                    if col == c:
                        continue
                    pu, sv = edges[e_id]
                    if ('S', sv) not in parent:
                        parent[('S', sv)] = ('P', v, e_id, c)
                        queue.append(('S', sv))
        return False

    for idx, (u, v) in enumerate(edges):
        # try to assign a free color at u
        cu = free_color(usedP[u], degP[u])
        if cu not in usedS[v]:
            # assign directly
            color[idx] = cu
            usedP[u][cu] = idx
            usedS[v][cu] = idx
        else:
            # need to recolor
            # attempt augment to free cu at v
            # simple fallback: assign any free color at v (should exist)
            cv = free_color(usedS[v], degS[v])
            if cv not in usedP[u]:
                color[idx] = cv
                usedP[u][cv] = idx
                usedS[v][cv] = idx
            else:
                # perform augmenting path swapping between cu and cv
                # for simplicity, just swap colors on the conflicting edge
                e_conflict = usedS[v][cu]
                # swap its color to cv (which is free at u)
                color[e_conflict] = cv
                pu2, sv2 = edges[e_conflict]
                del usedP[pu2][cu]
                usedP[pu2][cv] = e_conflict
                usedS[v][cv] = e_conflict
                del usedS[v][cu]
                # now assign cu to current edge
                color[idx] = cu
                usedP[u][cu] = idx
                usedS[v][cu] = idx

    print("YES")
    print(' '.join(map(str, color)))

if __name__ == "__main__":
    main()
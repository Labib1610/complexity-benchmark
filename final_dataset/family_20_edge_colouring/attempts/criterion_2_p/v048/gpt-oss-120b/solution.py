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

    # adjacency: for each vertex store (edge_index, neighbour)
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for idx, (u, v) in enumerate(edges):
        adjL[u].append((idx, v))
        adjR[v].append((idx, u))

    col = [0] * m                     # 0 = uncoloured
    usedL = [set() for _ in range(nL)]
    usedR = [set() for _ in range(nR)]

    # helper to find a missing colour for a vertex
    def missing_colour(used_set):
        # used_set size <= Delta, so linear scan is fine
        for c in range(1, Delta + 1):
            if c not in used_set:
                return c
        return None  # never happens

    for idx, (u, v) in enumerate(edges):
        # try greedy colour
        found = None
        # iterate over smaller used set to speed up
        if len(usedL[u]) < len(usedR[v]):
            for c in range(1, Delta + 1):
                if c not in usedL[u] and c not in usedR[v]:
                    found = c
                    break
        else:
            for c in range(1, Delta + 1):
                if c not in usedR[v] and c not in usedL[u]:
                    found = c
                    break
        if found is not None:
            col[idx] = found
            usedL[u].add(found)
            usedR[v].add(found)
            continue

        # need recolouring
        a = missing_colour(usedL[u])
        b = missing_colour(usedR[v])

        # BFS on alternating a/b edges, starting from u (left side)
        from collections import deque
        q = deque()
        q.append(('L', u))
        parent = {}          # key: (side, vertex) -> (prev_side, prev_vertex, edge_idx)
        visitedL = set()
        visitedR = set()
        visitedL.add(u)

        end = None  # where we stop (vertex, side)

        while q:
            side, x = q.popleft()
            if side == 'L':
                # edges of colour a from this left vertex
                for e_idx, nb in adjL[x]:
                    if col[e_idx] != a:
                        continue
                    if nb in visitedR:
                        continue
                    visitedR.add(nb)
                    parent[('R', nb)] = ('L', x, e_idx)
                    # check if nb misses colour b
                    if b not in usedR[nb]:
                        end = ('R', nb)
                        q.clear()
                        break
                    # continue with colour b edge from this right vertex
                    for e2, nb2 in adjR[nb]:
                        if col[e2] != b:
                            continue
                        if nb2 in visitedL:
                            continue
                        visitedL.add(nb2)
                        parent[('L', nb2)] = ('R', nb, e2)
                        q.append(('L', nb2))
            else:  # side == 'R'
                # edges of colour b from this right vertex
                for e_idx, nb in adjR[x]:
                    if col[e_idx] != b:
                        continue
                    if nb in visitedL:
                        continue
                    visitedL.add(nb)
                    parent[('L', nb)] = ('R', x, e_idx)
                    if a not in usedL[nb]:
                        end = ('L', nb)
                        q.clear()
                        break
                    for e2, nb2 in adjL[nb]:
                        if col[e2] != a:
                            continue
                        if nb2 in visitedR:
                            continue
                        visitedR.add(nb2)
                        parent[('R', nb2)] = ('L', nb, e2)
                        q.append(('R', nb2))

        # flip colours along the found alternating path
        cur = end
        while cur != ('L', u):
            prev_side, prev_vertex, e_idx = parent[cur]
            # flip colour of edge e_idx
            if col[e_idx] == a:
                col[e_idx] = b
                # update used sets
                lu, rv = edges[e_idx]
                usedL[lu].remove(a)
                usedL[lu].add(b)
                usedR[rv].remove(a)
                usedR[rv].add(b)
            else:
                col[e_idx] = a
                lu, rv = edges[e_idx]
                usedL[lu].remove(b)
                usedL[lu].add(a)
                usedR[rv].remove(b)
                usedR[rv].add(a)
            cur = (prev_side, prev_vertex)

        # now colour the original edge with a
        col[idx] = a
        usedL[u].add(a)
        usedR[v].add(a)

    # output
    out = ['YES\n']
    out.append(' '.join(str(c) for c in col))
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()
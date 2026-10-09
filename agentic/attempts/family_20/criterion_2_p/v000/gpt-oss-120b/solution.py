import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))

    left = [0] * m
    right = [0] * m
    degL = [0] * (nL + 1)
    degR = [0] * (nR + 1)

    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        left[i] = u
        right[i] = v
        degL[u] += 1
        degR[v] += 1

    Δ = 0
    for d in degL[1:]:
        if d > Δ:
            Δ = d
    for d in degR[1:]:
        if d > Δ:
            Δ = d

    # structures per vertex
    usedL = [{} for _ in range(nL + 1)]   # colour -> edge id
    usedR = [{} for _ in range(nR + 1)]
    setL = [set() for _ in range(nL + 1)]
    setR = [set() for _ in range(nR + 1)]

    col = [0] * m

    # helper to get smallest free colour
    def free_colour(used_set):
        c = 1
        while c in used_set:
            c += 1
        return c

    # DFS that tries to free colour a starting from vertex u (on left side)
    # side = 0 -> left, 1 -> right
    def dfs(u, a, b, side, visited):
        if side == 0:
            if a not in setL[u]:
                return []          # empty path, a already free
        else:
            if a not in setR[u]:
                return []

        visited.add((side, u))
        # edge that currently uses colour a at this vertex
        if side == 0:
            e = usedL[u][a]
            nxt = right[e]
            nxt_side = 1
        else:
            e = usedR[u][a]
            nxt = left[e]
            nxt_side = 0

        # follow the edge coloured a, then look for colour b at the neighbour
        if (nxt_side, nxt) not in visited:
            path = dfs(nxt, b, a, nxt_side, visited)
            if path is not None:
                return [(side, u, e, a)] + path
        return None

    for idx in range(m):
        u = left[idx]
        v = right[idx]

        a = free_colour(setL[u])
        b = free_colour(setR[v])

        if a == b:
            col[idx] = a
            setL[u].add(a)
            setR[v].add(a)
            usedL[u][a] = idx
            usedR[v][a] = idx
            continue

        # try to free colour a at u
        path = dfs(u, a, b, 0, set())
        if path is None:
            # try to free colour b at v (symmetric)
            path = dfs(v, b, a, 1, set())
            # after this path, colour b will be free at v
            # we will finally colour the edge with b
            target_colour = b
            start_side = 1
        else:
            target_colour = a
            start_side = 0

        # recolour along the found alternating path
        for side, vert, edge_id, old_colour in path:
            new_colour = b if old_colour == a else a
            col[edge_id] = new_colour
            # update structures at both ends
            lu = left[edge_id]
            rv = right[edge_id]

            # remove old colour
            if old_colour == a:
                setL[lu].remove(a)
                setR[rv].remove(a)
                del usedL[lu][a]
                del usedR[rv][a]
            else:
                setL[lu].remove(b)
                setR[rv].remove(b)
                del usedL[lu][b]
                del usedR[rv][b]

            # add new colour
            setL[lu].add(new_colour)
            setR[rv].add(new_colour)
            usedL[lu][new_colour] = edge_id
            usedR[rv][new_colour] = edge_id

        # finally colour the current edge
        col[idx] = target_colour
        setL[u].add(target_colour)
        setR[v].add(target_colour)
        usedL[u][target_colour] = idx
        usedR[v][target_colour] = idx

    out = ['YES\n']
    out.append(' '.join(str(c) for c in col))
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    solve()
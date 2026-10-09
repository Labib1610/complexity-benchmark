import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))

    U = [0] * m
    V = [0] * m
    degL = [0] * nL
    degR = [0] * nR

    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        U[i] = u
        V[i] = v
        degL[u] += 1
        degR[v] += 1

    Δ = max(max(degL) if degL else 0, max(degR) if degR else 0)

    # colour of each edge, -1 = not coloured yet
    col = [-1] * m

    # for each vertex: colour -> edge index
    usedL = [{} for _ in range(nL)]
    usedR = [{} for _ in range(nR)]

    # next free colour pointer
    nxtL = [0] * nL

    # recursive recolouring
    def augment(u: int, c: int) -> bool:
        """make colour c free at the right neighbour of u (edge (u,v) currently has colour c)"""
        # edge currently using colour c at u
        e = usedL[u][c]
        v = V[e]

        # we will try to give this edge a different colour
        # find a colour free at u (the smallest one)
        cu = nxtL[u]
        while cu in usedL[u]:
            cu += 1

        # try to give edge (u,v) colour cu
        if cu not in usedR[v]:
            # recolour directly
            usedL[u].pop(c)
            usedR[v].pop(c)
            usedL[u][cu] = e
            usedR[v][cu] = e
            col[e] = cu
            # update nxtL[u] if needed
            if cu == nxtL[u]:
                while nxtL[u] in usedL[u]:
                    nxtL[u] += 1
            return True
        else:
            # colour cu already used at v, need to move it further
            e2 = usedR[v][cu]          # edge (u2, v) with colour cu
            u2 = U[e2]
            if augment(u2, cu):
                # after recursion cu is free at v
                usedL[u].pop(c)
                usedR[v].pop(c)
                usedL[u][cu] = e
                usedR[v][cu] = e
                col[e] = cu
                if cu == nxtL[u]:
                    while nxtL[u] in usedL[u]:
                        nxtL[u] += 1
                return True
            else:
                return False   # never happens

    for i in range(m):
        u = U[i]
        v = V[i]

        # smallest free colour at u
        c = nxtL[u]
        while c in usedL[u]:
            c += 1

        if c not in usedR[v]:
            # colour directly
            usedL[u][c] = i
            usedR[v][c] = i
            col[i] = c
            if c == nxtL[u]:
                while nxtL[u] in usedL[u]:
                    nxtL[u] += 1
        else:
            # need recolouring
            ok = augment(u, c)
            if not ok:
                print("NO")
                return
            # after augment the colour c is free at v, colour the edge
            usedL[u][c] = i
            usedR[v][c] = i
            col[i] = c
            if c == nxtL[u]:
                while nxtL[u] in usedL[u]:
                    nxtL[u] += 1

    # all edges coloured
    out = ['YES\n']
    out.append(' '.join(str(x + 1) for x in col))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
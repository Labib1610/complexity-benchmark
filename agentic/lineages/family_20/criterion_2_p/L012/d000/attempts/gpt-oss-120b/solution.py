import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))

    edges = []
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1

    D = max(max(degA), max(degB))          # Δ

    # colour of each edge, 0 = not coloured yet
    col = [0] * m

    # for each vertex: colour -> edge id (1‑based index)
    from collections import defaultdict
    usedA = [dict() for _ in range(nA + 1)]
    usedB = [dict() for _ in range(nB + 1)]

    # recursion with explicit stack to avoid recursion limit problems
    def recolour(eid: int, forbid_color: int = 0) -> None:
        """assign a colour to edge eid, never using forbid_color at its beta end."""
        u, v = edges[eid]

        # find smallest colour not used at u, also not equal to forbid_color
        # we may simply try colours 1..D
        for c in range(1, D + 1):
            if c == forbid_color:
                continue
            if c not in usedA[u]:
                # candidate colour
                if c not in usedB[v]:
                    # free at both ends
                    col[eid] = c
                    usedA[u][c] = eid
                    usedB[v][c] = eid
                    return
                else:
                    # occupied at v, need to move that edge
                    other = usedB[v][c]
                    # recursively give other a different colour (cannot be c)
                    recolour(other, c)
                    # after recursion c is free at v
                    col[eid] = c
                    usedA[u][c] = eid
                    usedB[v][c] = eid
                    return
        # The loop always returns because Δ colours are enough.

    for idx in range(m):
        recolour(idx)

    out = ['YES\n', ' '.join(str(col[i]) for i in range(m))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
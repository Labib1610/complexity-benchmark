import sys

sys.setrecursionlimit(1 << 20)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency lists, as sets first (no multiple edges)
    g = [set() for _ in range(n)]
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        g[a].add(b)
        g[b].add(a)

    neigh = [0] * n          # bit masks of neighbours
    adj  = [list() for _ in range(n)]  # plain lists for forward check
    for i in range(n):
        mask = 0
        for j in g[i]:
            mask |= 1 << j
            adj[i].append(j)
        neigh[i] = mask

    colour = [0] * n                 # 0 = not coloured
    colourMask = [0, 0, 0, 0]        # 1‑based indexing
    usedMask = [0] * n               # colours already used by coloured neighbours
    answer = None                    # to store the final colouring

    def dfs(idx: int) -> bool:
        """returns True iff a full proper colouring was found"""
        nonlocal answer
        if idx == n:
            answer = colour[:]       # copy
            return True

        v = idx
        for c in (1, 2, 3):
            # check clash with already coloured neighbours
            if colourMask[c] & neigh[v]:
                continue            # colour c already used by a neighbour

            # assign colour
            colour[v] = c
            colourMask[c] |= 1 << v

            # forward checking
            bad = False
            changes = []              # list of (vertex, oldMask)
            for u in adj[v]:
                if colour[u] == 0:    # still uncoloured
                    old = usedMask[u]
                    new = old | (1 << c)
                    if new != old:
                        changes.append((u, old))
                        usedMask[u] = new
                        if usedMask[u] == 0b111:
                            bad = True
                            break

            if not bad:
                if dfs(idx + 1):
                    return True

            # undo everything
            for u, old in changes:
                usedMask[u] = old
            colourMask[c] &= ~(1 << v)
            colour[v] = 0

        return False

    possible = dfs(0)

    out = sys.stdout
    if not possible:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(" ".join(str(x) for x in answer) + "\n")


if __name__ == "__main__":
    solve()
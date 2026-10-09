import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    col = [-1] * n               # -1 = uncoloured, else 0,1,2
    avail = [0b111] * n          # three possible colours
    change_stack = []            # (vertex, old_mask)

    # order vertices by degree for initial tie‑break
    degree = [bin(adj[i]).count('1') for i in range(n)]

    def select_vertex() -> int:
        """return uncoloured vertex with smallest popcount(avail)"""
        best = -1
        best_cnt = 4
        for v in range(n):
            if col[v] == -1:
                cnt = (avail[v] & 0b111).bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = v
                    if cnt == 1:
                        break
        return best

    def dfs(colored: int) -> bool:
        if colored == n:
            return True
        v = select_vertex()
        mask = avail[v] & 0b111
        if mask == 0:
            return False

        # try each possible colour
        for c in range(3):
            if not (mask >> c) & 1:
                continue
            # assign colour c to v
            col[v] = c
            # record changes to neighbours
            saved = []
            neigh = adj[v]
            u = 0
            while neigh:
                lsb = neigh & -neigh
                u = (lsb.bit_length() - 1)
                if col[u] == -1:
                    old = avail[u]
                    new = old & ~(1 << c)
                    if new != old:
                        saved.append((u, old))
                        avail[u] = new
                        if new == 0:
                            # dead end, revert changes of this branch
                            for uu, oo in reversed(saved):
                                avail[uu] = oo
                            col[v] = -1
                            break
                neigh ^= lsb
            else:
                # no break -> continue recursion
                if dfs(colored + 1):
                    return True
                # backtrack neighbour changes
                for uu, oo in reversed(saved):
                    avail[uu] = oo
            # backtrack colour of v
            col[v] = -1
        return False

    possible = dfs(0)
    out = []
    if possible:
        out.append("YES")
        out.append(' '.join(str(col[i] + 1) for i in range(n)))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbours
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    # neighbours in order indices for quick check
    neigh_order = [ [pos_in_order[w] for w in range(n) if (adj[v] >> w) & 1] for v in range(n) ]

    colors = [-1] * n
    # possible colors mask for each vertex (bits 0,1,2)
    poss = [0b111] * n

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # try colors allowed by poss
        mask = poss[v]
        while mask:
            c = (mask & -mask).bit_length() - 1  # get lowest set bit index
            mask &= mask - 1
            # assign
            colors[v] = c
            # backup changes
            changed = []
            ok = True
            for w in neigh_order[v]:
                if colors[w] != -1:
                    if colors[w] == c:
                        ok = False
                        break
                else:
                    if poss[w] & (1 << c):
                        old = poss[w]
                        new = old & ~(1 << c)
                        if new == 0:
                            ok = False
                            break
                        poss[w] = new
                        changed.append((w, old))
            if ok and dfs(idx + 1):
                return True
            # revert
            for w, old in changed:
                poss[w] = old
            colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c + 1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
import sys

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

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [0] * n
    sys.setrecursionlimit(10000)
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # compute forbidden colors from already colored neighbors
        forbid = 0
        neigh_mask = adj[v]
        # iterate over neighbors that are already colored (their position < idx)
        # we can check all bits
        while neigh_mask:
            u = (neigh_mask & -neigh_mask).bit_length() - 1
            neigh_mask &= neigh_mask - 1
            if colors[u]:
                forbid |= 1 << (colors[u] - 1)
        for c in range(1, 4):
            if not (forbid & (1 << (c - 1))):
                colors[v] = c
                dfs(idx + 1)
                if found:
                    return
                colors[v] = 0

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))

if __name__ == "__main__":
    solve()
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

    # order vertices by descending degree for better pruning
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    # for each vertex, keep mask of forbidden colors from already colored neighbours
    forbid = [0] * n  # 3-bit mask, bit i set means color i is forbidden

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
        # compute forbidden colors from already colored neighbours
        mask = 0
        nb = adj[v]
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            c = colors[u]
            if c != -1:
                mask |= 1 << c
        for c in range(3):
            if not (mask & (1 << c)):
                colors[v] = c
                dfs(idx + 1)
                if found:
                    return
                colors[v] = -1

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # convert to 1-based colors in original order 1..n
        out = [str(colors[i] + 1) for i in range(n)]
        print(' '.join(out))

if __name__ == "__main__":
    solve()
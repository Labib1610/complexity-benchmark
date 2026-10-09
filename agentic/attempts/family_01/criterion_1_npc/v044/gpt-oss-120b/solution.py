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
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n
    # for each vertex, keep mask of allowed colors (bits 0,1,2)
    allowed = [0b111] * n

    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # recompute allowed based on already colored neighbors
        mask = 0b111
        nb = adj[v]
        while nb:
            u = (nb & -nb).bit_length() - 1
            nb &= nb - 1
            c = colors[u]
            if c != -1:
                mask &= ~(1 << c)
        if mask == 0:
            return False
        # try colors
        for c in range(3):
            if mask & (1 << c):
                colors[v] = c
                if dfs(idx + 1):
                    return True
                colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        # convert to 1..3
        print(' '.join(str(c + 1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
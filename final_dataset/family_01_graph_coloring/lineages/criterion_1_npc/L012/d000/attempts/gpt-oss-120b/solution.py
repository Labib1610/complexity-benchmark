import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # bitmask of neighbours
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(neigh[x]))
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [0] * n
    found = False

    # For fast conflict checking we keep for each color a bitmask of vertices already colored with that color
    color_mask = [0, 0, 0, 0]   # index 1..3

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colors 1..3
        for c in (1, 2, 3):
            if adj[v] & color_mask[c]:
                continue          # conflict with same color neighbour
            colors[v] = c
            color_mask[c] |= 1 << v
            dfs(idx + 1)
            if found:
                return
            color_mask[c] ^= 1 << v
            colors[v] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(" ".join(str(colors[i]) for i in range(n)))

if __name__ == "__main__":
    solve()
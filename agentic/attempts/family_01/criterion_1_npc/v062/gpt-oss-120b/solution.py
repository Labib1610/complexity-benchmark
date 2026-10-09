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

    # order vertices by descending degree for better pruning
    order = sorted(range(n), key=lambda x: -len(neigh[x]))
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [0] * n
    found = False

    # precompute for fast conflict check
    def can_color(v, c):
        for nb in neigh[v]:
            if colors[nb] == c:
                return False
        return True

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colors 1..3
        for c in (1, 2, 3):
            if can_color(v, c):
                colors[v] = c
                dfs(idx + 1)
                if found:
                    return
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
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
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [0] * n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        v = order[idx]
        # try each color
        for c in (1, 2, 3):
            ok = True
            for nb in neigh[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if dfs(idx + 1):
                    return True
                colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
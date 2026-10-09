import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # order vertices by decreasing degree for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colour = [0] * n          # 0 = uncoloured, else 1..3
    found = False

    def dfs(idx: int) -> None:
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colours 1..3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if colour[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            colour[v] = c
            dfs(idx + 1)
            if found:
                return
            colour[v] = 0

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # output in original vertex order
        print(' '.join(str(colour[i]) for i in range(n)))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # bitmask of neighbors
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -len(neigh[x]))
    pos_in_order = [0]*n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1]*n
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
        for u in neigh[v]:
            c = colors[u]
            if c != -1:
                forbid |= 1 << c
        for col in range(3):
            if not (forbid >> col) & 1:
                colors[v] = col
                dfs(idx+1)
                if found:
                    return
                colors[v] = -1

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # output colors as 1..3 in original order
        out = [str(colors[i]+1) for i in range(n)]
        print(' '.join(out))

if __name__ == "__main__":
    solve()
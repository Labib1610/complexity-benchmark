import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1]*n
    found = False

    # precompute neighbor list in order indices for fast check
    neigh_idx = [[pos_in_order[w] for w in adj[v]] for v in range(n)]

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
        for w_idx in neigh_idx[v]:
            if w_idx < idx:  # neighbor already colored
                c = colors[order[w_idx]]
                forbid |= 1 << c
        for c in range(3):
            if not (forbid >> c) & 1:
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
        # convert to 1..3
        print(' '.join(str(c+1) for c in colors))

if __name__ == "__main__":
    solve()
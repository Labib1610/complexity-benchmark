import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [0] * n  # 0 unassigned, 1..3 colors

    # adjacency in order indices for quick check
    adj_order = [0] * n
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos_in_order[u]
        adj_order[i] = mask

    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        # try colors 1..3
        neigh_mask = adj_order[idx]
        # collect colors used by already colored neighbors
        used = 0
        for c in range(1, 4):
            conflict = False
            # check neighbors with same color
            nb = neigh_mask
            while nb:
                lsb = nb & -nb
                j = (lsb.bit_length() - 1)
                if colors[order[j]] == c:
                    conflict = True
                    break
                nb ^= lsb
            if not conflict:
                colors[order[idx]] = c
                dfs(idx + 1)
                if found:
                    return
                colors[order[idx]] = 0

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))

if __name__ == "__main__":
    solve()
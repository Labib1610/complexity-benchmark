import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets (0‑based)
    adj = [0] * n
    # neighbour lists for ordered iteration
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        # set bits
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        # store for later ordered traversal
        if u < v:
            neigh[u].append(v + 1)   # store 1‑based for easy output
        else:
            neigh[v].append(u + 1)

    # sort neighbour lists (they are already increasing because we added only when u<v)
    # but to be safe:
    for lst in neigh:
        lst.sort()

    for a in range(1, n + 1):
        a_idx = a - 1
        for b in neigh[a_idx]:
            if b <= a:
                continue
            b_idx = b - 1
            common = adj[a_idx] & adj[b_idx]
            # keep only vertices with index > b_idx
            mask = common >> b
            if mask:
                # lowest set bit
                low = mask & -mask
                pos = low.bit_length() - 1
                c = b + 1 + pos
                # output in increasing order
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
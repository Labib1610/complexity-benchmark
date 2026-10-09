import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    neigh = [0] * (n + 1)          # 1‑based
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits
        neigh[u] |= 1 << (v - 1)
        neigh[v] |= 1 << (u - 1)
        # store for ordered iteration
        if u < v:
            adj[u].append(v)
        else:
            adj[v].append(u)

    for a in range(1, n + 1):
        # neighbours larger than a are already in adj[a] (by construction)
        for b in sorted(adj[a]):          # ensure increasing order
            # common neighbours of a and b
            common = neigh[a] & neigh[b]
            # keep only vertices > b
            mask = (1 << b) - 1            # bits 0..b-1 set
            common &= ~mask
            if common:
                low = common & -common      # lowest set bit
                c = low.bit_length()        # vertex number
                # a < b < c holds automatically
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
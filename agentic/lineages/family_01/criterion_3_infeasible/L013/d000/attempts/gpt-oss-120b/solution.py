import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 0‑based vertices
    adj = [0] * n
    # also store adjacency lists for ordered iteration
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        # store for later iteration (keep sorted)
        if u < v:
            neigh[u].append(v)
        else:
            neigh[v].append(u)

    # ensure each list is sorted (they already are because we added in input order,
    # but sorting is cheap and guarantees order)
    for lst in neigh:
        lst.sort()

    for a in range(n):
        for b in neigh[a]:          # b > a and edge a–b exists
            common = adj[a] & adj[b]
            # discard vertices <= b
            shifted = common >> (b + 1)
            if shifted:
                low = shifted & -shifted
                idx = low.bit_length() - 1   # position inside shifted
                c = idx + b + 1
                # output 1‑based, sorted
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
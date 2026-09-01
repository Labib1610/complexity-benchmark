import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_int = [0] * n          # bitmask of neighbors
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj_int[u] |= 1 << v
        adj_int[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(n):
        neigh[a].sort()
    # search lexicographically
    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_int[a] & adj_int[b]
            # mask out vertices <= b
            mask = ~((1 << (b + 1)) - 1) & ((1 << n) - 1)
            common &= mask
            if common:
                # get smallest c
                lsb = common & -common
                c = (lsb.bit_length() - 1) + 1  # back to 1‑based
                print(a + 1, b + 1, c)
                return

if __name__ == "__main__":
    solve()
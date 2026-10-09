import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # store undirected edge
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            neigh[u].append(v)
        else:
            neigh[v].append(u)

    # sort neighbour lists to guarantee increasing order
    for lst in neigh:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        for b in neigh[a]:          # b > a by construction
            # common neighbours of a and b
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b .. n-1 are 1
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length()          # 1‑based index
                # c is already > b because of mask
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)          # bitset, bit i-1 corresponds to vertex i
    neigh = [[] for _ in range(n + 1)]  # adjacency list for iteration
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # store both directions
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            neigh[u].append(v)
        else:
            neigh[v].append(u)

    full_mask = (1 << n) - 1
    for a in range(1, n + 1):
        # ensure neighbors are processed in increasing order
        neigh[a].sort()
        for b in neigh[a]:
            # b > a by construction
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b+1 .. n
            common &= mask
            if common:
                # lowest set bit gives smallest c
                low = common & -common
                c = low.bit_length()            # 1‑based index (since bit 0 -> 1)
                # c is already the vertex number
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()
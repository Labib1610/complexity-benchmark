import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n               # bitset for each vertex, 0‑based
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1
    for a in range(n):
        a_mask = adj[a]
        for b in range(a + 1, n):
            if (a_mask >> b) & 1:          # edge a–b ?
                common = a_mask & adj[b]   # neighbours of both
                # keep only vertices with index > b
                mask = full_mask ^ ((1 << (b + 1)) - 1)
                common &= mask
                if common:
                    # lowest set bit -> smallest c
                    low = common & -common
                    c = low.bit_length() - 1
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()
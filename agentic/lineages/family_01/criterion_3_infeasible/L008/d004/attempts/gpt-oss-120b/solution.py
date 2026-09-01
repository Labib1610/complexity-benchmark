import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n                     # bitset for each vertex, 0‑based
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        for b in range(a + 1, n):
            # edge (a,b) ?
            if (adj[a] >> b) & 1:
                common = adj[a] & adj[b]
                # keep only vertices > b
                mask = common >> (b + 1)
                if mask:
                    low = mask & -mask               # lowest set bit
                    c = (b + 1) + low.bit_length() - 1
                    # output 1‑based, sorted
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()
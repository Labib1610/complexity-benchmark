import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 1‑based indexing
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            # edge (a,b) ?
            if ((adj[a] >> b) & 1) == 0:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            common >>= b
            if common:
                lsb = common & -common          # lowest set bit
                pos = lsb.bit_length() - 1     # position after the shift
                c = b + 1 + pos
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
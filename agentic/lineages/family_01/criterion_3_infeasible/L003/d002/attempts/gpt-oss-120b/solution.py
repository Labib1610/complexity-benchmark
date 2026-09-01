import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bit masks, 1‑based indexing
    adj = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in range(a + 1, n + 1):
            # edge (a,b) ?
            if (mask_a >> (b - 1)) & 1:
                common = mask_a & adj[b]
                # keep only vertices with index >= b  (i.e. vertex number > b)
                candidate = common & (-1 << b)
                if candidate:
                    low = candidate & -candidate          # lowest set bit
                    c = low.bit_length()                  # vertex number (1‑based)
                    # a < b < c holds automatically
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
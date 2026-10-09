import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 1‑based indexing (bit i‑1 corresponds to vertex i)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # edge (a,b) must exist
            if (adj[a] >> (b - 1)) & 1:
                common = adj[a] & adj[b]          # vertices adjacent to both a and b
                mask_low = (1 << b) - 1           # bits of vertices ≤ b
                common2 = common & ~mask_low      # keep only vertices > b
                if common2:
                    lowbit = common2 & -common2    # lowest set bit → smallest c
                    c = lowbit.bit_length()       # vertex number (1‑based)
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()
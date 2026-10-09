import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 1‑based vertices, bits are 0‑based
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        a_mask = adj[a]
        for b in range(a + 1, n + 1):
            # edge a‑b ?
            if (a_mask >> (b - 1)) & 1:
                common = a_mask & adj[b]
                # discard vertices ≤ b
                common >>= b
                if common:
                    # position of lowest set bit
                    low = (common & -common).bit_length() - 1
                    c = b + 1 + low
                    # output in increasing order (they already are)
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
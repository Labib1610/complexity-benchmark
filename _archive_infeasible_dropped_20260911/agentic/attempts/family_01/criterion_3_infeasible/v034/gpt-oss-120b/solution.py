import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    # adjacency as bitsets, 1‑based vertices, bits 0..n-1
    adj = [0] * (n + 1)
    for _ in range(m):
        u = next(it)
        v = next(it)
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    for a in range(1, n - 1):
        mask_a = adj[a]
        for b in range(a + 1, n):
            # edge (a,b) ?
            if (mask_a >> (b - 1)) & 1:
                common = mask_a & adj[b]      # neighbours of both
                common >>= b                  # keep only c > b
                if common:
                    low = common & -common     # least significant set bit
                    pos = low.bit_length() - 1
                    c = b + 1 + pos
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
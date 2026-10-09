import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, vertices are 1‑based, bits are 0‑based
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in range(a + 1, n + 1):
            # edge (a,b) must exist
            if not ((mask_a >> (b - 1)) & 1):
                continue
            common = mask_a & adj[b]          # neighbours of both a and b
            common >>= b                      # keep only vertices > b
            if common:
                # lowest set bit gives smallest c
                low = common & -common
                pos = low.bit_length() - 1    # position inside shifted bits
                c = b + 1 + pos
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
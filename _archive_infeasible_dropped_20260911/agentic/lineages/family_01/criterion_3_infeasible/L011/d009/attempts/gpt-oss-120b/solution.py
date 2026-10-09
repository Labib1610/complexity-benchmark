import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    # adjacency as bitsets, 1‑based vertices, bit (v-1) corresponds to vertex v
    adj = [0] * (n + 1)

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        # iterate b > a
        # we can test edge existence by checking the bit
        bits_a = adj[a]
        for b in range(a + 1, n + 1):
            if not (bits_a >> (b - 1)) & 1:
                continue          # no edge a‑b
            # common neighbours of a and b
            common = adj[a] & adj[b]
            # keep only vertices > b
            common >>= b
            if common:
                # lowest set bit gives smallest c > b
                lsb = common & -common
                pos = lsb.bit_length() - 1   # position after the shift
                c = b + 1 + pos
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
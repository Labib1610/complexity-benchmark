import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * (n + 1)          # adjacency as bitsets, vertex i uses bit (i-1)

    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        bits_a = adj[a]
        for b in range(a + 1, n):
            # edge a‑b ?
            if (bits_a >> (b - 1)) & 1:
                common = bits_a & adj[b]
                # keep only vertices > b
                common &= ~((1 << b) - 1)
                if common:
                    # lowest set bit gives the smallest c > b
                    c = (common & -common).bit_length()
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
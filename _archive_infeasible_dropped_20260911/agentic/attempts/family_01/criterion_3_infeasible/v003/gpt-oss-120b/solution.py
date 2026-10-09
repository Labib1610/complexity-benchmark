import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency bitsets, 1‑based
    adj_int = [0] * (n + 1)
    # edge existence matrix for O(1) test
    has_edge = [bytearray(n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # set bits
        adj_int[u] |= 1 << v
        adj_int[v] |= 1 << u
        has_edge[u][v] = 1
        has_edge[v][u] = 1

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not has_edge[a][b]:
                continue
            common = adj_int[a] & adj_int[b]
            # keep only vertices > b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                # lowest set bit -> smallest c
                low = common & -common
                c = low.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
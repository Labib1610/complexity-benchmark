import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix for O(1) edge test
    adj_bool = [bytearray(n) for _ in range(n)]
    # adjacency bitsets
    adj_bits = [0] * n

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bool[u][v] = 1
        adj_bool[v][u] = 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u

    for a in range(n):
        row_a = adj_bits[a]
        for b in range(a + 1, n):
            if not adj_bool[a][b]:
                continue
            common = row_a & adj_bits[b]
            # keep only vertices > b
            common >>= b
            if common:
                low = common & -common          # lowest set bit
                offset = low.bit_length() - 1   # its index (0‑based)
                c = b + 1 + offset
                # output in 1‑based, sorted order
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
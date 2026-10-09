import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix for quick edge existence test
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]
    # bitset adjacency
    adj_bits = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        if not adj_mat[u][v]:
            adj_mat[u][v] = adj_mat[v][u] = 1
            adj_bits[u] |= 1 << (v - 1)
            adj_bits[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not adj_mat[a][b]:
                continue
            common = adj_bits[a] & adj_bits[b]
            # keep only vertices > b
            mask = ~((1 << b) - 1)
            cand = common & mask
            if cand:
                lowest = cand & -cand
                c = lowest.bit_length()  # 1‑based
                # c is guaranteed > b
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
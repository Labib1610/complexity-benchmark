import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix for fast pair iteration
    adj_mat = [[False] * (n + 1) for _ in range(n + 1)]
    # bitset per vertex
    adj_bit = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj_mat[u][v] = adj_mat[v][u] = True
        adj_bit[u] |= 1 << v
        adj_bit[v] |= 1 << u

    full_mask = (1 << (n + 1)) - 1  # bits 0..n set, bit 0 unused

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not adj_mat[a][b]:
                continue
            common = adj_bit[a] & adj_bit[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
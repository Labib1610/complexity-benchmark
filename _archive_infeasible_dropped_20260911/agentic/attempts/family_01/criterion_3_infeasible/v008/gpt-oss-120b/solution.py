import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bit = [0] * (n + 1)
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_bit[u] |= 1 << (v - 1)
        adj_bit[v] |= 1 << (u - 1)
        adj_mat[u][v] = adj_mat[v][u] = 1

    all_ones = (1 << n) - 1
    mask_gt = [0] * (n + 1)
    for b in range(n + 1):
        mask_gt[b] = all_ones ^ ((1 << b) - 1)   # bits for vertices > b

    out = []
    for a in range(1, n + 1):
        ba = adj_bit[a]
        for b in range(a + 1, n + 1):
            if not adj_mat[a][b]:
                continue
            common = ba & adj_bit[b] & mask_gt[b]
            if common:
                lowbit = common & -common
                c_index = lowbit.bit_length() - 1   # 0‑based
                c = c_index + 1
                out = [a, b, c]
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()
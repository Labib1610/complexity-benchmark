import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency boolean matrix (bytearray for speed)
    adj_bool = [bytearray(n + 1) for _ in range(n + 1)]
    # adjacency bit masks
    adj_mask = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj_bool[u][v] = adj_bool[v][u] = 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    for a in range(1, n + 1):
        mask_a = adj_mask[a]
        for b in range(a + 1, n + 1):
            if not adj_bool[a][b]:
                continue
            # vertices adjacent to both a and b
            common = mask_a & adj_mask[b]
            # keep only vertices > b
            common >>= b
            if not common:
                continue
            # lowest set bit -> smallest c
            lsb = common & -common
            pos = lsb.bit_length() - 1   # 0‑based inside shifted mask
            c = b + 1 + pos
            # output in ascending order (already a<b<c)
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # neighbour masks, 1‑based indexing, bit i‑1 corresponds to vertex i
    neigh = [0] * (n + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        neigh[u] |= bit_u
        neigh[v] |= bit_v

    for a in range(1, n - 1):
        mask_a = neigh[a]
        for b in range(a + 1, n):
            # check edge a‑b
            if not (mask_a >> (b - 1)) & 1:
                continue
            common = mask_a & neigh[b]   # vertices adjacent to both a and b
            # keep only vertices > b
            common >>= b
            if common:
                # lowest set bit -> smallest c
                low = common & -common
                offset = low.bit_length() - 1
                c = b + 1 + offset
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
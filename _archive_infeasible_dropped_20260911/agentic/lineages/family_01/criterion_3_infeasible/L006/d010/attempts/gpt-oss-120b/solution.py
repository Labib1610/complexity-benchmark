import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # masks[vertex] : bit i (0‑based) = 1  ⇔ edge (vertex, i+1) exists
    masks = [0] * (n + 1)          # 1‑based indexing

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = masks[a]
        for b in range(a + 1, n + 1):
            # check edge (a,b)
            if not (mask_a >> (b - 1)) & 1:
                continue
            common = mask_a & masks[b]
            # keep only vertices > b
            common_shifted = common >> b
            if common_shifted:
                # position of least significant set bit
                low = (common_shifted & -common_shifted).bit_length() - 1
                c = b + 1 + low
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
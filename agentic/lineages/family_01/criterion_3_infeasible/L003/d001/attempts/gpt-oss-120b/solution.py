import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    masks = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits for both directions
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = masks[a]
        for b in range(a + 1, n + 1):
            # edge a‑b ?
            if not (mask_a >> (b - 1)) & 1:
                continue
            # common neighbours of a and b
            common = mask_a & masks[b]
            # keep only vertices > b
            common &= ~((1 << b) - 1)
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length()            # index (1‑based)
                # c is already > b because we masked
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()
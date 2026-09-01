import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        mask_a = masks[a]
        for b in range(a + 1, n):
            # edge a‑b ?
            if (mask_a >> (b - 1)) & 1 == 0:
                continue
            common = mask_a & masks[b]
            # keep only vertices > b
            common >>= b
            if common:
                low = common & -common
                idx = low.bit_length() - 1   # position after shift
                c = idx + b + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
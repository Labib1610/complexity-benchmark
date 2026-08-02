import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    masks = [0] * (n + 1)  # 1-indexed
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = masks[a]
        for b in range(a + 1, n + 1):
            if not ((mask_a >> (b - 1)) & 1):
                continue
            inter = mask_a & masks[b]
            shifted = inter >> b  # drop bits <= b
            if shifted:
                low = shifted & -shifted
                c_offset = low.bit_length() - 1
                c = b + 1 + c_offset
                if c <= n:
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
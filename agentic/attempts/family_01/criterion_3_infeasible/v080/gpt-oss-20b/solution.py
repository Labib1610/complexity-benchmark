import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    bitmask = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bitmask[u] |= 1 << (v - 1)
        bitmask[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = bitmask[a]
        for b in range(a + 1, n + 1):
            # check if edge a-b exists
            if (mask_a >> (b - 1)) & 1:
                intersection = mask_a & bitmask[b]
                # shift to ignore bits <= b-1 (nodes <= b)
                shifted = intersection >> b
                if shifted:
                    # position of lowest set bit in shifted
                    pos = (shifted & -shifted).bit_length() - 1
                    c = b + pos + 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
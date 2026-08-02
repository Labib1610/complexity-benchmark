import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    for a in range(1, n - 1):
        mask_a = masks[a]
        for b in range(a + 1, n):
            # check if edge a-b exists
            if (mask_a >> (b - 1)) & 1:
                mask_b = masks[b]
                # common neighbors of a and b that are > b
                common = (mask_a & mask_b) & (~((1 << b) - 1))
                if common:
                    # lowest set bit in common
                    lowest = common & -common
                    c_index = lowest.bit_length() - 1  # 0-based index
                    c = c_index + 1
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()
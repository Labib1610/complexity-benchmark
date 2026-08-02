import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    masks = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    for a in range(n):
        mask_a = masks[a]
        # iterate over neighbors b > a
        b = a + 1
        while b < n:
            if (mask_a >> b) & 1:
                common = mask_a & masks[b]
                sub = common >> (b + 1)
                if sub:
                    lsb = sub & -sub
                    c_offset = lsb.bit_length() - 1
                    c = b + 1 + c_offset
                    print(a + 1, b + 1, c + 1)
                    return
            b += 1

if __name__ == "__main__":
    solve()
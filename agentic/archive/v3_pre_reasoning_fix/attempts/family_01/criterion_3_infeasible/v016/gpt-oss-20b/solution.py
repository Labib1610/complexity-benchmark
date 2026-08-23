import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * (n + 1)  # 1-indexed, bit i corresponds to employee i+1

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_mask[u] |= 1 << (v - 1)
        adj_mask[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = adj_mask[a]
        for b in range(a + 1, n + 1):
            if (mask_a >> (b - 1)) & 1:          # edge a-b exists
                common = mask_a & adj_mask[b]   # neighbors common to a and b
                # zero bits for employees <= b (positions 0..b-1)
                mask_after = common & ~((1 << b) - 1)
                if mask_after:
                    low = mask_after & -mask_after   # lowest set bit
                    c = low.bit_length()             # employee id
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
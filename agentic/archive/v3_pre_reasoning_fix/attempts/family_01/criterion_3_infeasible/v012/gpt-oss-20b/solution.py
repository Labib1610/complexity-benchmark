import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    # precompute mask of nodes greater than i
    mask_gt = [0] * (n + 2)  # mask_gt[n] = 0
    accum = 0
    for i in range(n, 0, -1):
        mask_gt[i] = accum
        accum |= 1 << (i - 1)

    for a in range(1, n + 1):
        mask_ab = adj[a] & mask_gt[a]
        while mask_ab:
            b_bit = mask_ab & -mask_ab
            b = b_bit.bit_length()  # node index
            mask = adj[a] & adj[b] & mask_gt[b]
            if mask:
                c_bit = mask & -mask
                c = c_bit.bit_length()
                print(a, b, c)
                return
            mask_ab -= b_bit

if __name__ == "__main__":
    solve()
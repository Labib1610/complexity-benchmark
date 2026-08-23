import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    mask_all = (1 << n) - 1
    mask_gt = [0] * n
    for a in range(n):
        mask_gt[a] = mask_all ^ ((1 << (a + 1)) - 1)

    for a in range(n):
        Na = adj[a] & mask_gt[a]
        temp = Na
        while temp:
            lsb = temp & -temp
            b = (lsb.bit_length() - 1)
            temp ^= lsb
            common = Na & adj[b]
            common_masked = common & mask_gt[b]
            if common_masked:
                lsb2 = common_masked & -common_masked
                c = (lsb2.bit_length() - 1)
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    full_mask = (1 << n) - 1
    mask_gt = [0] * (n + 2)
    for b in range(n + 1):  # b from 0..n
        mask_gt[b] = full_mask & ~((1 << b) - 1)

    for a in range(1, n - 1):
        a_mask = adj[a]
        for b in range(a + 1, n):
            inter = a_mask & adj[b] & mask_gt[b]
            if inter:
                lowbit = inter & -inter
                idx = lowbit.bit_length() - 1  # 0-based
                c = idx + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
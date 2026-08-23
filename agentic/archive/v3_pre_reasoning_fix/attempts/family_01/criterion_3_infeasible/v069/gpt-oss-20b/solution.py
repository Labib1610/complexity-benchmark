import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj_mask = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        mask_u = 1 << (v - 1)
        mask_v = 1 << (u - 1)
        adj_mask[u] |= mask_u
        adj_mask[v] |= mask_v
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    base_mask = (1 << n) - 1
    mask_gt = [0] * (n + 1)
    for i in range(n + 1):
        mask_gt[i] = base_mask ^ ((1 << i) - 1)

    for a in range(1, n + 1):
        na = neigh[a]
        for b in na:
            if b <= a:
                continue
            inter = adj_mask[a] & adj_mask[b] & mask_gt[b]
            if inter:
                c_bit = inter & -inter
                c = c_bit.bit_length()
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
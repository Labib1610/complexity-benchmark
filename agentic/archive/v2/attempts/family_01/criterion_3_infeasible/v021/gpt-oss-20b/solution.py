import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)  # 1-indexed
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1

    for a in range(1, n - 1):
        neigh_a = adj[a]
        for b in range(a + 1, n + 1):
            if not (neigh_a >> (b - 1)) & 1:
                continue
            inter = adj[a] & adj[b]
            mask_gt_b = (~((1 << b) - 1)) & full_mask
            cand = inter & mask_gt_b
            if cand:
                # lowest set bit
                low_bit = cand & -cand
                c = (low_bit.bit_length() - 1) + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
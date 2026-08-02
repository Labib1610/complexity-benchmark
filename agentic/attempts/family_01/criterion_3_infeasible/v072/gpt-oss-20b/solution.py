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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    # Precompute neighbor lists sorted ascending
    neigh = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        bits = adj[u]
        while bits:
            lsb = bits & -bits
            v = lsb.bit_length()  # 1-based node number
            neigh[u].append(v)
            bits ^= lsb

    max_mask = (1 << n) - 1
    mask_gt_node = [0] * (n + 1)
    for b in range(1, n + 1):
        mask_gt_node[b] = max_mask ^ ((1 << b) - 1)  # bits > b-1

    for a in range(1, n - 1):
        for b in neigh[a]:
            if b <= a:
                continue
            inter = adj[a] & adj[b]
            inter_gt = inter & mask_gt_node[b]
            if inter_gt:
                lsb = inter_gt & -inter_gt
                c = lsb.bit_length()  # node number
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
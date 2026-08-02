import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_mask = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for a in range(n):
        # sort neighbors of a once
        neigh_a = sorted(neighbors[a])
        mask_a = adj_mask[a]
        for b in neigh_a:
            if b <= a:
                continue
            # find intersection of a and b
            inter = mask_a & adj_mask[b]
            # mask out bits <= b
            mask2 = inter & (~((1 << (b + 1)) - 1))
            if mask2:
                # lowest set bit
                low = mask2 & -mask2
                c = low.bit_length() - 1  # 0-based index
                # output 1-based
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    for a in range(1, n + 1):
        mask_a = adj_mask[a]
        for b in neigh[a]:
            if b <= a:
                continue
            # intersection of neighbors of a and b
            inter = mask_a & adj_mask[b]
            # zero out bits <= b
            inter &= ~((1 << (b + 1)) - 1)
            if inter:
                # get least set bit
                c = (inter & -inter).bit_length() - 1
                # c is guaranteed > b
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
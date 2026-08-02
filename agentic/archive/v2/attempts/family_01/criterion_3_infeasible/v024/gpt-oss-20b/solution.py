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
        bit_u = 1 << (u - 1)
        bit_v = 1 << (v - 1)
        adj_mask[u] |= bit_v
        adj_mask[v] |= bit_u
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    # helper mask with all 1..n bits set
    all_ones = (1 << n) - 1

    for a in range(1, n + 1):
        mask_a = adj_mask[a]
        for b in neigh[a]:
            if b <= a:
                continue
            # common neighbours of a and b that are > b
            mask = mask_a & adj_mask[b] & (~((1 << b) - 1))
            if mask:
                sub = mask >> b          # shift so that node b+1 becomes bit 0
                low = sub & -sub         # lowest set bit
                pos = low.bit_length() - 1
                c = b + pos + 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
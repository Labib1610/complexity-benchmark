import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * n
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        # set bits
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(n):
        # ensure neighbors are sorted for lexicographic order
        neigh[a].sort()
    # iterate lexicographically
    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            # mask bits > b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                # lowest set bit
                low = common & -common
                c = low.bit_length() - 1
                # output in increasing order
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
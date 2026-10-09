import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # bitset adjacency
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        mask_a = adj[a]
        # iterate b > a where edge exists
        b_bits = mask_a >> (a + 1)
        while b_bits:
            lsb = b_bits & -b_bits
            b = (a + 1) + (lsb.bit_length() - 1)
            # common neighbours > b
            common = (adj[a] & adj[b]) >> (b + 1)
            if common:
                lsb_c = common & -common
                c = (b + 1) + (lsb_c.bit_length() - 1)
                print(a + 1, b + 1, c + 1)
                return
            b_bits ^= lsb  # remove this b

if __name__ == "__main__":
    solve()
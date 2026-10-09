import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1
    for a in range(n):
        mask_a = adj[a]
        # iterate b > a where edge exists
        b_bits = mask_a >> (a + 1)
        while b_bits:
            lsb = b_bits & -b_bits
            b = (lsb.bit_length() - 1) + a + 1
            # common neighbors of a and b
            common = adj[a] & adj[b]
            # keep only c > b
            higher_mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= higher_mask
            if common:
                c_lsb = common & -common
                c = c_lsb.bit_length() - 1
                # output 1-indexed in ascending order
                print(a + 1, b + 1, c + 1)
                return
            # clear this b bit
            b_bits ^= lsb

if __name__ == "__main__":
    solve()
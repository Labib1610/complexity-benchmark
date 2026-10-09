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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        mask_a = adj[a]
        # iterate b > a where edge exists
        b_bits = mask_a >> (a + 1)  # bits for indices > a
        while b_bits:
            # get lowest set bit relative to shifted position
            low_rel = (b_bits & -b_bits).bit_length() - 1
            b = a + 1 + low_rel
            # common neighbors of a and b
            common = adj[a] & adj[b]
            # zero out indices <= b
            mask = common & ~((1 << (b + 1)) - 1)
            if mask:
                c = (mask & -mask).bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return
            # clear this b bit and continue
            b_bits &= b_bits - 1

if __name__ == "__main__":
    solve()
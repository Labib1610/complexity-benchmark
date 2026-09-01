import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency as bitsets, 1‑based vertex numbers, bits 0..n-1
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full_mask = (1 << n) - 1          # bits 0 .. n-1 set

    for a in range(1, n - 1):
        a_adj = adj[a]
        for b in range(a + 1, n):
            # edge (a,b) must exist
            if not ((a_adj >> (b - 1)) & 1):
                continue
            # vertices adjacent to both a and b
            common = a_adj & adj[b]
            # keep only vertices with index >= b  (i.e. vertex number > b)
            mask = full_mask ^ ((1 << b) - 1)   # bits b .. n-1 are 1
            common &= mask
            if common:
                # smallest c : least significant set bit
                lsb = common & -common
                c = lsb.bit_length()          # gives index+1
                # c is already 1‑based because bit 0 -> vertex 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
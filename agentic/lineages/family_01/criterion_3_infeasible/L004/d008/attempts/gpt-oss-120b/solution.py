import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset for each vertex, 0‑based
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        a_adj = adj[a]
        # iterate b > a where edge a‑b exists
        # we can scan all b, checking the bit
        for b in range(a + 1, n):
            if (a_adj >> b) & 1 == 0:
                continue
            common = a_adj & adj[b]          # neighbours of both a and b
            # need c > b
            mask = common >> (b + 1)
            if mask:
                # lowest set bit
                low = mask & -mask
                c = low.bit_length() - 1 + (b + 1)
                # output 1‑based
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
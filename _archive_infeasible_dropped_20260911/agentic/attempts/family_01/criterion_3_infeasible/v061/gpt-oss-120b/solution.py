import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)          # bit i-1 corresponds to vertex i
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits for both directions
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        bits_a = adj[a]
        # iterate b > a where edge (a,b) exists
        # we can scan b linearly; n is only 2000
        for b in range(a + 1, n + 1):
            if (bits_a >> (b - 1)) & 1 == 0:
                continue
            common = bits_a & adj[b]          # vertices adjacent to both a and b
            # we need c > b
            mask = common >> b                # drop bits <= b
            if mask:
                low = mask & -mask             # lowest set bit
                idx = low.bit_length() - 1    # position from 0
                c = b + idx + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
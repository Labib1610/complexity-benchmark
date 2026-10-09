import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset of neighbours for each vertex

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        mask_a = adj[a]
        for b in range(a + 1, n):
            if (mask_a >> b) & 1 == 0:          # edge a‑b missing
                continue
            inter = mask_a & adj[b]             # common neighbours
            # delete vertices ≤ b
            inter &= ~((1 << (b + 1)) - 1)
            if inter:
                low = inter & -inter             # lowest set bit
                c = low.bit_length() - 1
                # output 1‑based, sorted
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()
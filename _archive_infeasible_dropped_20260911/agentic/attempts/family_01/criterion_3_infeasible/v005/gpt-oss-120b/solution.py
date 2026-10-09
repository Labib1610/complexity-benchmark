import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n - 1):
        mask_a = adj[a]
        for b in range(a + 1, n):
            if (mask_a >> b) & 1 == 0:
                continue          # edge (a,b) missing
            common = mask_a & adj[b]
            # keep only vertices > b
            common >>= b
            if common:
                low = common & -common          # lowest set bit
                offset = low.bit_length() - 1   # position of that bit
                c = b + 1 + offset
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
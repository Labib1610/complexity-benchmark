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

    full_mask = (1 << (n + 1)) - 1   # bits 0..n
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (adj[a] >> b) & 1 == 0:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = ~((1 << (b + 1)) - 1) & full_mask
            common &= mask
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
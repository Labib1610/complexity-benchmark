import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bit i set ⇔ edge to i
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << (n + 1)) - 1   # bits 0..n set, we ignore bit 0

    for a in range(1, n - 1):
        bits_a = adj[a]
        for b in range(a + 1, n):
            # does edge (a,b) exist ?
            if (bits_a >> b) & 1:
                common = bits_a & adj[b]
                # keep only vertices > b
                mask = full_mask ^ ((1 << (b + 1)) - 1)
                common &= mask
                if common:
                    low = common & -common          # lowest set bit
                    c = low.bit_length() - 1
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
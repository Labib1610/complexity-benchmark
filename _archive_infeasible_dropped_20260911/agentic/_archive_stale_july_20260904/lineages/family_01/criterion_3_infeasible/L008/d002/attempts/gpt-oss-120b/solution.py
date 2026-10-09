import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitset, 1‑based vertices
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n - 1):
        a_adj = adj[a]
        for b in range(a + 1, n + 1):
            if (a_adj >> b) & 1:          # edge (a,b) exists
                common = a_adj & adj[b]    # neighbours of both
                # keep only vertices > b
                mask = (1 << (b + 1)) - 1
                common &= ~mask
                if common:
                    low = common & -common
                    c = low.bit_length() - 1
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
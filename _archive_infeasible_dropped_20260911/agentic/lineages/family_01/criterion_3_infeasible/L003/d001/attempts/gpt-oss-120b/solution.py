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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        a_mask = adj[a]
        for b in range(a + 1, n + 1):
            if not (a_mask >> (b - 1)) & 1:   # edge (a,b) missing
                continue
            common = a_mask & adj[b]
            shifted = common >> b               # keep only vertices > b
            if shifted:
                low = shifted & -shifted
                c = low.bit_length() + b
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
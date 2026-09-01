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
        bit_v = 1 << (v - 1)
        bit_u = 1 << (u - 1)
        adj[u] |= bit_v
        adj[v] |= bit_u

    for a in range(1, n + 1):
        mask_a = adj[a]
        for b in range(a + 1, n + 1):
            # edge a‑b ?
            if not (mask_a >> (b - 1)) & 1:
                continue
            common = mask_a & adj[b]          # neighbours of both a and b
            # keep only vertices > b
            mask = common >> b
            if mask:
                low = mask & -mask
                idx = low.bit_length() - 1    # 0‑based inside shifted mask
                c = idx + b + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
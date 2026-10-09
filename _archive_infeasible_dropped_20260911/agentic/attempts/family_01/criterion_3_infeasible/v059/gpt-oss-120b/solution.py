import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n - 1):
        mask_a = adj[a]
        for b in range(a + 1, n):
            if (mask_a >> (b - 1)) & 1:          # edge a‑b exists
                common = mask_a & adj[b]         # vertices adjacent to both a and b
                shifted = common >> b            # keep only vertices > b
                if shifted:
                    lowbit = shifted & -shifted
                    offset = lowbit.bit_length() - 1
                    c = b + offset + 1
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
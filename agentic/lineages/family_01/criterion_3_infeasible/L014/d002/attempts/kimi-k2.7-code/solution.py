import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    full = (1 << n) - 1
    mask_gt = [0] * (n + 1)
    for b in range(1, n + 1):
        mask_gt[b] = full ^ ((1 << b) - 1)

    out = sys.stdout
    for a in range(1, n + 1):
        abits = adj[a]
        bits = abits
        while bits:
            low = bits & -bits
            b = low.bit_length()
            bits ^= low
            if b <= a:
                continue
            inter = abits & adj[b] & mask_gt[b]
            if inter:
                lowc = inter & -inter
                c = lowc.bit_length()
                out.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
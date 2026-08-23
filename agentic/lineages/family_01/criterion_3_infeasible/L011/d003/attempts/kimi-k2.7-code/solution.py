import sys

def solve():
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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << (n + 1)) - 1
    for a in range(1, n + 1):
        mask_a = full ^ ((1 << (a + 1)) - 1)
        cand = adj[a] & mask_a
        if not cand:
            continue
        adj_a = adj[a]
        while cand:
            lsb = cand & -cand
            b = lsb.bit_length() - 1
            cand ^= lsb
            mask_b = full ^ ((1 << (b + 1)) - 1)
            common = adj_a & adj[b] & mask_b
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

solve()
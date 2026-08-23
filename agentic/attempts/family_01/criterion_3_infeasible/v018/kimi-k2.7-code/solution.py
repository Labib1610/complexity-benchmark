import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    mask_gt = [~((1 << (i + 1)) - 1) for i in range(n)]

    for a in range(n):
        A = adj[a]
        bits = A & mask_gt[a]
        while bits:
            low = bits & -bits
            b = low.bit_length() - 1
            common = A & adj[b] & mask_gt[b]
            if common:
                c = (common & -common).bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}\n")
                return
            bits ^= low

solve()
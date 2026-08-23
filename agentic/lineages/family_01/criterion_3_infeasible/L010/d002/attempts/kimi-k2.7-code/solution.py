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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        mask_a = ~((1 << a) - 1)
        bits = adj[a] & mask_a
        while bits:
            low = bits & -bits
            b = low.bit_length()
            inter = adj[a] & adj[b]
            mask_b = ~((1 << b) - 1)
            inter_hi = inter & mask_b
            if inter_hi:
                c = (inter_hi & -inter_hi).bit_length()
                sys.stdout.write(f"{a} {b} {c}")
                return
            bits ^= low

if __name__ == "__main__":
    solve()
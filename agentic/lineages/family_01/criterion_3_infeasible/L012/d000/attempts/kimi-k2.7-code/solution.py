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

    full = (1 << n) - 1
    for a in range(1, n + 1):
        mask_b = full & ~((1 << a) - 1)
        cand_b = adj[a] & mask_b
        while cand_b:
            low = cand_b & -cand_b
            b = low.bit_length()
            mask_c = full & ~((1 << b) - 1)
            common = adj[a] & adj[b] & mask_c
            if common:
                lowc = common & -common
                c = lowc.bit_length()
                sys.stdout.write(f"{a} {b} {c}")
                return
            cand_b &= cand_b - 1

if __name__ == "__main__":
    solve()
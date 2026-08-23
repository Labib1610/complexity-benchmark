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

    for a in range(1, n + 1):
        mask_b = adj[a - 1] >> a
        while mask_b:
            low = mask_b & -mask_b
            b = a + low.bit_length()
            common = adj[a - 1] & adj[b - 1]
            common_high = common >> b
            if common_high:
                lowc = common_high & -common_high
                c = b + lowc.bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return
            mask_b ^= low

if __name__ == "__main__":
    solve()
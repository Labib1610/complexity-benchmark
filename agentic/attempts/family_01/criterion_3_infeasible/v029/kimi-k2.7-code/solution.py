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

    for a in range(n):
        mask = adj[a] & ~((1 << (a + 1)) - 1)
        while mask:
            lsb = mask & -mask
            b = lsb.bit_length() - 1
            common = adj[a] & adj[b]
            high = common >> (b + 1)
            if high:
                lsb2 = high & -high
                c = lsb2.bit_length() - 1 + b + 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}")
                return
            mask ^= lsb

if __name__ == "__main__":
    solve()
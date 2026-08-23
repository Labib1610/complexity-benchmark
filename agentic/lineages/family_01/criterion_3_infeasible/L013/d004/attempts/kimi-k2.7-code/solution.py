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
    suffix = [0] * (n + 1)
    for v in range(1, n + 1):
        suffix[v] = full ^ ((1 << v) - 1)

    for a in range(1, n - 1):
        bits_b = adj[a] & suffix[a]
        while bits_b:
            lsb = bits_b & -bits_b
            b = lsb.bit_length()
            common = adj[a] & adj[b] & suffix[b]
            if common:
                c = (common & -common).bit_length()
                sys.stdout.write(f"{a} {b} {c}")
                return
            bits_b ^= lsb

if __name__ == "__main__":
    solve()
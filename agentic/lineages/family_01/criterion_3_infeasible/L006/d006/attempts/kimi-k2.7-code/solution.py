import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * (n + 1)
    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n + 1):
        adj_a = adj[a]
        base = a + 1
        bits = adj_a >> base
        while bits:
            low = bits & -bits
            b = low.bit_length() - 1 + base
            common = adj_a & adj[b]
            if common:
                shifted = common >> b
                if shifted:
                    c = (shifted & -shifted).bit_length() - 1 + b
                    sys.stdout.write(f"{a} {b} {c}")
                    return
            bits ^= low

if __name__ == "__main__":
    solve()
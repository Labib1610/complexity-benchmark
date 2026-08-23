import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    bit = [1 << i for i in range(n)]
    adj = [0] * (n + 1)
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u] |= bit[v - 1]
        adj[v] |= bit[u - 1]
    for a in range(1, n + 1):
        B = adj[a] & ~((1 << a) - 1)
        while B:
            low = B & -B
            b = low.bit_length()
            C = adj[a] & adj[b]
            t = C & ~((1 << b) - 1)
            if t:
                c = (t & -t).bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return
            B ^= low

if __name__ == "__main__":
    solve()
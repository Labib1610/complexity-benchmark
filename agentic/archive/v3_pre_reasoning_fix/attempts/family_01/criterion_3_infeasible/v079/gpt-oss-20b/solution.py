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

    for a in range(1, n - 1):
        adj_a = adj[a]
        for b in range(a + 1, n):
            if not ((adj_a >> (b - 1)) & 1):
                continue
            inter = adj_a & adj[b]
            mask = ~((1 << b) - 1)
            inter_masked = inter & mask
            if inter_masked:
                c_bit = inter_masked & -inter_masked
                c = c_bit.bit_length()
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
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

    for a in range(1, n + 1):
        row_a = adj[a]
        for b in range(a + 1, n + 1):
            if (row_a >> (b - 1)) & 1:
                common = row_a & adj[b]
                mask = common >> b  # ignore indices <= b
                if mask:
                    lsb = mask & -mask
                    offset = lsb.bit_length() - 1
                    c = b + 1 + offset
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
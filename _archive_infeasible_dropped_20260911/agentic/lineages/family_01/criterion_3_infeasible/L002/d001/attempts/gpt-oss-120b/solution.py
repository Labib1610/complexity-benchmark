import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = next(it)
        v = next(it)
        bit_u = 1 << (v - 1)
        bit_v = 1 << (u - 1)
        adj[u] |= bit_u
        adj[v] |= bit_v

    for a in range(1, n - 1):
        bits_a = adj[a]
        for b in range(a + 1, n):
            # edge a‑b ?
            if (bits_a >> (b - 1)) & 1:
                common = bits_a & adj[b]
                mask = common >> b          # keep only vertices > b
                if mask:
                    lsb = mask & -mask       # lowest set bit
                    c_offset = lsb.bit_length() - 1
                    c = b + 1 + c_offset
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
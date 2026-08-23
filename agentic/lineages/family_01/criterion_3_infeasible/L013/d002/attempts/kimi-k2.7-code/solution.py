import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    m = data[1]
    adj = [0] * (n + 1)
    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        row_a = adj[a]
        mask = row_a >> a
        while mask:
            lsb = mask & -mask
            b = a + lsb.bit_length()
            common = row_a & adj[b]
            shifted = common >> b
            if shifted:
                lsb2 = shifted & -shifted
                c = b + lsb2.bit_length()
                sys.stdout.write(f"{a} {b} {c}\n")
                return
            mask ^= lsb

if __name__ == "__main__":
    solve()
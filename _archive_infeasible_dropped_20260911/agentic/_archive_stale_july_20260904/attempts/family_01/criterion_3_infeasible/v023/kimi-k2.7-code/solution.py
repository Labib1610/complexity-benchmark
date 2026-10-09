import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    p = 2
    for _ in range(m):
        u = int(data[p]) - 1
        v = int(data[p + 1]) - 1
        p += 2
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << n) - 1
    suffix = [0] * n
    for b in range(n):
        suffix[b] = full & ~((1 << (b + 1)) - 1)

    for a in range(n):
        mask = adj[a] >> (a + 1)
        base = a + 1
        while mask:
            lsb = mask & -mask
            b = base + lsb.bit_length() - 1
            common = adj[a] & adj[b] & suffix[b]
            if common:
                c = (common & -common).bit_length()
                sys.stdout.write(f"{a + 1} {b + 1} {c}")
                return
            mask ^= lsb

if __name__ == "__main__":
    solve()
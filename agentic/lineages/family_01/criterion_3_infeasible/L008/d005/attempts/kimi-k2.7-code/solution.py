import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    masks = [0] * (n + 1)
    p = 2
    for _ in range(m):
        u = data[p]
        v = data[p + 1]
        p += 2
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    high = [0] * (n + 1)
    for i in range(n + 1):
        high[i] = ~((1 << (i + 1)) - 1)

    for a in range(1, n + 1):
        ma = masks[a]
        nb = ma & high[a]
        while nb:
            lsb = nb & -nb
            b = lsb.bit_length() - 1
            cand = ma & masks[b] & high[b]
            if cand:
                c = (cand & -cand).bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return
            nb ^= lsb

if __name__ == "__main__":
    solve()
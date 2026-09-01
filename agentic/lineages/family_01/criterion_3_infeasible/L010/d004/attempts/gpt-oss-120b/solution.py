import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bit_u = 1 << (u - 1)
        bit_v = 1 << (v - 1)
        adj[u] |= bit_v
        adj[v] |= bit_u

    # higher[v] = bits of vertices > v
    full = (1 << n) - 1
    higher = [0] * (n + 1)
    for v in range(n + 1):
        higher[v] = full ^ ((1 << v) - 1)   # bits v, v+1, ... (0‑based)

    for a in range(1, n + 1):
        nb = adj[a] & higher[a]            # neighbours > a
        while nb:
            low = nb & -nb
            b = low.bit_length()           # 1‑based vertex number
            nb ^= low                       # remove this b

            common = adj[a] & adj[b] & higher[b]
            if common:
                lowc = common & -common
                c = lowc.bit_length()
                # a < b < c holds by construction
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
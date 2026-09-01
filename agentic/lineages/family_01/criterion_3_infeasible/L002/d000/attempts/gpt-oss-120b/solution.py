import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        # neighbours of a that are > a
        nb = adj[a] >> a
        while nb:
            lowb = (nb & -nb).bit_length() - 1   # position of lowest set bit
            b = a + 1 + lowb                       # actual vertex number
            # common neighbours of a and b
            common = adj[a] & adj[b]
            x = common >> b
            if x:
                lowc = (x & -x).bit_length() - 1
                c = b + lowc
                sys.stdout.write(f"{a} {b} {c}\n")
                return
            nb &= nb - 1   # clear lowest set bit

if __name__ == "__main__":
    solve()
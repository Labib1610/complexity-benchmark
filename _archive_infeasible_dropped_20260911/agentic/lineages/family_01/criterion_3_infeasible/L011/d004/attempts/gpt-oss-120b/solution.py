import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, adj[i] bit j (0‑based) => vertex j+1
    nbr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            nbr[u].append(v)
        else:
            nbr[v].append(u)

    # neighbours are already collected only > vertex, but need sorted
    for lst in nbr:
        lst.sort()

    for a in range(1, n + 1):
        for b in nbr[a]:                 # b > a, edge a-b exists
            common = adj[a] & adj[b]
            # discard vertices <= b
            x = common >> b
            if x:
                low = x & -x
                k = low.bit_length() - 1   # index of lowest set bit
                c = b + 1 + k
                # output lexicographically smallest triangle
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()
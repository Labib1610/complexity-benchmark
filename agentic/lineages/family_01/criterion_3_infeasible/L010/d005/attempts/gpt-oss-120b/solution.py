import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        g[u].append(v)
        g[v].append(u)

    # sort adjacency lists to guarantee increasing order of b
    for lst in g:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        for b in g[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b..n-1 are 1
            common &= mask
            if common:
                low = common & -common            # lowest set bit
                c = low.bit_length()             # 1‑based vertex id
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
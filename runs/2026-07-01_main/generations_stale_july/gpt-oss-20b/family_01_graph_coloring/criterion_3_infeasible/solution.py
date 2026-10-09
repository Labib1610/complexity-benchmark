import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        neigh[a].sort()
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            mask = (1 << b) - 1
            common &= ~mask
            if common:
                low = common & -common
                c = low.bit_length()
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
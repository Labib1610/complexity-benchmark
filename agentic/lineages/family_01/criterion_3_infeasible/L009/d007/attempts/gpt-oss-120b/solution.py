import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    edge_exists = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        # set bits (0‑based index)
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edge_exists[u].add(v)
        edge_exists[v].add(u)

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in edge_exists[a]:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                lsb = common & -common
                c = lsb.bit_length()          # 0‑based index -> vertex id
                # c is already 1‑based because bit 0 corresponds to vertex 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
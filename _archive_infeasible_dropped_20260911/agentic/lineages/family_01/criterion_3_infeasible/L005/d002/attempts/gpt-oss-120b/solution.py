import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i
    edges = []                  # list of (u,v) with u<v for iteration

    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))

    # For fast neighbour iteration per a, build list of neighbours > a
    neigh = [[] for _ in range(n + 1)]
    for u, v in edges:
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        # consider neighbours b > a
        for b in neigh[a]:
            if b <= a:
                continue
            # common neighbours of a and b
            common = adj[a] & adj[b]
            # discard vertices <= b
            mask = common >> b
            if mask:
                # lowest set bit
                low = (mask & -mask).bit_length() - 1
                c = b + 1 + low
                # we have a<b<c and triangle exists
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()
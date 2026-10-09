import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bits 0..n-1
    edges = []                   # store (u,v) with u < v

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # set bits
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))

    # Build neighbour lists for fast iteration of b > a
    neigh = [[] for _ in range(n + 1)]
    for u, v in edges:
        neigh[u].append(v)   # v > u by construction

    for a in range(1, n + 1):
        for b in neigh[a]:          # b > a, already increasing
            common = adj[a] & adj[b]
            # discard vertices <= b
            common >>= b
            if common == 0:
                continue
            low = common & -common
            c = (low.bit_length() - 1) + b + 1
            # a < b < c holds
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()
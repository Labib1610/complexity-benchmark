import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:
            continue
        # store undirected
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))
    # sort edges to ensure b increasing for each a
    edges.sort()
    # iterate lexicographically
    for a, b in edges:
        # common neighbors of a and b
        common = adj[a] & adj[b]
        # we need c > b
        mask = common >> b  # drop bits 0..b-1 (since vertices are 1-indexed)
        if mask:
            # lowest set bit in mask
            low = mask & -mask
            idx = low.bit_length() - 1  # position from 0
            c = b + 1 + idx
            # output sorted triple (a<b<c already)
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()
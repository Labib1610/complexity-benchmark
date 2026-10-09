import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # store undirected edge
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))

    best = None  # tuple (a,b,c)

    for u, v in edges:
        # common neighbours of u and v
        common = adj[u] & adj[v]
        # keep only vertices > v
        cand = common >> v
        if cand:
            low = cand & -cand               # lowest set bit
            w = (low.bit_length() - 1) + v   # restore original index
            tri = (u, v, w)
            if best is None or tri < best:
                best = tri

    # best is guaranteed to exist
    a, b, c = best
    sys.stdout.write(f"{a} {b} {c}")

if __name__ == "__main__":
    solve()
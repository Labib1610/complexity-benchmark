import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset for each vertex, 0‑based
    edges = []             # list of (u,v) with u<v

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))

    # sort edges to guarantee lexicographic order
    edges.sort()

    for u, v in edges:
        # common neighbours of u and v
        common = adj[u] & adj[v]
        # keep only vertices > v
        mask = common >> (v + 1)
        if mask:
            low = mask & -mask               # lowest set bit
            w = (low.bit_length() - 1) + v + 1
            # output 1‑based sorted triple
            a, b, c = u + 1, v + 1, w + 1
            sys.stdout.write(f"{a} {b} {c}")
            return

if __name__ == "__main__":
    solve()
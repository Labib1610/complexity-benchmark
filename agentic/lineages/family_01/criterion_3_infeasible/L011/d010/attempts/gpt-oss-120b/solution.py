import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based, bit i‑1 corresponds to vertex i
    edges = []                   # list of (a,b) with a<b

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        if u > v:
            u, v = v, u
        # set bits
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        edges.append((u, v))

    # sort edges to guarantee lexicographic order of (a,b)
    edges.sort()

    for a, b in edges:
        # vertices adjacent to both a and b
        common = adj[a] & adj[b]
        # discard vertices <= b
        common >>= b
        if common:
            # index of lowest set bit
            tz = (common & -common).bit_length() - 1
            c = b + 1 + tz
            print(a, b, c)
            return

if __name__ == "__main__":
    solve()
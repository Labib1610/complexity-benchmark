import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bit masks, 0‑based vertices
    edges = []             # list of edges with a<b (0‑based)

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

    # sort edges to guarantee lexicographic order of (a,b)
    edges.sort()

    for a, b in edges:
        # common neighbours of a and b
        common = adj[a] & adj[b]
        # keep only vertices > b
        common >>= b + 1
        if common:
            low = common & -common          # lowest set bit
            idx = low.bit_length() - 1      # position of that bit
            c = b + 1 + idx                  # back to original index
            # output 1‑based and sorted
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()
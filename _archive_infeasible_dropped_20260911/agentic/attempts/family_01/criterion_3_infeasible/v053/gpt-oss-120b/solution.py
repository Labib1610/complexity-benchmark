import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    edges = []

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        if u > v:
            u, v = v, u
        edges.append((u, v))

    edges.sort()                     # lexicographic order

    for a, b in edges:               # a < b
        common = adj[a] & adj[b]
        mask = common >> (b + 1)      # keep only vertices > b
        if mask:
            low = mask & -mask        # lowest set bit
            c = (low.bit_length() - 1) + (b + 1)
            print(a + 1, b + 1, c + 1)
            return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset for each vertex
    edges = []             # list of edges with u < v

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        # set bits
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))

    # sort edges to guarantee lexicographic order of (a,b)
    edges.sort()

    for u, v in edges:
        # common neighbours of u and v
        common = adj[u] & adj[v]
        # keep only vertices > v
        mask = common >> (v + 1)
        if mask:
            # position of least significant 1 bit
            low = (mask & -mask).bit_length() - 1
            c = low + v + 1
            # output 1‑based indices
            print(u + 1, v + 1, c + 1)
            return

if __name__ == "__main__":
    solve()
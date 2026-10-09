import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitset adjacency, 1‑based
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(1, n + 1):
        # neighbours larger than a
        mask = adj[a] >> (a + 1)          # bits for vertices > a
        if mask == 0:
            continue
        # collect them in increasing order
        neigh = []
        v = a + 1
        while mask:
            if mask & 1:
                neigh.append(v)
            mask >>= 1
            v += 1

        ln = len(neigh)
        for i in range(ln):
            b = neigh[i]
            for j in range(i + 1, ln):
                c = neigh[j]
                if (adj[b] >> c) & 1:     # edge (b,c) exists
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
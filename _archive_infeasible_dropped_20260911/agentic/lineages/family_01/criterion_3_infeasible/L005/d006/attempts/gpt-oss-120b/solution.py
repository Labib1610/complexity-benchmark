import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n               # bitset for each vertex
    neigh = [[] for _ in range(n)]   # neighbour lists (sorted later)

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b, larger than b
            common = (adj[a] & adj[b]) & ~((1 << (b + 1)) - 1)
            if common:
                # lowest set bit -> smallest c
                low = (common & -common).bit_length() - 1
                # output 1‑based and ordered
                print(a + 1, b + 1, low + 1)
                return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n          # bitset adjacency
    neigh = [[] for _ in range(n)]   # neighbour lists (sorted later)

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(n):
        neigh[i].sort()

    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = common >> (b + 1)
            if mask:
                low = mask & -mask          # lowest set bit
                offset = low.bit_length() - 1
                c = b + 1 + offset
                # output 1‑based, sorted
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
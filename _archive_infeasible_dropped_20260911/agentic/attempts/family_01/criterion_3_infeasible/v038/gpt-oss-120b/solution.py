import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        if u < v:
            neigh[u].append(v)
        else:
            neigh[v].append(u)

    for a in range(n):
        for b in neigh[a]:          # b > a, already sorted because we added in input order; we sort to be safe
            # ensure neighbours are processed in increasing order
            # (input order may not be sorted)
            # We'll sort once per vertex after reading all edges
            pass

    # sort neighbour lists
    for lst in neigh:
        lst.sort()

    for a in range(n):
        for b in neigh[a]:
            common = adj[a] & adj[b]
            # clear bits 0..b
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [0] * n  # bitsets for each node
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        neigh_a = adj[a]
        # iterate over b > a
        for b in range(a + 1, n):
            if (neigh_a >> b) & 1:
                common = neigh_a & adj[b]
                # mask bits > b
                mask = common & ~((1 << (b + 1)) - 1)
                if mask:
                    # lowest set bit gives smallest c
                    c = (mask & -mask).bit_length() - 1
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()
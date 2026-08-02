import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix as list of bytearray
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = 1
        adj[v][u] = 1

    for a in range(1, n - 1):
        # neighbors of a that are greater than a
        neigh = [v for v in range(a + 1, n + 1) if adj[a][v]]
        ln = len(neigh)
        if ln < 2:
            continue
        for i in range(ln):
            b = neigh[i]
            for j in range(i + 1, ln):
                c = neigh[j]
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
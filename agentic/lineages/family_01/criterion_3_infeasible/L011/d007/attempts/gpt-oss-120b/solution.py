import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix using bytearray for O(1) checks
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if not adj[u][v]:
            adj[u][v] = adj[v][u] = 1
            deg[u] += 1
            deg[v] += 1

    # For each a in increasing order, try pairs of its neighbors (b,c) with b<c
    # such that (b,c) is NOT an edge.
    for a in range(1, n + 1):
        # collect neighbors of a sorted
        neigh = [v for v in range(1, n + 1) if adj[a][v]]
        ln = len(neigh)
        if ln < 2:
            continue
        # iterate pairs
        for i in range(ln):
            b = neigh[i]
            for j in range(i + 1, ln):
                c = neigh[j]
                if not adj[b][c]:
                    # found triple a,b,c; need output sorted a<b<c
                    triple = sorted((a, b, c))
                    print(triple[0], triple[1], triple[2])
                    return

if __name__ == "__main__":
    solve()
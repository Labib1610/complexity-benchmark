import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if adj[u][v]:
            continue  # ignore duplicate edges
        adj[u][v] = 1
        adj[v][u] = 1
        neigh[u].append(v)
        neigh[v].append(u)

    # sort neighbor lists once
    for lst in neigh:
        lst.sort()

    out = sys.stdout
    for a in range(1, n + 1):
        # consider only neighbors greater than a to maintain a < b < c
        na = [v for v in neigh[a] if v > a]
        sz = len(na)
        for i in range(sz):
            b = na[i]
            for j in range(i + 1, sz):
                c = na[j]
                if adj[b][c]:
                    out.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
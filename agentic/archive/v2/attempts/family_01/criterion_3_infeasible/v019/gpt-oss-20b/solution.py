import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    # adjacency matrix as list of bytearray for O(1) checks
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = 1
        adj[v][u] = 1
        neigh[u].append(v)
        neigh[v].append(u)

    for u in range(1, n + 1):
        # sort neighbors once for this u
        neigh[u].sort()
        neigh_u = neigh[u]
        sz = len(neigh_u)
        for i in range(sz):
            v = neigh_u[i]
            if v <= u:
                continue
            for j in range(i + 1, sz):
                w = neigh_u[j]
                if w <= v:
                    continue
                if adj[v][w]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    main()
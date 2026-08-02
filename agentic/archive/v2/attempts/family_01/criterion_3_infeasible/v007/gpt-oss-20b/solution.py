import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    neigh = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = 1
        adj[v][u] = 1
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(1, n + 1):
        neigh[i].sort()

    for a in range(1, n + 1):
        na = neigh[a]
        for b in na:
            if b <= a:
                continue
            nb = neigh[b]
            # For lexicographic order we need w > b
            for w in na:
                if w <= b:
                    continue
                if adj[b][w]:
                    print(a, b, w)
                    return

if __name__ == "__main__":
    solve()
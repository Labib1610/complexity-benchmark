import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [bytearray(n + 1) for _ in range(n + 1)]
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = next(it)
        v = next(it)
        if not adj[u][v]:
            adj[u][v] = adj[v][u] = 1
            neigh[u].append(v)
            neigh[v].append(u)

    for a in range(1, n - 1):
        lst = sorted(neigh[a])  # neighbors of a in ascending order
        # find indices where neighbor > a
        for i in range(len(lst)):
            b = lst[i]
            if b <= a:
                continue
            for j in range(i + 1, len(lst)):
                c = lst[j]
                if c <= a:
                    continue
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
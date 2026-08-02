import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].add(v)
        adj[v].add(u)

    # Pre-sort adjacency lists for deterministic iteration
    sorted_adj = [sorted(adj[i]) for i in range(n + 1)]

    for a in range(1, n + 1):
        # Consider only neighbors greater than a
        neigh = [v for v in sorted_adj[a] if v > a]
        ln = len(neigh)
        for i in range(ln):
            b = neigh[i]
            for j in range(i + 1, ln):
                c = neigh[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
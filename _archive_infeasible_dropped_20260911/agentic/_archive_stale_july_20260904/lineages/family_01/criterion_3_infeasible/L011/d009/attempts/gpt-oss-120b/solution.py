import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)

    # adjacency matrix for O(1) edge check
    mat = [[False] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            mat[u][v] = True

    for a in range(1, n + 1):
        # neighbors greater than a, sorted
        neigh = [v for v in adj[a] if v > a]
        neigh.sort()
        ln = len(neigh)
        for i in range(ln):
            b = neigh[i]
            for j in range(i + 1, ln):
                c = neigh[j]
                if mat[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
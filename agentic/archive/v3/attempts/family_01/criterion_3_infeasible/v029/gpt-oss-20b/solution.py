import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    # adjacency matrix
    adj = [bytearray(n+1) for _ in range(n+1)]
    # adjacency lists
    neigh = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u][v] = 1
        adj[v][u] = 1
        neigh[u].append(v)
        neigh[v].append(u)
    # sort neighbor lists
    for lst in neigh:
        lst.sort()
    # search lexicographically smallest triangle
    for a in range(1, n+1):
        # for each neighbor b > a
        for b in neigh[a]:
            if b <= a:
                continue
            # iterate over neighbors of a that are > b
            for c in neigh[a]:
                if c <= b:
                    continue
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
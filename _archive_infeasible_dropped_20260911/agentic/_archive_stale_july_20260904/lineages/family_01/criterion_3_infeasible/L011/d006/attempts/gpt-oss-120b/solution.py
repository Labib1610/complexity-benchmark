import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix for O(1) edge check
    adj_mat = [bytearray(n) for _ in range(n)]
    # adjacency lists (sorted)
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if not adj_mat[u][v]:
            adj_mat[u][v] = adj_mat[v][u] = 1
            adj[u].append(v)
            adj[v].append(u)

    for i in range(n):
        adj[i].sort()

    # search for lexicographically smallest triangle
    for a in range(n):
        for b in adj[a]:
            if b <= a:
                continue
            # iterate c > b that is neighbor of a
            # we can scan adjacency list of a starting after b
            # using binary search index
            # but n is small, simple loop
            for c in adj[a]:
                if c <= b:
                    continue
                if adj_mat[b][c]:
                    # found triangle a,b,c
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()
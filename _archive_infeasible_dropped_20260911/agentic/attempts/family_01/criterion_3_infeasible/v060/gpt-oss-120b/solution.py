import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n + 1)]
    # also build a boolean matrix for O(1) edge test (optional)
    adj_mat = [bytearray(n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
        adj_mat[u][v] = adj_mat[v][u] = 1

    # iterate a, then b in increasing order
    for a in range(1, n + 1):
        # neighbours larger than a, sorted
        for b in sorted(v for v in adj[a] if v > a):
            # intersection of neighbours
            # iterate over the smaller set for efficiency
            if len(adj[a]) < len(adj[b]):
                common = adj[a] & adj[b]
            else:
                common = adj[b] & adj[a]

            best_c = None
            for c in common:
                if c > b:
                    if best_c is None or c < best_c:
                        best_c = c
            if best_c is not None:
                # a < b < best_c holds
                sys.stdout.write(f"{a} {b} {best_c}")
                return

if __name__ == "__main__":
    solve()
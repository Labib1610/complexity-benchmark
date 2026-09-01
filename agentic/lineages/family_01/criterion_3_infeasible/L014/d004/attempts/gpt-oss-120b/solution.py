import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix: bytearray for fast O(1) test
    adj = [bytearray(n + 1) for _ in range(n + 1)]
    nbr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u][v] = adj[v][u] = 1
        nbr[u].append(v)
        nbr[v].append(u)

    # sort neighbour lists (they are small, O(m log deg) is fine)
    for i in range(1, n + 1):
        nbr[i].sort()

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if not adj[a][b]:
                continue
            # find smallest c > b that is neighbour of both a and b
            for c in nbr[a]:
                if c <= b:
                    continue
                if adj[b][c]:
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
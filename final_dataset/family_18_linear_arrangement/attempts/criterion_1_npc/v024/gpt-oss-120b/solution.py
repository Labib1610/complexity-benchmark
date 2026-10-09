import sys, itertools

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[False]*n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u][v] = adj[v][u] = True

    # try all permutations (feasible for n up to ~10)
    for perm in itertools.permutations(range(1, n+1)):
        pos = [0]*n
        for idx, zone in enumerate(perm):
            pos[idx] = zone  # zone assigned to crop idx+1
        # compute total length
        total = 0
        for u, v in edges:
            total += abs(pos[u] - pos[v])
            if total > B:
                break
        if total <= B:
            print("YES")
            print(' '.join(map(str, pos)))
            return
    print("NO")

if __name__ == "__main__":
    solve()
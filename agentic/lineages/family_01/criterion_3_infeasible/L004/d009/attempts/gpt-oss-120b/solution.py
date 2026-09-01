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
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)

    for a in range(1, n - 1):
        neigh = sorted(adj[a])
        # iterate b > a
        for i, b in enumerate(neigh):
            if b <= a:
                continue
            # iterate c > b among the same neighbour list
            for c in neigh[i + 1:]:
                if c in adj[b]:
                    # triangle (a,b,c) found – it is the smallest one
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
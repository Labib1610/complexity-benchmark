import sys

def solve() -> None:
    data = list(map(int, sys.stdin.read().split()))
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

    sorted_adj = [sorted(adj[i]) for i in range(n + 1)]

    for a in range(1, n + 1):
        neigh_a = adj[a]
        for b in sorted_adj[a]:
            if b <= a:
                continue
            for c in sorted_adj[b]:
                if c <= b:
                    continue
                if c in neigh_a:
                    sys.stdout.write(f"{a} {b} {c}\n")
                    return

if __name__ == "__main__":
    solve()
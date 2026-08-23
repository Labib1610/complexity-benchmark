import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_set = [set() for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj_set[u].add(v)
        adj_set[v].add(u)

    # Build sorted adjacency lists for lexicographic iteration
    for node in range(1, n + 1):
        if adj_set[node]:
            adj_list[node] = sorted(adj_set[node])

    for a in range(1, n + 1):
        neigh = adj_list[a]
        if len(neigh) < 2:
            continue
        # iterate over pairs (b,c) with b < c
        for i, b in enumerate(neigh):
            if b <= a:
                continue
            for c in neigh[i + 1:]:
                if c <= b:
                    continue
                if c in adj_set[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
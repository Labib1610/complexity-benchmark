def solve():
    n, m = map(int, input().split())
    incompatible = set()
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible.add(tuple(sorted((u, v))))

    best_cluster = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in incompatible and (a, c) in incompatible and (b, c) in incompatible:
                    if best_cluster is None:
                        best_cluster = (a, b, c)
                    else:
                        if (a, b, c) < best_cluster:
                            best_cluster = (a, b, c)

    print(best_cluster[0], best_cluster[1], best_cluster[2])

solve()
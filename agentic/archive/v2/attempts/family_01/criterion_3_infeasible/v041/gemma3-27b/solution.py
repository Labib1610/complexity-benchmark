def solve():
    n, m = map(int, input().split())
    conflicts = set()
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.add(tuple(sorted((u, v))))

    best_triple = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in conflicts and (a, c) in conflicts and (b, c) in conflicts:
                    if best_triple is None or (a, b, c) < best_triple:
                        best_triple = (a, b, c)

    print(best_triple[0], best_triple[1], best_triple[2])

solve()
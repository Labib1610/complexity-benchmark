def solve():
    n, m = map(int, input().split())
    restrictions = set()
    for _ in range(m):
        u, v = map(int, input().split())
        restrictions.add(tuple(sorted((u, v))))

    best_trio = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in restrictions and (a, c) in restrictions and (b, c) in restrictions:
                    if best_trio is None or (a, b, c) < best_trio:
                        best_trio = (a, b, c)

    print(best_trio[0], best_trio[1], best_trio[2])

solve()
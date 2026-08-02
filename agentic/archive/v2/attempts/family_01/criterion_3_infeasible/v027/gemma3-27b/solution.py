def solve():
    n, m = map(int, input().split())
    prohibited = set()
    for _ in range(m):
        u, v = map(int, input().split())
        prohibited.add(tuple(sorted((u, v))))

    best_triple = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if tuple(sorted((a, b))) in prohibited and \
                   tuple(sorted((a, c))) in prohibited and \
                   tuple(sorted((b, c))) in prohibited:
                    
                    if best_triple is None:
                        best_triple = (a, b, c)
                    else:
                        if a < best_triple[0]:
                            best_triple = (a, b, c)
                        elif a == best_triple[0] and b < best_triple[1]:
                            best_triple = (a, b, c)
                        elif a == best_triple[0] and b == best_triple[1] and c < best_triple[2]:
                            best_triple = (a, b, c)
    
    print(best_triple[0], best_triple[1], best_triple[2])

solve()
def solve():
    n, m = map(int, input().split())
    conflicts = set()
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.add(tuple(sorted((u, v))))
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if tuple(sorted((a, b))) in conflicts and \
                   tuple(sorted((a, c))) in conflicts and \
                   tuple(sorted((b, c))) in conflicts:
                    print(a, b, c)
                    return

solve()
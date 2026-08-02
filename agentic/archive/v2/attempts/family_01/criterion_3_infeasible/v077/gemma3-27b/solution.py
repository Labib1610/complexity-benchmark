def solve():
    n, m = map(int, input().split())
    incompatible = set()
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible.add(tuple(sorted((u, v))))
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in incompatible and (a, c) in incompatible and (b, c) in incompatible:
                    print(a, b, c)
                    return

solve()
def solve():
    n, m = map(int, input().split())
    incompatibilities = set()
    for _ in range(m):
        u, v = map(int, input().split())
        incompatibilities.add(tuple(sorted((u, v))))
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in incompatibilities and (a, c) in incompatibilities and (b, c) in incompatibilities:
                    print(a, b, c)
                    return

solve()
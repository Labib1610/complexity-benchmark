def solve():
    n, m = map(int, input().split())
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        edges.add(tuple(sorted((u, v))))
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in edges and (a, c) in edges and (b, c) in edges:
                    print(a, b, c)
                    return

solve()
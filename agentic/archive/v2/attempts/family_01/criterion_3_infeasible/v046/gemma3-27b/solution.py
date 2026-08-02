def solve():
    n, m = map(int, input().split())
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        edges.add(tuple(sorted((u, v))))
    
    ans = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if tuple(sorted((a, b))) in edges and tuple(sorted((a, c))) in edges and tuple(sorted((b, c))) in edges:
                    if ans is None:
                        ans = (a, b, c)
                    else:
                        if a < ans[0]:
                            ans = (a, b, c)
                        elif a == ans[0] and b < ans[1]:
                            ans = (a, b, c)
                        elif a == ans[0] and b == ans[1] and c < ans[2]:
                            ans = (a, b, c)
    
    print(ans[0], ans[1], ans[2])

solve()
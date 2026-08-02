def solve():
    n, m = map(int, input().split())
    prohibited = set()
    for _ in range(m):
        u, v = map(int, input().split())
        prohibited.add(tuple(sorted((u, v))))
    
    ans = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if tuple(sorted((a, b))) in prohibited and \
                   tuple(sorted((a, c))) in prohibited and \
                   tuple(sorted((b, c))) in prohibited:
                    if ans is None:
                        ans = (a, b, c)
                    else:
                        if (a, b, c) < ans:
                            ans = (a, b, c)
    
    print(ans[0], ans[1], ans[2])

solve()
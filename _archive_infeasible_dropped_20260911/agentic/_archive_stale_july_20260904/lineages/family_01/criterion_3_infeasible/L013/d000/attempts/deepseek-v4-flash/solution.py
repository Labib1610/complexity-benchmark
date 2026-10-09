n, m = map(int, input().split())
adj = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = True
    adj[v][u] = True

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if adj[a][b]:
            for c in range(b + 1, n + 1):
                if adj[a][c] and adj[b][c]:
                    print(a, b, c)
                    exit()
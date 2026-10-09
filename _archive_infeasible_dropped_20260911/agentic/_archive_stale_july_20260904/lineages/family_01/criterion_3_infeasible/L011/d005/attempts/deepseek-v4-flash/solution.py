n, m = map(int, input().split())
adj = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = True

# Iterate over all edges in increasing order
for u in range(1, n + 1):
    for v in range(u + 1, n + 1):
        if adj[u][v]:
            for w in range(v + 1, n + 1):
                if adj[u][w] and adj[v][w]:
                    print(u, v, w)
                    exit()
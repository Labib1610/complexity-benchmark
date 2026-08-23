n, m = map(int, input().split())
adj = [[False] * (n + 1) for _ in range(n + 1)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = True
    if u > v:
        u, v = v, u
    edges.append((u, v))

# Sort edges lexicographically
edges.sort()

for u, v in edges:
    for w in range(v + 1, n + 1):
        if adj[u][w] and adj[v][w]:
            print(u, v, w)
            exit()
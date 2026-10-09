n, m = map(int, input().split())
adj = [[False] * (n + 1) for _ in range(n + 1)]
neighbors = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = True
    neighbors[u].append(v)
    neighbors[v].append(u)

# Sort neighbors for lexicographic order
for i in range(1, n + 1):
    neighbors[i].sort()

# Find the smallest triangle
for a in range(1, n + 1):
    for b in neighbors[a]:
        if b <= a:
            continue
        for c in neighbors[b]:
            if c <= b:
                continue
            if adj[a][c]:
                print(a, b, c)
                exit()
n, m = map(int, input().split())
edges = set()
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    edges.add((u, v))
    adj[u].append(v)
    adj[v].append(u)

# Find the lexicographically smallest triangle
for a in range(1, n + 1):
    for i in range(len(adj[a])):
        b = adj[a][i]
        if b <= a:
            continue
        for j in range(i + 1, len(adj[a])):
            c = adj[a][j]
            if c <= b:
                continue
            if (b, c) in edges:
                print(a, b, c)
                exit()
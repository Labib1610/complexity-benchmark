n, m = map(int, input().split())
adj = [set() for _ in range(n)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].add(v)
    adj[v].add(u)
    edges.append((u, v))

# Sort edges by vertex order for lexicographic smallest triangle
edges.sort()

for u, v in edges:
    # Find common neighbor
    common = adj[u] & adj[v]
    if common:
        w = min(common)
        a, b, c = sorted([u+1, v+1, w+1])
        print(a, b, c)
        break
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

# Try to find a triangle
for u, v in edges:
    # Find common neighbor
    common = adj[u] & adj[v]
    if common:
        w = min(common)
        # Output sorted
        a, b, c = sorted([u, v, w])
        print(a + 1, b + 1, c + 1)
        break
n, m = map(int, input().split())
adj = [set() for _ in range(n)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].add(v)
    adj[v].add(u)
    if u > v:
        u, v = v, u
    edges.append((u, v))

edges.sort()

for u, v in edges:
    # find w > v such that w in adj[u] and w in adj[v]
    common = adj[u] & adj[v]
    for w in sorted(common):
        if w > v:
            print(u + 1, v + 1, w + 1)
            exit()
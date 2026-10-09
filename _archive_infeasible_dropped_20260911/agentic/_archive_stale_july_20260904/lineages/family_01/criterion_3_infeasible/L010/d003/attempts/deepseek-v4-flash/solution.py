n, m = map(int, input().split())
adj = [set() for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)
    if u > v:
        u, v = v, u
    edges.append((u, v))

edges.sort()

for u, v in edges:
    # Find smallest w > v connected to both u and v
    for w in sorted(adj[v]):
        if w > v and w in adj[u]:
            print(u, v, w)
            exit()
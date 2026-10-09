n, m = map(int, input().split())
adj = [set() for _ in range(n)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u > v:
        u, v = v, u
    edges.append((u, v))
    adj[u].add(v)
    adj[v].add(u)

edges.sort()

for u, v in edges:
    # find smallest w > v that is neighbor of both u and v
    for w in sorted(adj[v]):
        if w > v and w in adj[u]:
            print(u + 1, v + 1, w + 1)
            exit()
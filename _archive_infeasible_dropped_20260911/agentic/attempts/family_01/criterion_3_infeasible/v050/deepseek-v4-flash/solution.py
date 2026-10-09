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

best = None

for u, v in edges:
    # find w > v such that u-w and v-w exist
    for w in adj[u]:
        if w > v and w in adj[v]:
            if best is None or (u, v, w) < best:
                best = (u, v, w)

a, b, c = best
print(a + 1, b + 1, c + 1)
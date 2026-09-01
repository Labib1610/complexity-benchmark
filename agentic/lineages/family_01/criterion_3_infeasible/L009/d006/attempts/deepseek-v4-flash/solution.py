n, m = map(int, input().split())
adj = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)

for u in range(1, n + 1):
    for v in range(u + 1, n + 1):
        if v in adj[u]:
            for w in range(v + 1, n + 1):
                if w in adj[u] and w in adj[v]:
                    print(u, v, w)
                    exit()
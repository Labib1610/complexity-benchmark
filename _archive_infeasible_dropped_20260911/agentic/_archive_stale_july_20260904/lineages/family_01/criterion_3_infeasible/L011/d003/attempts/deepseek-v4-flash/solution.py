n, m = map(int, input().split())
adj = [set() for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

found = False
for u in range(1, n + 1):
    for v in sorted(adj[u]):
        if v > u:
            for w in sorted(adj[v]):
                if w > v and w in adj[u]:
                    print(u, v, w)
                    found = True
                    break
            if found:
                break
    if found:
        break
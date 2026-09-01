n, m = map(int, input().split())
adj = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].add(v)
    adj[v].add(u)

for a in range(n):
    for b in sorted(adj[a]):
        if b > a:
            for c in sorted(adj[a]):
                if c > b and c in adj[b]:
                    print(a+1, b+1, c+1)
                    exit()
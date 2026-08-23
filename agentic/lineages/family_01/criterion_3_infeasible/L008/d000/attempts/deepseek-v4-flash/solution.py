n, m = map(int, input().split())
adj = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u] |= 1 << v
    adj[v] |= 1 << u

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if (adj[a] >> b) & 1:
            common = adj[a] & adj[b]
            # find smallest c > b in common
            c = b + 1
            while c <= n and not ((common >> c) & 1):
                c += 1
            if c <= n:
                print(a, b, c)
                exit()
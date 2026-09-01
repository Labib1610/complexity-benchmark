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

best = None
for a in range(n):
    for b in adj[a]:
        if b > a:
            # find smallest c > b connected to both
            for c in adj[a]:
                if c > b and c in adj[b]:
                    if best is None or (a, b, c) < best:
                        best = (a, b, c)
                    break  # since adj[a] is a set, iteration order not sorted, so we need to check all
            # Actually we need to find the smallest c, so we should iterate sorted
            # Let's do sorted intersection
            common = sorted(adj[a] & adj[b])
            for c in common:
                if c > b:
                    if best is None or (a, b, c) < best:
                        best = (a, b, c)
                    break

# Output 1-based
a, b, c = best
print(a+1, b+1, c+1)
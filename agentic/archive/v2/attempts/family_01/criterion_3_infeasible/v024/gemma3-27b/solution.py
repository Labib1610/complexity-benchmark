def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    best_cluster = None

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (b in adj[a] and c in adj[a] and c in adj[b]):
                    if best_cluster is None:
                        best_cluster = (a, b, c)
                    else:
                        if (a, b, c) < best_cluster:
                            best_cluster = (a, b, c)

    print(best_cluster[0], best_cluster[1], best_cluster[2])

solve()
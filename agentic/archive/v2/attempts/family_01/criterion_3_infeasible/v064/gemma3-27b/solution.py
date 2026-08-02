def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((min(u, v), max(u, v)))
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    best_triplet = None
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if b in adj[a] and c in adj[a] and c in adj[b]:
                    if best_triplet is None:
                        best_triplet = (a, b, c)
                    else:
                        if (a, b, c) < best_triplet:
                            best_triplet = (a, b, c)
    
    print(best_triplet[0], best_triplet[1], best_triplet[2])

solve()
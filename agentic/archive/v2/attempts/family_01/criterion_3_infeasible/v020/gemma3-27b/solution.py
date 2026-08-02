def solve():
    n, m = map(int, input().split())
    conflicts = []
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts.append((min(u, v), max(u, v)))
    
    adj = [[] for _ in range(n + 1)]
    for u, v in conflicts:
        adj[u].append(v)
        adj[v].append(u)
    
    best_triple = None
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in adj[a]:
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        triple = (a, b, c)
                        if best_triple is None or triple < best_triple:
                            best_triple = triple
    
    print(*best_triple)

solve()
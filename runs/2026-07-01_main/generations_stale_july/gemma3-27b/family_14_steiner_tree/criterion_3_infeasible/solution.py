def solve():
    n, m, t = map(int, input().split())
    required_sites = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v))
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    disconnected_sites = []
    for site in required_sites:
        if not adj[site]:
            disconnected_sites.append(site)
    
    if disconnected_sites:
        print(min(disconnected_sites))
    else:
        print(-1)

solve()
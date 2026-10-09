def solve():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def is_covered(sensors):
        covered = [False] * (n + 1)
        for sensor in sensors:
            covered[sensor] = True
            for neighbor in adj[sensor]:
                covered[neighbor] = True
        
        for i in range(1, n + 1):
            if not covered[i]:
                return False
        return True
    
    import itertools
    
    for sensors in itertools.combinations(range(1, n + 1), min(k, n)):
        if is_covered(sensors):
            print("YES")
            print(*sensors)
            return
    
    print("NO")

solve()
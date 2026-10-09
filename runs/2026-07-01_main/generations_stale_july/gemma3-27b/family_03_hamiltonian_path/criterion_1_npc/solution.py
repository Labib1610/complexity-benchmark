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
    
    def find_route(path, visited):
        if len(path) == n:
            return path
        
        last_node = path[-1]
        for neighbor in adj[last_node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_visited = visited | {neighbor}
                result = find_route(new_path, new_visited)
                if result:
                    return result
        
        return None
    
    best_route = None
    
    for start_node in range(1, n + 1):
        route = find_route([start_node], {start_node})
        if route:
            if best_route is None or route < best_route:
                best_route = route
    
    if best_route:
        print("YES")
        print(*best_route)
    else:
        print("NO")

solve()
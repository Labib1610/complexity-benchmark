from collections import defaultdict, deque

def solve():
    import sys
    import threading
    
    def main():
        input = sys.stdin.read
        data = input().split()
        
        k = int(data[0])
        t = int(data[1])
        
        if t < k:
            print("NO")
            return
            
        index = 2
        routes = {}  # route -> vehicle
        dispatches = []  # list of (route, vehicle, driver)
        driver_options = defaultdict(list)  # route -> list of (vehicle, driver)
        
        for _ in range(t):
            x = int(data[index])
            y = int(data[index+1])
            z = int(data[index+2])
            index += 3
            dispatches.append((x, y, z))
            if x not in routes:
                routes[x] = y
            driver_options[x].append((y, z))
        
        # Check if we have exactly k routes
        if len(routes) < k:
            print("NO")
            return
            
        # Build bipartite graph for matching drivers to routes
        # Left side: routes (1 to k), Right side: drivers (1 to k)
        # Edge exists if there's a dispatch with that route and driver
        
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        
        # Group dispatches by (route, driver)
        route_driver_dispatch = {}
        for x, y, z in dispatches:
            route_driver_dispatch[(x, z)] = (x, y, z)
            graph[x].append(z)
            rev_graph[z].append(x)
            
        # Try to find a matching that covers all routes
        # This is a maximum bipartite matching problem
        
        match_route_to_driver = [-1] * (k + 1)
        match_driver_to_route = [-1] * (k + 1)
        
        def dfs(u, visited):
            for v in graph[u]:
                if visited[v]:
                    continue
                visited[v] = True
                if match_driver_to_route[v] == -1 or dfs(match_driver_to_route[v], visited):
                    match_route_to_driver[u] = v
                    match_driver_to_route[v] = u
                    return True
            return False
        
        matched = 0
        for route in range(1, k + 1):
            if route not in routes:
                continue
            visited = [False] * (k + 1)
            if dfs(route, visited):
                matched += 1
                
        if matched < k:
            print("NO")
            return
            
        print("YES")
        for route in range(1, k + 1):
            if route not in routes:
                continue
            driver = match_route_to_driver[route]
            vehicle = routes[route]
            print(route, vehicle, driver)

    threading.Thread(target=main).start()

solve()
import sys
sys.setrecursionlimit(10000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    # For each driver, store the truck (same for all their plans)
    driver_truck = [0] * (k + 1)
    # adjacency: driver -> list of routes
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        driver_truck[x] = y
        adj[x].append(z)
    
    # Matching: route -> driver
    match_route = [0] * (k + 1)
    
    def dfs(driver, visited):
        for route in adj[driver]:
            if not visited[route]:
                visited[route] = True
                if match_route[route] == 0 or dfs(match_route[route], visited):
                    match_route[route] = driver
                    return True
        return False
    
    match_count = 0
    for driver in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(driver, visited):
            match_count += 1
    
    if match_count != k:
        print("NO")
        return
    
    print("YES")
    for route in range(1, k + 1):
        driver = match_route[route]
        truck = driver_truck[driver]
        print(driver, truck, route)

if __name__ == "__main__":
    solve()
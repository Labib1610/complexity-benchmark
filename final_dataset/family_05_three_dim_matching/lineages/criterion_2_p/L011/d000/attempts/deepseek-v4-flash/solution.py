import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    plans = []
    driver_to_truck = {}
    adj = [[] for _ in range(k + 1)]  # driver -> list of routes

    for _ in range(t):
        x, y, z = map(int, input().split())
        plans.append((x, y, z))
        driver_to_truck[x] = y
        adj[x].append(z)

    # Matching: route -> driver
    match_route = [0] * (k + 1)  # match_route[route] = driver

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
        truck = driver_to_truck[driver]
        print(driver, truck, route)

if __name__ == "__main__":
    solve()
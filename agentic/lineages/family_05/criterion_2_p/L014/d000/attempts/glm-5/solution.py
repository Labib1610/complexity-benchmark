import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # route -> list of drivers (vehicle is fixed per route)
    route_drivers = [[] for _ in range(k + 1)]
    route_vehicle = [0] * (k + 1)
    
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        route_drivers[x].append(z)
        route_vehicle[x] = y
    
    # Check all routes have at least one feasible dispatch
    for x in range(1, k + 1):
        if not route_drivers[x]:
            print("NO")
            return
    
    # Bipartite matching: routes (left) to drivers (right)
    # Routes 1..k, Drivers 1..k
    match_driver = [0] * (k + 1)  # driver -> route
    match_route = [0] * (k + 1)    # route -> driver
    
    # Build adjacency for routes
    adj = [None] * (k + 1)
    for x in range(1, k + 1):
        adj[x] = route_drivers[x]
    
    def bpm(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_driver[v] == 0 or bpm(match_driver[v], visited):
                    match_driver[v] = u
                    match_route[u] = v
                    return True
        return False
    
    result = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if bpm(u, visited):
            result += 1
        else:
            break
    
    if result == k:
        print("YES")
        out = []
        for x in range(1, k + 1):
            out.append(f"{x} {route_vehicle[x]} {match_route[x]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")

solve()
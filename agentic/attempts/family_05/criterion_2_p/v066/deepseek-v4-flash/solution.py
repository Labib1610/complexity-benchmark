import sys
sys.setrecursionlimit(10000000)

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each crew, store possible routes
    crew_routes = [[] for _ in range(k)]
    # Also store the airframe for each crew (given by Stage 1)
    crew_airframe = [0] * k
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        z -= 1
        crew_routes[x].append(z)
        crew_airframe[x] = y  # same for all proposals of this crew
    
    # match_route[route] = crew assigned to this route, or -1
    match_route = [-1] * k
    
    def dfs(crew, visited):
        for route in crew_routes[crew]:
            if visited[route]:
                continue
            visited[route] = True
            if match_route[route] == -1 or dfs(match_route[route], visited):
                match_route[route] = crew
                return True
        return False
    
    for crew in range(k):
        visited = [False] * k
        if not dfs(crew, visited):
            print("NO")
            return
    
    # If we reach here, matching exists
    print("YES")
    for route, crew in enumerate(match_route):
        print(crew + 1, crew_airframe[crew], route + 1)

if __name__ == "__main__":
    main()
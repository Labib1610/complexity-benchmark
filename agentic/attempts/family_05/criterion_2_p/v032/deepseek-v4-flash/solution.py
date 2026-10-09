import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # ground_to_key[x] = y
    ground_to_key = [0] * (k + 1)
    # adj[x] = list of satellites z for ground station x
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        ground_to_key[x] = y
        adj[x].append(z)
    
    # Bipartite matching: ground stations -> satellites
    match_sat = [0] * (k + 1)  # match_sat[z] = x if satellite z matched to ground x
    match_ground = [0] * (k + 1)  # match_ground[x] = z
    
    def dfs(x, visited):
        for z in adj[x]:
            if not visited[z]:
                visited[z] = True
                if match_sat[z] == 0 or dfs(match_sat[z], visited):
                    match_sat[z] = x
                    match_ground[x] = z
                    return True
        return False
    
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(x, visited):
            print("NO")
            return
    
    # If we matched all ground stations, output YES
    print("YES")
    for x in range(1, k + 1):
        z = match_ground[x]
        y = ground_to_key[x]
        print(x, y, z)

if __name__ == "__main__":
    solve()
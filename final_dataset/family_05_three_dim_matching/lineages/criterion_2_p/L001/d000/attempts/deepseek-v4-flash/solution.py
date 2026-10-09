import sys
sys.setrecursionlimit(1000000)

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each drone, store the list of frequencies it can use
    freq_for_drone = [[] for _ in range(k + 1)]
    station_for_drone = [0] * (k + 1)
    
    for _ in range(t):
        d, c, f = map(int, input().split())
        station_for_drone[d] = c
        freq_for_drone[d].append(f)
    
    # Matching: frequency -> drone
    match_freq = [0] * (k + 1)
    
    def dfs(drone, visited):
        for f in freq_for_drone[drone]:
            if not visited[f]:
                visited[f] = True
                if match_freq[f] == 0 or dfs(match_freq[f], visited):
                    match_freq[f] = drone
                    return True
        return False
    
    for d in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(d, visited):
            print("NO")
            return
    
    print("YES")
    for f in range(1, k + 1):
        d = match_freq[f]
        print(d, station_for_drone[d], f)

if __name__ == "__main__":
    main()
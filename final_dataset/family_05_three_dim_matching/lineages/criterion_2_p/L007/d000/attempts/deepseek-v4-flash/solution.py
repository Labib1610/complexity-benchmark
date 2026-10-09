import sys
sys.setrecursionlimit(10000000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each pilot, store the set of missions they can take
    pilot_missions = [[] for _ in range(k)]
    for _ in range(t):
        p, s, m = map(int, input().split())
        pilot_missions[p-1].append(m-1)
    
    # match_mission[pilot] = mission assigned to this pilot, or -1
    match_mission = [-1] * k
    # match_pilot[mission] = pilot assigned to this mission, or -1
    match_pilot = [-1] * k
    
    def dfs(pilot, visited):
        for mission in pilot_missions[pilot]:
            if not visited[mission]:
                visited[mission] = True
                if match_pilot[mission] == -1 or dfs(match_pilot[mission], visited):
                    match_pilot[mission] = pilot
                    match_mission[pilot] = mission
                    return True
        return False
    
    for pilot in range(k):
        visited = [False] * k
        if not dfs(pilot, visited):
            print("NO")
            return
    
    # If we matched all pilots, output the result
    print("YES")
    for p in range(k):
        s = p + 1  # pilot p is tied to starfighter p+1 (since each pilot has a distinct starfighter)
        m = match_mission[p] + 1
        print(p+1, s, m)

if __name__ == "__main__":
    solve()
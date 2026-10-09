import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # pilot -> mech mapping
    pilot_mech = [0] * (k + 1)
    # pilot -> list of phases
    pilot_phases = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        pilot_mech[x] = y
        pilot_phases[x].append(z)
    
    # Bipartite matching: pilots (1..k) to phases (1..k)
    match_phase = [0] * (k + 1)  # phase -> pilot
    match_pilot = [0] * (k + 1)  # pilot -> phase
    
    def dfs(pilot, visited):
        for phase in pilot_phases[pilot]:
            if not visited[phase]:
                visited[phase] = True
                if match_phase[phase] == 0 or dfs(match_phase[phase], visited):
                    match_phase[phase] = pilot
                    match_pilot[pilot] = phase
                    return True
        return False
    
    for pilot in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(pilot, visited):
            print("NO")
            return
    
    # If we reach here, matching exists
    print("YES")
    for pilot in range(1, k + 1):
        phase = match_pilot[pilot]
        mech = pilot_mech[pilot]
        print(pilot, mech, phase)

if __name__ == "__main__":
    solve()
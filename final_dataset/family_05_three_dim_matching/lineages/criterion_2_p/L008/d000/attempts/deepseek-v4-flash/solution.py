import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    # For each specialist, store allowed time slots
    allowed = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[x].append(z)
    
    # Bipartite matching: specialists -> time slots
    match_time = [0] * (k + 1)  # which specialist is assigned to each time slot
    def dfs(spec, visited):
        for time_slot in allowed[spec]:
            if not visited[time_slot]:
                visited[time_slot] = True
                if match_time[time_slot] == 0 or dfs(match_time[time_slot], visited):
                    match_time[time_slot] = spec
                    return True
        return False
    
    result = []
    for spec in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(spec, visited):
            print("NO")
            return
    
    # Build output
    # We need to know machine for each specialist
    # We can store machine per specialist from input
    machine_of = [0] * (k + 1)
    # Re-read input? We already consumed it. We can store during reading.
    # Let's redo reading with storage.
    
    # Actually, we need to re-read. Let's restructure.
    
if __name__ == "__main__":
    solve()
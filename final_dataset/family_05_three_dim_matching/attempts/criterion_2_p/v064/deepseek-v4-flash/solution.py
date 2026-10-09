import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each specialist, store possible time slots
    adj = [[] for _ in range(k)]
    machine_of = [0] * k  # machine assigned to each specialist (0-indexed)
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        machine_of[x] = y
        adj[x].append(z)
    
    # Bipartite matching: specialists -> time slots
    match_slot = [-1] * k  # which specialist is assigned to each time slot
    match_spec = [-1] * k  # which time slot is assigned to each specialist
    
    def dfs(spec, visited):
        for slot in adj[spec]:
            if not visited[slot]:
                visited[slot] = True
                if match_slot[slot] == -1 or dfs(match_slot[slot], visited):
                    match_slot[slot] = spec
                    match_spec[spec] = slot
                    return True
        return False
    
    for spec in range(k):
        visited = [False] * k
        if not dfs(spec, visited):
            print("NO")
            return
    
    print("YES")
    for spec in range(k):
        slot = match_spec[spec]
        print(spec + 1, machine_of[spec] + 1, slot + 1)

if __name__ == "__main__":
    solve()
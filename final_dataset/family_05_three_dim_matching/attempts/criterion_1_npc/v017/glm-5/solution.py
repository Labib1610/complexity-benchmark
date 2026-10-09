import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    configs = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        configs.append((x, y, z))
    
    # Build adjacency list: arm -> list of (sensor, module, config_index)
    adj = [[] for _ in range(k + 1)]
    for idx, (x, y, z) in enumerate(configs):
        adj[x].append((y, z, idx))
    
    match_y = [-1] * (k + 1)  # which arm uses sensor y
    match_z = [-1] * (k + 1)  # which arm uses module z
    
    result = [None] * (k + 1)  # result[arm] = (y, z)
    
    def dfs(arm, visited_y, visited_z):
        for y, z, _ in adj[arm]:
            if visited_y[y] or visited_z[z]:
                continue
            visited_y[y] = True
            visited_z[z] = True
            other_arm_y = match_y[y]
            other_arm_z = match_z[z]
            
            if other_arm_y == -1 and other_arm_z == -1:
                match_y[y] = arm
                match_z[z] = arm
                result[arm] = (y, z)
                return True
            elif other_arm_y == other_arm_z:
                # Both y and z are matched to the same arm, we can try to reassign that arm
                other_arm = other_arm_y
                old_y, old_z = result[other_arm]
                match_y[old_y] = -1
                match_z[old_z] = -1
                result[other_arm] = None
                
                if dfs(other_arm, visited_y, visited_z):
                    match_y[y] = arm
                    match_z[z] = arm
                    result[arm] = (y, z)
                    return True
                
                # Backtrack
                match_y[old_y] = other_arm
                match_z[old_z] = other_arm
                result[other_arm] = (old_y, old_z)
            # If other_arm_y != other_arm_z, this creates a conflict we can't resolve simply
        return False
    
    for arm in range(1, k + 1):
        visited_y = [False] * (k + 1)
        visited_z = [False] * (k + 1)
        if not dfs(arm, visited_y, visited_z):
            print("NO")
            return
    
    print("YES")
    for arm in range(1, k + 1):
        y, z = result[arm]
        print(f"{arm} {y} {z}")

if __name__ == "__main__":
    solve()
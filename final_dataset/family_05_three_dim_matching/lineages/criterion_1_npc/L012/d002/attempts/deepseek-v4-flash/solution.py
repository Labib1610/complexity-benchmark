import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    points_by_x = [[] for _ in range(k+1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        points_by_x[x].append((y, z))
    
    # If any x has no points, impossible
    for x in range(1, k+1):
        if not points_by_x[x]:
            print("NO")
            return
    
    # Sort points for deterministic order
    for x in range(1, k+1):
        points_by_x[x].sort()
    
    used_y = [False] * (k+1)
    used_z = [False] * (k+1)
    chosen = [None] * (k+1)
    
    # Precompute for each x the list of (y,z) that are still possible given used_y, used_z
    # We'll do DFS with pruning.
    
    def dfs(x):
        if x > k:
            return True
        # Prune: count remaining y and z availability
        remaining_y = sum(1 for i in range(1, k+1) if not used_y[i])
        remaining_z = sum(1 for i in range(1, k+1) if not used_z[i])
        remaining_x = k - x + 1
        if remaining_y < remaining_x or remaining_z < remaining_x:
            return False
        
        for y, z in points_by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen[x] = (x, y, z)
                if dfs(x+1):
                    return True
                used_y[y] = False
                used_z[z] = False
        return False
    
    if dfs(1):
        print("YES")
        for x in range(1, k+1):
            print(*chosen[x])
    else:
        print("NO")

if __name__ == "__main__":
    solve()
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    paths = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        paths.append((x, y, z))
    
    # We need to select exactly k paths such that:
    # - Each x from 1..k appears exactly once
    # - Each y from 1..k appears exactly once
    # - Each z from 1..k appears exactly once
    
    # Build adjacency: for each x (1..k), which paths have that x
    paths_by_x = [[] for _ in range(k + 1)]
    for idx, (x, y, z) in enumerate(paths):
        paths_by_x[x].append((idx, y, z))
    
    # Check if any x has no paths
    for x in range(1, k + 1):
        if not paths_by_x[x]:
            print("NO")
            return
    
    # Bipartite matching between y and z
    # For each x, we need to pick one path, and the y's and z's must all be distinct
    
    match_y = [0] * (k + 1)  # match_y[y] = x that uses this y
    match_z = [0] * (k + 1)  # match_z[z] = x that uses this z
    match_path = [None] * (k + 1)  # match_path[x] = (y, z) path index
    
    def dfs(x, seen_y, seen_z):
        for idx, y, z in paths_by_x[x]:
            if seen_y[y] or seen_z[z]:
                continue
            seen_y[y] = True
            seen_z[z] = True
            
            conflict_y = match_y[y]
            conflict_z = match_z[z]
            
            if conflict_y == 0 and conflict_z == 0:
                # Both y and z are free
                match_y[y] = x
                match_z[z] = x
                match_path[x] = (idx, y, z)
                return True
            elif conflict_y == conflict_z:
                # Same x conflicts with both, need to reassign it
                old_x = conflict_y
                old_idx, old_y, old_z = match_path[old_x]
                # Unassign old
                match_y[old_y] = 0
                match_z[old_z] = 0
                match_path[old_x] = None
                # Assign new
                match_y[y] = x
                match_z[z] = x
                match_path[x] = (idx, y, z)
                # Try to reassign old_x
                if dfs(old_x, seen_y, seen_z):
                    return True
                # Revert
                match_y[y] = 0
                match_z[z] = 0
                match_path[x] = None
                match_y[old_y] = old_x
                match_z[old_z] = old_x
                match_path[old_x] = (old_idx, old_y, old_z)
            elif conflict_y == 0:
                # Only z is taken by conflict_z
                old_x = conflict_z
                old_idx, old_y, old_z = match_path[old_x]
                # Unassign old
                match_y[old_y] = 0
                match_z[old_z] = 0
                match_path[old_x] = None
                # Assign new
                match_y[y] = x
                match_z[z] = x
                match_path[x] = (idx, y, z)
                # Try to reassign old_x
                if dfs(old_x, seen_y, seen_z):
                    return True
                # Revert
                match_y[y] = 0
                match_z[z] = 0
                match_path[x] = None
                match_y[old_y] = old_x
                match_z[old_z] = old_x
                match_path[old_x] = (old_idx, old_y, old_z)
            elif conflict_z == 0:
                # Only y is taken by conflict_y
                old_x = conflict_y
                old_idx, old_y, old_z = match_path[old_x]
                # Unassign old
                match_y[old_y] = 0
                match_z[old_z] = 0
                match_path[old_x] = None
                # Assign new
                match_y[y] = x
                match_z[z] = x
                match_path[x] = (idx, y, z)
                # Try to reassign old_x
                if dfs(old_x, seen_y, seen_z):
                    return True
                # Revert
                match_y[y] = 0
                match_z[z] = 0
                match_path[x] = None
                match_y[old_y] = old_x
                match_z[old_z] = old_x
                match_path[old_x] = (old_idx, old_y, old_z)
            else:
                # Both y and z are taken by different x's
                old_x_y = conflict_y
                old_x_z = conflict_z
                old_idx_y, old_y_y, old_z_y = match_path[old_x_y]
                old_idx_z, old_y_z, old_z_z = match_path[old_x_z]
                # Unassign both
                match_y[old_y_y] = 0
                match_z[old_z_y] = 0
                match_path[old_x_y] = None
                match_y[old_y_z] = 0
                match_z[old_z_z] = 0
                match_path[old_x_z] = None
                # Assign new
                match_y[y] = x
                match_z[z] = x
                match_path[x] = (idx, y, z)
                # Try to reassign both
                if dfs(old_x_y, seen_y, seen_z) and dfs(old_x_z, seen_y, seen_z):
                    return True
                # Revert
                match_y[y] = 0
                match_z[z] = 0
                match_path[x] = None
                match_y[old_y_y] = old_x_y
                match_z[old_z_y] = old_x_y
                match_path[old_x_y] = (old_idx_y, old_y_y, old_z_y)
                match_y[old_y_z] = old_x_z
                match_z[old_z_z] = old_x_z
                match_path[old_x_z] = (old_idx_z, old_y_z, old_z_z)
        return False
    
    for x in range(1, k + 1):
        seen_y = [False] * (k + 1)
        seen_z = [False] * (k + 1)
        if not dfs(x, seen_y, seen_z):
            print("NO")
            return
    
    # Verify all matched
    for x in range(1, k + 1):
        if match_path[x] is None:
            print("NO")
            return
    
    print("YES")
    for x in range(1, k + 1):
        idx, y, z = match_path[x]
        print(y, z, x)

if __name__ == "__main__":
    solve()
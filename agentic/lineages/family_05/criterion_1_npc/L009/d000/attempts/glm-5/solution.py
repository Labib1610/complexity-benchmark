import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Build adjacency list: for each specialist x, list of (y, z) pairs
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        adj[x].append((y, z))
    
    # Matching arrays
    match_y = [0] * (k + 1)  # match_y[y] = z matched with y
    match_z = [0] * (k + 1)  # match_z[z] = y matched with z
    
    def dfs(x, seen_y, seen_z):
        for y, z in adj[x]:
            if seen_y[y] or seen_z[z]:
                continue
            seen_y[y] = True
            seen_z[z] = True
            # If y or z is free, or we can reassign
            if match_y[y] == 0:
                match_y[y] = z
                match_z[z] = y
                return True
            # Try to reassign: y is matched to match_y[y] (some z')
            # We need to find a new match for that z'
            old_z = match_y[y]
            # Temporarily unmatch
            match_y[y] = 0
            match_z[old_z] = 0
            # Try to find new match for old_z
            # old_z was matched to y, now we need to find a new y' for old_z
            # Search for a y' that can be matched to old_z
            found = False
            for y2 in range(1, k + 1):
                if y2 == y:
                    continue
                if match_y[y2] == 0:
                    # Check if (y2, old_z) is a valid edge
                    # We need to check if there exists x' such that (x', y2, old_z) is allowed
                    # But we don't have reverse lookup efficiently
                    # Instead, let's try a different approach
                    pass
            # This approach is getting complicated. Let me reconsider.
            
            # Actually, let's use a cleaner DFS for 3D matching
            # The key insight: we're matching (y, z) pairs to x
            # When we try to assign (y, z) to x, if (y, z) is already assigned to some x',
            # we try to find a new (y', z') for x'
            
            # Let me restart with a cleaner implementation
            pass
        return False
    
    # Let me implement a cleaner version
    # match[x] = (y, z) assigned to specialist x
    match_x = [None] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    
    def dfs2(x, visited):
        for y, z in adj[x]:
            if used_y[y] and used_z[z]:
                continue
            if used_y[y] or used_z[z]:
                continue
            # Both y and z are free
            used_y[y] = True
            used_z[z] = True
            match_x[x] = (y, z)
            return True
        
        # Try to reassign: find a conflict and resolve
        for y, z in adj[x]:
            if used_y[y] and used_z[z]:
                continue
            if used_y[y]:
                # y is used, z is free
                # Find who is using y
                for x2 in range(1, k + 1):
                    if match_x[x2] is not None and match_x[x2][0] == y:
                        # Try to reassign x2
                        old_match = match_x[x2]
                        match_x[x2] = None
                        used_y[y] = False
                        used_z[old_match[1]] = False
                        if dfs2(x2, visited):
                            used_y[y] = True
                            used_z[z] = True
                            match_x[x] = (y, z)
                            return True
                        # Restore
                        match_x[x2] = old_match
                        used_y[y] = True
                        used_z[old_match[1]] = True
                continue
            if used_z[z]:
                # z is used, y is free
                for x2 in range(1, k + 1):
                    if match_x[x2] is not None and match_x[x2][1] == z:
                        old_match = match_x[x2]
                        match_x[x2] = None
                        used_y[old_match[0]] = False
                        used_z[z] = False
                        if dfs2(x2, visited):
                            used_y[y] = True
                            used_z[z] = True
                            match_x[x] = (y, z)
                            return True
                        match_x[x2] = old_match
                        used_y[old_match[0]] = True
                        used_z[z] = True
                continue
        
        return False
    
    # The above is still not quite right. Let me think more carefully.
    # This is a 3D matching problem. For small k, we can use a cleaner approach.
    
    # Reset and use a proper DFS with backtracking
    match_x = [None] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    
    def dfs3(x):
        if x > k:
            return True
        for y, z in adj[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                match_x[x] = (y, z)
                if dfs3(x + 1):
                    return True
                used_y[y] = False
                used_z[z] = False
                match_x[x] = None
        return False
    
    if dfs3(1):
        print("YES")
        for x in range(1, k + 1):
            y, z = match_x[x]
            print(x, y, z)
    else:
        print("NO")

solve()
from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    # Read all allowed combinations
    allowed = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed.append((x, y, z))
    
    # Special case: if k=1, just check if the only combination works
    if k == 1:
        if t >= 1 and (1, 1, 1) in allowed:
            print("YES")
            print("1 1 1")
        else:
            print("NO")
        return
    
    # Build a graph representation
    # For each specialist x, store which (y,z) pairs are allowed
    graph = defaultdict(list)
    for x, y, z in allowed:
        graph[x].append((y, z))
    
    # Try all possible matchings using backtracking
    # We'll use a 3D matching approach
    
    # Keep track of which machines and time slots are used
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    result = []
    
    def backtrack(x):
        # If we've assigned all specialists, we're done
        if x > k:
            return True
            
        # Try each allowed (y, z) pair for specialist x
        for y, z in graph[x]:
            # Check if machine y and time slot z are available
            if not used_y[y] and not used_z[z]:
                # Use this combination
                used_y[y] = True
                used_z[z] = True
                result.append((x, y, z))
                
                # Recurse to the next specialist
                if backtrack(x + 1):
                    return True
                    
                # Backtrack
                used_y[y] = False
                used_z[z] = False
                result.pop()
        
        return False
    
    # Start backtracking from specialist 1
    if backtrack(1):
        print("YES")
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

solve()
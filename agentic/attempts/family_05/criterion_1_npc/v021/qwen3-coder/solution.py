def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    pockets = []
    index = 2
    for i in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        pockets.append((x, y, z))
        index += 3
    
    # If we need 0 pockets, it's always possible
    if k == 0:
        print("YES")
        return
        
    # If we don't have enough pockets, impossible
    if t < k:
        print("NO")
        return
    
    # Try to find a matching using backtracking with pruning
    # We'll model this as a bipartite matching problem
    
    # For each pocket, we can think of it as connecting x-coordinate to a (y,z) pair
    # But actually, it's a 3D matching problem - we want to select k pockets such that
    # all x, y, z coordinates are unique
    
    # Let's use backtracking with constraint propagation
    
    def backtrack(selected, used_x, used_y, used_z, pos):
        if len(selected) == k:
            return selected[:]
        
        if pos >= t:
            return None
            
        # Pruning: if even selecting all remaining pockets won't give us k,
        # then it's impossible
        if len(selected) + (t - pos) < k:
            return None
            
        # Try including current pocket
        x, y, z = pockets[pos]
        if x not in used_x and y not in used_y and z not in used_z:
            selected.append((x, y, z))
            used_x.add(x)
            used_y.add(y)
            used_z.add(z)
            
            result = backtrack(selected, used_x, used_y, used_z, pos + 1)
            if result is not None:
                return result
                
            selected.pop()
            used_x.remove(x)
            used_y.remove(y)
            used_z.remove(z)
        
        # Try not including current pocket
        result = backtrack(selected, used_x, used_y, used_z, pos + 1)
        return result
    
    # Optimization: sort pockets to try "better" ones first
    # This doesn't change correctness but might help with early pruning
    
    result = backtrack([], set(), set(), set(), 0)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for x, y, z in result:
            print(x, y, z)

solve()
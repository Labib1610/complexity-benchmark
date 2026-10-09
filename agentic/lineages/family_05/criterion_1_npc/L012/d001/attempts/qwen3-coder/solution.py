from collections import defaultdict
import sys

def solve():
    k, t = map(int, input().split())
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    pockets = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        pockets.append((x, y, z))
    
    # Create dictionaries to store pockets by each coordinate
    by_x = defaultdict(list)
    by_y = defaultdict(list)
    by_z = defaultdict(list)
    
    for i, (x, y, z) in enumerate(pockets):
        by_x[x].append(i)
        by_y[y].append(i)
        by_z[z].append(i)
    
    # Try to find a valid assignment using backtracking
    # We'll try to assign each depth (1 to k) to a unique pocket
    # such that no two pockets share x, y, or z coordinates
    
    # This is essentially finding a matching in a 3-dimensional bipartite graph
    # We can model this as finding a maximum matching where each selected pocket
    # has a unique x, y, and z coordinate
    
    def backtrack(selected, used_x, used_y, used_z, pos):
        if pos == k:
            return selected[:]
        
        # Try each available pocket for position 'pos'
        for i in range(t):
            x, y, z = pockets[i]
            if i not in selected and x not in used_x and y not in used_y and z not in used_z:
                selected.append(i)
                used_x.add(x)
                used_y.add(y)
                used_z.add(z)
                
                result = backtrack(selected, used_x, used_y, used_z, pos + 1)
                if result:
                    return result
                
                selected.pop()
                used_x.remove(x)
                used_y.remove(y)
                used_z.remove(z)
        
        return None
    
    # Optimization: if any coordinate has more than k values, it's impossible
    if len(by_x) < k or len(by_y) < k or len(by_z) < k:
        print("NO")
        return
    
    # More precise check: each coordinate value should appear in at least one pocket
    # But actually, we just need to be able to select k pockets with distinct coords
    
    result = backtrack([], set(), set(), set(), 0)
    
    if result:
        print("YES")
        for idx in result:
            x, y, z = pockets[idx]
            print(x, y, z)
    else:
        print("NO")

solve()
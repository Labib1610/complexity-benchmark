from collections import defaultdict

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
    
    # Create mappings for each coordinate
    x_pockets = defaultdict(list)
    y_pockets = defaultdict(list)
    z_pockets = defaultdict(list)
    
    for i, (x, y, z) in enumerate(pockets):
        x_pockets[x].append(i)
        y_pockets[y].append(i)
        z_pockets[z].append(i)
    
    # Try to find a valid assignment using backtracking
    # We'll try to assign each depth (1 to k) to a unique pocket
    # such that all x, y, z coordinates are unique
    
    def backtrack(depth, used_x, used_y, used_z, selected):
        if depth > k:
            return len(selected) == k
        
        # For current depth, try all pockets with this depth
        for pocket_idx in x_pockets[depth]:
            x, y, z = pockets[pocket_idx]
            if y not in used_y and z not in used_z:
                # This pocket can be selected
                used_x.add(x)
                used_y.add(y)
                used_z.add(z)
                selected.append(pocket_idx)
                
                if backtrack(depth + 1, used_x, used_y, used_z, selected):
                    return True
                
                # Backtrack
                used_x.remove(x)
                used_y.remove(y)
                used_z.remove(z)
                selected.pop()
        
        return False
    
    # Also try another approach - build a bipartite matching problem
    # Actually, let's think differently - this is essentially finding a 3D matching
    # We can model this as finding a permutation where each element satisfies constraints
    
    # Let's use a different backtracking approach
    # Try to build a solution incrementally by depth
    
    used_y = set()
    used_z = set()
    selected_indices = []
    
    # For each depth from 1 to k, pick a pocket with that depth
    # that doesn't conflict with already picked pockets
    def can_select(pocket_idx):
        x, y, z = pockets[pocket_idx]
        return y not in used_y and z not in used_z
    
    def select_pocket(pocket_idx):
        x, y, z = pockets[pocket_idx]
        used_y.add(y)
        used_z.add(z)
        selected_indices.append(pocket_idx)
    
    def deselect_pocket(pocket_idx):
        x, y, z = pockets[pocket_idx]
        used_y.remove(y)
        used_z.remove(z)
        selected_indices.remove(pocket_idx)
    
    # Recursive function to try filling depths 1 to k
    def solve_depth(depth):
        if depth > k:
            return len(selected_indices) == k
        
        # Try each pocket with the required depth
        for pocket_idx in x_pockets[depth]:
            if can_select(pocket_idx):
                select_pocket(pocket_idx)
                if solve_depth(depth + 1):
                    return True
                deselect_pocket(pocket_idx)
        
        return False
    
    if solve_depth(1):
        print("YES")
        for idx in selected_indices:
            x, y, z = pockets[idx]
            print(x, y, z)
    else:
        print("NO")

solve()
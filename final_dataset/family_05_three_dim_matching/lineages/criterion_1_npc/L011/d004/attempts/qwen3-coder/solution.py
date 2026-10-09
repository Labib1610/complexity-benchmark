from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    configs = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        configs.append((x, y, z))
        idx += 3
    
    # We need to find a permutation of [1..k] for each of the three parameters
    # That means we're looking for a k-length subset of configs where:
    # - frequencies are a permutation of [1..k]
    # - modulations are a permutation of [1..k]
    # - encryptions are a permutation of [1..k]
    
    # This is essentially finding a perfect matching in a 3-dimensional bipartite graph
    # We can model this as finding a permutation matrix in each dimension
    
    # For small k (up to 22), we can try all permutations for one dimension
    # and check if we can complete the selection
    
    # Let's create mappings for faster lookup
    config_set = set(configs)
    
    # Try all permutations of [1..k] for frequencies
    values = list(range(1, k+1))
    
    # We'll try all possible permutations for the three dimensions
    # But this is too much; let's think differently
    
    # This is equivalent to finding a Latin square or a 3D matching
    # Let's approach with backtracking
    
    def backtrack(selected, used_x, used_y, used_z):
        if len(selected) == k:
            return selected
        
        # Find next available x
        next_x = None
        for x in values:
            if x not in used_x:
                next_x = x
                break
        
        if next_x is None:
            return None
            
        # Try all configs with this x
        for i, (x, y, z) in enumerate(configs):
            if x == next_x and y not in used_y and z not in used_z:
                used_x.add(x)
                used_y.add(y)
                used_z.add(z)
                selected.append(i)
                
                result = backtrack(selected, used_x, used_y, used_z)
                if result is not None:
                    return result
                    
                selected.pop()
                used_x.remove(x)
                used_y.remove(y)
                used_z.remove(z)
        
        return None
    
    # Optimization: try starting with each possible x,y,z
    used_x = set()
    used_y = set()
    used_z = set()
    selected_indices = []
    
    result = backtrack(selected_indices, used_x, used_y, used_z)
    
    if result is None:
        # Try another approach - build incrementally
        selected_indices = []
        used_x = set()
        used_y = set()
        used_z = set()
        
        def build_solution(pos):
            if pos == k:
                return True
                
            # Try to place item at position 'pos' 
            # which should have values (pos+1, some_y, some_z)
            target_x = pos + 1
            
            for i, (x, y, z) in enumerate(configs):
                if x == target_x and y not in used_y and z not in used_z:
                    used_x.add(x)
                    used_y.add(y)
                    used_z.add(z)
                    selected_indices.append(i)
                    
                    if build_solution(pos + 1):
                        return True
                        
                    selected_indices.pop()
                    used_x.remove(x)
                    used_y.remove(y)
                    used_z.remove(z)
            
            return False
        
        if not build_solution(0):
            print("NO")
            return
            
        print("YES")
        for i in selected_indices:
            x, y, z = configs[i]
            print(x, y, z)
    else:
        print("YES")
        for i in result:
            x, y, z = configs[i]
            print(x, y, z)

solve()
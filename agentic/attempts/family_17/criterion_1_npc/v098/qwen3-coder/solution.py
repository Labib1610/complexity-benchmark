from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    procedures = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        procedures.append((a, b, c))
        index += 3
    
    # Try all combinations of q procedures
    # Since q <= 200 and t <= 20000, we need an efficient approach
    # This is essentially a maximum matching problem or set packing
    
    # Model as hypergraph matching: each procedure is a hyperedge connecting 3 vertices
    # We want to find q disjoint hyperedges (procedures that don't share materials)
    
    # Use backtracking with pruning
    def can_extend(selected, candidates, material_used):
        # Check if we can extend selected procedures with candidates
        # Simple heuristic: if even if we take all remaining candidates, 
        # do we have enough to reach q?
        needed = q - len(selected)
        if len(candidates) < needed:
            return False
        return True
    
    def backtrack(selected, candidates, material_used):
        if len(selected) == q:
            return selected
        
        if not can_extend(selected, candidates, material_used):
            return None
            
        for i, proc in enumerate(candidates):
            a, b, c = proc
            if a not in material_used and b not in material_used and c not in material_used:
                # Try this procedure
                material_used.add(a)
                material_used.add(b)
                material_used.add(c)
                selected.append(i)
                
                # Remaining candidates
                remaining = candidates[i+1:]
                
                result = backtrack(selected, remaining, material_used)
                if result is not None:
                    return result
                    
                # Backtrack
                material_used.remove(a)
                material_used.remove(b)
                material_used.remove(c)
                selected.pop()
        
        return None
    
    # Optimization: sort procedures by some heuristic?
    # For small inputs, direct backtracking might work
    
    # Let's try a different approach: build conflict graph and find maximum independent set
    # Actually, we want maximum matching in 3-uniform hypergraph
    
    # Greedy approach first
    def greedy():
        used_materials = set()
        selected_procedures = []
        available = list(range(t))
        
        for _ in range(q):
            found = False
            new_available = []
            for i in available:
                a, b, c = procedures[i]
                if a not in used_materials and b not in used_materials and c not in used_materials:
                    if not found:
                        # Select this procedure
                        used_materials.add(a)
                        used_materials.add(b)
                        used_materials.add(c)
                        selected_procedures.append(procedures[i])
                        found = True
                    else:
                        new_available.append(i)
                else:
                    new_available.append(i)
            
            if not found:
                return None
                
            available = new_available
            
        return selected_procedures
    
    # Try greedy first
    result = greedy()
    
    if result is not None:
        print("YES")
        for proc in result:
            print(proc[0], proc[1], proc[2])
    else:
        # Try more thorough search for small cases
        if q <= 20:  # Only for reasonably small q
            material_used = set()
            selected_indices = []
            
            def backtrack2(idx):
                if len(selected_indices) == q:
                    return True
                if idx >= t:
                    return False
                
                # Pruning
                if len(selected_indices) + (t - idx) < q:
                    return False
                    
                # Try not taking current procedure
                if backtrack2(idx + 1):
                    return True
                
                # Try taking current procedure
                a, b, c = procedures[idx]
                if a not in material_used and b not in material_used and c not in material_used:
                    material_used.add(a)
                    material_used.add(b)
                    material_used.add(c)
                    selected_indices.append(idx)
                    
                    if backtrack2(idx + 1):
                        return True
                        
                    material_used.remove(a)
                    material_used.remove(b)
                    material_used.remove(c)
                    selected_indices.pop()
                
                return False
            
            if backtrack2(0):
                print("YES")
                for idx in selected_indices:
                    a, b, c = procedures[idx]
                    print(a, b, c)
            else:
                print("NO")
        else:
            print("NO")

if __name__ == "__main__":
    main()
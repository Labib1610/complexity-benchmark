from collections import defaultdict
import sys

def solve():
    k, t = map(int, sys.stdin.readline().split())
    
    reactions = []
    for _ in range(t):
        x, y, z = map(int, sys.stdin.readline().split())
        reactions.append((x, y, z))
    
    # Try to find a perfect matching using backtracking
    # This is essentially finding a Latin square-like structure
    
    # We can model this as a bipartite matching problem or use backtracking
    # Let's use backtracking approach
    
    # For each base fluid, we need to assign a unique catalyst and thermal profile
    # This is equivalent to finding a permutation of catalysts and thermal profiles
    # such that all the required reactions exist
    
    def backtrack(fluid_index, used_catalysts, used_profiles, current_selection):
        if fluid_index == k + 1:
            return True
            
        for i in range(t):
            x, y, z = reactions[i]
            if x == fluid_index and y not in used_catalysts and z not in used_profiles:
                used_catalysts.add(y)
                used_profiles.add(z)
                current_selection.append(i)
                
                if backtrack(fluid_index + 1, used_catalysts, used_profiles, current_selection):
                    return True
                    
                used_catalysts.remove(y)
                used_profiles.remove(z)
                current_selection.pop()
        
        return False
    
    # Better approach: try all possible assignments
    # Since k <= 22, we need something smarter
    
    # Create mappings
    reactions_by_fluid = defaultdict(list)
    for i, (x, y, z) in enumerate(reactions):
        reactions_by_fluid[x].append((y, z, i))
    
    # Check if we have at least k fluids
    if len(reactions_by_fluid) < k:
        for f in range(1, k + 1):
            if f not in reactions_by_fluid:
                print("NO")
                return
    
    # Use backtracking with bitmasks for efficiency
    def solve_recursive(pos, catalyst_mask, profile_mask, selected):
        if pos > k:
            return True, selected[:]
            
        for c, p, idx in reactions_by_fluid[pos]:
            c_bit = 1 << (c - 1)
            p_bit = 1 << (p - 1)
            if not (catalyst_mask & c_bit) and not (profile_mask & p_bit):
                catalyst_mask |= c_bit
                profile_mask |= p_bit
                selected.append(idx)
                
                res, solution = solve_recursive(pos + 1, catalyst_mask, profile_mask, selected)
                if res:
                    return True, solution
                    
                catalyst_mask ^= c_bit
                profile_mask ^= p_bit
                selected.pop()
                
        return False, []
    
    # Start with fluid 1
    found, result_indices = solve_recursive(1, 0, 0, [])
    
    if found:
        print("YES")
        for idx in result_indices:
            print(*reactions[idx])
    else:
        print("NO")

solve()
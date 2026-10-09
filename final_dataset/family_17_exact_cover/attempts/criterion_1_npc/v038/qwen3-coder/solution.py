from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    index = 2
    scripts = []
    for i in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        scripts.append((a, b, c))
        index += 3
    
    # Build a graph where each module is a node and each script is a hyperedge
    # We can model this as a matching problem
    # Since each script covers exactly 3 modules and we need to cover 3q modules exactly once,
    # we need exactly q scripts.
    
    # This is a exact cover problem. We can use backtracking or DLX, but given the constraints,
    # a backtracking approach should work.
    
    # Use backtracking to find a perfect matching
    # Each script covers 3 modules. We have t scripts and need to select q of them to cover all 3q modules.
    
    modules = list(range(1, 3*q + 1))
    
    # Convert scripts to sets for easier processing
    script_sets = [set(script) for script in scripts]
    
    # Try to find a combination of q scripts that covers all modules exactly once
    def backtrack(script_indices, covered, selected):
        if len(selected) == q:
            if len(covered) == 3*q:
                return selected[:]
            else:
                return None
        
        if len(covered) >= 3*q:
            return None
            
        # Pruning: if remaining scripts cannot cover remaining modules
        remaining_modules = 3*q - len(covered)
        remaining_scripts_needed = q - len(selected)
        if remaining_scripts_needed * 3 < remaining_modules:
            return None
            
        # Try next script
        start = script_indices[-1] + 1 if script_indices else 0
        for i in range(start, t):
            script_set = script_sets[i]
            # Check if this script has any overlap with already covered modules
            if script_set & covered:
                continue
            # Add this script
            new_covered = covered | script_set
            selected.append(i)
            script_indices.append(i)
            result = backtrack(script_indices, new_covered, selected)
            if result is not None:
                return result
            selected.pop()
            script_indices.pop()
        
        return None
    
    # Also try a more efficient approach using bitmasks for small q
    # But with q up to 200, that's not feasible.
    # Let's try a greedy approach first or a more optimized backtracking
    
    # Actually, let's model this properly. 
    # We have t scripts, each covering 3 modules. We want to select exactly q scripts
    # such that the union of their modules is exactly the set {1,2,...,3q}
    
    # This is essentially a hitting set or exact cover problem.
    # For the given constraints, let's try a backtracking with optimizations
    
    # Optimization: precompute which scripts contain each module
    module_to_scripts = defaultdict(list)
    for i, (a, b, c) in enumerate(scripts):
        module_to_scripts[a].append(i)
        module_to_scripts[b].append(i)
        module_to_scripts[c].append(i)
    
    # Sort modules by number of scripts that contain them (ascending)
    # This might help in pruning
    modules_sorted = sorted(modules, key=lambda m: len(module_to_scripts[m]))
    
    selected_scripts = []
    used_scripts = [False] * t
    covered_modules = [False] * (3*q + 1)
    
    def backtrack_opt(pos):
        if len(selected_scripts) == q:
            # Check if all modules are covered
            for i in range(1, 3*q + 1):
                if not covered_modules[i]:
                    return False
            return True
            
        if pos == 3*q:
            return len(selected_scripts) == q and all(covered_modules[1:])
            
        # Find the first uncovered module
        module = None
        for i in range(1, 3*q + 1):
            if not covered_modules[i]:
                module = i
                break
                
        if module is None:
            return len(selected_scripts) == q
            
        # Try all scripts that contain this module
        for script_idx in module_to_scripts[module]:
            if used_scripts[script_idx]:
                continue
                
            a, b, c = scripts[script_idx]
            if covered_modules[a] or covered_modules[b] or covered_modules[c]:
                continue
                
            # Use this script
            selected_scripts.append(script_idx)
            used_scripts[script_idx] = True
            covered_modules[a] = True
            covered_modules[b] = True
            covered_modules[c] = True
            
            if backtrack_opt(pos + 1):
                return True
                
            # Backtrack
            selected_scripts.pop()
            used_scripts[script_idx] = False
            covered_modules[a] = False
            covered_modules[b] = False
            covered_modules[c] = False
            
        return False
    
    # For large inputs, even this might be too slow. Let's try the first approach but with better pruning
    def solve():
        selected = []
        covered = set()
        
        def bt(pos):
            if len(selected) == q:
                return [] if len(covered) == 3*q else None
                
            if pos == t:
                return [] if len(selected) == q and len(covered) == 3*q else None
                
            # Pruning
            remaining_scripts = t - pos
            remaining_needed = q - len(selected)
            if remaining_needed > remaining_scripts:
                return None
            if remaining_needed == 0:
                return [] if len(covered) == 3*q else None
                
            # Try including current script
            script_set = script_sets[pos]
            if not (script_set & covered):  # No overlap
                # Include it
                selected.append(pos)
                new_covered = covered | script_set
                old_covered = covered.copy()
                covered.update(script_set)
                res = bt(pos + 1)
                if res is not None:
                    return [pos] + res
                selected.pop()
                covered.clear()
                covered.update(old_covered)
                
            # Try not including it
            res = bt(pos + 1)
            return res
            
        return bt(0)
    
    # Even simpler recursive with memoization won't work due to state size
    # Let's go back to the approach that tries to cover one by one
    
    result = backtrack_opt(0)
    
    if result:
        print("YES")
        for idx in selected_scripts:
            a, b, c = scripts[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()
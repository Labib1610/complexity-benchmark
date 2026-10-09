from collections import defaultdict
import sys

def solve():
    q, t = map(int, input().split())
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    units = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        units.append((a, b, c))
    
    if q == 0:
        print("YES")
        return
    
    # Try to find a matching using backtracking
    # This is essentially a 3D matching problem
    
    # Build a graph where each operator points to units containing it
    operator_to_units = defaultdict(list)
    for i, (a, b, c) in enumerate(units):
        operator_to_units[a].append(i)
        operator_to_units[b].append(i)
        operator_to_units[c].append(i)
    
    # Check if any operator is in no units
    for op in range(1, 3*q + 1):
        if op not in operator_to_units:
            print("NO")
            return
    
    # Try to find a valid assignment using backtracking
    selected_units = [False] * t  # which units are selected
    used_operators = [False] * (3*q + 1)  # which operators are used
    result = []
    
    def backtrack(unit_index):
        # If we've selected q units, we're done
        if len(result) == q:
            return True
            
        # If we've considered all units, return False
        if unit_index >= t:
            return False
            
        # Try skipping this unit
        if backtrack(unit_index + 1):
            return True
            
        # Try including this unit if none of its operators are used
        a, b, c = units[unit_index]
        if not used_operators[a] and not used_operators[b] and not used_operators[c]:
            # Mark operators as used
            used_operators[a] = True
            used_operators[b] = True
            used_operators[c] = True
            result.append(units[unit_index])
            selected_units[unit_index] = True
            
            # Continue with next unit
            if backtrack(unit_index + 1):
                return True
                
            # Backtrack
            used_operators[a] = False
            used_operators[b] = False
            used_operators[c] = False
            result.pop()
            selected_units[unit_index] = False
            
        return False
    
    # Optimization: sort units by minimum operator number to try smaller units first
    unit_indices = list(range(t))
    unit_indices.sort(key=lambda i: min(units[i]))
    
    def backtrack_optimized(indices_used, current_index):
        # If we've selected q units, we're done
        if len(result) == q:
            return True
            
        # If we've considered all units, return False
        if current_index >= t:
            return False
        
        unit_idx = unit_indices[current_index]
        
        # Try skipping this unit
        if backtrack_optimized(indices_used, current_index + 1):
            return True
            
        # Try including this unit if none of its operators are used
        a, b, c = units[unit_idx]
        if not used_operators[a] and not used_operators[b] and not used_operators[c]:
            # Mark operators as used
            used_operators[a] = True
            used_operators[b] = True
            used_operators[c] = True
            result.append(units[unit_idx])
            
            # Continue with next unit
            if backtrack_optimized(indices_used | {unit_idx}, current_index + 1):
                return True
                
            # Backtrack
            used_operators[a] = False
            used_operators[b] = False
            used_operators[c] = False
            result.pop()
            
        return False
    
    # Even better approach - greedy first then backtrack
    if backtrack_optimized(set(), 0):
        print("YES")
        for unit in result:
            print(*unit)
    else:
        print("NO")

solve()
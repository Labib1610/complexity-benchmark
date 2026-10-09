from itertools import combinations
import sys

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    units = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        units.append((a, b, c))
    
    # Try all combinations of q units from the available t units
    for selected_indices in combinations(range(t), q):
        # Check if this combination covers all operators exactly once
        used_operators = set()
        valid = True
        selected_units = []
        
        for i in selected_indices:
            unit = units[i]
            # Check if any operator in this unit is already used
            if any(op in used_operators for op in unit):
                valid = False
                break
            # Add operators to used set
            used_operators.update(unit)
            selected_units.append(unit)
        
        # If we've selected q units and covered exactly 3*q operators
        if valid and len(used_operators) == n:
            print("YES")
            for unit in selected_units:
                print(unit[0], unit[1], unit[2])
            return
    
    print("NO")

solve()
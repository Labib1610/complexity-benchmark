from collections import defaultdict
import sys

def find_matching(q, t, schematics):
    # Create adjacency list for hypergraph matching
    # Each gear can be in multiple schematics
    # We want to find a perfect matching covering all 3q gears
    
    if t == 0:
        if q == 0:
            return []
        else:
            return None
    
    # Build graph: each schematic is a hyperedge connecting 3 vertices (gears)
    # We need to find a matching that covers all vertices exactly once
    
    # This is equivalent to finding an exact cover problem
    # We'll model this as a bipartite matching where:
    # Left side: schematics 
    # Right side: gears
    # But since each schematic needs exactly 3 gears, we use a different approach
    
    # Try to solve with backtracking
    gears = list(range(1, 3*q + 1))
    used_gears = [False] * (3*q + 1)  # indexed by gear number
    selected_schematics = []
    
    def backtrack(schematic_index):
        # If we've selected q schematics, we're done
        if len(selected_schematics) == q:
            return True
            
        # If we've considered all schematics, but haven't selected enough
        if schematic_index >= t:
            return False
            
        # Pruning: if remaining schematics + current selection < q, impossible
        if len(selected_schematics) + (t - schematic_index) < q:
            return False
            
        # Try including current schematic
        a, b, c = schematics[schematic_index]
        if not used_gears[a] and not used_gears[b] and not used_gears[c]:
            # Include this schematic
            used_gears[a] = used_gears[b] = used_gears[c] = True
            selected_schematics.append((a, b, c))
            
            if backtrack(schematic_index + 1):
                return True
                
            # Backtrack
            used_gears[a] = used_gears[b] = used_gears[c] = False
            selected_schematics.pop()
        
        # Try skipping current schematic
        if backtrack(schematic_index + 1):
            return True
            
        return False
    
    # Optimization: sort schematics by how many gears they share with already considered ones?
    # Or just try direct backtracking
    
    if backtrack(0):
        return selected_schematics
    else:
        return None

def solve():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip())
    
    q, t = map(int, input_lines[0].split())
    schematics = []
    
    for i in range(1, t + 1):
        a, b, c = map(int, input_lines[i].split())
        schematics.append((a, b, c))
    
    result = find_matching(q, t, schematics)
    
    if result is not None:
        print("YES")
        for schematic in result:
            print(schematic[0], schematic[1], schematic[2])
    else:
        print("NO")

solve()
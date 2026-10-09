from collections import defaultdict
import sys

def solve():
    k, t = map(int, input().split())
    commands = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        commands.append((x, y, z))
    
    # Try all subsets of exactly k commands
    # Since k <= 22 and t <= k^3, t can be up to 10648, so we can't check all subsets
    # But we can model this as a matching problem or use backtracking
    
    # Let's use backtracking with pruning
    # We want to select exactly k commands such that no two commands share a register in any bank
    
    # This is equivalent to finding a maximum matching in a 3-dimensional matching problem
    # But since k is small, we can try backtracking
    
    # Let's represent the state:
    # locked_A, locked_B, locked_C are sets of locked registers
    # selected is the list of selected commands
    # index is the current index in commands list we're considering
    
    def backtrack(index, locked_A, locked_B, locked_C, selected):
        # If we've selected k commands, we're done
        if len(selected) == k:
            return selected[:]
        
        # If we can't possibly select enough commands, return None
        if len(selected) + (t - index) < k:
            return None
            
        # Try each remaining command
        for i in range(index, t):
            x, y, z = commands[i]
            # Check if this command can be executed
            if x not in locked_A and y not in locked_B and z not in locked_C:
                # Execute this command
                locked_A.add(x)
                locked_B.add(y)
                locked_C.add(z)
                selected.append((x, y, z))
                
                # Recurse
                result = backtrack(i + 1, locked_A, locked_B, locked_C, selected)
                if result is not None:
                    return result
                
                # Backtrack
                locked_A.remove(x)
                locked_B.remove(y)
                locked_C.remove(z)
                selected.pop()
        
        return None
    
    # Start backtracking
    result = backtrack(0, set(), set(), set(), [])
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for x, y, z in result:
            print(x, y, z)

solve()
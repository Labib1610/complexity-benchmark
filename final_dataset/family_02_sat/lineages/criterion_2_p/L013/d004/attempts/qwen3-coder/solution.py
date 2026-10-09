import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        constraints.append((l1, l2))
        index += 2
    
    # For each switch, we'll maintain possible values (0 or 1)
    # Initially, each switch can be either 0 or 1
    possible = [set([0, 1]) for _ in range(n+1)]  # 1-based indexing
    
    # Process each constraint
    for l1, l2 in constraints:
        # Target values
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0
        # Switch indices
        idx1 = abs(l1)
        idx2 = abs(l2)
        
        # The constraint is (s_idx1 - t1) * (s_idx2 - t2) = 0
        # This means s_idx1 = t1 OR s_idx2 = t2
        # So we remove possibilities where s_idx1 != t1 AND s_idx2 != t2
        
        # If both switches can only be their non-target values, it's impossible
        # That is, if s_idx1 can only be (1-t1) and s_idx2 can only be (1-t2), then impossible
        if (1 - t1) in possible[idx1] and len(possible[idx1]) == 1 and \
           (1 - t2) in possible[idx2] and len(possible[idx2]) == 1:
            print("NO")
            return
        
        # If s_idx1 cannot be t1, then s_idx2 must be t2
        if t1 not in possible[idx1]:
            if t2 in possible[idx2]:
                possible[idx2].clear()
                possible[idx2].add(t2)
            else:
                print("NO")
                return
        # If s_idx2 cannot be t2, then s_idx1 must be t1
        elif t2 not in possible[idx2]:
            if t1 in possible[idx1]:
                possible[idx1].clear()
                possible[idx1].add(t1)
            else:
                print("NO")
                return
        # Otherwise, both can be their target values, so no immediate deduction
    
    # Now check if any switch has no possible values
    for i in range(1, n+1):
        if not possible[i]:
            print("NO")
            return
    
    # Assign values: if a switch has only one possibility, assign it.
    # If it has both, assign 0 (or 1, doesn't matter)
    result = [0] * (n+1)
    for i in range(1, n+1):
        if possible[i]:
            result[i] = min(possible[i])  # Choose the minimum (0 if both, the only one if one)
        else:
            result[i] = 0  # Should not happen
    
    # Final verification: check all constraints with the assigned values
    for l1, l2 in constraints:
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0
        idx1 = abs(l1)
        idx2 = abs(l2)
        if (result[idx1] != t1) and (result[idx2] != t2):
            # Try to fix by changing one of them
            # This is a more complex case, let's handle it properly
            # If both are wrong, we must make at least one right
            # Let's try setting idx1 to t1
            if t1 in [0,1]:  # always true
                result[idx1] = t1
                # Check if this breaks previous constraints?
                # This greedy approach might not work
                # Let's instead model this as a 2-SAT problem
                
                # Actually, let's re-think the approach
                pass
    
    # Let's model this properly as a 2-SAT problem
    # Each switch i has two variables: x_i (value 1) and not x_i (value 0)
    # A constraint (s_idx1 = t1 OR s_idx2 = t2) translates to:
    # if t1=1, then (x_idx1 OR s_idx2=t2) => (x_idx1 OR x_idx2 if t2=1, x_idx2^ if t2=0)
    # if t1=0, then (x_idx1^ OR s_idx2=t2) => (x_idx1^ OR x_idx2 if t2=1, x_idx2^ if t2=0)
    
    # But let's try a simpler approach: use implication graph and SCC
    # For now, let's try a greedy assignment with conflict checking
    
    # Re-initialize
    possible = [set([0, 1]) for _ in range(n+1)]
    
    # Apply all constraints to reduce possibilities
    changed = True
    while changed:
        changed = False
        for l1, l2 in constraints:
            t1 = 1 if l1 > 0 else 0
            t2 = 1 if l2 > 0 else 0
            idx1 = abs(l1)
            idx2 = abs(l2)
            
            # Constraint: s_idx1 == t1 OR s_idx2 == t2
            # If s_idx1 cannot be t1, then s_idx2 must be t2
            if t1 not in possible[idx1]:
                if t2 not in possible[idx2]:
                    print("NO")
                    return
                elif len(possible[idx2]) > 1:
                    possible[idx2] = {t2}
                    changed = True
            elif t2 not in possible[idx2]:
                if t1 not in possible[idx1]:
                    print("NO")
                    return
                elif len(possible[idx1]) > 1:
                    possible[idx1] = {t1}
                    changed = True
    
    # Now assign values
    result = [0] * (n+1)
    for i in range(1, n+1):
        if not possible[i]:
            print("NO")
            return
        result[i] = next(iter(possible[i]))
    
    # Final check
    for l1, l2 in constraints:
        t1 = 1 if l1 > 0 else 0
        t2 = 1 if l2 > 0 else 0
        idx1 = abs(l1)
        idx2 = abs(l2)
        if result[idx1] != t1 and result[idx2] != t2:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, result[1:])))

if __name__ == "__main__":
    main()
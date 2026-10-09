def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    if t == 0:
        if k == 0:
            print("YES")
        else:
            print("NO")
        return
    
    modules = []
    idx = 2
    for i in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        modules.append((x, y, z))
        idx += 3
    
    # If k is 0, we need zero modules
    if k == 0:
        print("YES")
        return
    
    # Try to find a valid selection using backtracking
    # We'll model this as a matching problem:
    # We need to select k modules such that each frequency, amplitude, phase from 1 to k appears exactly once
    
    # This is equivalent to finding a perfect matching in a 3-dimensional matching problem
    # We can reduce it to finding a permutation of frequencies, amplitudes and phases
    
    # Let's use backtracking approach
    def backtrack(pos, freq_used, amp_used, phase_used, selected):
        if pos == k:
            return True
            
        for i in range(t):
            f, a, p = modules[i]
            # Check if this module can be placed at position 'pos'
            # with frequency (pos+1), amplitude (pos+1), phase (pos+1)
            if f == pos + 1 and a == pos + 1 and p == pos + 1:
                if not freq_used[f] and not amp_used[a] and not phase_used[p]:
                    freq_used[f] = True
                    amp_used[a] = True
                    phase_used[p] = True
                    selected.append(i)
                    
                    if backtrack(pos + 1, freq_used, amp_used, phase_used, selected):
                        return True
                        
                    freq_used[f] = False
                    amp_used[a] = False
                    phase_used[p] = False
                    selected.pop()
        
        return False

    # Better approach: try all possible combinations of k modules and check constraints
    from itertools import combinations
    
    # But since k <= 22 and t <= k^3 = 8*10^3, combinations could be too large
    # Let's think differently - this is a tripartite matching problem
    
    # Model as finding a maximum matching where:
    # Left part: frequencies 1..k
    # Middle part: amplitudes 1..k  
    # Right part: phases 1..k
    # Edges represent available modules
    
    # This is 3D matching which is NP-hard, but since k<=22 we might be able to do something smarter
    
    # Actually let's just try backtracking with pruning
    selected_modules = []
    freq_taken = [False] * (k + 1)
    amp_taken = [False] * (k + 1)  
    phase_taken = [False] * (k + 1)
    
    def backtrack2(index):
        if len(selected_modules) == k:
            return True
        if index >= t:
            return False
            
        # Try including current module
        f, a, p = modules[index]
        if not freq_taken[f] and not amp_taken[a] and not phase_taken[p]:
            freq_taken[f] = True
            amp_taken[a] = True
            phase_taken[p] = True
            selected_modules.append(modules[index])
            
            if backtrack2(index + 1):
                return True
                
            freq_taken[f] = False
            amp_taken[a] = False
            phase_taken[p] = False
            selected_modules.pop()
        
        # Try not including current module
        if backtrack2(index + 1):
            return True
            
        return False
    
    # Special case when k=0
    if k == 0:
        print("YES")
        return
        
    if backtrack2(0):
        print("YES")
        for mod in selected_modules:
            print(mod[0], mod[1], mod[2])
    else:
        print("NO")

solve()
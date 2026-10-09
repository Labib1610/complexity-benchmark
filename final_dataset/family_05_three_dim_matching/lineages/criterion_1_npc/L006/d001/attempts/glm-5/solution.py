import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    struts = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        struts.append((x, y, z))
    
    # We need to select k struts such that all x's are distinct, all y's are distinct, all z's are distinct
    # This is a 3D matching problem. Since k <= 22, we can use DP with bitmask.
    
    # Group struts by x-coordinate
    struts_by_x = [[] for _ in range(k + 1)]
    for s in struts:
        struts_by_x[s[0]].append(s)
    
    # dp[mask_y][mask_z] = True if achievable
    # We process x from 1 to k, and for each x we either skip it or pick one strut with that x
    
    # Since k <= 22, we need 2^22 * 2^22 which is too large
    # Instead, we use a dictionary to store reachable states
    
    # dp[mask_y][mask_z] = list of selected struts (or just True and reconstruct)
    # Let's use dict: key = (mask_y, mask_z), value = list of struts
    
    # Actually, let's use a single dict with (mask_y, mask_z) as key
    # and store the list of struts used to reach this state
    
    # But storing lists is memory heavy. Let's store parent pointers.
    # parent[mask_y][mask_z] = (prev_mask_y, prev_mask_z, strut_used) or None
    
    # Since we iterate through x in order, we can use a dict for current layer
    
    # dp is a dict: (mask_y, mask_z) -> True
    # We also need to reconstruct, so we store for each state, which strut was added
    
    # Let's use: dp[mask_y][mask_z] = strut_index (the last strut added)
    # But we need to know the previous state. Since we add one strut at a time,
    # previous state is (mask_y ^ (1<<y), mask_z ^ (1<<z))
    
    # So we can just store dp[mask_y][mask_z] = (y, z) of the strut added
    # and reconstruct backwards
    
    # Initialize
    dp = {}
    dp[(0, 0)] = []  # empty selection
    
    for x in range(1, k + 1):
        new_dp = {}
        for (mask_y, mask_z), selected in dp.items():
            # Option 1: don't select any strut with this x
            if (mask_y, mask_z) not in new_dp or len(new_dp[(mask_y, mask_z)]) < len(selected):
                new_dp[(mask_y, mask_z)] = selected
            
            # Option 2: select one strut with this x
            for s in struts_by_x[x]:
                sx, sy, sz = s
                bit_y = 1 << (sy - 1)
                bit_z = 1 << (sz - 1)
                if (mask_y & bit_y) == 0 and (mask_z & bit_z) == 0:
                    new_mask_y = mask_y | bit_y
                    new_mask_z = mask_z | bit_z
                    new_selected = selected + [s]
                    if (new_mask_y, new_mask_z) not in new_dp or len(new_dp[(new_mask_y, new_mask_z)]) < len(new_selected):
                        new_dp[(new_mask_y, new_mask_z)] = new_selected
        
        dp = new_dp
    
    # Find the best solution with k struts
    full_mask = (1 << k) - 1
    target = (full_mask, full_mask)
    
    if target in dp and len(dp[target]) == k:
        print("YES")
        for s in dp[target]:
            print(s[0], s[1], s[2])
    else:
        print("NO")

solve()
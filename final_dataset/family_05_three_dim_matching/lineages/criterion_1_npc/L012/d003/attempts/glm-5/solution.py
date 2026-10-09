import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    pockets = []
    for i in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        pockets.append((x-1, y-1, z-1))  # 0-indexed
    
    if k == 0:
        print("YES")
        return
    
    # Check feasibility: each value must be covered by at least one pocket
    depth_pockets = [[] for _ in range(k)]
    lat_pockets = [[] for _ in range(k)]
    lon_pockets = [[] for _ in range(k)]
    
    for i, (x, y, z) in enumerate(pockets):
        depth_pockets[x].append(i)
        lat_pockets[y].append(i)
        lon_pockets[z].append(i)
    
    for i in range(k):
        if not depth_pockets[i] or not lat_pockets[i] or not lon_pockets[i]:
            print("NO")
            return
    
    # Values: 0..k-1 = depths, k..2k-1 = latitudes, 2k..3k-1 = longitudes
    # For each value, list of pocket indices covering it
    value_pockets = []
    for i in range(k):
        value_pockets.append(depth_pockets[i])
    for i in range(k):
        value_pockets.append(lat_pockets[i])
    for i in range(k):
        value_pockets.append(lon_pockets[i])
    
    # Order values by frequency (ascending) for better pruning
    value_order = sorted(range(3*k), key=lambda v: len(value_pockets[v]))
    
    full_mask = (1 << (3*k)) - 1
    result = [None]
    
    def backtrack(covered, count, start_val_idx):
        if count == k:
            return covered == full_mask
        
        # Find next uncovered value in order
        while start_val_idx < 3*k and (covered >> value_order[start_val_idx]) & 1:
            start_val_idx += 1
        
        if start_val_idx >= 3*k:
            return covered == full_mask
        
        val = value_order[start_val_idx]
        
        # Pruning: check if all remaining uncovered values can still be covered
        # (each has at least one pocket not yet used)
        # This is expensive, skip for now and rely on the structure
        
        for pidx in value_pockets[val]:
            x, y, z = pockets[pidx]
            bits = (1 << x) | (1 << (k + y)) | (1 << (2*k + z))
            if covered & bits:
                continue  # pocket doesn't add new coverage for all its values
            # Actually we need to check if this pocket is "useful" - adds the current value at least
            # Since val is uncovered and pocket covers val, it's useful
            
            new_covered = covered | bits
            if backtrack(new_covered, count + 1, start_val_idx + 1):
                result[0] = pidx
                return True
        
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        # Reconstruct - we only stored last, need to store all
        # Let me redo with list
        pass
    else:
        print("NO")
        return
    
    # Redo with proper reconstruction
    selected = []
    def backtrack2(covered, count, start_val_idx):
        if count == k:
            return covered == full_mask
        
        while start_val_idx < 3*k and (covered >> value_order[start_val_idx]) & 1:
            start_val_idx += 1
        
        if start_val_idx >= 3*k:
            return covered == full_mask
        
        val = value_order[start_val_idx]
        
        for pidx in value_pockets[val]:
            x, y, z = pockets[pidx]
            bits = (1 << x) | (1 << (k + y)) | (1 << (2*k + z))
            if covered & bits:
                continue
            new_covered = covered | bits
            if backtrack2(new_covered, count + 1, start_val_idx + 1):
                selected.append(pidx)
                return True
        
        return False
    
    backtrack2(0, 0, 0)
    for pidx in selected:
        x, y, z = pockets[pidx]
        print(f"{x+1} {y+1} {z+1}")

solve()
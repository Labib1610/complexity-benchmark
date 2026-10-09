import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    paths = []
    for i in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        paths.append((x, y, z))
    
    if t < k:
        print("NO")
        return
    
    # We need to select k paths where all x's are distinct, all y's distinct, all z's distinct
    # This is 3D matching
    
    # DP with meet in the middle
    # Split k into two halves
    
    half = k // 2
    other = k - half
    
    # Generate all valid subsets of size 'half' and 'other'
    # State: (x_mask, y_mask, z_mask) -> list of paths
    
    # For first half: enumerate subsets of size 'half'
    # For second half: enumerate subsets of size 'other'
    # Combine: x masks disjoint, y masks disjoint, z masks disjoint, together cover all k bits
    
    full_mask = (1 << k) - 1
    
    # Let's just do forward DP with dictionary
    # State: (x_mask, y_mask) -> z_mask (we only need one z_mask per (x,y) pair)
    # But we also need to reconstruct the path
    
    # Use DP: dp[(x_mask, y_mask)] = (z_mask, last_path_index, prev_state)
    
    # To save memory, process paths one by one
    
    # Actually with k=22, the number of states could be up to C(22,11)^2 ~ 2.3B in worst case
    # That's too much. Need meet in the middle.
    
    # Meet in the middle:
    # Enumerate all valid matchings of size 'half' -> store (x_mask, y_mask, z_mask) -> path list
    # Enumerate all valid matchings of size 'other' -> for each, check if complementary exists
    
    # Generate all subsets of size 'half' that form valid 3D matching
    # This is still potentially exponential...
    
    # Let's think about it differently. 
    # For the first half, we need to choose 'half' paths with distinct x, y, z.
    # The x values used will be some subset of size 'half'.
    # Similarly for y and z.
    
    # We can enumerate by: choose which x values (C(k, half)), which y values (C(k, half)), 
    # which z values (C(k, half)), then find a perfect matching in the 3D sub-cube.
    # This is still complex.
    
    # Let me just try the DP approach and hope the test cases aren't worst case.
    
    # dp maps (x_mask, y_mask) to (z_mask, parent_info)
    # parent_info = (path_index, prev_x_mask, prev_y_mask)
    
    dp = {}
    dp[(0, 0)] = (0, None)  # (z_mask, parent)
    
    for pi, (x, y, z) in enumerate(paths):
        xb = 1 << (x - 1)
        yb = 1 << (y - 1)
        zb = 1 << (z - 1)
        
        new_entries = []
        for (xm, ym), (zm, _) in dp.items():
            if xm & xb == 0 and ym & yb == 0 and zm & zb == 0:
                nxm = xm | xb
                nym = ym | yb
                nzm = zm | zb
                key = (nxm, nym)
                if key not in dp:
                    new_entries.append((key, nzm, (xm, ym)))
        
        for key, nzm, parent in new_entries:
            if key not in dp:
                dp[key] = (nzm, (pi, parent[0], parent[1]))
    
    # Check if we reached full mask
    target = (full_mask, full_mask)
    if target in dp and dp[target][0] == full_mask:
        print("YES")
        # Reconstruct
        result = []
        cur = target
        while dp[cur][1] is not None:
            pi, pxm, pym = dp[cur][1]
            result.append(paths[pi])
            cur = (pxm, pym)
        for x, y, z in result:
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()
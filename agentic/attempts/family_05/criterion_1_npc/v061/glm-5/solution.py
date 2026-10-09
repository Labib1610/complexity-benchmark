import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    pair_to_zs = defaultdict(list)
    for _ in range(t):
        x = int(input_data[idx]) - 1; idx += 1
        y = int(input_data[idx]) - 1; idx += 1
        z = int(input_data[idx]) - 1; idx += 1
        pair_to_zs[(x, y)].append(z)
    
    pairs = sorted(pair_to_zs.keys())
    pair_zs = [pair_to_zs[p] for p in pairs]
    n_pairs = len(pairs)
    
    full = (1 << k) - 1
    
    # DP: state (mx, my) -> mz, with parent tracking
    # Use dict for sparse representation
    dp = {(0, 0): (0, None, None, None)}  # (mz, prev_mx, prev_my, choice)
    
    for pi in range(n_pairs):
        x, y = pairs[pi]
        z_list = pair_zs[pi]
        bx, by = 1 << x, 1 << y
        
        new_dp = {}
        for (mx, my), (mz, _, _, _) in dp.items():
            # Option 1: skip this pair
            key = (mx, my)
            if key not in new_dp or mz < new_dp[key][0]:
                new_dp[key] = (mz, mx, my, -1)
            
            # Option 2: use this pair with some z
            if mx & bx or my & by:
                continue
            for z in z_list:
                bz = 1 << z
                if mz & bz:
                    continue
                nmx = mx | bx
                nmy = my | by
                nmz = mz | bz
                key = (nmx, nmy)
                if key not in new_dp or nmz < new_dp[key][0]:
                    new_dp[key] = (nmz, mx, my, z)
        
        # Prune: for same (mx, my), keep only min mz
        # (already done by keeping min)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Find target state (full, full) with mz == full
    target_key = (full, full)
    if target_key not in dp:
        print("NO")
        return
    
    mz = dp[target_key][0]
    if mz != full:
        print("NO")
        return
    
    # Backtrack
    result = []
    cur = target_key
    for pi in range(n_pairs - 1, -1, -1):
        x, y = pairs[pi]
        mz, pmx, pmy, z = dp[cur]
        if z != -1:
            result.append((x + 1, y + 1, z + 1))
        cur = (pmx, pmy)
    
    print("YES")
    for r in result:
        print(*r)

solve()
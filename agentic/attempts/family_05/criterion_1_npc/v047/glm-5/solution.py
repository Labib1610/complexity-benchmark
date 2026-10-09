import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Group configurations by shift
    by_shift = defaultdict(list)
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        by_shift[z].append((x, y))
    
    full = (1 << k) - 1
    
    # DP: state = (spec_mask, mach_mask) -> list of (shift, x, y) for reconstruction
    # We process shifts 1..k
    # dp maps (spec_mask, mach_mask) -> parent info for reconstruction
    
    # Use iterative approach
    # dp is a dict: (spec_mask, mach_mask) -> (prev_spec_mask, prev_mach_mask, shift, x, y)
    
    dp = {}
    dp[(0, 0)] = None  # initial state
    
    for shift in range(1, k + 1):
        configs = by_shift.get(shift, [])
        if not configs:
            # This shift has no configurations, impossible
            print("NO")
            return
        
        new_dp = {}
        for (spec_mask, mach_mask), _ in dp.items():
            for (x, y) in configs:
                si = x - 1
                mi = y - 1
                if (spec_mask >> si) & 1:
                    continue
                if (mach_mask >> mi) & 1:
                    continue
                new_spec = spec_mask | (1 << si)
                new_mach = mach_mask | (1 << mi)
                key = (new_spec, new_mach)
                if key not in new_dp:
                    new_dp[key] = (spec_mask, mach_mask, shift, x, y)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Check if full state is reachable
    target = (full, full)
    if target not in dp:
        print("NO")
        return
    
    # Reconstruct
    result = []
    cur = target
    while dp[cur] is not None:
        prev_spec, prev_mach, shift, x, y = dp[cur]
        result.append((x, y, shift))
        cur = (prev_spec, prev_mach)
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    freq_data = [[] for _ in range(k + 1)]
    for _ in range(t):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        freq_data[w].append((u, v))
    
    full_mask = (1 << k) - 1
    
    if k == 0:
        print("YES")
        return
    
    half1 = k // 2
    half2 = k - half1
    
    freqs1 = list(range(1, half1 + 1))
    freqs2 = list(range(half1 + 1, k + 1))
    
    def compute_states(freqs):
        # Returns dict: (in_mask, out_mask) -> list of (freq, u, v) representing the matching
        # Using DP over frequency subsets
        # State: (in_mask, out_mask) -> matching info
        # But storing full matching info is expensive, so we store parent pointers
        
        # dp[freq_subset_mask] = dict mapping (in_mask, out_mask) -> (prev_state, freq, u, v)
        # This is too memory intensive. Let's use iterative approach.
        
        # Instead: dp is dict: (in_mask, out_mask) -> matching (as tuple of (freq,u,v) pairs)
        # But that's expensive. Let's store just one path.
        
        # Better: process frequencies one by one, keeping dict of (in_mask, out_mask) -> path
        # path is a list of (freq, u, v)
        
        dp = {(0, 0): []}
        for freq in freqs:
            new_dp = dict(dp)  # option: don't use this frequency
            for (in_mask, out_mask), path in dp.items():
                for u, v in freq_data[freq]:
                    u_bit = 1 << (u - 1)
                    v_bit = 1 << (v - 1)
                    if (in_mask & u_bit) == 0 and (out_mask & v_bit) == 0:
                        new_state = (in_mask | u_bit, out_mask | v_bit)
                        if new_state not in new_dp:
                            new_dp[new_state] = path + [(freq, u, v)]
            dp = new_dp
        return dp
    
    dp1 = compute_states(freqs1)
    
    # For dp2, we need to find complementary states
    # For each state in dp1 with (in1, out1), we need dp2 state with (in2, out2) where
    # in1 | in2 == full_mask and out1 | out2 == full_mask
    # i.e., in2 == full_mask & ~in1, out2 == full_mask & ~out1
    
    # Process dp2 frequencies one by one, and at each step check if we have a match
    # Actually, let's just compute dp2 fully then check
    
    # But dp2 could be large. Let's compute it and check during computation.
    
    # Actually, let's compute dp2 and store in a set for quick lookup
    dp2 = compute_states(freqs2)
    
    # Build lookup: (in_mask, out_mask) -> path
    # For each dp1 state, check if complementary exists in dp2
    for (in1, out1), path1 in dp1.items():
        in2 = full_mask & ~in1
        out2 = full_mask & ~out1
        key2 = (in2, out2)
        if key2 in dp2:
            path2 = dp2[key2]
            result = path1 + path2
            print("YES")
            for freq, u, v in result:
                print(f"{u} {v} {freq}")
            return
    
    print("NO")

solve()
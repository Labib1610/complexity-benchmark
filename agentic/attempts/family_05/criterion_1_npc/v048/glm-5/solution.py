import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    configs_by_chassis = defaultdict(list)
    for _ in range(t):
        c = int(input_data[idx]); idx += 1
        e = int(input_data[idx]); idx += 1
        g = int(input_data[idx]); idx += 1
        configs_by_chassis[c].append((e, g))
    
    full = (1 << k) - 1
    
    # DP: process chassis 1..k in order
    # state: (core_mask, payload_mask)
    # dp maps state -> (prev_state, e, g) for backtracking
    
    dp = {}
    start = (0, 0)
    dp[start] = None
    
    for i in range(1, k + 1):
        new_dp = {}
        for (cm, pm), _ in dp.items():
            for (e, g) in configs_by_chassis[i]:
                eb = 1 << (e - 1)
                gb = 1 << (g - 1)
                if cm & eb: continue
                if pm & gb: continue
                ncm = cm | eb
                npm = pm | gb
                ns = (ncm, npm)
                if ns not in new_dp:
                    new_dp[ns] = (cm, pm, e, g)
        dp = new_dp
        if not dp:
            break
    
    target = (full, full)
    if target not in dp:
        print("NO")
        return
    
    print("YES")
    # Backtrack
    results = []
    state = target
    while dp[state] is not None:
        pcm, ppm, e, g = dp[state]
        i = bin(ppm).count('1')
        results.append((i, e, g))
        state = (pcm, ppm)
    
    results.sort()
    for c, e, g in results:
        print(f"{c} {e} {g}")

solve()
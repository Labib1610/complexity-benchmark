import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        p1 = int(next(it))
        p2 = int(next(it))
        p3 = int(next(it))
        triples.append((p1, p2, p3))
    
    # We need to select k triples such that:
    # - Each p1 value 1..k appears exactly once
    # - Each p2 value 1..k appears exactly once
    # - Each p3 value 1..k appears exactly once
    
    # Group triples by p1 value
    by_p1 = [[] for _ in range(k + 1)]
    for idx, (p1, p2, p3) in enumerate(triples):
        by_p1[p1].append(idx)
    
    # Check if any p1 has no options
    for p1 in range(1, k + 1):
        if not by_p1[p1]:
            print("NO")
            return
    
    # DP with bitmask
    # State: (used_p2_mask, used_p3_mask) -> (selected_indices)
    # We process p1 values from 1 to k
    
    dp = {}
    dp[(0, 0)] = []
    
    for p1 in range(1, k + 1):
        new_dp = {}
        for (used_p2, used_p3), indices in dp.items():
            for idx in by_p1[p1]:
                p2, p3 = triples[idx][1], triples[idx][2]
                bit_p2 = 1 << (p2 - 1)
                bit_p3 = 1 << (p3 - 1)
                if (used_p2 & bit_p2) == 0 and (used_p3 & bit_p3) == 0:
                    new_mask = (used_p2 | bit_p2, used_p3 | bit_p3)
                    if new_mask not in new_dp:
                        new_dp[new_mask] = indices + [idx]
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Check if we have a complete solution
    full_mask = ((1 << k) - 1, (1 << k) - 1)
    if full_mask in dp:
        print("YES")
        for idx in dp[full_mask]:
            p1, p2, p3 = triples[idx]
            print(p1, p2, p3)
    else:
        print("NO")

solve()
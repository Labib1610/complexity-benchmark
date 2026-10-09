import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # allowed[x][y] = set of z values
    allowed = [[set() for _ in range(k+1)] for _ in range(k+1)]
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        allowed[x][y].add(z)
    
    # We need to find a permutation y of [1..k] and a permutation z of [1..k]
    # such that for each x, (x, y[x], z[x]) is allowed.
    # y and z are both permutations, so each value used exactly once.
    
    # Try all permutations of y (k! possibilities), for each check if a perfect
    # matching exists in the bipartite graph x -> z where edge exists if
    # (x, y[x], z) is allowed.
    # k <= 22, so k! is too large for k=22. Need smarter approach.
    
    # Alternative: This is a 3-dimensional matching problem. NP-hard in general
    # but here k <= 22. We can use inclusion-exclusion / DP over subsets.
    
    # Let's think of it as: choose a permutation y[1..k] and permutation z[1..k].
    # For each x, (x, y[x], z[x]) must be allowed.
    
    # DP over subsets: dp[mask_y][mask_z] = can we assign first popcount(mask_y) x's
    # using y's in mask_y and z's in mask_z. But that's 2^22 * 2^22 = too much.
    
    # Better: dp[mask] where mask is over z (or y), and we track which x's are done
    # implicitly by popcount, and which y's are used... still need both.
    
    # Actually, let's do: iterate over x from 1 to k. For each x, we pick (y, z).
    # dp[mask_z] = set of possible mask_y values (as a set or bitmask of bitmasks).
    # mask_y has 2^22 possible values, storing a set of them is too much.
    
    # Let's try: dp[mask_y] = set of mask_z values achievable. Same issue.
    
    # With k=22, 2^22 = ~4M. If we store dp as a set of (mask_y, mask_z) pairs,
    # worst case could be huge. But maybe in practice it's manageable?
    
    # Actually, let's think differently. We can iterate x from 1 to k.
    # State: (mask_y, mask_z) = which y's and z's are used.
    # We need to find if (full_mask, full_mask) is reachable.
    # The number of reachable states could be up to C(22,11)^2 ~ 10^12 in theory.
    
    # Let's try a different approach: fix the y-permutation by trying all k! 
    # permutations. For k=22, that's 22! ~ 10^21, way too much.
    
    # Hmm, k=22 is large. Let me think about this more carefully.
    
    # Actually, maybe we can do DP where we process x's one by one, and the state
    # is (mask_y, mask_z). We use a set of reachable states.
    # At step i, we have used i x's, so mask_y and mask_z each have exactly i bits.
    # Number of states at step i is C(k,i)^2. Sum over i is C(2k,k) ~ C(44,22)/... 
    # C(44,22) ~ 2.3*10^12. Too much.
    
    # But wait - maybe the constraints of the problem (allowed combinations) 
    # limit the reachable states significantly. Let's just try the DP approach
    # and see if it works within time/memory.
    
    # Actually, let's reconsider. The problem says k <= 22 and time limit 5s.
    # Maybe the intended solution is the subset DP with state (mask_y, mask_z).
    
    # Let's try a meet-in-the-middle approach: process first k/2 x's to get
    # reachable (mask_y, mask_z) states, then process last k/2 x's backwards.
    # For matching, we need: for a state (my1, mz1) from first half and 
    # (my2, mz2) from second half, my1 | my2 == full and mz1 | mz2 == full
    # and my1 & my2 == 0 and mz1 & mz2 == 0.
    
    # This is still complex. Let me just try the forward DP with a set of states.
    
    from itertools import combinations
    
    full_mask = (1 << k) - 1
    
    # dp: set of (mask_y, mask_z) tuples
    # Start with (0, 0), process x = 1, 2, ..., k
    dp = {(0, 0)}
    
    for x in range(1, k+1):
        new_dp = set()
        for (my, mz) in dp:
            for y in range(1, k+1):
                if my & (1 << (y-1)):
                    continue
                if not allowed[x][y]:
                    continue
                for z in allowed[x][y]:
                    if mz & (1 << (z-1)):
                        continue
                    new_dp.add((my | (1 << (y-1)), mz | (1 << (z-1))))
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # If we reach here, dp contains (full_mask, full_mask) or we need to check
    # Actually after processing all k x's, any state in dp has mask with k bits
    # which must be full_mask
    
    if not dp:
        print("NO")
        return
    
    # We need to reconstruct the solution. Let's redo the DP with parent tracking.
    # That's memory intensive. Instead, let's redo with a different approach:
    # store dp as dict: (mask_y, mask_z) -> (y, z) that led here from previous step
    
    # Actually, let's just redo the DP storing parent info
    dp = {(0, 0): None}  # state -> (prev_state, y, z)
    
    for x in range(1, k+1):
        new_dp = {}
        for (my, mz) in dp:
            for y in range(1, k+1):
                if my & (1 << (y-1)):
                    continue
                if not allowed[x][y]:
                    continue
                for z in allowed[x][y]:
                    if mz & (1 << (z-1)):
                        continue
                    state = (my | (1 << (y-1)), mz | (1 << (z-1)))
                    if state not in new_dp:
                        new_dp[state] = ((my, mz), y, z)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Find the full state
    final_state = (full_mask, full_mask)
    if final_state not in dp:
        print("NO")
        return
    
    # Reconstruct
    crews = []
    state = final_state
    while dp[state] is not None:
        prev_state, y, z = dp[state]
        x = bin(prev_state[0]).count('1') + 1  # x is determined by position
        crews.append((x, y, z))
        state = prev_state
    
    crews.reverse()
    print("YES")
    for x, y, z in crews:
        print(x, y, z)

solve()
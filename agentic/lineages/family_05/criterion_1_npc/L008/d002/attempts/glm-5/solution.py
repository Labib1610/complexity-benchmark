import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Build adjacency: for each (x, y), which z values are available
    adj = [[[] for _ in range(k+1)] for _ in range(k+1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        adj[x][y].append(z)
    
    if k == 0:
        print("YES")
        return
    
    # For small k, try all Y-permutations
    if k <= 8:
        for perm in permutations(range(1, k+1)):
            # perm[i-1] = y for x=i
            # Now find Z-permutation via bipartite matching
            # Build bipartite graph: x -> z
            bip_adj = [[] for _ in range(k)]  # 0-indexed: x-1 -> list of z-1
            for i in range(k):
                x = i + 1
                y = perm[i]
                bip_adj[i] = [z-1 for z in adj[x][y]]
            
            # Hungarian matching
            match_z = [-1] * k  # match_z[x] = z
            match_x = [-1] * k  # match_x[z] = x
            
            def try_kuhn(v, visited):
                for to in bip_adj[v]:
                    if not visited[to]:
                        visited[to] = True
                        if match_x[to] == -1 or try_kuhn(match_x[to], visited):
                            match_x[to] = v
                            match_z[v] = to
                            return True
                return False
            
            ok = True
            for i in range(k):
                visited = [False] * k
                if not try_kuhn(i, visited):
                    ok = False
                    break
            
            if ok:
                print("YES")
                for i in range(k):
                    print(f"{i+1} {perm[i]} {match_z[i]+1}")
                return
        print("NO")
        return
    
    # For larger k, use DP with bitmask
    # State: (x_mask, y_mask) -> we need to find if there's a valid Z assignment
    # This is still 2^k * 2^k which is too large for k=22
    # 
    # Alternative: DP over x_mask, tracking y_mask, and use bipartite matching for Z
    # But we need to track the actual assignment for reconstruction
    
    # Let's use a different approach: DP where state is y_mask (which Y's are used)
    # and we process X-planes in order. For each state, we track if it's reachable
    # and the Z-assignment is checked via matching.
    
    # Actually, let's think differently. The problem is 3D matching.
    # We can reduce: fix the X-Y assignment (a permutation), then check if Z-permutation exists.
    # But there are k! permutations.
    
    # Better: Use inclusion-exclusion or DP with bitmask on one dimension.
    # DP state: y_mask (which Y-planes used), and we assign X-planes 1..k in order.
    # For Z, we need a perfect matching in the bipartite graph formed.
    # But checking matching at each step is expensive.
    
    # Let's try: DP[y_mask] = set of reachable z_masks
    # This is 2^k * 2^k in worst case but with dictionary it might work for sparse cases
    
    from collections import defaultdict
    
    # dp: dict mapping y_mask -> set of z_mask (or dict for parent tracking)
    # Start: y_mask=0, z_mask=0, x=0 (no X assigned yet)
    
    # We process X-planes 1 to k in order
    # dp[y_mask] = set of z_masks reachable
    
    dp = [defaultdict(list) for _ in range(k+1)]  # dp[x][y_mask] = list of (z_mask, parent_y_mask, y_choice, z_choice)
    dp[0][0] = [(0, -1, -1, -1)]  # (z_mask, parent_y_mask, y_chosen, z_chosen) - initial
    
    # Actually let's simplify: dp[x][y_mask] = dict: z_mask -> (parent_y_mask, y_choice, z_choice)
    dp = [dict() for _ in range(k+1)]
    dp[0][0] = (0, -1, -1, -1)  # z_mask=0, parent=-1, y=-1, z=-1
    
    # Hmm, this doesn't work because multiple z_masks can be reachable from same y_mask
    # Let me reconsider
    
    # dp[x] = dict mapping (y_mask, z_mask) -> (parent_y_mask, y_choice, z_choice)
    # State space: 2^k * 2^k, but sparse
    
    dp = [dict() for _ in range(k+1)]
    dp[0][(0, 0)] = (-1, -1, -1)
    
    for x in range(k):
        xp = x + 1
        for (ym, zm), (pym, yc, zc) in dp[x].items():
            for y in range(1, k+1):
                ybit = 1 << (y-1)
                if ym & ybit:
                    continue
                for z in adj[xp][y]:
                    zbit = 1 << (z-1)
                    if zm & zbit:
                        continue
                    nym = ym | ybit
                    nzm = zm | zbit
                    key = (nym, nzm)
                    if key not in dp[x+1]:
                        dp[x+1][key] = (ym, y, z)
    
    full = (1 << k) - 1
    if (full, full) in dp[k]:
        print("YES")
        # Reconstruct
        result = []
        ym, zm = full, full
        for x in range(k, 0, -1):
            pym, y, z = dp[x][(ym, zm)]
            result.append((x, y, z))
            ym, zm = pym, ym  # wait, need to get z_mask too
            # Actually dp[x][(ym, zm)] = (parent_ym, y, z)
            # parent zm = zm without z bit
            # Let me fix: we need to track parent z_mask too
            pass
        # Let me fix the reconstruction
        result = []
        ym, zm = full, full
        for x in range(k, 0, -1):
            pym, y, z = dp[x][(ym, zm)]
            result.append((x, y, z))
            ym = pym
            zm = zm ^ (1 << (z-1))
        for x, y, z in reversed(result):
            print(f"{x} {y} {z}")
        return
    
    print("NO")

solve()
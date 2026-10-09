import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    blueprints = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        blueprints.append((x - 1, y - 1, z - 1))
    
    # Create mapping from (worker, equipment) to schedule block
    we_to_z = {}
    for x, y, z in blueprints:
        key = (x, y)
        if key not in we_to_z:
            we_to_z[key] = z
    
    # Try all possible matchings for workers to equipment
    # For each matching, check if corresponding schedule blocks form a permutation
    for perm in range(k):
        # perm is a bitmask representing which equipment units are matched
        # We'll use DP: dp[mask] = (z_mask, assignment) or None
        # assignment is a list of (worker, equipment, schedule) tuples
        dp = [None] * (1 << k)
        dp[0] = (0, [])
        
        for mask in range(1 << k):
            if dp[mask] is None:
                continue
            z_mask = dp[mask][0]
            assignments = dp[mask][1]
            
            # Find next worker to assign (first unassigned)
            w = -1
            for i in range(k):
                if not (mask & (1 << i)):
                    w = i
                    break
            
            if w == -1:
                continue
            
            # Try all equipment units not yet assigned
            for e in range(k):
                if mask & (1 << e):
                    continue
                
                key = (w, e)
                if key not in we_to_z:
                    continue
                
                z = we_to_z[key]
                if z_mask & (1 << z):
                    continue
                
                new_mask = mask | (1 << e)
                new_z_mask = z_mask | (1 << z)
                if dp[new_mask] is None:
                    dp[new_mask] = (new_z_mask, assignments + [(w, e, z)])
    
    full_mask = (1 << k) - 1
    if dp[full_mask] is not None and dp[full_mask][0] == full_mask:
        print("YES")
        for w, e, z in dp[full_mask][1]:
            print(w + 1, e + 1, z + 1)
    else:
        print("NO")

solve()
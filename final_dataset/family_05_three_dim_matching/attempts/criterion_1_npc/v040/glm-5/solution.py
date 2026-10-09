import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    pathways = []
    for _ in range(t):
        f = int(next(it))
        c = int(next(it))
        m = int(next(it))
        pathways.append((f - 1, c - 1, m - 1))
    
    # Build adjacency: for each (feed, core) pair, list of memory banks
    adj = {}
    for f, c, m in pathways:
        key = (f, c)
        if key not in adj:
            adj[key] = []
        adj[key].append(m)
    
    # dp[mask_f][mask_c] = mask_m (bitmask of used memory banks)
    # parent[mask_f][mask_c] = (prev_mask_f, prev_mask_c, f, c, m)
    dp = {}
    parent = {}
    
    dp[(0, 0)] = 0
    
    for _ in range(k):
        new_dp = {}
        new_parent = {}
        for (mask_f, mask_c), mask_m in dp.items():
            # Try to add a pathway
            for f in range(k):
                if mask_f & (1 << f):
                    continue
                for c in range(k):
                    if mask_c & (1 << c):
                        continue
                    key = (f, c)
                    if key not in adj:
                        continue
                    for m in adj[key]:
                        if mask_m & (1 << m):
                            continue
                        new_mask_f = mask_f | (1 << f)
                        new_mask_c = mask_c | (1 << c)
                        new_mask_m = mask_m | (1 << m)
                        new_key = (new_mask_f, new_mask_c)
                        if new_key not in new_dp:
                            new_dp[new_key] = new_mask_m
                            new_parent[new_key] = (mask_f, mask_c, f, c, m)
        dp = new_dp
        parent = new_parent
    
    # Check if we have a complete solution
    full_mask = (1 << k) - 1
    solution_key = None
    for (mask_f, mask_c), mask_m in dp.items():
        if mask_f == full_mask and mask_c == full_mask and mask_m == full_mask:
            solution_key = (mask_f, mask_c)
            break
    
    if solution_key is None:
        print("NO")
        return
    
    print("YES")
    
    # Reconstruct solution
    result = []
    current = solution_key
    for _ in range(k):
        mask_f, mask_c = current
        prev_mask_f, prev_mask_c, f, c, m = parent[(mask_f, mask_c)]
        result.append((f + 1, c + 1, m + 1))
        current = (prev_mask_f, prev_mask_c)
    
    for pathway in result:
        print(f"{pathway[0]} {pathway[1]} {pathway[2]}")

if __name__ == "__main__":
    solve()
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    routes = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        routes.append((x - 1, y - 1, z - 1))
    
    # Group routes by source
    routes_by_source = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(routes):
        routes_by_source[x].append((y, z, idx))
    
    # DP: dp[mask_y][mask_z] = (prev_mask_y, prev_mask_z, route_idx) or None
    # We'll use dictionary for sparse representation
    dp = {}
    dp[(0, 0)] = None
    
    for source in range(k):
        new_dp = {}
        for (mask_y, mask_z), prev in dp.items():
            for y, z, route_idx in routes_by_source[source]:
                if (mask_y >> y) & 1:
                    continue
                if (mask_z >> z) & 1:
                    continue
                new_mask_y = mask_y | (1 << y)
                new_mask_z = mask_z | (1 << z)
                if (new_mask_y, new_mask_z) not in new_dp:
                    new_dp[(new_mask_y, new_mask_z)] = (mask_y, mask_z, route_idx)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Find a complete assignment
    full_mask = (1 << k) - 1
    if (full_mask, full_mask) not in dp:
        print("NO")
        return
    
    # Backtrack to find routes
    result = []
    mask_y, mask_z = full_mask, full_mask
    for source in range(k - 1, -1, -1):
        prev_mask_y, prev_mask_z, route_idx = dp[(mask_y, mask_z)]
        result.append(routes[route_idx])
        mask_y, mask_z = prev_mask_y, prev_mask_z
    
    print("YES")
    for x, y, z in reversed(result):
        print(f"{x + 1} {y + 1} {z + 1}")

if __name__ == "__main__":
    solve()
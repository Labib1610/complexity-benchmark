import sys
sys.setrecursionlimit(1000000)

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
        routes.append((x, y, z))
    
    # Build adjacency: source -> list of (route_index, transformer, destination)
    adj = [[] for _ in range(k + 1)]
    for i, (x, y, z) in enumerate(routes):
        adj[x].append((i, y, z))
    
    # State: used_transformers (bitmask), used_destinations (bitmask)
    # Memo: (source_index, used_t_mask, used_d_mask) -> route_index or -1
    memo = {}
    
    def dfs(src_idx, used_t, used_d):
        if src_idx > k:
            return True
        
        key = (src_idx, used_t, used_d)
        if key in memo:
            return False
        
        for route_idx, y, z in adj[src_idx]:
            t_bit = 1 << (y - 1)
            d_bit = 1 << (z - 1)
            if (used_t & t_bit) == 0 and (used_d & d_bit) == 0:
                if dfs(src_idx + 1, used_t | t_bit, used_d | d_bit):
                    memo[key] = route_idx
                    return True
        
        memo[key] = -1
        return False
    
    if dfs(1, 0, 0):
        print("YES")
        result = []
        src_idx = 1
        used_t = 0
        used_d = 0
        while src_idx <= k:
            key = (src_idx, used_t, used_d)
            route_idx = memo[key]
            x, y, z = routes[route_idx]
            result.append((x, y, z))
            used_t |= 1 << (y - 1)
            used_d |= 1 << (z - 1)
            src_idx += 1
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

solve()
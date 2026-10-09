import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    essential = [int(next(it)) for _ in range(t)]
    essential_set = set(essential)
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    
    if t == 1:
        print(0)
        return
    
    edges.sort()
    
    INF = float('inf')
    # dp[mask] = (cost, degree1_count, parent_mask, edge_idx)
    dp = [(INF, 0, -1, -1) for _ in range(1 << t)]
    dp[0] = (0, 0, -1, -1)
    
    for i, (w, u, v) in enumerate(edges):
        mu = 0
        if u in essential_set:
            mu = 1 << essential.index(u)
        mv = 0
        if v in essential_set:
            mv = 1 << essential.index(v)
        
        new_dp = list(dp)
        
        for mask in range(1 << t):
            cur_cost, cur_deg1, _, _ = dp[mask]
            if cur_cost == INF:
                continue
            
            new_mask = mask | mu | mv
            new_cost = cur_cost + w
            new_deg1 = cur_deg1
            
            if mu != 0 and not (mask & mu):
                new_deg1 += 1
            if mv != 0 and not (mask & mv):
                new_deg1 += 1
            
            if new_deg1 <= t:
                if new_cost < new_dp[new_mask][0]:
                    new_dp[new_mask] = (new_cost, new_deg1, mask, i)
        
        dp = new_dp
    
    full_mask = (1 << t) - 1
    print(dp[full_mask][0])

solve()
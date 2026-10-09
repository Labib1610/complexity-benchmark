import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    required = [int(next(iterator)) - 1 for _ in range(t)]
    
    INF = 10**15
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
            
    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            dist_i = dist[i]
            dist_i_k = dist_i[k]
            if dist_i_k == INF:
                continue
            for j in range(n):
                val = dist_i_k + dist_k[j]
                if val < dist_i[j]:
                    dist_i[j] = val

    if t == 1:
        print(0)
        return

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        term = required[i]
        for v in range(n):
            dp[1 << i][v] = dist[term][v]
            
    for mask in range(1, num_masks):
        if (mask & (mask - 1)) == 0:
            continue
        
        dp_mask = dp[mask]
        sub = (mask - 1) & mask
        while sub > (mask ^ sub):
            dp_sub = dp[sub]
            dp_comp = dp[mask ^ sub]
            for v in range(n):
                val = dp_sub[v] + dp_comp[v]
                if val < dp_mask[v]:
                    dp_mask[v] = val
            sub = (sub - 1) & mask
            
        new_dp = [INF] * n
        for u in range(n):
            dist_u = dist[u]
            min_val = INF
            for v in range(n):
                cost = dp_mask[v] + dist_u[v]
                if cost < min_val:
                    min_val = cost
            new_dp[u] = min_val
        dp[mask] = new_dp
        
    ans = dp[num_masks - 1][required[0]]
    print(ans)

if __name__ == '__main__':
    solve()
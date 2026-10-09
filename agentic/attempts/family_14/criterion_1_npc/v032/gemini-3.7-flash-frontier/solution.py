import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    terminals = [int(next(iterator)) - 1 for _ in range(t)]
    
    if t <= 1:
        print(0)
        return
    
    INF = 10**18
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
            dik = dist_i[k]
            if dik == INF:
                continue
            for j in range(n):
                if dist_i[j] > dik + dist_k[j]:
                    dist_i[j] = dik + dist_k[j]

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        term = terminals[i]
        mask = 1 << i
        dp_mask = dp[mask]
        dist_term = dist[term]
        for v in range(n):
            dp_mask[v] = dist_term[v]
            
    for mask in range(1, num_masks):
        # If mask is a power of 2, step 1 is already handled by base case
        if (mask & (mask - 1)) != 0:
            dp_mask = dp[mask]
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:
                    break
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
                sub = (sub - 1) & mask
                
            # Step 2: update distances for this mask
            temp = list(dp_mask)
            for u in range(n):
                min_val = dp_mask[u]
                for v in range(n):
                    val = temp[v] + dist[v][u]
                    if val < min_val:
                        min_val = val
                dp_mask[u] = min_val

    ans = min(dp[(1 << t) - 1])
    print(ans)

if __name__ == '__main__':
    solve()
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    idx = 3
    terminals = [int(input_data[idx + i]) - 1 for i in range(t)]
    idx += t
    
    INF = 10**15
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
            
    if t <= 1:
        print(0)
        return

    # Floyd-Warshall for all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            for j in range(n):
                if dist[k][j] < INF:
                    new_d = dik + dist[k][j]
                    if new_d < dist[i][j]:
                        dist[i][j] = new_d

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_masks):
        # Step 1: Submask combination
        # Only needed if mask has at least 2 bits
        if (mask & (mask - 1)) != 0:
            # Iterate submasks (to avoid duplicate symmetric pairs, fix the lowest set bit)
            lowest_bit = mask & -mask
            sub = (mask - 1) & mask
            while sub > 0:
                if sub & lowest_bit:
                    comp = mask ^ sub
                    dp_sub = dp[sub]
                    dp_comp = dp[comp]
                    dp_mask = dp[mask]
                    for u in range(n):
                        val = dp_sub[u] + dp_comp[u]
                        if val < dp_mask[u]:
                            dp_mask[u] = val
                sub = (sub - 1) & mask
        
        # Step 2: Metric closure / shortest path propagation
        dp_mask = dp[mask]
        new_dp = [INF] * n
        for v in range(n):
            min_val = INF
            for u in range(n):
                val = dp_mask[u] + dist[u][v]
                if val < min_val:
                    min_val = val
            new_dp[v] = min_val
        dp[mask] = new_dp

    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()
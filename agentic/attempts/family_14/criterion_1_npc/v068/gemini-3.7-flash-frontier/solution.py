import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    ptr = 3
    terminals = [int(x) - 1 for x in data[ptr:ptr+t]]
    ptr += t
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for _ in range(m):
        u = int(data[ptr]) - 1
        v = int(data[ptr+1]) - 1
        w = int(data[ptr+2])
        ptr += 3
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
                if dik + dist_k[j] < dist_i[j]:
                    dist_i[j] = dik + dist_k[j]
                    
    if t <= 1:
        print(0)
        return

    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        dp_mask = dp[mask]
        
        # Submask combination
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub < other:
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask
            
        # Distance relaxation
        new_dp = [INF] * n
        for v in range(n):
            base = dp_mask[v]
            if base == INF:
                continue
            dist_v = dist[v]
            for u in range(n):
                val = base + dist_v[u]
                if val < new_dp[u]:
                    new_dp[u] = val
        dp[mask] = new_dp

    ans = min(dp[(1 << t) - 1])
    print(ans)

if __name__ == '__main__':
    main()
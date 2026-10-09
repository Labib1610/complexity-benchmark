import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    primaries = []
    for _ in range(t):
        primaries.append(int(input_data[idx]) - 1)
        idx += 1
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                if dk[j] < INF and dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    
    if t <= 1:
        print(0)
        return
    
    # Map primaries to indices 0..t-1
    # dp[mask][v] = min cost tree connecting primaries in mask, rooted at v
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]
    
    for i in range(t):
        p = primaries[i]
        bit = 1 << i
        for v in range(n):
            dp[bit][v] = dist[p][v]
    
    # Process masks in increasing order
    for mask in range(1, size):
        if mask & (mask - 1) == 0:
            continue  # single bit, already initialized
        
        # First: extend by adding one primary (using submask without that primary)
        for i in range(t):
            bit = 1 << i
            if mask & bit:
                sub = mask ^ bit
                if sub == 0:
                    continue
                dp_sub = dp[sub]
                for p in primaries:
                    dp_p = dist[p]
                    for v in range(n):
                        val = dp_sub[v] + dp_p[v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
        
        # Second: merge two proper subsets
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                dp_sub = dp[sub]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask
    
    full = size - 1
    ans = min(dp[full])
    print(ans)

solve()
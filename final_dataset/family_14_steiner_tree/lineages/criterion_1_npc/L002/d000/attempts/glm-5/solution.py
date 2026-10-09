import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    terminals = [int(data[idx+i]) for i in range(t)]
    idx += t
    
    INF = 10**18
    dist = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(1, n+1):
        dk = dist[k]
        for i in range(1, n+1):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(1, n+1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    if t <= 1:
        print(0)
        return
    
    # DP over subsets of terminals
    size = 1 << t
    dp = [INF] * size
    for i in range(t):
        dp[1 << i] = 0
    
    for mask in range(1, size):
        if dp[mask] == INF:
            continue
        # try to add a new terminal j
        for j in range(t):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                # connect terminal j to some terminal i in mask
                # best: min over i in mask of dist[terminals[i]][terminals[j]]
                # but we can also use Steiner-like merge below
                # We'll handle via subset merge instead for correctness with Steiner nodes
                pass
    
    # Better: standard Dreyfus-Wagner style using subset merge
    # dp[mask] = min cost to connect terminals in mask
    # We already initialized singletons.
    # For each mask, try splitting into two submasks.
    for mask in range(1, size):
        # subset iteration
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            val = dp[sub] + dp[other]
            if val < dp[mask]:
                dp[mask] = val
            sub = (sub - 1) & mask
        
        # Now try to extend by picking a Steiner node as center:
        # dp[mask] = min over center c of (min cost to connect mask using c as hub)
        # which is sum over i in mask of dist[terminals[i]][c], but that's only valid
        # when we form a star. Actually the correct recurrence:
        # dp[mask] = min_{c} ( sum_{i in mask} dist[terminals[i]][c] ) is NOT generally correct
        # because it double counts edges. The correct Steiner tree DP:
        # dp[mask][v] = min over submasks of dp[sub][v] + dp[mask^sub][v]
        #              and min over u of dp[mask][u] + dist[u][v]
        # We need per-vertex DP.
    
    # Redo with per-vertex DP (Dreyfus-Wagner)
    dpv = [[INF]*(n+1) for _ in range(size)]
    for i in range(t):
        s = 1 << i
        for v in range(1, n+1):
            dpv[s][v] = dist[terminals[i]][v]
    
    for mask in range(1, size):
        if mask & (mask-1) == 0:
            continue  # singleton, already set
        # merge submasks at same vertex
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            for v in range(1, n+1):
                val = dpv[sub][v] + dpv[other][v]
                if val < dpv[mask][v]:
                    dpv[mask][v] = val
            sub = (sub - 1) & mask
        # relax: dpv[mask][v] = min over u of dpv[mask][u] + dist[u][v]
        # We can compute this by running a shortest path from all vertices simultaneously
        # using the current dpv[mask] as initial distances.
        # Since graph is small (n<=100), we can do Dijkstra from each vertex or Floyd already done.
        # Use Floyd result: dpv[mask][v] = min_u (dpv[mask][u] + dist[u][v])
        best = INF
        for u in range(1, n+1):
            du = dpv[mask][u]
            if du == INF:
                continue
            du_row = dist[u]
            for v in range(1, n+1):
                nd = du + du_row[v]
                if nd < dpv[mask][v]:
                    dpv[mask][v] = nd
    
    ans = min(dpv[size-1][v] for v in range(1, n+1))
    print(ans)

solve()
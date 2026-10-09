import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    terminals = [int(next(it)) - 1 for _ in range(t)]
    
    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
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
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    full = 1 << t
    dp = [[INF] * n for _ in range(full)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
    
    for mask in range(1, full):
        # combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] + dp[other][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[other][v]
            sub = (sub - 1) & mask
        
        # relax via shortest paths
        # Dijkstra from all nodes with finite dp[mask][v]
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v in range(n):
                nd = d + dist[u][v]
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    ans = min(dp[full - 1][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
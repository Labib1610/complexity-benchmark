import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, t = map(int, input_data[:3])
    targets = list(map(int, input_data[3:3+t]))
    targets = [x-1 for x in targets]
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    idx = 3 + t
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        w = int(input_data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # If only one target, cost is 0
    if t == 1:
        print(0)
        return
    
    # Dijkstra from each target to all nodes
    INF = 10**18
    dist = [[INF]*n for _ in range(t)]
    for i, src in enumerate(targets):
        d = dist[i]
        d[src] = 0
        pq = [(0, src)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # DP over subsets of terminals
    # dp[mask][v] = min cost to connect terminals in mask, ending at v
    full_mask = (1 << t) - 1
    dp = [[INF]*n for _ in range(1 << t)]
    
    for i in range(t):
        dp[1 << i][targets[i]] = 0
    
    # Combine subsets
    for mask in range(1 << t):
        # Subset DP: combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Relax via Dijkstra for this mask
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            du, u = heapq.heappop(pq)
            if du != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
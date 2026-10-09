import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]
    
    INF = 10**18
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each terminal to all nodes
    term_dist = []
    for s in terminals:
        d = [INF]*n
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        term_dist.append(d)
    
    # DP over subsets of terminals
    # dp[mask][i] = min cost to connect terminals in mask, ending at node i
    full = 1 << t
    dp = [[INF]*n for _ in range(full)]
    
    for i in range(t):
        for v in range(n):
            dp[1<<i][v] = term_dist[i][v]
    
    for mask in range(full):
        # combine two submasks
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid duplicate work
                for i in range(n):
                    dp[mask][i] = min(dp[mask][i], dp[sub][i] + dp[other][i])
            sub = (sub-1) & mask
        
        # relax via Dijkstra for this mask
        pq = [(dp[mask][i], i) for i in range(n) if dp[mask][i] < INF]
        heapq.heapify(pq)
        while pq:
            du, u = heapq.heappop(pq)
            if du != dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    ans = min(dp[full-1][i] for i in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
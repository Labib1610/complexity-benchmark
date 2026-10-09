import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    terminals = []
    for i in range(t):
        terminals.append(int(input_data[idx]) - 1); idx += 1
    
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # All-pairs shortest paths using Dijkstra from each node
    dist = [[10**18] * n for _ in range(n)]
    for src in range(n):
        dist[src][src] = 0
        pq = [(0, src)]
        while pq:
            d, u = heappop(pq)
            if d > dist[src][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[src][v]:
                    dist[src][v] = nd
                    heappush(pq, (nd, v))
    
    # Dreyfus-Wagner Steiner tree DP
    # dp[S][v] = min cost tree connecting terminals in S, rooted at v
    INF = 10**18
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Base case: single terminals
    for i in range(t):
        bit = 1 << i
        for v in range(n):
            dp[bit][v] = dist[terminals[i]][v]
    
    # Fill DP for all subsets
    for S in range(1, full + 1):
        if S & (S - 1) == 0:
            continue  # single element, already initialized
        
        # Find lowest set bit to use as fixed element
        low = S & (-S)
        low_idx = low.bit_length() - 1
        
        # Merge: dp[S][v] = min over S' containing low, S' proper subset: dp[S'][v] + dp[S^S'][v]
        # Iterate over subsets of S that contain low and are proper subsets
        rest = S ^ low
        sub = rest
        while sub > 0:
            S1 = low | sub
            S2 = S ^ S1
            for v in range(n):
                val = dp[S1][v] + dp[S2][v]
                if val < dp[S][v]:
                    dp[S][v] = val
            sub = (sub - 1) & rest
        
        # Move root: dp[S][v] = min over u: dp[S][u] + dist[u][v]
        # This is like running a shortest path relaxation
        # We can do this with Dijkstra since dist satisfies triangle inequality
        pq = []
        for v in range(n):
            if dp[S][v] < INF:
                heappush(pq, (dp[S][v], v))
        
        while pq:
            d, u = heappop(pq)
            if d > dp[S][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[S][v]:
                    dp[S][v] = nd
                    heappush(pq, (nd, v))
    
    print(dp[full][terminals[0]])

solve()
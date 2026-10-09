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
    core = [int(next(it)) - 1 for _ in range(t)]
    
    # Build graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # Map core languages to bit positions
    core_index = {lang: i for i, lang in enumerate(core)}
    
    # dp[mask][v] = min cost to connect core set 'mask' and end at node v
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize: each core alone
    for i, lang in enumerate(core):
        dp[1 << i][lang] = 0
    
    # Dijkstra for each mask
    for mask in range(1 << t):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double work
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Run Dijkstra from current dp[mask]
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        while pq:
            d, u = heapq.heappop(pq)
            if d != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(n))
    print(ans)

if __name__ == "__main__":
    solve()
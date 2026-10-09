import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    terminals = [int(input_data[idx + i]) - 1 for i in range(t)]
    idx += t
    
    INF = 10**18
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # DP[mask][node] = min cost to connect terminals in mask ending at node
    dp = [[INF] * n for _ in range(1 << t)]
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
    
    # For each subset mask, run Dijkstra from all nodes in that mask state
    for mask in range(1 << t):
        # Combine two submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other > sub:  # avoid duplicate work
                for node in range(n):
                    dp[mask][node] = min(dp[mask][node], dp[sub][node] + dp[other][node])
            sub = (sub - 1) & mask
        
        # Dijkstra to propagate through standard nodes
        pq = []
        for node in range(n):
            if dp[mask][node] < INF:
                heapq.heappush(pq, (dp[mask][node], node))
        while pq:
            dist, u = heapq.heappop(pq)
            if dist != dp[mask][u]:
                continue
            for v, w in graph[u]:
                nd = dist + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << t) - 1
    answer = min(dp[full_mask])
    print(answer)

if __name__ == "__main__":
    solve()
import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    idx = 3
    terminals = [int(x) - 1 for x in data[idx:idx + t]]
    idx += t
    
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    num_subsets = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_subsets)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_subsets):
        # 1. Combine submasks
        # To avoid symmetric pairs, we can fix the lowest set bit of mask to be in submask
        lowbit = mask & -mask
        submask = (mask - 1) & mask
        while submask > 0:
            if submask & lowbit:
                rem = mask ^ submask
                dp_mask = dp[mask]
                dp_sub = dp[submask]
                dp_rem = dp[rem]
                for v in range(n):
                    val = dp_sub[v] + dp_rem[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            submask = (submask - 1) & mask
            
        # 2. Dijkstra across graph for the current mask
        pq = []
        dp_mask = dp[mask]
        for v in range(n):
            if dp_mask[v] < INF:
                pq.append((dp_mask[v], v))
        
        heapq.heapify(pq)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if dp_mask[u] + w < dp_mask[v]:
                    dp_mask[v] = dp_mask[u] + w
                    heapq.heappush(pq, (dp_mask[v], v))
                    
    ans = min(dp[(1 << t) - 1])
    print(ans)

if __name__ == '__main__':
    main()
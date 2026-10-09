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
    terminals = [int(data[idx + i]) - 1 for i in range(t)]
    idx += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    INF = 10**18
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0

    for mask in range(1, num_masks):
        # Combination step (only if mask is not a power of 2)
        if (mask & (mask - 1)) != 0:
            dp_mask = dp[mask]
            sub = (mask - 1) & mask
            while sub > (mask ^ sub):
                other = mask ^ sub
                dp_sub = dp[sub]
                dp_other = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
                sub = (sub - 1) & mask

        # Dijkstra relaxation step
        pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
        heapq.heapify(pq)
        
        dp_mask = dp[mask]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if d + w < dp_mask[v]:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))

    full_mask = num_masks - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == '__main__':
    main()
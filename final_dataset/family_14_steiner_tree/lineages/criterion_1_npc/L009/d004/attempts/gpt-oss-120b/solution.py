import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t == 1:
        print(0)
        return

    INF = 10**18
    full = 1 << t
    dp = [[INF] * n for _ in range(full)]

    # initialize single terminals
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # precompute list of masks in increasing order of bits
    masks = list(range(1, full))
    masks.sort(key=lambda x: (x.bit_count(), x))

    for mask in masks:
        # combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # to avoid duplicate work we can ensure sub < other, but not necessary
            for v in range(n):
                val = dp[sub][v] + dp[other][v]
                if val < dp[mask][v]:
                    dp[mask][v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph for this mask
        dist = dp[mask][:]
        pq = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(pq)
        visited = [False] * n
        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        dp[mask] = dist

    answer = min(dp[full - 1])
    print(answer)

if __name__ == "__main__":
    solve()
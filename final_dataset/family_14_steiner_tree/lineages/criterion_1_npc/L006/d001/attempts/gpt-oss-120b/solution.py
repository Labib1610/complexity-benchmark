import sys, heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    terminals = [int(next(it)) for _ in range(t)]
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t == 1:
        print(0)
        return

    INF = 10**18
    full = (1 << t) - 1
    dp = [[INF] * (n + 1) for _ in range(full + 1)]

    # initialise single terminals
    for idx, node in enumerate(terminals):
        dp[1 << idx][node] = 0

    # DP over subsets
    for mask in range(1, full + 1):
        # combine smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dpm = dp[mask]
                dps = dp[sub]
                dpo = dp[other]
                for v in range(1, n + 1):
                    val = dps[v] + dpo[v]
                    if val < dpm[v]:
                        dpm[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph
        dist = dp[mask]
        heap = [(dist[v], v) for v in range(1, n + 1) if dist[v] < INF]
        heapq.heapify(heap)
        visited = [False] * (n + 1)
        while heap:
            d, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    answer = min(dp[full][v] for v in range(1, n + 1))
    print(answer)

if __name__ == "__main__":
    solve()
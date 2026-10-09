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
    cores = [int(next(it)) - 1 for _ in range(t)]
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t <= 1:
        print(0)
        return

    INF = 10**18
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    # initialize singletons
    for i, node in enumerate(cores):
        dp[1 << i][node] = 0

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
                for v in range(n):
                    val = dps[v] + dpo[v]
                    if val < dpm[v]:
                        dpm[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph
        dist = dp[mask]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for to, w in adj[u]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(heap, (nd, to))

    answer = min(dp[full])
    print(answer)

if __name__ == "__main__":
    solve()
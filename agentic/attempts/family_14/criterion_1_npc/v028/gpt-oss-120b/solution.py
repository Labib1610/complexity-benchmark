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
    terminals = [int(next(it)) for _ in range(t)]

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if t == 1:
        print(0)
        return

    FULL = (1 << t) - 1
    INF = 10 ** 18
    dp = [[INF] * (n + 1) for _ in range(1 << t)]

    # initialise single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # iterate over all masks
    for mask in range(1, 1 << t):
        # merge smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:  # both non‑empty
                dpm = dp[mask]
                dps = dp[sub]
                dpo = dp[other]
                for v in range(1, n + 1):
                    cand = dps[v] + dpo[v]
                    if cand < dpm[v]:
                        dpm[v] = cand
            sub = (sub - 1) & mask

        # Dijkstra to propagate through edges
        dist = dp[mask]
        heap = [(dist[v], v) for v in range(1, n + 1)]
        heapq.heapify(heap)

        while heap:
            d, v = heapq.heappop(heap)
            if d != dist[v]:
                continue
            for to, w in adj[v]:
                nd = d + w
                if nd < dist[to]:
                    dist[to] = nd
                    heapq.heappush(heap, (nd, to))

    answer = min(dp[FULL][1:])
    print(answer)


if __name__ == "__main__":
    solve()
import sys
import heapq

INF = 10**18

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) - 1 for _ in range(t)]

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

    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]

    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # iterate masks in increasing order
    for mask in range(1, full_mask + 1):
        # combine smaller subsets
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dps = dp[sub]
                dpo = dp[other]
                dpm = dp[mask]
                for v in range(n):
                    cand = dps[v] + dpo[v]
                    if cand < dpm[v]:
                        dpm[v] = cand
            sub = (sub - 1) & mask

        # Dijkstra for this mask
        heap = []
        dpm = dp[mask]
        for v in range(n):
            if dpm[v] < INF:
                heap.append((dpm[v], v))
        heapq.heapify(heap)

        while heap:
            d, v = heapq.heappop(heap)
            if d != dpm[v]:
                continue
            for to, w in graph[v]:
                nd = d + w
                if nd < dpm[to]:
                    dpm[to] = nd
                    heapq.heappush(heap, (nd, to))

    answer = min(dp[full_mask])
    print(answer)


if __name__ == "__main__":
    solve()
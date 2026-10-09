import sys
import heapq

INF = 10 ** 18

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]          # 0‑based
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(full + 1)]

    # initial masks – single terminals
    for i, node in enumerate(terminals):
        dp[1 << i][node] = 0

    # process all masks
    for mask in range(1, full + 1):
        # ----- subset merging -----
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            # to avoid doing both (sub,other) and (other,sub) we enforce sub < other
            if sub < other:
                dps = dp[sub]
                dpo = dp[other]
                dpm = dp[mask]
                for v in range(n):
                    val = dps[v] + dpo[v]
                    if val < dpm[v]:
                        dpm[v] = val
            sub = (sub - 1) & mask

        # ----- multi‑source Dijkstra -----
        dist = dp[mask]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)

        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    ans = min(dp[full])
    print(ans)


if __name__ == "__main__":
    solve()
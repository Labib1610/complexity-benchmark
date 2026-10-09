import sys
import heapq

INF = 10 ** 18

def solve() -> None:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        adj[u].append((v, w))
        adj[v].append((u, w))

    full = 1 << t
    dp = [[INF] * n for _ in range(full)]

    # initial masks: single terminals
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0

    # process masks in increasing order of bits
    for mask in range(1, full):
        # merge submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dps = dp[sub]
                dpo = dp[other]
                dp_mask = dp[mask]
                # try to improve via meeting at same vertex
                for v in range(n):
                    val = dps[v] + dpo[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask

        # Dijkstra to propagate through graph edges
        dist = dp[mask]
        heap = [(dist[v], v) for v in range(n) if dist[v] < INF]
        heapq.heapify(heap)
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

    ans = min(dp[full - 1])
    print(ans)


if __name__ == "__main__":
    solve()
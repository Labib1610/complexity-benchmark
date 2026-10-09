import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    terminals = [next(it) - 1 for _ in range(t)]

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    full = 1 << t
    INF = 10**30
    dp = [[INF] * n for _ in range(full)]

    for i, terminal in enumerate(terminals):
        dp[1 << i][terminal] = 0

    for mask in range(1, full):
        row = dp[mask]

        if mask & (mask - 1):
            lowest_bit = mask & -mask
            sub = (mask - 1) & mask

            while sub:
                if sub & lowest_bit:
                    other = mask ^ sub
                    left = dp[sub]
                    right = dp[other]
                    for v in range(n):
                        candidate = left[v] + right[v]
                        if candidate < row[v]:
                            row[v] = candidate
                sub = (sub - 1) & mask

        heap = [(cost, v) for v, cost in enumerate(row) if cost < INF]
        heapq.heapify(heap)

        while heap:
            dist, u = heapq.heappop(heap)
            if dist != row[u]:
                continue

            for v, weight in graph[u]:
                new_dist = dist + weight
                if new_dist < row[v]:
                    row[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    print(min(dp[full - 1]))

if __name__ == "__main__":
    main()
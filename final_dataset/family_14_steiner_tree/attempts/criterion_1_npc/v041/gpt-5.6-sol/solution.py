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

    if t == 1:
        print(0)
        return

    inf = 10**30
    size = 1 << t
    dp = [[inf] * n for _ in range(size)]

    for i, vertex in enumerate(terminals):
        dp[1 << i][vertex] = 0

    for mask in range(1, size):
        current = dp[mask]

        if mask & (mask - 1):
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:
                    left = dp[sub]
                    right = dp[other]
                    for v in range(n):
                        value = left[v] + right[v]
                        if value < current[v]:
                            current[v] = value
                sub = (sub - 1) & mask

        heap = [(current[v], v) for v in range(n) if current[v] < inf]
        heapq.heapify(heap)

        while heap:
            dist, u = heapq.heappop(heap)
            if dist != current[u]:
                continue
            for v, weight in graph[u]:
                new_dist = dist + weight
                if new_dist < current[v]:
                    current[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
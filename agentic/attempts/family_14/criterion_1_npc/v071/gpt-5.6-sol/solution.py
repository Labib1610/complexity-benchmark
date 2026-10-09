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

        heap = [(distance, v) for v, distance in enumerate(current)
                if distance < inf]
        heapq.heapify(heap)

        while heap:
            distance, u = heapq.heappop(heap)
            if distance != current[u]:
                continue
            for v, weight in graph[u]:
                new_distance = distance + weight
                if new_distance < current[v]:
                    current[v] = new_distance
                    heapq.heappush(heap, (new_distance, v))

    print(min(dp[-1]))

if __name__ == "__main__":
    main()
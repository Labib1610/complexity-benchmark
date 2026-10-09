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
    total_masks = 1 << t
    dp = [[inf] * n for _ in range(total_masks)]

    for mask in range(1, total_masks):
        current = dp[mask]

        if mask & (mask - 1) == 0:
            bit = mask.bit_length() - 1
            current[terminals[bit]] = 0
        else:
            lowest_bit = mask & -mask
            submask = (mask - 1) & mask

            while submask:
                if submask & lowest_bit:
                    other = mask ^ submask
                    left = dp[submask]
                    right = dp[other]

                    for v in range(n):
                        candidate = left[v] + right[v]
                        if candidate < current[v]:
                            current[v] = candidate

                submask = (submask - 1) & mask

        heap = [(cost, v) for v, cost in enumerate(current) if cost < inf]
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

    print(min(dp[total_masks - 1]))

if __name__ == "__main__":
    main()
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
    dp = [None] * size

    for mask in range(1, size):
        costs = [inf] * n

        if mask & (mask - 1) == 0:
            bit = mask.bit_length() - 1
            costs[terminals[bit]] = 0
        else:
            submask = (mask - 1) & mask
            while submask:
                other = mask ^ submask
                if submask < other:
                    left = dp[submask]
                    right = dp[other]
                    for v in range(n):
                        candidate = left[v] + right[v]
                        if candidate < costs[v]:
                            costs[v] = candidate
                submask = (submask - 1) & mask

        heap = [(costs[v], v) for v in range(n) if costs[v] < inf]
        heapq.heapify(heap)

        while heap:
            dist, u = heapq.heappop(heap)
            if dist != costs[u]:
                continue
            for v, weight in graph[u]:
                new_dist = dist + weight
                if new_dist < costs[v]:
                    costs[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        dp[mask] = costs

    print(min(dp[size - 1]))

if __name__ == "__main__":
    main()
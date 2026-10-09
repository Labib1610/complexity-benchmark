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

    INF = 10**30
    total_masks = 1 << t
    dp = [None] * total_masks

    for mask in range(1, total_masks):
        cur = [INF] * n

        if mask & (mask - 1) == 0:
            terminal_index = mask.bit_length() - 1
            cur[terminals[terminal_index]] = 0
        else:
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:
                    left = dp[sub]
                    right = dp[other]
                    for v in range(n):
                        candidate = left[v] + right[v]
                        if candidate < cur[v]:
                            cur[v] = candidate
                sub = (sub - 1) & mask

        heap = [(cur[v], v) for v in range(n) if cur[v] < INF]
        heapq.heapify(heap)

        while heap:
            dist, u = heapq.heappop(heap)
            if dist != cur[u]:
                continue
            for v, weight in graph[u]:
                new_dist = dist + weight
                if new_dist < cur[v]:
                    cur[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        dp[mask] = cur

    print(min(dp[-1]))

if __name__ == "__main__":
    main()
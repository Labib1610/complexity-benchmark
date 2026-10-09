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
    size = 1 << t
    dp = [[INF] * n for _ in range(size)]

    for mask in range(1, size):
        cur = dp[mask]

        if mask & (mask - 1) == 0:
            terminal_index = mask.bit_length() - 1
            cur[terminals[terminal_index]] = 0
        else:
            lowbit = mask & -mask
            sub = (mask - 1) & mask

            while sub:
                if sub & lowbit:
                    other = mask ^ sub
                    a = dp[sub]
                    b = dp[other]
                    for v in range(n):
                        candidate = a[v] + b[v]
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

    print(dp[size - 1][terminals[0]])

if __name__ == "__main__":
    main()
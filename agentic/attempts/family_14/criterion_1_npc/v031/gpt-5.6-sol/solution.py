import sys
import heapq

def main():
    input = sys.stdin.buffer.readline
    n, m, t = map(int, input().split())
    terminals = [x - 1 for x in map(int, input().split())]

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    if t == 1:
        print(0)
        return

    inf = 10**30
    total_masks = 1 << t
    dp = [[inf] * n for _ in range(total_masks)]

    for i, terminal in enumerate(terminals):
        dp[1 << i][terminal] = 0

    for mask in range(1, total_masks):
        dist = dp[mask]

        if mask & (mask - 1):
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if sub < other:
                    a = dp[sub]
                    b = dp[other]
                    for v in range(n):
                        value = a[v] + b[v]
                        if value < dist[v]:
                            dist[v] = value
                sub = (sub - 1) & mask

        heap = [(d, v) for v, d in enumerate(dist) if d < inf]
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

    print(min(dp[-1]))

if __name__ == "__main__":
    main()
import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    target = bytearray(n)
    for _ in range(t):
        target[next(it) - 1] = 1

    graph = [[] for _ in range(n)]
    degree = [0] * n
    total = 0

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
        total += w

    removed = bytearray(n)
    queue = deque(
        i for i in range(n)
        if not target[i] and degree[i] <= 1
    )

    while queue:
        u = queue.popleft()
        if removed[u] or target[u] or degree[u] > 1:
            continue

        removed[u] = 1
        for v, w in graph[u]:
            if not removed[v]:
                total -= w
                degree[v] -= 1
                degree[u] -= 1
                if not target[v] and degree[v] == 1:
                    queue.append(v)
                break

    print(total)

if __name__ == "__main__":
    main()
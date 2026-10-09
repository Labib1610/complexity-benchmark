import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m, t = map(int, input().split())

    critical = bytearray(n)
    terminals = []
    while len(terminals) < t:
        terminals.extend(map(int, input().split()))
    for x in terminals:
        critical[x - 1] = 1

    graph = [[] for _ in range(n)]
    degree = [0] * n
    total_cost = 0

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
        total_cost += w

    queue = deque(
        i for i in range(n)
        if not critical[i] and degree[i] <= 1
    )
    removed = bytearray(n)

    while queue:
        node = queue.popleft()
        if removed[node]:
            continue
        removed[node] = 1

        for neighbor, cost in graph[node]:
            if not removed[neighbor]:
                total_cost -= cost
                degree[neighbor] -= 1
                if not critical[neighbor] and degree[neighbor] == 1:
                    queue.append(neighbor)
                break

    print(total_cost)

if __name__ == "__main__":
    main()
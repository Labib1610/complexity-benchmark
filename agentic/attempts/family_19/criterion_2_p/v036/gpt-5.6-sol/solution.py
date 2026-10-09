import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    _ = next(it)

    s = next(it) - 1
    t = next(it) - 1
    demand = next(it)

    graph = [[] for _ in range(n)]
    original = []

    def add_edge(u, v, capacity):
        forward_index = len(graph[u])
        reverse_index = len(graph[v]) + (1 if u == v else 0)

        graph[u].append([v, capacity, reverse_index])
        graph[v].append([u, 0, forward_index])
        original.append((u, forward_index, capacity))

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        add_edge(u, v, capacity)

    if s == t:
        if demand == 0:
            print("YES")
            print(*([0] * m))
        else:
            print("NO")
        return

    total_flow = 0
    level = [-1] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v, capacity, _ in graph[u]:
                if capacity > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    if v == t:
                        return True
                    queue.append(v)
        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(graph[u]):
            edge_index = ptr[u]
            edge = graph[u][edge_index]
            v, capacity, reverse_index = edge

            if capacity > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, capacity))
                if sent:
                    edge[1] -= sent
                    graph[v][reverse_index][1] += sent
                    return sent

            ptr[u] += 1

        return 0

    while total_flow < demand and bfs():
        ptr = [0] * n
        while total_flow < demand:
            sent = dfs(s, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        print("NO")
        return

    flows = []
    for u, edge_index, initial_capacity in original:
        remaining_capacity = graph[u][edge_index][1]
        flows.append(initial_capacity - remaining_capacity)

    print("YES")
    print(*flows)


if __name__ == "__main__":
    main()
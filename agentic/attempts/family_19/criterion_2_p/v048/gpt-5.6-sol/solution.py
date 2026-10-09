import sys
from collections import deque

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
    to = []
    residual = []
    original_capacity = []
    edge_indices = []

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)

        idx = len(to)
        graph[u].append(idx)
        to.append(v)
        residual.append(capacity)

        graph[v].append(idx + 1)
        to.append(u)
        residual.append(0)

        edge_indices.append(idx)
        original_capacity.append(capacity)

    if s == t:
        if demand != 0:
            print("NO")
        else:
            print("YES")
            print(" ".join("0" for _ in range(m)))
        return

    sys.setrecursionlimit(max(1_000_000, n * 2 + 10))
    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            v = queue.popleft()
            next_level = level[v] + 1
            for edge in graph[v]:
                u = to[edge]
                if residual[edge] > 0 and level[u] == -1:
                    level[u] = next_level
                    queue.append(u)

        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed

        while ptr[v] < len(graph[v]):
            edge = graph[v][ptr[v]]
            u = to[edge]

            if residual[edge] > 0 and level[u] == level[v] + 1:
                sent = dfs(u, min(pushed, residual[edge]))
                if sent:
                    residual[edge] -= sent
                    residual[edge ^ 1] += sent
                    return sent

            ptr[v] += 1

        return 0

    flow = 0
    while flow < demand and bfs():
        ptr[:] = [0] * n
        while flow < demand:
            sent = dfs(s, demand - flow)
            if sent == 0:
                break
            flow += sent

    if flow < demand:
        print("NO")
        return

    answer = [
        original_capacity[i] - residual[edge_indices[i]]
        for i in range(m)
    ]

    print("YES")
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()
import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    _k = next(it)

    s = next(it) - 1
    t = next(it) - 1
    demand = next(it)

    edges_input = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        edges_input.append((u, v, capacity))

    if s == t:
        if demand == 0:
            print("YES")
            print(" ".join(["0"] * m))
        else:
            print("NO")
        return

    if demand < 0:
        demand = -demand
        s, t = t, s

    if demand == 0:
        print("YES")
        print(" ".join(["0"] * m))
        return

    graph = [[] for _ in range(n)]
    to = []
    residual = []

    for u, v, capacity in edges_input:
        edge_id = len(to)
        to.append(v)
        residual.append(capacity)
        graph[u].append(edge_id)

        to.append(u)
        residual.append(0)
        graph[v].append(edge_id + 1)

    sys.setrecursionlimit(max(1_000_000, 2 * n + 100))

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            v = queue.popleft()
            next_level = level[v] + 1
            for edge_id in graph[v]:
                u = to[edge_id]
                if residual[edge_id] > 0 and level[u] == -1:
                    level[u] = next_level
                    queue.append(u)

        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed

        while ptr[v] < len(graph[v]):
            edge_id = graph[v][ptr[v]]
            u = to[edge_id]

            if residual[edge_id] > 0 and level[u] == level[v] + 1:
                sent = dfs(u, min(pushed, residual[edge_id]))
                if sent:
                    residual[edge_id] -= sent
                    residual[edge_id ^ 1] += sent
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
        capacity - residual[2 * i]
        for i, (_, _, capacity) in enumerate(edges_input)
    ]

    print("YES")
    print(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()
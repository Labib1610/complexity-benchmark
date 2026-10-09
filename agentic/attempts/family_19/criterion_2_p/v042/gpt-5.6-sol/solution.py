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
    target = next(it)

    graph = [[] for _ in range(n)]
    to = []
    capacity = []
    original_edges = []
    limits = []

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        limit = next(it)

        edge_id = len(to)
        to.append(v)
        capacity.append(limit)
        graph[u].append(edge_id)

        to.append(u)
        capacity.append(0)
        graph[v].append(edge_id + 1)

        original_edges.append(edge_id)
        limits.append(limit)

    if target == 0:
        sys.stdout.write("YES\n" + " ".join(["0"] * m) + "\n")
        return

    if s == t:
        sys.stdout.write("NO\n")
        return

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
                if capacity[edge_id] > 0 and level[u] == -1:
                    level[u] = next_level
                    queue.append(u)

        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed

        edges = graph[v]
        while ptr[v] < len(edges):
            edge_id = edges[ptr[v]]
            u = to[edge_id]

            if capacity[edge_id] > 0 and level[u] == level[v] + 1:
                sent = dfs(u, min(pushed, capacity[edge_id]))
                if sent:
                    capacity[edge_id] -= sent
                    capacity[edge_id ^ 1] += sent
                    return sent

            ptr[v] += 1

        return 0

    flow = 0
    while flow < target and bfs():
        ptr[:] = [0] * n
        while flow < target:
            sent = dfs(s, target - flow)
            if sent == 0:
                break
            flow += sent

    if flow < target:
        sys.stdout.write("NO\n")
        return

    result = [
        str(limit - capacity[edge_id])
        for edge_id, limit in zip(original_edges, limits)
    ]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(result) + "\n")

if __name__ == "__main__":
    main()
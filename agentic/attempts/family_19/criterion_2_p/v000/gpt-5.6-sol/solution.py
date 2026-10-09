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

    s = next(it)
    t = next(it)
    demand = next(it)

    graph = [[] for _ in range(n + 1)]
    to = []
    capacity = []
    original_edges = []

    def add_edge(u, v, cap):
        edge_id = len(to)
        to.append(v)
        capacity.append(cap)
        graph[u].append(edge_id)

        to.append(u)
        capacity.append(0)
        graph[v].append(edge_id + 1)

        original_edges.append(edge_id)

    for _ in range(m):
        u = next(it)
        v = next(it)
        cap = next(it)
        add_edge(u, v, cap)

    if demand == 0:
        sys.stdout.write("YES\n" + " ".join(["0"] * m) + "\n")
        return

    if s == t:
        sys.stdout.write("NO\n")
        return

    sys.setrecursionlimit(max(1_000_000, 2 * n + 100))

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for edge_id in graph[u]:
                v = to[edge_id]
                if capacity[edge_id] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)

        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(graph[u]):
            edge_id = graph[u][ptr[u]]
            v = to[edge_id]

            if capacity[edge_id] > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, capacity[edge_id]))
                if sent:
                    capacity[edge_id] -= sent
                    capacity[edge_id ^ 1] += sent
                    return sent

            ptr[u] += 1

        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        for i in range(n + 1):
            ptr[i] = 0

        while total_flow < demand:
            sent = dfs(s, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        sys.stdout.write("NO\n")
        return

    flows = [str(capacity[edge_id ^ 1]) for edge_id in original_edges]
    sys.stdout.write("YES\n" + " ".join(flows) + "\n")

if __name__ == "__main__":
    main()
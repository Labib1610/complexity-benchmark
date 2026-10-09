import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

class Edge:
    __slots__ = ("to", "rev", "cap", "original")

    def __init__(self, to, rev, cap, original=0):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.original = original


def add_edge(graph, u, v, cap):
    if u == v:
        idx = len(graph[u])
        forward = Edge(v, idx + 1, cap, cap)
        backward = Edge(u, idx, 0, 0)
        graph[u].append(forward)
        graph[u].append(backward)
    else:
        forward = Edge(v, len(graph[v]), cap, cap)
        backward = Edge(u, len(graph[u]), 0, 0)
        graph[u].append(forward)
        graph[v].append(backward)
    return forward


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    _ = next(it)

    source = next(it) - 1
    sink = next(it) - 1
    demand = next(it)

    graph = [[] for _ in range(n)]
    original_edges = []

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        original_edges.append(add_edge(graph, u, v, cap))

    if source == sink:
        print("YES")
        print(*([0] * m))
        return

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if edge.cap > 0 and level[edge.to] == -1:
                    level[edge.to] = level[u] + 1
                    if edge.to == sink:
                        return True
                    queue.append(edge.to)
        return level[sink] != -1

    def dfs(u, pushed):
        if u == sink:
            return pushed

        while ptr[u] < len(graph[u]):
            edge = graph[u][ptr[u]]
            if edge.cap > 0 and level[edge.to] == level[u] + 1:
                sent = dfs(edge.to, min(pushed, edge.cap))
                if sent:
                    edge.cap -= sent
                    graph[edge.to][edge.rev].cap += sent
                    return sent
            ptr[u] += 1
        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        ptr[:] = [0] * n
        while total_flow < demand:
            sent = dfs(source, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        print("NO")
    else:
        flows = [edge.original - edge.cap for edge in original_edges]
        print("YES")
        print(*flows)


if __name__ == "__main__":
    main()
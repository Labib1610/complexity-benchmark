import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


class Edge:
    __slots__ = ("to", "rev", "cap")

    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    next(it)  # Number of asset types, always 1.

    s = next(it) - 1
    t = next(it) - 1
    demand = next(it)

    graph = [[] for _ in range(n)]
    original_edges = []

    def add_edge(u, v, cap):
        forward = Edge(v, len(graph[v]), cap)
        backward = Edge(u, len(graph[u]), 0)
        graph[u].append(forward)
        graph[v].append(backward)
        return forward

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        if u == v:
            original_edges.append((None, 0))
        else:
            edge = add_edge(u, v, cap)
            original_edges.append((edge, cap))

    if demand == 0:
        print("YES")
        print(*([0] * m))
        return

    if s == t:
        print("NO")
        return

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if edge.cap > 0 and level[edge.to] == -1:
                    level[edge.to] = level[u] + 1
                    if edge.to == t:
                        return True
                    queue.append(edge.to)
        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
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

    allocation = []
    for edge, initial_cap in original_edges:
        allocation.append(0 if edge is None else initial_cap - edge.cap)

    print("YES")
    print(*allocation)


if __name__ == "__main__":
    main()
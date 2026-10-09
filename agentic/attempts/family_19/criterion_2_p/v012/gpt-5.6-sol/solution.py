import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


class Edge:
    __slots__ = ("to", "cap", "rev")

    def __init__(self, to, cap):
        self.to = to
        self.cap = cap
        self.rev = None


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
    original_edges = []

    def add_edge(u, v, cap):
        forward = Edge(v, cap)
        backward = Edge(u, 0)
        forward.rev = backward
        backward.rev = forward
        graph[u].append(forward)
        graph[v].append(backward)
        original_edges.append((forward, cap))

    for _ in range(m):
        u = next(it)
        v = next(it)
        cap = next(it)
        add_edge(u, v, cap)

    if demand < 0 or (s == t and demand != 0):
        print("NO")
        return

    if demand == 0:
        print("YES")
        print(*([0] * m))
        return

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)

    def bfs():
        level[:] = [-1] * (n + 1)
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if edge.cap > 0 and level[edge.to] == -1:
                    level[edge.to] = level[u] + 1
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
                    edge.rev.cap += sent
                    return sent
            ptr[u] += 1

        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        ptr[:] = [0] * (n + 1)
        while total_flow < demand:
            sent = dfs(s, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        print("NO")
        return

    flows = [initial_cap - edge.cap for edge, initial_cap in original_edges]
    print("YES")
    print(*flows)


if __name__ == "__main__":
    main()
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

    s = next(it) - 1
    t = next(it) - 1
    required = next(it)

    graph = [[] for _ in range(n)]
    original_edges = []

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)

        forward = Edge(v, capacity)
        backward = Edge(u, 0)
        forward.rev = backward
        backward.rev = forward

        graph[u].append(forward)
        graph[v].append(backward)
        original_edges.append((forward, capacity))

    if required == 0:
        print("YES")
        print(" ".join("0" for _ in range(m)))
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
                    edge.rev.cap += sent
                    return sent
            ptr[u] += 1
        return 0

    total_flow = 0
    while total_flow < required and bfs():
        ptr[:] = [0] * n
        while total_flow < required:
            sent = dfs(s, required - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < required:
        print("NO")
    else:
        flows = [str(capacity - edge.cap) for edge, capacity in original_edges]
        print("YES")
        print(" ".join(flows))


if __name__ == "__main__":
    main()
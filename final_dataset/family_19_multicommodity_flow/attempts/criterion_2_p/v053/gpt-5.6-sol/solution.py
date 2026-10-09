import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


def read_ints():
    data = sys.stdin.buffer.read()
    number = 0
    in_number = False
    for byte in data:
        if 48 <= byte <= 57:
            number = number * 10 + byte - 48
            in_number = True
        elif in_number:
            yield number
            number = 0
            in_number = False
    if in_number:
        yield number


class Edge:
    __slots__ = ("to", "rev", "cap")

    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [-1] * n
        self.ptr = [0] * n

    def add_edge(self, u, v, capacity):
        forward = Edge(v, len(self.graph[v]), capacity)
        backward = Edge(u, len(self.graph[u]), 0)
        self.graph[u].append(forward)
        self.graph[v].append(backward)
        return forward

    def bfs(self, source, sink):
        level = self.level
        for i in range(self.n):
            level[i] = -1

        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            next_level = level[u] + 1
            for edge in self.graph[u]:
                if edge.cap > 0 and level[edge.to] == -1:
                    level[edge.to] = next_level
                    queue.append(edge.to)

        return level[sink] != -1

    def dfs(self, u, sink, pushed):
        if pushed == 0:
            return 0
        if u == sink:
            return pushed

        graph = self.graph
        level = self.level
        ptr = self.ptr

        while ptr[u] < len(graph[u]):
            edge = graph[u][ptr[u]]
            if edge.cap > 0 and level[edge.to] == level[u] + 1:
                flow = self.dfs(edge.to, sink, min(pushed, edge.cap))
                if flow:
                    edge.cap -= flow
                    graph[edge.to][edge.rev].cap += flow
                    return flow
            ptr[u] += 1

        return 0

    def max_flow(self, source, sink, limit):
        total = 0
        while total < limit and self.bfs(source, sink):
            self.ptr = [0] * self.n
            while total < limit:
                pushed = self.dfs(source, sink, limit - total)
                if pushed == 0:
                    break
                total += pushed
        return total


def main():
    values = iter(read_ints())
    try:
        n = next(values)
    except StopIteration:
        return

    m = next(values)
    _ = next(values)

    source = next(values) - 1
    sink = next(values) - 1
    required = next(values)

    dinic = Dinic(n)
    references = [None] * m
    capacities = [0] * m

    for i in range(m):
        u = next(values) - 1
        v = next(values) - 1
        capacity = next(values)
        capacities[i] = capacity

        if u != v:
            references[i] = dinic.add_edge(u, v, capacity)

    if source == sink:
        if required != 0:
            sys.stdout.write("NO\n")
            return
        flows = [0] * m
    else:
        flow = dinic.max_flow(source, sink, required)
        if flow != required:
            sys.stdout.write("NO\n")
            return

        flows = [
            0 if references[i] is None else capacities[i] - references[i].cap
            for i in range(m)
        ]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, flows)) + "\n")


if __name__ == "__main__":
    main()
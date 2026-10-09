import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [-1] * n
        self.ptr = [0] * n

    def add_edge(self, u, v, capacity):
        forward = [v, len(self.graph[v]), capacity]
        backward = [u, len(self.graph[u]), 0]
        self.graph[u].append(forward)
        self.graph[v].append(backward)
        return forward

    def bfs(self, source, sink):
        self.level = [-1] * self.n
        self.level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for v, _, capacity in self.graph[u]:
                if capacity > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    if v == sink:
                        return True
                    queue.append(v)

        return self.level[sink] != -1

    def dfs(self, u, sink, pushed):
        if u == sink:
            return pushed

        while self.ptr[u] < len(self.graph[u]):
            edge = self.graph[u][self.ptr[u]]
            v, reverse_index, capacity = edge

            if capacity > 0 and self.level[v] == self.level[u] + 1:
                sent = self.dfs(v, sink, min(pushed, capacity))
                if sent:
                    edge[2] -= sent
                    self.graph[v][reverse_index][2] += sent
                    return sent

            self.ptr[u] += 1

        return 0

    def max_flow(self, source, sink, limit):
        flow = 0

        while flow < limit and self.bfs(source, sink):
            self.ptr = [0] * self.n
            while flow < limit:
                sent = self.dfs(source, sink, limit - flow)
                if sent == 0:
                    break
                flow += sent

        return flow


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    _k = next(it)

    source = next(it) - 1
    sink = next(it) - 1
    required = next(it)

    dinic = Dinic(n)
    edges = []

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)

        if u == v:
            edges.append((capacity, None))
        else:
            edge = dinic.add_edge(u, v, capacity)
            edges.append((capacity, edge))

    if required < 0:
        print("NO")
        return

    if source == sink:
        if required != 0:
            print("NO")
            return
        print("YES")
        print(*([0] * m))
        return

    flow = dinic.max_flow(source, sink, required)

    if flow != required:
        print("NO")
        return

    answer = []
    for capacity, edge in edges:
        answer.append(0 if edge is None else capacity - edge[2])

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()
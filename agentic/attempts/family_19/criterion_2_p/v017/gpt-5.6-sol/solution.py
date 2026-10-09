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
    edge_ids = []

    def add_edge(u, v, capacity):
        eid = len(to)
        to.append(v)
        residual.append(capacity)
        original_capacity.append(capacity)
        graph[u].append(eid)

        to.append(u)
        residual.append(0)
        original_capacity.append(0)
        graph[v].append(eid ^ 1)
        return eid

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        edge_ids.append(add_edge(u, v, capacity))

    if demand == 0:
        sys.stdout.write("YES\n" + " ".join(["0"] * m) + "\n")
        return

    if s == t:
        sys.stdout.write("NO\n")
        return

    sys.setrecursionlimit(max(1_000_000, n * 2 + 10))
    level = [-1] * n
    ptr = [0] * n

    def bfs():
        for i in range(n):
            level[i] = -1
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            next_level = level[u] + 1
            for eid in graph[u]:
                v = to[eid]
                if residual[eid] > 0 and level[v] == -1:
                    level[v] = next_level
                    queue.append(v)

        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        edges = graph[u]
        while ptr[u] < len(edges):
            eid = edges[ptr[u]]
            v = to[eid]

            if residual[eid] > 0 and level[v] == level[u] + 1:
                amount = dfs(v, min(pushed, residual[eid]))
                if amount:
                    residual[eid] -= amount
                    residual[eid ^ 1] += amount
                    return amount

            ptr[u] += 1

        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        ptr = [0] * n
        while total_flow < demand:
            pushed = dfs(s, demand - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow < demand:
        sys.stdout.write("NO\n")
        return

    flows = [
        str(original_capacity[eid] - residual[eid])
        for eid in edge_ids
    ]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(flows) + "\n")

if __name__ == "__main__":
    main()
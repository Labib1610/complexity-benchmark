import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


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
    edge_refs = []

    def add_edge(u, v, capacity):
        forward_index = len(graph[u])
        reverse_index = len(graph[v])
        if u == v:
            graph[u].append([v, reverse_index + 1, capacity])
            graph[v].append([u, forward_index, 0])
        else:
            graph[u].append([v, reverse_index, capacity])
            graph[v].append([u, forward_index, 0])
        edge_refs.append((u, forward_index, capacity))

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        add_edge(u, v, capacity)

    if demand == 0 or s == t:
        sys.stdout.write("YES\n" + " ".join(["0"] * m) + "\n")
        return

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            next_level = level[u] + 1
            for v, _, capacity in graph[u]:
                if capacity > 0 and level[v] == -1:
                    level[v] = next_level
                    if v == t:
                        return True
                    queue.append(v)

        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(graph[u]):
            edge = graph[u][ptr[u]]
            v, reverse_index, capacity = edge

            if capacity > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, capacity))
                if sent:
                    edge[2] -= sent
                    graph[v][reverse_index][2] += sent
                    return sent

            ptr[u] += 1

        return 0

    total_flow = 0

    while total_flow < demand and bfs():
        ptr[:] = [0] * n
        while total_flow < demand:
            sent = dfs(s, demand - total_flow)
            if sent == 0:
                break
            total_flow += sent

    if total_flow < demand:
        sys.stdout.write("NO\n")
        return

    flows = []
    for u, index, original_capacity in edge_refs:
        flows.append(str(original_capacity - graph[u][index][2]))

    sys.stdout.write("YES\n" + " ".join(flows) + "\n")


if __name__ == "__main__":
    main()
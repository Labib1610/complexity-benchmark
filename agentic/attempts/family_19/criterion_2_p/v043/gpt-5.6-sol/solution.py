import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)
    next(it)  # Number of commodities, always 1

    s = next(it) - 1
    t = next(it) - 1
    demand = next(it)

    graph = [[] for _ in range(n)]
    original = []

    def add_edge(u, v, capacity):
        forward_index = len(graph[u])
        reverse_index = len(graph[v])
        graph[u].append([v, reverse_index, capacity])
        graph[v].append([u, forward_index, 0])
        return forward_index

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        if u == v:
            original.append(None)
        else:
            edge_index = add_edge(u, v, capacity)
            original.append((u, edge_index, capacity))

    if demand < 0 or (s == t and demand != 0):
        print("NO")
        return

    if demand == 0:
        print("YES")
        print(" ".join(["0"] * m))
        return

    sys.setrecursionlimit(max(1_000_000, 2 * n + 100))

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v, _, capacity in graph[u]:
                if capacity > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)

        return level[t] != -1

    def dfs(u, pushed):
        if u == t or pushed == 0:
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
        print("NO")
        return

    flows = []
    for edge_info in original:
        if edge_info is None:
            flows.append("0")
        else:
            u, edge_index, initial_capacity = edge_info
            residual_capacity = graph[u][edge_index][2]
            flows.append(str(initial_capacity - residual_capacity))

    print("YES")
    print(" ".join(flows))

if __name__ == "__main__":
    main()
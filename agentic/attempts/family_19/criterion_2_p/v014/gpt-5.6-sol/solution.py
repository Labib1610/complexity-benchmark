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

    adj = [[] for _ in range(n)]
    to = []
    residual = []
    original_edges = []

    def add_edge(u, v, capacity):
        edge_id = len(to)
        to.append(v)
        residual.append(capacity)
        to.append(u)
        residual.append(0)
        adj[u].append(edge_id)
        adj[v].append(edge_id ^ 1)
        original_edges.append((edge_id, capacity))

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        capacity = next(it)
        add_edge(u, v, capacity)

    if demand == 0:
        print("YES")
        print(*([0] * m))
        return

    if s == t:
        print("NO")
        return

    sys.setrecursionlimit(max(1000000, n * 2 + 10))
    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for edge_id in adj[u]:
                v = to[edge_id]
                if residual[edge_id] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    if v == t:
                        return True
                    queue.append(v)
        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(adj[u]):
            edge_id = adj[u][ptr[u]]
            v = to[edge_id]

            if residual[edge_id] > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, residual[edge_id]))
                if sent:
                    residual[edge_id] -= sent
                    residual[edge_id ^ 1] += sent
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

    answer = [
        capacity - residual[edge_id]
        for edge_id, capacity in original_edges
    ]

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()
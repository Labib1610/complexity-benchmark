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

    s = next(it)
    t = next(it)
    demand = next(it)

    size = n + 1
    adj = [[] for _ in range(size)]
    to = []
    residual = []
    original = []
    input_edges = []

    def add_edge(u, v, capacity):
        edge_id = len(to)
        to.append(v)
        residual.append(capacity)
        original.append(capacity)
        adj[u].append(edge_id)

        to.append(u)
        residual.append(0)
        original.append(0)
        adj[v].append(edge_id + 1)
        return edge_id

    for _ in range(m):
        u = next(it)
        v = next(it)
        capacity = next(it)
        input_edges.append(add_edge(u, v, capacity))

    if s == t:
        if demand == 0:
            print("YES")
            print(" ".join("0" for _ in range(m)))
        else:
            print("NO")
        return

    sys.setrecursionlimit(max(1_000_000, n * 2 + 10))
    level = [-1] * size
    ptr = [0] * size

    def bfs():
        for i in range(size):
            level[i] = -1
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for eid in adj[u]:
                v = to[eid]
                if residual[eid] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    if v == t:
                        return True
                    queue.append(v)
        return level[t] != -1

    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed

        while ptr[u] < len(adj[u]):
            eid = adj[u][ptr[u]]
            v = to[eid]

            if residual[eid] > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, residual[eid]))
                if sent:
                    residual[eid] -= sent
                    residual[eid ^ 1] += sent
                    return sent

            ptr[u] += 1

        return 0

    flow = 0
    while flow < demand and bfs():
        for i in range(size):
            ptr[i] = 0

        while flow < demand:
            sent = dfs(s, demand - flow)
            if sent == 0:
                break
            flow += sent

    if flow < demand:
        print("NO")
        return

    answer = [str(original[eid] - residual[eid]) for eid in input_edges]
    print("YES")
    print(" ".join(answer))

if __name__ == "__main__":
    main()
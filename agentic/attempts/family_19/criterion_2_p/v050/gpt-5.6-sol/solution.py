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
    capacity = []
    original = []

    for i in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)

        edge_id = len(to)
        to.append(v)
        capacity.append(c)
        graph[u].append(edge_id)

        to.append(u)
        capacity.append(0)
        graph[v].append(edge_id ^ 1)

        original.append(c)

    if demand < 0 or (s == t and demand != 0):
        print("NO")
        return

    if demand == 0:
        print("YES")
        print(" ".join(["0"] * m))
        return

    sys.setrecursionlimit(max(1000000, n + 100))
    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            next_level = level[u] + 1
            for eid in graph[u]:
                v = to[eid]
                if capacity[eid] > 0 and level[v] == -1:
                    level[v] = next_level
                    queue.append(v)

        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(graph[u]):
            eid = graph[u][ptr[u]]
            v = to[eid]

            if capacity[eid] > 0 and level[v] == level[u] + 1:
                amount = dfs(v, min(pushed, capacity[eid]))
                if amount:
                    capacity[eid] -= amount
                    capacity[eid ^ 1] += amount
                    return amount

            ptr[u] += 1

        return 0

    flow = 0
    while flow < demand and bfs():
        ptr[:] = [0] * n
        while flow < demand:
            pushed = dfs(s, demand - flow)
            if pushed == 0:
                break
            flow += pushed

    if flow != demand:
        print("NO")
        return

    result = [str(original[i] - capacity[2 * i]) for i in range(m)]
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()
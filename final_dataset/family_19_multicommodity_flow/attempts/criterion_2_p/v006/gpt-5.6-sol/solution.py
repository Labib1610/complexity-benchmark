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
    edge_refs = []

    def add_edge(u, v, cap):
        forward_index = len(graph[u])
        reverse_index = len(graph[v])
        graph[u].append([v, reverse_index, cap])
        graph[v].append([u, forward_index, 0])
        return forward_index

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)

        if u == v:
            edge_refs.append(None)
        else:
            idx = add_edge(u, v, cap)
            edge_refs.append((u, idx, cap))

    if demand == 0:
        print("YES")
        print(" ".join(["0"] * m))
        return

    if s == t:
        print("YES")
        print(" ".join(["0"] * m))
        return

    sys.setrecursionlimit(max(1000000, 2 * n + 100))

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v, rev, cap in graph[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    if v == t:
                        return True
                    queue.append(v)
        return level[t] != -1

    def dfs(u, pushed):
        if u == t:
            return pushed

        while ptr[u] < len(graph[u]):
            edge = graph[u][ptr[u]]
            v, rev, cap = edge

            if cap > 0 and level[v] == level[u] + 1:
                sent = dfs(v, min(pushed, cap))
                if sent:
                    edge[2] -= sent
                    graph[v][rev][2] += sent
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
    for ref in edge_refs:
        if ref is None:
            flows.append("0")
        else:
            u, idx, original_cap = ref
            flows.append(str(original_cap - graph[u][idx][2]))

    print("YES")
    print(" ".join(flows))

if __name__ == "__main__":
    main()
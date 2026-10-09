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
    required = next(it)

    graph = [[] for _ in range(n)]
    original_caps = [0] * m
    edge_refs = [None] * m

    for i in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        original_caps[i] = cap

        if u == v:
            continue

        forward = [v, len(graph[v]), cap]
        reverse = [u, len(graph[u]), 0]
        graph[u].append(forward)
        graph[v].append(reverse)
        edge_refs[i] = forward

    if required == 0:
        print("YES")
        print(" ".join(["0"] * m))
        return

    if s == t:
        print("NO")
        return

    sys.setrecursionlimit(max(1_000_000, n + 100))

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        queue = deque([s])

        while queue:
            v = queue.popleft()
            next_level = level[v] + 1
            for edge in graph[v]:
                if edge[2] > 0 and level[edge[0]] == -1:
                    level[edge[0]] = next_level
                    queue.append(edge[0])

        return level[t] != -1

    def dfs(v, pushed):
        if v == t:
            return pushed

        while ptr[v] < len(graph[v]):
            edge = graph[v][ptr[v]]
            to, rev, cap = edge

            if cap > 0 and level[to] == level[v] + 1:
                sent = dfs(to, min(pushed, cap))
                if sent:
                    edge[2] -= sent
                    graph[to][rev][2] += sent
                    return sent

            ptr[v] += 1

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
        return

    flows = []
    for i in range(m):
        ref = edge_refs[i]
        if ref is None:
            flows.append("0")
        else:
            flows.append(str(original_caps[i] - ref[2]))

    print("YES")
    print(" ".join(flows))

if __name__ == "__main__":
    main()
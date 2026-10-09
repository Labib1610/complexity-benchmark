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
    cap = []
    original_edges = []
    original_caps = []

    def add_edge(u, v, c):
        idx = len(to)
        to.extend((v, u))
        cap.extend((c, 0))
        adj[u].append(idx)
        adj[v].append(idx ^ 1)
        return idx

    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        idx = add_edge(u, v, c)
        original_edges.append(idx)
        original_caps.append(c)

    if demand < 0 or (s == t and demand != 0):
        print("NO")
        return

    if demand == 0:
        print("YES")
        print(*([0] * m))
        return

    sys.setrecursionlimit(max(1000000, 2 * n + 10))

    level = [-1] * n
    ptr = [0] * n

    def bfs():
        level[:] = [-1] * n
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for edge_idx in adj[v]:
                u = to[edge_idx]
                if cap[edge_idx] > 0 and level[u] == -1:
                    level[u] = level[v] + 1
                    if u == t:
                        return True
                    q.append(u)
        return level[t] != -1

    def dfs(v, pushed):
        if v == t:
            return pushed

        while ptr[v] < len(adj[v]):
            edge_idx = adj[v][ptr[v]]
            u = to[edge_idx]

            if cap[edge_idx] > 0 and level[u] == level[v] + 1:
                sent = dfs(u, min(pushed, cap[edge_idx]))
                if sent:
                    cap[edge_idx] -= sent
                    cap[edge_idx ^ 1] += sent
                    return sent

            ptr[v] += 1

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

    result = [
        original_caps[i] - cap[original_edges[i]]
        for i in range(m)
    ]

    print("YES")
    print(*result)

if __name__ == "__main__":
    main()
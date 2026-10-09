import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # product type, always 1
    s = int(next(it)) - 1
    t = int(next(it)) - 1
    d = int(next(it))

    edges = []
    graph = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        graph[u].append([v, c, i, len(graph[v])])
        graph[v].append([u, 0, i, len(graph[u]) - 1])
        edges.append((u, v, c))

    # Dinic's algorithm
    level = [-1] * n
    it_ptr = [0] * n

    def bfs():
        for i in range(n):
            level[i] = -1
        q = deque()
        q.append(s)
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, idx, rev in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def dfs(u, f):
        if u == t:
            return f
        while it_ptr[u] < len(graph[u]):
            v, cap, idx, rev = graph[u][it_ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(f, cap))
                if ret > 0:
                    graph[u][it_ptr[u]][1] -= ret
                    graph[v][rev][1] += ret
                    return ret
            it_ptr[u] += 1
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        it_ptr = [0] * n
        while True:
            f = dfs(s, INF)
            if f == 0:
                break
            flow += f

    if flow != d:
        print("NO")
        return

    # Extract flow on each original edge
    ans = [0] * m
    for u in range(n):
        for v, cap, idx, rev in graph[u]:
            if idx != -1 and edges[idx][0] == u and edges[idx][1] == v:
                ans[idx] = edges[idx][2] - cap  # original capacity - remaining capacity

    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()
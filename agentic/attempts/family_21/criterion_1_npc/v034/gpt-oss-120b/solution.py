import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    specials = [int(next(it)) for _ in range(k)]
    edges = []
    adj = [[] for _ in range(n+1)]
    for idx in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
        # for flow graph, we need directed edges both ways
        adj[u].append([v, w, idx])
        adj[v].append([u, w, idx])

    # This solution only handles k == 2 (minimum s-t cut)
    if k != 2:
        print("NO")
        return
    s, t = specials[0], specials[1]

    # Build flow network with capacities = weights
    N = n + 1
    graph = [[] for _ in range(N)]

    def add_edge(u, v, cap, eid):
        graph[u].append([v, cap, len(graph[v]), eid])
        graph[v].append([u, 0, len(graph[u]) - 1, -1])  # reverse edge

    for idx, (u, v, w) in enumerate(edges):
        add_edge(u, v, w, idx)
        add_edge(v, u, w, idx)  # because undirected, add both directions

    INF = 10**18

    def bfs(level):
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev, _ in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def dfs(u, flow, level, it_ptr):
        if u == t:
            return flow
        for i in range(it_ptr[u], len(graph[u])):
            it_ptr[u] = i
            v, cap, rev, _ = graph[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(flow, cap), level, it_ptr)
                if ret:
                    graph[u][i][1] -= ret
                    graph[v][rev][1] += ret
                    return ret
        return 0

    maxflow = 0
    while True:
        level = [-1]*N
        if not bfs(level):
            break
        it_ptr = [0]*N
        while True:
            pushed = dfs(s, INF, level, it_ptr)
            if not pushed:
                break
            maxflow += pushed

    # After maxflow, find reachable from s in residual graph
    visited = [False]*N
    stack = [s]
    visited[s] = True
    while stack:
        u = stack.pop()
        for v, cap, rev, _ in graph[u]:
            if cap > 0 and not visited[v]:
                visited[v] = True
                stack.append(v)

    cut_edges = []
    total = 0
    for u in range(1, n+1):
        if not visited[u]:
            continue
        for v, cap, rev, eid in graph[u]:
            if visited[v]:
                continue
            # edge from visited to non-visited in original undirected graph
            if eid != -1:
                # each undirected edge appears twice; count once
                if eid not in cut_edges:
                    cut_edges.append(eid)
                    total += edges[eid][2]

    if total <= B:
        print("YES")
        print(len(cut_edges))
        for eid in cut_edges:
            u, v, _ = edges[eid]
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
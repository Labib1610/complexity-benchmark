import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        edges.append((u, v, c))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Check if max flow >= d using Dinic's algorithm
    # Build flow network
    N = n + 1
    source = s
    sink = t
    
    # Edge structure: to, rev, cap, flow, edge_id
    graph = [[] for _ in range(N)]
    edge_info = []
    
    for i, (u, v, c) in enumerate(edges):
        # Forward edge
        graph[u].append([v, len(graph[v]), c, 0, i])
        # Backward edge
        graph[v].append([u, len(graph[u]) - 1, 0, 0, -1])
        edge_info.append((u, len(graph[u]) - 1, v, len(graph[v]) - 1))
    
    def bfs():
        level = [-1] * N
        q = deque([source])
        level[source] = 0
        while q:
            u = q.popleft()
            for v, rev, cap, flow, _ in graph[u]:
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, pushed, level, ptr):
        if u == sink:
            return pushed
        for i in range(ptr[u], len(graph[u])):
            ptr[u] = i
            v, rev, cap, flow, _ = graph[u][i]
            if cap - flow > 0 and level[v] == level[u] + 1:
                tr = dfs(v, min(pushed, cap - flow), level, ptr)
                if tr > 0:
                    graph[u][i][3] += tr
                    graph[v][rev][3] -= tr
                    return tr
        return 0
    
    total_flow = 0
    while True:
        level = bfs()
        if level[sink] == -1:
            break
        ptr = [0] * N
        while True:
            pushed = dfs(source, float('inf'), level, ptr)
            if pushed == 0:
                break
            total_flow += pushed
            if total_flow >= d:
                break
        if total_flow >= d:
            break
    
    if total_flow < d:
        print("NO")
        return
    
    print("YES")
    result = [0] * m
    for i in range(m):
        u = edges[i][0]
        # Find the forward edge in graph[u] with edge_id i
        for edge in graph[u]:
            if edge[4] == i:
                result[i] = edge[3]
                break
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
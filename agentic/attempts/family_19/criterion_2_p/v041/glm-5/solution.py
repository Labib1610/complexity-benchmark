import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    _ = int(input_data[idx]); idx += 1
    s = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        cap = int(input_data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Dinic's max flow
    # edge representation: to, rev, cap
    graph = [[] for _ in range(n + 1)]
    for i, (u, v, cap) in enumerate(edges):
        graph[u].append([v, len(graph[v]), cap])
        graph[v].append([u, len(graph[u]) - 1, 0])
    
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph[u]:
                v, rev, cap = e
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0
    
    def dfs(u, f):
        if u == t:
            return f
        while ptr[u] < len(graph[u]):
            e = graph[u][ptr[u]]
            v = e[0]
            if e[2] > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(f, e[2]))
                if pushed > 0:
                    e[2] -= pushed
                    graph[v][e[1]][2] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    flow = 0
    while bfs():
        for i in range(n + 1):
            ptr[i] = 0
        while True:
            f = dfs(s, float('inf'))
            if f == 0:
                break
            flow += f
    
    if flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i, (u, v, cap) in enumerate(edges):
        # The flow on edge i is the residual capacity of the reverse edge
        # Find the forward edge in graph[u]
        for e in graph[u]:
            if e[0] == v:
                # This is the forward edge, its remaining capacity is e[2]
                # Flow = original cap - remaining cap
                result.append(cap - e[2])
                break
    
    print(' '.join(map(str, result)))

solve()
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    s = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append((u, v, w))
        adj[u].append([v, w, len(adj[v])])
        adj[v].append([u, w, len(adj[u]) - 1])
    
    if s == t:
        print("NO")
        return
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * (n + 1)
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in adj[u]:
                v, cap, _ = e
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, pushed, level, it):
        if u == t:
            return pushed
        while it[u] < len(adj[u]):
            e = adj[u][it[u]]
            v, cap, rev = e[0], e[1], e[2]
            if cap > 0 and level[v] == level[u] + 1:
                d = dfs(v, min(pushed, cap), level, it)
                if d > 0:
                    adj[u][it[u]][1] -= d
                    adj[v][rev][1] += d
                    return d
            it[u] += 1
        return 0
    
    while True:
        level = bfs()
        if level[t] < 0:
            break
        it = [0] * (n + 1)
        while True:
            f = dfs(s, float('inf'), level, it)
            if f == 0:
                break
    
    # Find min cut: BFS from s in residual graph
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        for e in adj[u]:
            v, cap, _ = e
            if cap > 0 and not visited[v]:
                visited[v] = True
                q.append(v)
    
    # Collect cut edges
    cut_edges = []
    total = 0
    for i, (u, v, w) in enumerate(edges):
        if visited[u] != visited[v]:
            cut_edges.append((u, v))
            total += w
    
    if total <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

solve()
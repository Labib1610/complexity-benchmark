import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges_input = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges_input.append((u, v, cap))
    
    # Build graph for max flow
    # Nodes: 1..n, plus super source (n+1) and super sink (n+2)
    source = n + 1
    sink = n + 2
    N = n + 2
    
    adj = [[] for _ in range(N + 1)]
    edges = []
    
    def add_edge(u, v, cap):
        edges.append([v, cap, 0])
        edges.append([u, 0, 0])
        adj[u].append(len(edges) - 2)
        adj[v].append(len(edges - 1))
    
    # Add original edges
    for u, v, cap in edges_input:
        add_edge(u, v, cap)
    
    # Add super source to s, and t to super sink
    add_edge(source, s, d)
    add_edge(t, sink, d)
    
    # Dinic's algorithm
    level = [0] * (N + 1)
    ptr = [0] * (N + 1)
    
    def bfs():
        for i in range(N + 1):
            level[i] = -1
        q = deque([source])
        level[source] = 0
        while q:
            u = q.popleft()
            for idx in adj[u]:
                v, cap, flow = edges[idx]
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[sink] != -1
    
    def dfs(u, pushed):
        if pushed == 0 or u == sink:
            return pushed
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            idx = adj[u][i]
            v, cap, flow = edges[idx]
            if level[v] != level[u] + 1:
                continue
            tr = dfs(v, min(pushed, cap - flow))
            if tr == 0:
                continue
            edges[idx][2] += tr
            edges[idx ^ 1][2] -= tr
            return tr
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * (N + 1)
        while True:
            pushed = dfs(source, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow != d:
        print("NO")
        return
    
    print("YES")
    # Extract flows from original edges
    # Original edges are at indices 0, 2, 4, ..., 2*(m-1)
    result = []
    for i in range(m):
        idx = 2 * i
        result.append(str(edges[idx][2]))
    print(" ".join(result))

if __name__ == "__main__":
    solve()
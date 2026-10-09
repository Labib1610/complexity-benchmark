import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # extract type, not used
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
    
    # Build residual graph for Dinic's algorithm
    N = n + 2
    S = 0
    T = n + 1
    graph = [[] for _ in range(N)]
    edge_info = []
    
    def add_edge(u, v, cap):
        graph[u].append(len(edge_info))
        edge_info.append([v, cap, len(edge_info) + 1])
        graph[v].append(len(edge_info))
        edge_info.append([u, 0, len(edge_info) - 1])
    
    # Add edges from super source
    add_edge(S, s, d)
    
    # Add original edges
    for u, v, cap in edges:
        add_edge(u, v, cap)
    
    # Add edge to super sink
    add_edge(t, T, d)
    
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for idx in graph[u]:
                v, cap, _ = edge_info[idx]
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[T] != -1
    
    def dfs(u, flow):
        if u == T:
            return flow
        while ptr[u] < len(graph[u]):
            idx = graph[u][ptr[u]]
            v, cap, rev = edge_info[idx]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    edge_info[idx][1] -= pushed
                    edge_info[rev][1] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * N
        while True:
            pushed = dfs(S, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed
    
    if max_flow != d:
        print("NO")
        return
    
    print("YES")
    # Extract flows from original edges (indices 2, 4, 6, ... in edge_info)
    result = []
    for i in range(m):
        # Original edge is at index 2 + 2*i
        # The reverse edge stores the flow
        rev_idx = 2 + 2*i + 1
        flow = edge_info[rev_idx][1]
        result.append(str(flow))
    print(' '.join(result))

if __name__ == "__main__":
    solve()
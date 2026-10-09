import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # event type, always 1
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
        adj[v].append((u, i))
    
    # Build flow network
    N = n + 2
    S = 0
    T = n + 1
    flow_adj = [[] for _ in range(N)]
    edge_info = []  # (to, rev, cap, flow, is_original)
    
    def add_edge(u, v, cap):
        # forward edge
        flow_adj[u].append(len(edge_info))
        edge_info.append([v, len(flow_adj[v]), cap, 0, True])
        # backward edge
        flow_adj[v].append(len(edge_info))
        edge_info.append([u, len(flow_adj[u]) - 1, 0, 0, False])
    
    # Add edges from original graph
    for u, v, cap in edges:
        add_edge(u, v, cap)
    
    # Add super source and super sink
    add_edge(S, s, d)
    add_edge(t, T, d)
    
    # Dinic's algorithm
    level = [0] * N
    ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            u = q.popleft()
            for idx in flow_adj[u]:
                v, rev, cap, flow, _ = edge_info[idx]
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[T] != -1
    
    def dfs(u, pushed):
        if pushed == 0 or u == T:
            return pushed
        for i in range(ptr[u], len(flow_adj[u])):
            ptr[u] = i
            idx = flow_adj[u][i]
            v, rev, cap, flow, _ = edge_info[idx]
            if level[v] != level[u] + 1:
                continue
            tr = dfs(v, min(pushed, cap - flow))
            if tr == 0:
                continue
            edge_info[idx][3] += tr
            edge_info[rev][3] -= tr
            return tr
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
    
    # Extract flow values for original edges
    result = []
    edge_idx = 0
    for u, v, cap in edges:
        # Find the edge in flow_adj[u] that goes to v
        for idx in flow_adj[u]:
            info = edge_info[idx]
            if info[0] == v and info[4]:  # is_original
                result.append(info[3])  # flow
                break
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
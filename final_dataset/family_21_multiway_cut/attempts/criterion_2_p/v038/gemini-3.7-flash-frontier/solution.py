import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])
    t = int(input_data[3])
    B = int(input_data[4])
    
    ptr = 5
    original_edges = []
    
    # Dinic's Algorithm setup
    # Adjacency list with edge structure: [to, capacity, residual_flow, rev_index]
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        w = int(input_data[ptr + 2])
        ptr += 3
        
        original_edges.append((u, v, w))
        
        # Add undirected edge as two directed edges
        # Edge u -> v
        idx_u = len(graph[u])
        idx_v = len(graph[v])
        
        graph[u].append([v, w, idx_v])
        graph[v].append([u, w, idx_u])
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                v, cap, rev_idx = edge
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level[t] != -1

    cur = [0] * (n + 1)
    
    def dfs(u, flow):
        if u == t or flow == 0:
            return flow
        for i in range(cur[u], len(graph[u])):
            cur[u] = i
            edge = graph[u][i]
            v, cap, rev_idx = edge
            if level[v] == level[u] + 1 and cap > 0:
                pushed = dfs(v, min(flow, cap))
                if pushed > 0:
                    edge[1] -= pushed
                    graph[v][rev_idx][1] += pushed
                    return pushed
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        cur = [0] * (n + 1)
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            max_flow += pushed
            if max_flow > B:
                break
        if max_flow > B:
            break
            
    if max_flow > B:
        sys.stdout.write("NO\n")
        return
        
    # Reachability from s in residual graph
    visited = [False] * (n + 1)
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for edge in graph[u]:
            v, cap, rev_idx = edge
            if cap > 0 and not visited[v]:
                visited[v] = True
                queue.append(v)
                
    cut_edges = []
    for u, v, w in original_edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))
            
    out = ["YES\n", str(len(cut_edges)), "\n"]
    for u, v in cut_edges:
        out.append(f"{u} {v}\n")
    sys.stdout.write("".join(out))

if __name__ == '__main__':
    solve()
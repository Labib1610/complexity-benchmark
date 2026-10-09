import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = next(iterator) # 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    # Adjacency list for Dinic
    # Each edge: [to, capacity, flow, rev_index, original_edge_index]
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        
        idx_u = len(adj[u])
        idx_v = len(adj[v])
        if u == v:
            idx_v += 1
            
        edge_uv = [v, cap, 0, idx_v, i]
        edge_vu = [u, 0, 0, idx_u, -1]
        
        adj[u].append(edge_uv)
        adj[v].append(edge_vu)
        edges.append(edge_uv)
        
    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for edge in adj[v]:
                to, cap, flow, _, _ = edge
                if cap - flow > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    queue.append(to)
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        for cid in range(ptr[v], len(adj[v])):
            ptr[v] = cid
            edge = adj[v][cid]
            to, cap, flow, rev, _ = edge
            tr = cap - flow
            if level[v] + 1 != level[to] or tr == 0:
                continue
            push = dfs(to, min(pushed, tr))
            if push == 0:
                continue
            edge[2] += push
            adj[to][rev][2] -= push
            return push
        return 0

    total_flow = 0
    while total_flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = 0
        while total_flow < d:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow == d:
        print("YES")
        ans = [0] * m
        for edge in edges:
            ans[edge[4]] = edge[2]
        print(*(ans[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
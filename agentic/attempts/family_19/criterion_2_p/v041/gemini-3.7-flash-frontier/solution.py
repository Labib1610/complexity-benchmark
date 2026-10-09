import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
    except StopIteration:
        return
    n = int(n_str)
    m = int(next(iterator))
    _ = next(iterator)
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    # Graph representation for Dinic
    # Each edge: [to, cap, flow, rev_index, original_edge_index]
    adj = [[] for _ in range(n + 1)]
    edge_indices = []
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        
        idx_u = len(adj[u])
        idx_v = len(adj[v])
        
        edge_uv = [v, cap, 0, idx_v, i]
        edge_vu = [u, 0, 0, idx_u, -1]
        
        adj[u].append(edge_uv)
        adj[v].append(edge_vu)
        
        edge_indices.append((u, idx_u))
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for edge in adj[u]:
                v, cap, flow, _, _ = edge
                if cap - flow > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != -1

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        for cid in range(ptr[u], len(adj[u])):
            ptr[u] = cid
            edge = adj[u][cid]
            v = edge[0]
            tr = edge[1] - edge[2]
            if level[u] + 1 != level[v] or tr == 0:
                continue
            push = min(pushed, tr)
            pushed_now = dfs(v, push)
            if pushed_now == 0:
                continue
            edge[2] += pushed_now
            rev_idx = edge[3]
            adj[v][rev_idx][2] -= pushed_now
            return pushed_now
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

    if total_flow < d:
        print("NO")
    else:
        print("YES")
        ans = [0] * m
        for i in range(m):
            u, idx = edge_indices[i]
            ans[i] = adj[u][idx][2]
        print(*(ans))

if __name__ == '__main__':
    solve()
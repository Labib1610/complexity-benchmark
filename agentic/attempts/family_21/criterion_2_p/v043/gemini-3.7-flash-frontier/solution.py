import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    s = int(data[2])
    t = int(data[3])
    B = int(data[4])
    
    edges_input = []
    idx = 5
    
    # Adjacency list for Dinic
    # Each entry in adj[u]: [to, capacity, flow, rev_idx, edge_id]
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        edges_input.append((u, v, w))
        
        # Undirected edge
        idx_u = len(adj[u])
        idx_v = len(adj[v])
        adj[u].append([v, w, 0, idx_v, i])
        adj[v].append([u, w, 0, idx_u, i])
        
    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to, cap, flow, rev, eid in adj[v]:
                if cap - flow > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        for cid in range(ptr[v], len(adj[v])):
            ptr[v] = cid
            to, cap, flow, rev, eid = adj[v][cid]
            tr = level[to]
            if level[v] + 1 != tr or cap - flow == 0:
                continue
            tr_pushed = dfs(to, min(pushed, cap - flow))
            if tr_pushed == 0:
                continue
            adj[v][cid][2] += tr_pushed
            adj[to][rev][2] -= tr_pushed
            return tr_pushed
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = 0
        while True:
            pushed = dfs(s, INF)
            if not pushed:
                break
            max_flow += pushed

    if max_flow > B:
        print("NO")
        return

    # Find reachable vertices in residual graph from s
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        for to, cap, flow, rev, eid in adj[v]:
            if cap - flow > 0 and not visited[to]:
                visited[to] = True
                q.append(to)

    cut_edges = []
    for u, v, w in edges_input:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()
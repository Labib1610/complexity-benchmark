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
    
    s -= 1
    t -= 1
    
    edges = []
    # Dinic's algorithm setup
    # Adjacency list for flow network: to, cap, flow, rev
    adj = [[] for _ in range(n)]
    
    idx = 5
    for i in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3
        edges.append((u, v, w, i))
        
        # For undirected edge with capacity w:
        # We can add u -> v cap w and v -> u cap w
        # In Dinic, we can represent this as:
        # edge 1: u -> v, cap w, rev index in adj[v]
        # edge 2: v -> u, cap w, rev index in adj[u]
        # Note: if both directions have capacity w, the residual graph works with:
        # forward cap w (flow 0), backward cap w (flow 0).
        # When pushing flow from u to v, flow of u->v increases and residual capacity of v->u increases.
        # Standard implementation for undirected edge:
        e1 = [v, w, len(adj[v])]
        e2 = [u, w, len(adj[u])]
        adj[u].append(e1)
        adj[v].append(e2)
        
    level = [-1] * n
    
    def bfs():
        for i in range(n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, rev in adj[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    ptr = [0] * n
    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        for cid in range(ptr[u], len(adj[u])):
            ptr[u] = cid
            v, cap, rev = adj[u][cid]
            tr = adj[v][rev]
            if level[u] + 1 != level[v] or cap == 0:
                continue
            tr_pushed = dfs(v, min(pushed, cap))
            if tr_pushed == 0:
                continue
            adj[u][cid][1] -= tr_pushed
            adj[v][rev][1] += tr_pushed
            return tr_pushed
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        ptr = [0] * n
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            flow += pushed

    if flow > B:
        print("NO")
        return

    # Find reachable vertices from s in residual graph
    visited = [False] * n
    q = deque([s])
    visited[s] = True
    while q:
        u = q.popleft()
        for v, cap, rev in adj[u]:
            if cap > 0 and not visited[v]:
                visited[v] = True
                q.append(v)

    # Cut edges are those with one endpoint in visited and the other not
    cut_edges = []
    for u, v, w, i in edges:
        if visited[u] != visited[v]:
            cut_edges.append((u + 1, v + 1))

    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()
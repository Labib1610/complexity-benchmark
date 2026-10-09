import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    s = int(next(iterator))
    t = int(next(iterator))
    B = int(next(iterator))
    
    # Store original edges to identify cut edges later
    original_edges = []
    
    # Dinic's algorithm setup
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    
    def add_edge(u, v, w):
        # Forward edge u -> v
        nxt.append(head[u])
        head[u] = len(to)
        to.append(v)
        cap.append(w)
        
        # Backward edge v -> u
        nxt.append(head[v])
        head[v] = len(to)
        to.append(u)
        cap.append(w)

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        original_edges.append((u, v))
        add_edge(u, v, w)
        
    level = [-1] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] != -1

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e]
            if level[v] == level[u] + 1 and tr > 0:
                push = min(pushed, tr)
                flow = dfs(v, push)
                if flow > 0:
                    cap[e] -= flow
                    cap[e ^ 1] += flow
                    return flow
            ptr[u] = nxt[e]
            e = nxt[e]
        return 0

    max_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
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
        print("NO")
        return
        
    # Find all vertices reachable from s in the residual graph
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    while q:
        u = q.popleft()
        e = head[u]
        while e != -1:
            v = to[e]
            if cap[e] > 0 and not visited[v]:
                visited[v] = True
                q.append(v)
            e = nxt[e]
            
    cut_edges = []
    for u, v in original_edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))
            
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()
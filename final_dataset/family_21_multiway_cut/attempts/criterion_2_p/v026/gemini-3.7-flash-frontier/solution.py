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
    
    original_edges = []
    
    # Dinic's Algorithm
    head = [-1] * (n + 1)
    to = []
    cap = []
    nxt = []
    
    def add_edge(u, v, c):
        nxt.append(head[u])
        to.append(v)
        cap.append(c)
        head[u] = len(to) - 1
        
        nxt.append(head[v])
        to.append(u)
        cap.append(c)
        head[v] = len(to) - 1

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        original_edges.append((u, v, w))
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
        return level[t] >= 0

    ptr = [0] * (n + 1)
    
    def dfs(u, pushed):
        if pushed == 0 or u == t:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e]
            if level[u] + 1 == level[v] and tr > 0:
                push = dfs(v, min(pushed, tr))
                if push > 0:
                    cap[e] -= push
                    cap[e ^ 1] += push
                    return push
            e = nxt[e]
            ptr[u] = e
        return 0

    flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, INF)
            if pushed == 0:
                break
            flow += pushed
            if flow > B:
                break
        if flow > B:
            break
            
    if flow > B:
        print("NO")
        return

    # Find reachable vertices in residual graph
    visited = [False] * (n + 1)
    q = deque([s])
    visited[s] = True
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
    for u, v, w in original_edges:
        if visited[u] != visited[v]:
            cut_edges.append((u, v))
            
    print("YES")
    print(len(cut_edges))
    for u, v in cut_edges:
        print(f"{u} {v}")

if __name__ == '__main__':
    solve()
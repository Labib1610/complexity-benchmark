import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = next(iterator)
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    # Dinic's Algorithm
    # Nodes: 0 (super-source), 1..n
    src = 0
    dst = t
    
    head = [-1] * (n + 1)
    to = []
    nxt = []
    cap = []
    flow = []
    
    def add_edge(u, v, c):
        to.append(v)
        cap.append(c)
        flow.append(0)
        nxt.append(head[u])
        head[u] = len(to) - 1
        
        to.append(u)
        cap.append(0)
        flow.append(0)
        nxt.append(head[v])
        head[v] = len(to) - 1

    add_edge(src, s, d)
    
    edge_indices = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        edge_indices.append(len(to))
        add_edge(u, v, c)
        
    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[dst] != -1

    def dfs(u, pushed):
        if pushed == 0 or u == dst:
            return pushed
        e = ptr[u]
        while e != -1:
            v = to[e]
            tr = cap[e] - flow[e]
            if level[u] + 1 == level[v] and tr > 0:
                p = dfs(v, min(pushed, tr))
                if p > 0:
                    flow[e] += p
                    flow[e ^ 1] -= p
                    return p
            e = nxt[e]
            ptr[u] = e
        return 0

    total_flow = 0
    INF = 10**18
    while bfs():
        for i in range(n + 1):
            ptr[i] = head[i]
        while True:
            p = dfs(src, INF)
            if p == 0:
                break
            total_flow += p

    if total_flow == d:
        print("YES")
        ans = [str(flow[idx]) for idx in edge_indices]
        print(" ".join(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
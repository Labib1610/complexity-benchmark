import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # number of items, always 1
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for j in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap, j))
        adj[u].append(j)
        adj[v].append(j)
    
    # Build flow network
    # Edge index j in input corresponds to edge index 2*j in flow graph
    N = n
    M = 2 * m
    head = [-1] * (N + 1)
    to = [0] * M
    nxt = [0] * M
    cap = [0] * M
    flow = [0] * M
    edge_cnt = 0
    
    def add_edge(u, v, c):
        nonlocal edge_cnt
        to[edge_cnt] = v
        cap[edge_cnt] = c
        flow[edge_cnt] = 0
        nxt[edge_cnt] = head[u]
        head[u] = edge_cnt
        edge_cnt += 1
        
        to[edge_cnt] = u
        cap[edge_cnt] = 0
        flow[edge_cnt] = 0
        nxt[edge_cnt] = head[v]
        head[v] = edge_cnt
        edge_cnt += 1
    
    for u, v, c, _ in edges:
        add_edge(u, v, c)
    
    # Dinic's algorithm
    level = [0] * (N + 1)
    ptr = [0] * (N + 1)
    
    def bfs():
        for i in range(1, N + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if level[v] == -1 and cap[e] - flow[e] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
                e = nxt[e]
        return level[t] != -1
    
    def dfs(u, pushed):
        if u == t:
            return pushed
        while ptr[u] != -1:
            e = ptr[u]
            v = to[e]
            if level[v] == level[u] + 1 and cap[e] - flow[e] > 0:
                ret = dfs(v, min(pushed, cap[e] - flow[e]))
                if ret > 0:
                    flow[e] += ret
                    flow[e ^ 1] -= ret
                    return ret
            ptr[u] = nxt[e]
        return 0
    
    max_flow = 0
    while bfs():
        for i in range(1, N + 1):
            ptr[i] = head[i]
        while True:
            pushed = dfs(s, d - max_flow)
            if pushed == 0:
                break
            max_flow += pushed
            if max_flow >= d:
                break
        if max_flow >= d:
            break
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    result = [0] * m
    for j in range(m):
        result[j] = flow[2 * j]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
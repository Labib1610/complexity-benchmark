import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))
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
    
    head = list(range(m))
    def find(x):
        while head[x] != x:
            head[x] = head[head[x]]
            x = head[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            head[ra] = rb
    
    for i, (u, v, cap) in enumerate(edges):
        if cap > 0:
            for _, j in adj[u]:
                if j != i and edges[j][0] == v and edges[j][1] == u and edges[j][2] > 0:
                    union(i, j)
    
    comp_edges = {}
    for i in range(m):
        if edges[i][2] == 0:
            continue
        r = find(i)
        if r not in comp_edges:
            comp_edges[r] = []
        comp_edges[r].append(i)
    
    comp_list = list(comp_edges.values())
    num_comp = len(comp_list)
    comp_id = [-1] * m
    for cid, members in enumerate(comp_list):
        for e in members:
            comp_id[e] = cid
    
    N = num_comp + 2
    S = num_comp
    T = num_comp + 1
    
    g = [[] for _ in range(N)]
    edge_flow = [0] * m
    edge_cap = [0] * m
    edge_to = [0] * m
    edge_rev = [0] * m
    
    def add_edge(fr, to, cap):
        g[fr].append(len(edge_flow))
        edge_flow.append(0)
        edge_cap.append(cap)
        edge_to.append(to)
        edge_rev.append(len(edge_flow) + 1)
        g[to].append(len(edge_flow))
        edge_flow.append(0)
        edge_cap.append(0)
        edge_to.append(fr)
        edge_rev.append(len(edge_flow) - 1)
    
    for cid, members in enumerate(comp_list):
        total_cap = 0
        for e in members:
            total_cap += edges[e][2]
        add_edge(S, cid, total_cap)
        add_edge(cid, T, total_cap)
    
    for i, (u, v, cap) in enumerate(edges):
        if cap == 0:
            continue
        cid = comp_id[i]
        if u == s:
            add_edge(S, cid, cap)
        if u == t:
            add_edge(T, cid, cap)
        if v == s:
            add_edge(cid, S, cap)
        if v == t:
            add_edge(cid, T, cap)
    
    level = [0] * N
    it_ptr = [0] * N
    
    def bfs():
        for i in range(N):
            level[i] = -1
        level[S] = 0
        q = deque([S])
        while q:
            x = q.popleft()
            for eid in g[x]:
                if edge_cap[eid] > edge_flow[eid] and level[edge_to[eid]] < 0:
                    level[edge_to[eid]] = level[x] + 1
                    q.append(edge_to[eid])
        return level[T] >= 0
    
    def dfs(x, f):
        if x == T:
            return f
        while it_ptr[x] < len(g[x]):
            eid = g[x][it_ptr[x]]
            if edge_cap[eid] > edge_flow[eid] and level[edge_to[eid]] == level[x] + 1:
                ret = dfs(edge_to[eid], min(f, edge_cap[eid] - edge_flow[eid]))
                if ret > 0:
                    edge_flow[eid] += ret
                    edge_flow[edge_rev[eid]] -= ret
                    return ret
            it_ptr[x] += 1
        return 0
    
    flow = 0
    while bfs():
        it_ptr = [0] * N
        while True:
            f = dfs(S, d - flow)
            if f == 0:
                break
            flow += f
            if flow >= d:
                break
        if flow >= d:
            break
    
    if flow < d:
        print("NO")
        return
    
    comp_in = [0] * num_comp
    comp_out = [0] * num_comp
    for eid in range(len(edge_flow)):
        if edge_cap[eid] > 0:
            fr = -1
            to = edge_to[eid]
            for node in range(N):
                if eid in g[node]:
                    fr = node
                    break
            if fr == S and to < num_comp:
                comp_in[to] += edge_flow[eid]
            elif fr < num_comp and to == T:
                comp_out[fr] += edge_flow[eid]
    
    answer = [0] * m
    for cid, members in enumerate(comp_list):
        total = comp_in[cid]
        for e in members:
            answer[e] = min(edges[e][2], total)
            total -= answer[e]
    
    print("YES")
    print(' '.join(map(str, answer)))

solve()
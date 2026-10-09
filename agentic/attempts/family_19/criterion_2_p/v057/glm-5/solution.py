import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    _ = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        cap = int(data[idx]); idx += 1
        edges.append((u, v, cap))
        adj[u].append((v, i, False))
        adj[v].append((u, i, True))
    
    # Dinic's max flow
    # edge representation: to, rev_index, cap
    graph = [[] for _ in range(n + 1)]
    for i, (u, v, cap) in enumerate(edges):
        graph[u].append([v, len(graph[v]), cap])
        graph[v].append([u, len(graph[u]) - 1, 0])
    
    level = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph[u]:
                v, rev, cap = e
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0
    
    def dfs(u, f):
        if u == t:
            return f
        while ptr[u] < len(graph[u]):
            e = graph[u][ptr[u]]
            v = e[0]
            rev = e[1]
            cap = e[2]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = dfs(v, min(f, cap))
                if pushed > 0:
                    e[2] -= pushed
                    graph[v][rev][2] += pushed
                    return pushed
            ptr[u] += 1
        return 0
    
    max_flow = 0
    while bfs():
        ptr = [0] * (n + 1)
        while True:
            f = dfs(s, float('inf'))
            if f == 0:
                break
            max_flow += f
    
    if max_flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i, (u, v, cap) in enumerate(edges):
        # forward edge is graph[u][?], the residual cap tells us how much was used
        # find the forward edge
        for e in graph[u]:
            if e[0] == v:
                # this is the forward edge, used = cap - remaining
                # but we need to identify the correct one
                pass
        # Actually, let's track it differently
        # The forward edge for edge i is the one we added first
        # Let's just compute used = original_cap - current_cap of forward edge
        # We stored edges in order, so forward edge for edge i is graph[u] at some position
        # Let's find it by matching
        used = 0
        for j, e in enumerate(graph[u]):
            if e[0] == v and j == 0 or (e[0] == v):
                # This is tricky, let's use a different approach
                pass
        break
    
    # Let me redo this properly
    # Store forward edge reference
    # Actually, the forward edge for input edge i is graph[u][first occurrence]
    # But since we add them in order, and each edge adds exactly one forward edge to graph[u]
    # Let's track the index
    
    # Redo with proper tracking
    forward_edges = []
    graph2 = [[] for _ in range(n + 1)]
    for i, (u, v, cap) in enumerate(edges):
        forward_idx = len(graph2[u])
        backward_idx = len(graph2[v])
        graph2[u].append([v, backward_idx, cap, i])
        graph2[v].append([u, forward_idx, 0, -1])
        forward_edges.append((u, forward_idx))
    
    level2 = [0] * (n + 1)
    
    def bfs2():
        for i in range(n + 1):
            level2[i] = -1
        level2[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph2[u]:
                v, rev, cap, _ = e
                if cap > 0 and level2[v] < 0:
                    level2[v] = level2[u] + 1
                    q.append(v)
        return level2[t] >= 0
    
    def dfs2(u, f):
        if u == t:
            return f
        while ptr2[u] < len(graph2[u]):
            e = graph2[u][ptr2[u]]
            v = e[0]
            rev = e[1]
            cap = e[2]
            if cap > 0 and level2[v] == level2[u] + 1:
                pushed = dfs2(v, min(f, cap))
                if pushed > 0:
                    e[2] -= pushed
                    graph2[v][rev][2] += pushed
                    return pushed
            ptr2[u] += 1
        return 0
    
    max_flow2 = 0
    while bfs2():
        ptr2 = [0] * (n + 1)
        while True:
            f = dfs2(s, float('inf'))
            if f == 0:
                break
            max_flow2 += f
    
    if max_flow2 < d:
        print("NO")
        return
    
    result = [0] * m
    for i in range(m):
        u, fidx = forward_edges[i]
        orig_cap = edges[i][2]
        curr_cap = graph2[u][fidx][2]
        result[i] = orig_cap - curr_cap
    
    print(' '.join(map(str, result)))

solve()
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    groups = []
    for _ in range(k):
        s = int(next(it))
        t = int(next(it))
        d = int(next(it))
        groups.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
    
    # Build adjacency for original graph
    adj = [[] for _ in range(n + 1)]
    for j, (u, v, cap) in enumerate(edges):
        adj[u].append((v, j))
        adj[v].append((u, j))  # reverse edge for reachability
    
    # Check reachability for each group
    reachable = []
    for i in range(k):
        s, t, d = groups[i]
        visited = [False] * (n + 1)
        visited[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            if u == t:
                break
            for v, j in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        reachable.append(visited[t])
    
    if not all(reachable):
        print("NO")
        return
    
    # Build flow network
    # Node indexing:
    # For group i, node u: base[i] + u
    # Super source: 0, super sink: last
    base = [0] * (k + 1)
    for i in range(k):
        base[i + 1] = base[i] + n + 1
    total_nodes = base[k] + 2
    source = base[k]
    sink = base[k] + 1
    
    graph = [[] for _ in range(total_nodes)]
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])
    
    # Source to group starts
    for i in range(k):
        s, t, d = groups[i]
        add_edge(source, base[i] + s, d)
    
    # Group ends to sink
    for i in range(k):
        s, t, d = groups[i]
        add_edge(base[i] + t, sink, d)
    
    # Original edges with shared capacity
    for j, (u, v, cap) in enumerate(edges):
        for i in range(k):
            add_edge(base[i] + u, base[i] + v, cap)
    
    # Dinic's max flow
    def bfs():
        level = [-1] * total_nodes
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v, cap, rev in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, pushed, level, it_list):
        if u == sink:
            return pushed
        while it_list[u] < len(graph[u]):
            e = graph[u][it_list[u]]
            v, cap, rev = e
            if cap > 0 and level[v] == level[u] + 1:
                d = dfs(v, min(pushed, cap), level, it_list)
                if d > 0:
                    e[1] -= d
                    graph[v][rev][1] += d
                    return d
            it_list[u] += 1
        return 0
    
    total_flow = 0
    while True:
        level = bfs()
        if level[sink] < 0:
            break
        it_list = [0] * total_nodes
        while True:
            f = dfs(source, float('inf'), level, it_list)
            if f == 0:
                break
            total_flow += f
    
    total_demand = sum(d for _, _, d in groups)
    if total_flow < total_demand:
        print("NO")
        return
    
    # Extract solution
    result = [[0] * m for _ in range(k)]
    for j, (u, v, cap) in enumerate(edges):
        for i in range(k):
            # Find the edge from base[i]+u to base[i]+v
            node_u = base[i] + u
            for e in graph[node_u]:
                if e[0] == base[i] + v:
                    # Flow used = cap - remaining
                    # But we need to find the original capacity
                    # The edge capacity was 'cap', remaining is e[1]
                    # Flow = cap - e[1]
                    result[i][j] = cap - e[1]
                    break
    
    print("YES")
    for row in result:
        print(' '.join(map(str, row)))

solve()
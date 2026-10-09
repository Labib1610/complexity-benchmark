import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    priority = set()
    for _ in range(t):
        priority.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each priority tower
    dist = {}
    for p in priority:
        d = [float('inf')] * (n + 1)
        d[p] = 0
        pq = [(0, p)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > d[u]:
                continue
            for v, w in adj[u]:
                if d[v] > du + w:
                    d[v] = du + w
                    heapq.heappush(pq, (d[v], v))
        dist[p] = d
    
    # Build graph on priority nodes
    priority_list = list(priority)
    plen = len(priority_list)
    p_index = {priority_list[i]: i for i in range(plen)}
    
    edges = []
    for i in range(plen):
        p1 = priority_list[i]
        d1 = dist[p1]
        # Direct edges between priority nodes
        for j in range(i + 1, plen):
            p2 = priority_list[j]
            w = d1[p2]
            edges.append((w, i, j))
        
        # Edges through non-priority nodes
        for v in range(1, n + 1):
            if v not in priority:
                w = d1[v]
                if w < float('inf'):
                    edges.append((w, i, v))
    
    # Kruskal's algorithm
    # We need to connect all priority nodes
    # Non-priority nodes can be used as intermediate nodes
    
    # Map all nodes to indices for DSU
    total_nodes = n
    parent = list(range(total_nodes + 1))
    rank = [0] * (total_nodes + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    edges.sort()
    total_cost = 0
    components = plen
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            components -= 1
            if components == 1:
                break
    
    print(total_cost)

solve()
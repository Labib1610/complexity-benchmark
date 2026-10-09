import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    targets = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    if t == 1:
        print(0)
        return
    
    # Kruskal's MST
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
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
    
    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst_adj = [[] for _ in range(n + 1)]
    for u, v, w in sorted_edges:
        if union(u, v):
            mst_adj[u].append((v, w))
            mst_adj[v].append((u, w))
    
    # BFS to find path between consecutive targets in MST
    def path_cost(a, b):
        if a == b:
            return 0
        visited = [False] * (n + 1)
        visited[a] = True
        queue = [(a, 0)]
        head = 0
        while head < len(queue):
            node, dist = queue[head]
            head += 1
            for neighbor, w in mst_adj[node]:
                if not visited[neighbor]:
                    if neighbor == b:
                        return dist + w
                    visited[neighbor] = True
                    queue.append((neighbor, dist + w))
        return 0
    
    total = 0
    for i in range(t - 1):
        total += path_cost(targets[i], targets[i + 1])
    
    print(total)

solve()
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    cores = []
    for _ in range(t):
        cores.append(int(data[idx]) - 1)
        idx += 1
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # Kruskal's MST
    parent = list(range(n))
    rank = [0] * n
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
    mst_adj = [[] for _ in range(n)]
    mst_cost = 0
    for u, v, w in sorted_edges:
        if union(u, v):
            mst_adj[u].append((v, w))
            mst_adj[v].append((u, w))
            mst_cost += w
    
    # BFS from each core to compute distances within MST
    dist = [[0]*n for _ in range(n)]
    for s in cores:
        visited = [False]*n
        visited[s] = True
        dist[s][s] = 0
        queue = [s]
        head = 0
        while head < len(queue):
            u = queue[head]; head += 1
            for v, w in mst_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[s][v] = dist[s][u] + w
                    queue.append(v)
    
    total = 0
    for i in range(t-1):
        total += dist[cores[i]][cores[i+1]]
    
    print(total)

solve()
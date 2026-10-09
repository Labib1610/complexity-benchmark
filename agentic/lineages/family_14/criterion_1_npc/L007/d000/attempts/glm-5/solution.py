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
    
    required = [int(next(it)) for _ in range(t)]
    required_set = set(required)
    
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
    
    # Compute shortest paths between all pairs of required sites
    dist = {}
    for s in required:
        d = [float('inf')] * (n + 1)
        d[s] = 0
        pq = [(0, s)]
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d > d[u]:
                continue
            for v, w in adj[u]:
                nd = cur_d + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
        dist[s] = d
    
    # Build complete graph on required sites
    edges = []
    for i in range(t):
        for j in range(i + 1, t):
            u, v = required[i], required[j]
            edges.append((dist[u][v], u, v))
    
    # Kruskal's MST
    edges.sort()
    parent = {x: x for x in required}
    rank = {x: 0 for x in required}
    
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
    
    total = 0
    count = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            count += 1
            if count == t - 1:
                break
    
    print(total)

if __name__ == "__main__":
    solve()
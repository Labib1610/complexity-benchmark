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
    
    terminals = set()
    for _ in range(t):
        terminals.add(int(next(it)))
    
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
    
    # Dijkstra from each terminal
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for s in terminals:
        dist[s][s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[s][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[s][v]:
                    dist[s][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Build complete graph on terminals
    terminal_list = list(terminals)
    T = len(terminal_list)
    edges = []
    for i in range(T):
        u = terminal_list[i]
        for j in range(i + 1, T):
            v = terminal_list[j]
            w = dist[u][v]
            edges.append((w, u, v))
    
    # Kruskal's MST
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
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
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    edges.sort()
    total = 0
    edges_used = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            edges_used += 1
            if edges_used == T - 1:
                break
    
    print(total)

if __name__ == "__main__":
    solve()
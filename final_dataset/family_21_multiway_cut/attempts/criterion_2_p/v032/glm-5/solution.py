import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    t = int(next(it))
    B = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
    
    # Dijkstra from s
    dist_s = [float('inf')] * (n+1)
    dist_s[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_s[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_s[v] > d + w:
                dist_s[v] = d + w
                heapq.heappush(pq, (dist_s[v], v))
    
    # Dijkstra from t
    dist_t = [float('inf')] * (n+1)
    dist_t[t] = 0
    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_t[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_t[v] > d + w:
                dist_t[v] = d + w
                heapq.heappush(pq, (dist_t[v], v))
    
    # Check if s and t are connected at all
    if dist_s[t] == float('inf'):
        print("YES")
        print(0)
        return
    
    # Find min-cut edges
    min_dist = dist_s[t]
    cut_edges = []
    for i, (u, v, w) in enumerate(edges):
        if dist_s[u] + w + dist_t[v] == min_dist or dist_s[v] + w + dist_t[u] == min_dist:
            cut_edges.append(i)
    
    total_cost = sum(edges[i][2] for i in cut_edges)
    
    if total_cost <= B:
        print("YES")
        print(len(cut_edges))
        for i in cut_edges:
            u, v, _ = edges[i]
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
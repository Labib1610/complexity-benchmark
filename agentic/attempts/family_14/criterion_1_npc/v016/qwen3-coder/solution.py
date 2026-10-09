import sys
import heapq
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    terminals = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-based indexing
    terminals = [x - 1 for x in terminals]
    
    # Build graph
    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # If there's only one terminal, cost is 0
    if t <= 1:
        print(0)
        return
    
    # Compute shortest paths from each terminal using Dijkstra
    dist = []
    for start in terminals:
        d = [float('inf')] * n
        d[start] = 0
        pq = [(0, start)]
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > d[u]:
                continue
            for v, w in graph[u]:
                alt = d[u] + w
                if alt < d[v]:
                    d[v] = alt
                    heapq.heappush(pq, (alt, v))
        dist.append(d)
    
    # Build a complete graph among terminals with shortest path distances
    # Then find MST of this complete graph
    # We'll use Kruskal's algorithm
    
    # Generate all edges between terminals based on shortest paths
    terminal_edges = []
    for i in range(t):
        for j in range(i+1, t):
            u = terminals[i]
            v = terminals[j]
            # Distance between terminal i and terminal j
            w = dist[i][v]
            terminal_edges.append((w, i, j))
    
    # Sort edges by weight
    terminal_edges.sort()
    
    # Union-Find for Kruskal's
    parent = list(range(t))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    # Kruskal's algorithm to find MST
    total_cost = 0
    edge_count = 0
    for w, u, v in terminal_edges:
        if union(u, v):
            total_cost += w
            edge_count += 1
            if edge_count == t - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
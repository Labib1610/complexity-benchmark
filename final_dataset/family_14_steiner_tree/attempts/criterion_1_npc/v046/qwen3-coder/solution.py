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
    
    regulated = set()
    for _ in range(t):
        regulated.add(int(data[idx]))
        idx += 1
    
    # If t <= 1, no links needed
    if t <= 1:
        print(0)
        return
    
    # Build graph
    graph = defaultdict(list)
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute shortest paths from each regulated node to all other nodes
    # Using Dijkstra's algorithm
    dist = {}
    for reg in regulated:
        dist[reg] = [float('inf')] * (n + 1)
        dist[reg][reg] = 0
        pq = [(0, reg)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[reg][u]:
                continue
            for v, w in graph[u]:
                alt = d + w
                if alt < dist[reg][v]:
                    dist[reg][v] = alt
                    heapq.heappush(pq, (alt, v))
    
    # Create a complete graph among regulated nodes with shortest path weights
    # Then find MST of this complete graph
    reg_list = list(regulated)
    k = len(reg_list)
    
    # Build edge list for the complete graph on regulated nodes
    edges = []
    for i in range(k):
        for j in range(i+1, k):
            u = reg_list[i]
            v = reg_list[j]
            # Weight is the shortest path between u and v in original graph
            w = float('inf')
            # The shortest path between u and v could go through any node
            # But we already have dist[u][v] from Dijkstra above
            # Actually, we need to compute all-pairs shortest paths involving regulated nodes
            # Let's recompute: for each pair of regulated nodes, find the shortest path between them
            # We can do this by running Dijkstra from each regulated node
            # Already did that above
            weight = dist[u][v]
            edges.append((weight, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find for Kruskal's algorithm
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Kruskal's algorithm
    total_cost = 0
    edges_used = 0
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
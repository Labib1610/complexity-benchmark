import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, end, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == end:
            return d
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist[end]

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    cores = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    # Build graph
    graph = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    # Find minimum cost to connect all core banks in sequence
    # We need to find minimum spanning tree that connects all core banks
    # But we have a specific sequence, so we need paths between consecutive core banks
    
    # However, we want minimum cost subgraph such that for each consecutive pair in cores,
    # there's a path between them in the subgraph
    
    # This is essentially finding a subgraph with minimum total edge weight such that
    # all consecutive pairs in cores are connected
    
    # We can use Union-Find and MST approach but we need to ensure all core pairs are connected
    # Actually, let's think differently - we want to build a graph where all core nodes 
    # are in the same component
    
    # But we have a sequence constraint - we need path from c1 to c2, c2 to c3, etc.
    # So all core nodes must be connected in the final graph
    
    # Let's use the fact that we want minimum cost to connect all core nodes
    # We can create a complete graph on core nodes where edge weights are shortest paths
    # Then find MST of this complete graph
    
    # But simpler approach: run Kruskal's algorithm but only consider edges until
    # all core nodes are connected
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Union-Find data structure
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n + 1))
            self.rank = [0] * (n + 1)
            
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
            
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            return True
            
        def connected(self, x, y):
            return self.find(x) == self.find(y)
    
    # Check if all core nodes are connected
    def all_cores_connected(uf, cores):
        if len(cores) <= 1:
            return True
        root = uf.find(cores[0])
        for i in range(1, len(cores)):
            if uf.find(cores[i]) != root:
                return False
        return True
    
    uf = UnionFind(n)
    total_cost = 0
    
    # First check if consecutive core nodes are already connected
    for i in range(len(cores) - 1):
        if not uf.connected(cores[i], cores[i+1]):
            # Need to connect them
            pass
    
    # Apply Kruskal's algorithm until all core nodes are connected
    for u, v, w in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            total_cost += w
            # Check if all core nodes are now connected
            if all_cores_connected(uf, cores):
                break
                
    print(total_cost)

solve()
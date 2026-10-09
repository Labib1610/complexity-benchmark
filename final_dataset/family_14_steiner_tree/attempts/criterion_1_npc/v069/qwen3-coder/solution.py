import sys
import heapq
from collections import defaultdict

def find_mst_with_priority_nodes(n, edges, priority_nodes):
    if len(priority_nodes) <= 1:
        return 0
    
    # Build the full graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Use Prim's algorithm to find the minimum spanning tree that connects all priority nodes
    # We'll use a modified version that only cares about connecting the priority nodes
    
    # First, let's see if we can connect all priority nodes with 0 cost when there are no edges
    if not edges:
        return 0
        
    # We'll use Dijkstra-like approach to find minimum cost to connect all priority nodes
    # State: (cost, node)
    
    # But actually, we want to find the minimum spanning tree of the subgraph that connects all priority nodes
    # This is essentially the Steiner tree problem, but since t <= 10, we can use a different approach
    
    # Let's build a complete graph where edge weights are shortest paths between priority nodes
    # Then find MST of this complete graph
    
    # Compute shortest paths between all pairs of priority nodes
    priority_list = list(priority_nodes)
    dist = {}
    
    # Run Dijkstra from each priority node
    for start in priority_list:
        # Dijkstra
        d = {i: float('inf') for i in range(1, n+1)}
        d[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            cost, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            
            for v, w in graph[u]:
                if d[v] > cost + w:
                    d[v] = cost + w
                    heapq.heappush(pq, (d[v], v))
        
        for end in priority_list:
            if start != end:
                dist[(start, end)] = d[end]
    
    # Now we have a complete graph on priority nodes with edge weights as shortest paths
    # Find MST of this graph using Kruskal's algorithm
    
    # Generate all edges in the complete graph
    priority_edges = []
    for i in range(len(priority_list)):
        for j in range(i+1, len(priority_list)):
            u, v = priority_list[i], priority_list[j]
            priority_edges.append((dist[(u, v)], u, v))
    
    # Sort edges by weight
    priority_edges.sort()
    
    # Union-Find for Kruskal's
    parent = {node: node for node in priority_list}
    
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
    
    for w, u, v in priority_edges:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == len(priority_list) - 1:
                break
                
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

priority_departments = set(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and print result
result = find_mst_with_priority_nodes(n, edges, priority_departments)
print(result)
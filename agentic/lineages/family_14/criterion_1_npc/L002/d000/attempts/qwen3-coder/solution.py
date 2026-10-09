import sys
import heapq
from collections import defaultdict

def find_mst_cost(n, edges, terminals):
    # Prim's algorithm modified for Steiner Tree approximation
    # We'll use a greedy approach: build MST on the terminal nodes
    # by treating non-terminals as potential Steiner points
    
    if len(terminals) <= 1:
        return 0
    
    # Build graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Use Dijkstra-like approach to find minimum cost to connect all terminals
    # This is essentially finding the minimum spanning tree of the metric closure
    # of the terminal nodes
    
    # First, compute shortest paths between all pairs of terminals
    dist = {}
    for start in terminals:
        dist[start] = {}
        d = [float('inf')] * (n + 1)
        d[start] = 0
        pq = [(0, start)]
        
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > d[u]:
                continue
                
            for v, w in graph[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heapq.heappush(pq, (d[v], v))
        
        for end in terminals:
            dist[start][end] = d[end]
    
    # Now we have complete graph on terminals, find MST of this
    # Using Prim's algorithm
    terminal_list = list(terminals)
    if len(terminal_list) <= 1:
        return 0
        
    in_mst = {term: False for term in terminal_list}
    min_edge = {term: float('inf') for term in terminal_list}
    
    # Start with first terminal
    min_edge[terminal_list[0]] = 0
    total_cost = 0
    
    for _ in range(len(terminal_list)):
        # Find vertex with minimum edge weight not yet in MST
        u = None
        min_weight = float('inf')
        for v in terminal_list:
            if not in_mst[v] and min_edge[v] < min_weight:
                u = v
                min_weight = min_edge[v]
        
        if u is None:
            break
            
        in_mst[u] = True
        total_cost += min_weight
        
        # Update key values of adjacent vertices
        for v in terminal_list:
            if not in_mst[v] and dist[u][v] < min_edge[v]:
                min_edge[v] = dist[u][v]
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

terminals = set(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve using the Steiner tree approach
result = find_mst_cost(n, edges, terminals)
print(result)
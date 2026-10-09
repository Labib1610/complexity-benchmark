import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start, nodes):
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

def find_mst_cost(graph, terminals, nodes):
    if len(terminals) <= 1:
        return 0
    
    # Create a complete graph with terminals using shortest paths
    # We use Prim's algorithm on the terminal nodes
    cost = {}
    for t in terminals:
        cost[t] = dijkstra(graph, t, nodes)
    
    # Now we have all pairwise distances between terminals
    # Apply Prim's algorithm to connect terminals
    in_tree = [False] * len(terminals)
    min_cost = [float('inf')] * len(terminals)
    min_cost[0] = 0
    total_cost = 0
    
    for _ in range(len(terminals)):
        # Find vertex with minimum cost not yet in tree
        u = -1
        for j in range(len(terminals)):
            if not in_tree[j] and (u == -1 or min_cost[j] < min_cost[u]):
                u = j
        
        in_tree[u] = True
        total_cost += min_cost[u]
        
        # Update costs to all other vertices
        for j in range(len(terminals)):
            if not in_tree[j]:
                t1, t2 = terminals[u], terminals[j]
                min_cost[j] = min(min_cost[j], cost[t1][t2])
    
    return total_cost

# Read input
line = sys.stdin.readline().split()
n, m, t = int(line[0]), int(line[1]), int(line[2])

terminals = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
all_nodes = set()

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    all_nodes.add(u)
    all_nodes.add(v)

# Add missing nodes if any
for i in range(1, n+1):
    all_nodes.add(i)

# Solve
result = find_mst_cost(graph, terminals, all_nodes)
print(result)
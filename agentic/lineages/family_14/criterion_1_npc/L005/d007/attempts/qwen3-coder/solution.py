import sys
from itertools import combinations
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    # Dijkstra's algorithm to find shortest path between start and end
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
            
        visited.add(node)
        
        if node == end:
            return current_dist
            
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return float('inf')

def find_min_cost_to_connect_pair(graph, n, flag1, flag2):
    # We need to make exactly flag1 and flag2 TRUE
    # This is equivalent to finding a way to toggle only these two flags
    # In the XOR space, this means we want to reach state where only flag1 and flag2 are 1
    
    # To achieve this, we can use the fact that executing a script twice cancels out
    # So we only care about the parity of executions for each script
    
    # The key insight is that we want to find a combination of scripts such that:
    # - flag1 and flag2 appear an odd number of times
    # - all other flags appear an even number of times
    
    # This is equivalent to finding a path in a modified graph
    # But there's a simpler approach: we can use the fact that we're looking for
    # a way to create a state with exactly two specific flags set
    
    # In terms of linear algebra over GF(2), we want to express the vector
    # with 1s in positions flag1 and flag2 only as a sum of script vectors
    
    # But for this problem, we can think of it as: we need to be able to
    # toggle exactly flag1 and flag2, which means we need a path that
    # connects flag1 and flag2 while allowing all other nodes to be "cancelled"
    
    # The minimum cost to connect flag1 and flag2 is the shortest path
    # between them in the graph formed by the selected scripts
    
    return dijkstra(graph, flag1, flag2)

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical_flags = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    scripts = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        scripts.append((u, v, w))
    
    # For each pair of critical flags, we need to be able to toggle exactly those two
    # This means we need to connect them in some way using the scripts
    
    # The key insight is that we can model this as a minimum spanning tree problem
    # But not exactly - we need to ensure connectivity between all critical flags
    
    # Actually, let's think differently:
    # We need to be able to generate any pair of critical flags being TRUE
    # This means for any two critical flags i and j, we need to be able to
    # create a state where only i and j are TRUE
    
    # In graph terms, if we have scripts as edges, we need to ensure that
    # for any pair of critical flags, there's a way to "isolate" their toggle
    
    # The approach:
    # 1. We need the subgraph induced by selected scripts to allow toggling
    #    any pair of critical flags while keeping others FALSE
    # 2. This is equivalent to saying the critical flags must be connected
    #    in such a way that we can create any pair
    
    # Key insight: we need to make sure that for any pair of critical flags,
    # we can find a set of scripts whose execution toggles exactly those two flags
    # This means in the "toggle space", we need to be able to generate all
    # basis vectors for pairs of critical flags
    
    # Simpler approach:
    # The minimum way to do this is to connect all critical flags in a tree
    # Then we can toggle any pair by doing:
    # - path from first to LCA
    # - path from second to LCA
    # - but this is complex
    
    # Even simpler: we just need all critical flags to be connected
    # Then we can toggle any pair
    
    # So we need to find the minimum cost to connect all critical flags
    # This is a Steiner tree problem, but with small t (t <= 10), we can try all approaches
    
    # Let's use a different approach:
    # Build a complete graph where edge weights are shortest paths between critical flags
    # Then find MST of this graph
    
    # First, for each pair of critical flags, compute the minimum cost to connect them
    # (shortest path in the original graph)
    
    # Build graph
    graph = defaultdict(list)
    for u, v, w in scripts:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Compute all-pairs shortest paths between critical flags
    critical_distances = {}
    for i in range(t):
        for j in range(i+1, t):
            flag1, flag2 = critical_flags[i], critical_flags[j]
            dist = dijkstra(graph, flag1, flag2)
            critical_distances[(flag1, flag2)] = dist
            critical_distances[(flag2, flag1)] = dist
    
    # Now we have a complete graph on critical flags
    # Find the minimum spanning tree of this graph
    # We'll use Kruskal's algorithm
    
    edges = []
    for i in range(t):
        for j in range(i+1, t):
            flag1, flag2 = critical_flags[i], critical_flags[j]
            edges.append((critical_distances[(flag1, flag2)], flag1, flag2))
    
    edges.sort()
    
    # Union-Find for Kruskal's
    parent = {flag: flag for flag in critical_flags}
    
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
    
    total_cost = 0
    edges_used = 0
    
    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

solve()